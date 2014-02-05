mwhois
=====
*** 

whois is a small python whois search module capable of finding multiple available domains via a file or list type. It's a good way to search for domains that are available to buy. (http://jrosco.github.io/mwhois)

Features 
* Search for Single domains 
* Search for multiple domains 
* Show only available domains   
* 100 searchable tld's 

Features to come
* TODO: Caching results for quicker responses and avoid exceeding query limits
* TODO: Print results to csv and pdf
* TODO: Search second whois server if first one fails
* TODO: Ability to connect to whois server via a proxy

How to use mwhois python module 
---
![](http://www.sbg.bio.ic.ac.uk/phyre2/html/images/infoIcon.gif)Note: In beta, use with caution, criticism welcomed
***
Install 
---- 
1. Clone repo(requires git to be installed): <code>git clone https://github.com/jrosco/mwhois.git mwhois </code>
   or
   Download Zip File to the right (https://github.com/jrosco/mwhois/archive/master.zip)
2. If you downloaded zip file ("unzip mwhois-master.zip" and "cd mwhois-master/mwhois2"
3. If you used git clone ("cd mwhois/mwhois2")
4. Now Run: python setup.py install
5. See examples below on how to use this these modules (These are also shown in mwhois2/examples/examples.py)

Examples 
----
Search for single domain 
<code> 
python mwhois2/examples/cmd.py github.com 
</code>

Search for multiple domains using one liner wordlist 
<code>
python mwhois2/examples/cmd.py -t com -i files/wordlist-sample
</code>

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
#  
# s = WhoisSearch(dname='google.org')
# s.whois_search()
# print(s.response())
# 
# """Print Whois attributes returned as a list"""
# print(s.creation_date())
# print(s.expiry_date())
# print(s.update_date())
# print(s.registrant())
# print(s.nameservers())
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
