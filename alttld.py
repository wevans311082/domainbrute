import sys, socket
import urllib



def list_of_tlds():
    file = urllib.URLopener()
    file.retrieve("https://data.iana.org/TLD/tlds-alpha-by-domain.txt", "tld.txt")
    # Need to remove the first line which is a # Info Message from IANA
    tidy_tld_file()
    with open("tld.txt") as f:
        tldlist = f.readlines()
    tldlist = [x.strip() for x in tldlist]
    return tldlist


def lookup_host(name):
# perform the actual lookup and returning the ip if it errors catch it and just return 0
    try:

        ip = socket.gethostbyname(name)
        return ip
    except Exception:
     #   print(name+ " Not Found")
        return 0


def tidy_tld_file():
    with open('tld.txt', 'r+') as f:
        f.readline()
        data = f.read()
        f.seek(0)
        f.write(data)
        f.truncate()



def display_usage():
    #display usage message
    print("Usage: alttld.py <domain name without TLD>")
    sys.exit(1)

def main():
    global tldlist
    hostname = sys.argv[1]
    tldlist = list_of_tlds()
    for x in tldlist:
        check = hostname + "." + x
        ip = lookup_host(check)
        if str(ip) == "127.0.53.53":
            next
        else:
            if ip != 0:
                print("Found :" + check + " [" + str(ip) + "]")




if __name__ == "__main__":
    if len(sys.argv) != 2:
        display_usage()
    main()