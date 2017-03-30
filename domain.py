import sys, socket
import threading
import time

ip = ""
hostname = ""
#a threat to creaate a watchdog, timer type thread that will report back every 30 seconds to show the code is still running
class progressthread(threading.Thread):

    def run(self):
        while domainlist.isEmpty() != True :
            print(str(domainlist.size())+" Subdomains Left to Check")
            time.sleep(30)
        print("Complete - Waiting to Kill all Threads... might be slow!")
# the worker thread - simple at the moment, and badly implemented will be changing to improve at the near future
class workerthread(threading.Thread):

    def run(self):
        while domainlist.isEmpty() != True :
            #need to pop the entry to be tested off the shared global stack ... had to add .rstrip('/n') otherwise it got messy!
            check = str(domainlist.pop().rstrip('\n') + "." + hostname)
           # print(str(domainlist.size()) + " Thread ID =:" + str(self.ident))
            ip = lookup_host(check)
          # if the return from the lookup (ip) is anything other than zero it was successful and lets output it else assume it failed
            if ip != 0:
                print(check + "[" + str(ip) + "]")

        return
#create a default stack with some default methods - easier to use!
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def load_sd_stack():
    #loads the stack using push reading the file 1 line at a time
        with open('subdomainback.txt') as domains:
            for line in domains:
               domainlist.push(line)
        nosd = domainlist.size()
        print("Loaded " + str(nosd) + " Domains prefixes to be check")

def lookup_from_stack(dom):
    #an example stack lookup function - early debugging
    for x in range(domainlist.size()):
        check=str(domainlist.pop().rstrip('\n')+"."+dom)
        print()
        ip = lookup_host(check)
        if ip != 0:
            print(check + "[" + str(ip) + "]")


def create_threads():
    timer = progressthread()
    timer.start()
    # create a number of threads (currently I create as many as possible but it will use memory and cpu like no one
    for x in range(domainlist.size()):
        t = workerthread()
        t.start()

def lookup_host(name):
# perform the actual lookup and returning the ip if it errors catch it and just return 0
    try:
       #  print("checking domain:"+name)
        ip = socket.gethostbyname(name)
        return ip
    except Exception:
        return 0


def brute_subdomains(dom):
    with open('subdomainback.txt') as domains:
        for line in domains:
            ip=lookup_host(line.rstrip('\n')+"."+dom)
            if ip != 0:
                print(line.rstrip('\n')+"."+dom + "["+str(ip)+"]")


def main():
# main code

    global nosd
    global domainlist
    global hostname


    nosd=""
    domainlist = Stack()
# check if the argument provided is valid
    try:
        hostname=sys.argv[1]
        result = lookup_host(hostname)
        load_sd_stack()
        if result == 0:
            print(hostname + " is Invalid")
        else:
            print(result)
          #  brute_subdomains(hostname)
          #  lookup_from_stack(hostname)
            create_threads()
    except Exception:
        # if the argv is invalid and bombs out - lets use a test domain for now
        # a help page will be provided later
        print ("You must provide a hostname - TEST MODE")
        hostname = "hazzy.co.uk"
        result = lookup_host(hostname)
        #load the contents of the domain subfile into a stack
        load_sd_stack()
        if result == 0:
            print(hostname + " is Invalid")
        else:
            print(result)
            #  brute_subdomains(hostname)
            #  lookup_from_stack(hostname)
            create_threads()
            print("Testing Complete")
        exit(31)
if __name__ == "__main__":
    main()
