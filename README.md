=====
*** 

m-whois is a small python whois search module capable of finding multiple available domains via a file or list type. It's a good way to search for domains that are available to buy. (http://jrosco.github.io/mwhois)

Dependencies
* Python >= 2.7.3 (Python 3 not supported yet) Download from http://www.python.org/download/
* To use the proxy feature you'll need the pysocks module installed. Download from https://pypi.python.org/pypi/PySocks/ 
* N.B: If you want to run the example GUI application you'll need the python module wx (can still run cmd.py without this module, but only with command line support) Download wx from http://wxpython.org/

Features 
* Search for single/multiple domains with direct connection to a large list of  whois servers  
* Show only available domains 
* 100+ searchable TLDS
* 30+ gTLDS e.g .graphics, .guru, .technology, .today etc
* Search second whois server if first one fails (limited to certain tld's)
* Connect to whois server via a proxy

Features to come
* TODO: Caching results for quicker responses and avoid exceeding query limits
* TODO: Print results to csv and pdf

How to use mwhois python module 
---
![](http://www.sbg.bio.ic.ac.uk/phyre2/html/images/infoIcon.gif)Note: In beta, use with caution, criticism welcomed
***
Install 
---- 
1. Clone repo(requires git to be installed): <code>git clone https://github.com/jrosco/mwhois.git mwhois </code>
   or
   Download Zip File to the right (https://github.com/jrosco/mwhois/archive/master.zip)
2. If you downloaded zip file ("unzip mwhois-master.zip" and "cd mwhois-master/src"
3. If you used git clone ("cd mwhois/")
4. Now Run: python setup.py install (you'll need correct permissions to install module. For linux use the sudo command)
5. See examples below on how to use this these modules (These are also shown in examples/examples.py)

Examples 
----
Search for single domain 
<code> 
python examples/cmd.py github.com 
</code>

Search for multiple domains using one liner wordlist 
<code>
python examples/cmd.py -t com -i files/wordlist-sample
</code>

You can also run a sample GUI using the default TkInter module
<code>
python examples/GUI/mgui.py
</code>

You can find a mature application built around this module here http://sourceforge.net/projects/xwh0i5/

Usage
---
<pre>
# """Get the whois server url by providing a domain name"""
# from mwhois.whois import WhoisInfo
#   
# w = WhoisInfo()
# w.domain = "on.net"
# whoisserver = w.get_whois_server()
# print(whoisserver)
#   
#   
# """Get 'not found' text on whois server by providing a domain name"""
# from mwhois.whois import WhoisInfo
#  
# w2 = WhoisInfo()
# w2.domain = "ping.net"
# w2.get_domain_tld()
# txt = w2.tld_not_found_text()
# print(txt)
#  
# """Get 'not found' text on whois server by providing a tld .e.g .com)"""
# from mwhois.whois import WhoisInfo
#  
# w3 = WhoisInfo()
# w3.tld = "jp"
# txt2 = w3.tld_not_found_text()
# print(txt2)
#  
# """Single domain search"""
# from mwhois.whosearch import WhoisSearch
# import mwhois.const as CONST
#
# s = WhoisSearch(dname='google.org', debug=False)
# s.connection.proxy = True
# s.connection.proxy_host = '127.0.0.1'
# s.connection.proxy_port = 1107
# s.connection.proxy_type = CONST.PROXY_TYPE_SOCKS5
# s.whois_search()
# print(s.response())
# #
# """Print Whois attributes returned as a list"""
# print(s.creation_date())
# print(s.expiry_date())
# print(s.update_date())
# print(s.registrant())
# print(s.nameservers())
# print(s.emails())
#  
# """ Search for multiple domains """
#from mwhois.whosearch import WhoisSearch
#      
#domain_list = ['google','doesnotexist123','yahoo']
#  
# """ deadonly will only show dead domains if set to true otherwise all domains are shown """
#m = WhoisSearch(tld='org',wordlist=domain_list, deadonly=False)
# multi = m.whois_multi_search()
#     
# """Returns True(1) if found or False(0) is not found"""
# for i in multi:
#     print i
#
# """ Your can also use a file as a wordlist """
# from mwhois.whosearch import WhoisSearch
# 
# m = WhoisSearch(debug=False)
# m.tld='com'
# m.wordlist='./wordlist.txt'
# 
# txt_file = m.whois_multi_search()
# 
# """ Loop over txt_file generator and print list results containing ['status value', 'domain name']""" 
# for x in txt_file:
#      
#     domain = x[1]
#      
#     if x[0] == 1:
#         status = 'taken'
#     else:
#         status = 'not taken'
#      
#     print('Domain %s is %s ' % (domain, status))
#      
# """ Loop over txt_file generator and print whois attributes"""
# for x in txt_file:
#     
#     domain = x[1]
#     
#     try: 
#         date = m.creation_date()[0]
#     except:
#         date = 'N/A'
#         
#     print('Domain %s has creation date %s' % (domain, date))
</pre>