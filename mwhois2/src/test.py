from whosearch import WhoisSearch

dlist = ['foo', 'goololololo', 'lolololo', 'dfdfgfgfgf', 'insp']
x = WhoisSearch(debug=True)

x.wordlist=dlist
x.tld='org'
s = x.whois_multi_search()

for i in s:
    print(i)
 
