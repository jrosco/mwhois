from whosearch import WhoisSearch
 
s = WhoisSearch(debug=False)
s.dname = 'yahoo.org'
 
s.whois_search()
 
print(s.creation_date())
 
print(s.expiry_date())
 
print(s.update_date())
 
print(s.nameservers())
 
print(s.registrant())
 
print(s.whois_status())

#print(s.response())