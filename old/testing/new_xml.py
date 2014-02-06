import xml.etree.ElementTree as ET

tree = ET.parse('../files/mwhois.xml')
root = tree.getroot()

for info in root.findall('host'):
    
    tag = info.tag
    first = info.get('hostname')
    tld = info.get('tld')
    
    if tld == 'com':
        print(first, tld)
        print(root[0][1].text)
        
        
for neighbor in root.iter('host/domaininfo'):
    print(neighbor.attrib)