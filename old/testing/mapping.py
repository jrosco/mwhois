server_map = {'org' : ['whois.publicinterestregistry.net','whois.domain.com','Status: free', 'WHOIS LIMIT EXCEEDED'], \
              'com' : ['whois.verisign-grs.com','whois.domain.com','Status: free', 'WHOIS LIMIT EXCEEDED']}

info_map = {'org' : ['Creation Date:\s*(.+)', 'Updated Date:\s*(.+)', 'Expiry Date:\s*(.+)', 'Registrant\s*(.+)','Name Server:\s*(.+)' ], \
            'com' : ['Creation Date:\s*(.+)', 'Updated Date:\s*(.+)', 'Expiry Date:\s*(.+)', 'Registrant\s*(.+)','Name Server:\s*(.+)' ]}

emails = {}

print server_map['org'][2]
print server_map['com'][0]

print info_map['org'][1]
print info_map['com'][3]