import re

from whosearch import WhoisSearch


m = WhoisSearch(dname='google.com.au')



txt = m.single_search()

#print txt

# txt = 'Creation Date: 1998-10-21T04:00:00Z\n' \
#         'Updated Date: 2013-09-18T09:17:35Z\n' \
#         'Registry Expiry Date: 2014-10-20T04:00:00Z\n' \
#         'Sponsoring Registrar: MarkMonitor Inc.\n' \
#         'Sponsoring Registrar IANA ID: 292\n' \
#         'WHOIS Server: \n' \
#         'Referral URL: \n' \
#         'Domain Status: clientDeleteProhibited\n' \
#         'Domain Status: clientTransferProhibited\n' \
#         'Domain Status: clientUpdateProhibited\n' \
#         'Admin Email: dns-admin@google.com\n' \
#         'Registrant ID: mmr-32097\n' \
#         'Registrant Name: DNS Admin\n' \
#         'Registrant Organization: Google Inc.\n' \
#         'Registrant Street: 1600 Amphitheatre Parkway\n' \
#         'Registrant City: Mountain View\n' \
#         'Registrant State/Province: CA\n' \
#         'Registrant Postal Code: 94043\n' \
#         'Registrant Country: US\n' \
#         'Registrant Phone: +1.6506234000\n' \
#         'Registrant Phone Ext: \n' \
#         'Registrant Fax: +1.6506188571\n' \
#         'Registrant Fax Ext: \n' \
#         'Registrant Email: dns-admin@google.com\n' \
#         'Tech Email: dns-admin@google.com\n' \
#         'Name Server: NS2.GOOGLE.COM\n' \
#         'Name Server: NS1.GOOGLE.COM\n' \
#         'Name Server: NS3.GOOGLE.COM\n' \
#         'Name Server: NS4.GOOGLE.COM\n'

creation_date_map = {'org' \
                          : 'Creation Date:\s*(.+)'}

updated_date_map = {'org' \
                          : 'Updated Date:\s*(.+)'}

expiry_date_map = {'org' \
                          : 'Expiry Date:\s*(.+)'}


email_map = {'org' \
                    : 'Email:\s*(.+)'}

registrant_map = {'org' \
                  : 'Registrant\s*(.+)'}


nameserver_map = {'org' \
                  : 'Name Server:\s*(.+)'}


cdate = creation_date_map['org']
udate = updated_date_map['org']
edate = expiry_date_map['org']
email = email_map['org']
registrant = registrant_map['org']
nameserver = nameserver_map['org']



for item in re.findall(cdate, txt):
    print "Creation Date: %s" % item
    
for item in re.findall(udate, txt):
    print "Updated: %s" % item
    
for item in re.findall(edate, txt):
    print "Expiry Date: %s" % item
    
for item in re.findall(email, txt):
    print "Email: %s" % item

for item in re.findall(nameserver, txt):
    print "Name Servers: %s" % item
     
    
    
    