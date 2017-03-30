# domainbrute
A  basic python subdomain Domain finding tool

Other tools I found were painfully slow - some taking an hour to check for domains based on a large list, so I thought I would make one which is slightly faster.

usage - python domain.py domain.com

This simple program will spawn some threads and do a NSlookup on the domain name to find subdomains

currently it uses the GSSEC discovery list of common sub domains (114607 entries)

WARNING - to speed things up - it tries to create as many threads as it can - using Memory and CPU - it then takes a while to close down and kill all the spawned threads.

normally take about 2/3 Mins on my laptop to check the list against a domain.

TODO
---------------------------

Better output
Export Output
allow parameters such as define number of threads
counter of number of entries

