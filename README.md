Multi Whois Client
=====
*** 

Multi-Whois is a small whois domain name search program capable of finding multiple available domains via a file or a MySQL query. It's a good way to search for domains that are available to buy. (http://jrosco.github.io/mwhois)


Install 
====
***

Dependencies:
* Python >= 2.7.3 (Python 3 not supported yet) Download from http://www.python.org/download/
* Python Module wx (can still run mwhois without this module, but only with command line support) Donwload from http://wxpython.org/

1. Download zip file mwhois.zip https://github.com/jrosco/mwhois/archive/master.zip
2. Unzip mwhois.zip 
3. Windows Only. Ensure that python is in your environment variables e.g C:\Python27 
3. Run run.bat (windows) or run.sh (linux)

Note: For help run 'python mwhois.py --help' via the command line (without quotes). 

How to use mwhois client 
====

* * * 

Run with GUI: 
---
<code> Run run.bat (windows) or run.sh (Linux) </code>

You can either search for a single domain or use a list of names to search for and provide a tld to use e.g .com. A sample file can be found in files/wordlist-sample from the download. To search multiple domains select the "Multi Search" tab and open the file to use, don't worry about selecting a save file this will be done for you, but if you would like to specify a file for saving the the output use the save file function. Now select a tld to use (ATM only a few to choose from) then hit the begin button. Now you'll see all available domains from the wordlist you selected to search.  


Run via command line: 
---
<pre>
Usage: mwhois.py [options] -i [file-to-read-from] -o [file-to-write-too] 
 
Examples:
mwhois -t net -i /tmp/wordlist -o /tmp/domains
mwhois -s sourceforge.net

Options:
  -h, --help            show this help message and exit
  -t TLD, --tld=TLD     --tld com/net/org/biz/edu/info - Search for these
                        TLD's (Only use one of these tlds for each whois
                        search
  -s, --single          Single domain search
  -a, --advance         Advanced domain search
  -i FILEIN, --file-in=FILEIN
                        File to read from
  -o FILEOUT, --file-out=FILEOUT
                        File to write to
  -g, --gui             Start GUI Interface

</pre>

How to use mwhois py modules 
====
![](http://www.dojoportal.com/static/site-images/icons/warn-icon.gif)WARNING: Still in Alpha state, use with caution

* * * 
1. Clone repo(requires git to be installed): git clone https://github.com/jrosco/mwhois.git mwhois
   or
   Download Zip File to the right (https://github.com/jrosco/mwhois/archive/master.zip)
2. cd mwhois/mwhois2
3. Run: python setup.py install
4. See examples below

<pre>
# """Get the whois server url by providing a domain name"""
# from whoismap import WhoisServerMap
#  
# w = WhoisServerMap()
# w.domain = "on.net"
# whoisserver = w.get_whois_server()
# print(whoisserver)
#  
#  
# """Get 'not found' text on whois server by providing a domain name"""
# from whoismap import WhoisServerMap
# 
# w2 = WhoisServerMap()
# w2.domain = "ping.net"
# w2.get_domain_tld()
# txt = w2.tld_not_found_text()
# print(txt)
# 
# """Get 'not found' text on whois server by providing a tld .e.g .com)"""
# from whoismap import WhoisServerMap
# 
# w3 = WhoisServerMap()
# w3.tld = "jp"
# txt2 = w3.tld_not_found_text()
# print(txt2)
# 
# """Single domain search"""
# from whoissearch import WhoisSearch
# 
# s = WhoisSearch(dname='on.net')
# print s.single_search()
# 
# """ Search for multiple domains """
# from whoissearch import WhoisSearch
#   
# domain_list = ['google.com','doesnotexist123.net','yahoo']
#   
# """ deadonly will only show dead domains if set to true otherwise all domains are shown """
# m = WhoisSearch(wordlist=domain_list, deadonly=False)
#multi = m.basic_search()
#  
#"""Returns True(1) if found or False(0) is not found"""
#for i in multi:
#    print i
#  
# """ Your can also use a file as a wordlist """
# m.wordlist='./wordlist.txt'
# txt_file = m.basic_search()
# for x in txt_file:
#     print x
# """ Deeper multiple search (Experimental)"""
# from whoissearch import WhoisSearch
# 
# domain_list = ['google','doesnotexist123','yahoo']
# 
# d = WhoisSearch(tld='com', wordlist='./wordlist.txt', deadonly=False)
# dmulti = d.deeper_search()
# for f in  dmulti:
#     print f
</pre>


Contact
===
***

joel_c at zoho dot com
