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
# 
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
