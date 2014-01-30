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