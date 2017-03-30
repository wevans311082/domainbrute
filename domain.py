import sys, socket
import threading
import time
from Queue import Queue


ip = ""
hostname = ""

class progressthread(threading.Thread):

    def run(self):
        while domainlist.isEmpty() != True :
            print(str(domainlist.size())+" Subdomains Left to Check")
            time.sleep(30)
        exit(0)

class workerthread(threading.Thread):

    def run(self):
        while domainlist.isEmpty() != True :
            check = str(domainlist.pop().rstrip('\n') + "." + hostname)
           # print(str(domainlist.size()) + " Thread ID =:" + str(self.ident))
            ip = lookup_host(check)
            if ip != 0:
                print(check + "[" + str(ip) + "]")

        return

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
        with open('subdomainback.txt') as domains:
            for line in domains:
               domainlist.push(line)
        nosd = domainlist.size()
        print("Loaded " + str(nosd) + " Domains prefixes to be check")

def lookup_from_stack(dom):
    for x in range(domainlist.size()):
        check=str(domainlist.pop().rstrip('\n')+"."+dom)
        print()
        ip = lookup_host(check)
        if ip != 0:
            print(check + "[" + str(ip) + "]")


def create_threads():
    timer = progressthread()
    timer.start()
    for x in range(domainlist.size()):
        t = workerthread()
        t.start()

def lookup_host(name):

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


    global nosd
    global domainlist
    global hostname


    nosd=""
    domainlist = Stack()

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
        print ("You must provide a hostname - TEST MODE")
        hostname = "hazzy.co.uk"
        result = lookup_host(hostname)
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
