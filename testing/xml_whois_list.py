import urllib2
import xml.etree.ElementTree 
from xml.etree import ElementTree
import os.path

URL='http://serverlist.domaininformation.de/'
XML_FILE='.serverlist.xml'

def get_xml_whois_servers(url):
    
    print "Getting XML file from %s" % (URL)
    
    try:
        repsonse = urllib2.urlopen(url=url, timeout=30)
        xml = repsonse.read()
        return str(xml)
    except:
        print "Error getting XML file from %s" % (URL)
        return False
    
def write_xml_whois_list(file, force):
    
    if os.path.isfile(XML_FILE) and force == False:
        print "Already Exist"
        return False
    
    else:
        print "Writing XML file to %s" % (XML_FILE)
        try:
            file = open(file, 'w')
            file.write(get_xml_whois_servers(URL))
            file.close()
            return True
        except:
            return False

def build_element_tree():
    
    root = ElementTree.parse(source=XML_FILE).getroot()
    return root
    

write_xml_whois_list(file=XML_FILE, force=False)
xml_tree = build_element_tree()

for x in xml_tree.findall('server'):
    
    tld = x.find('domain')
    ava = x.find('availstring')

    try: 
        #if tld.get('name') == "net": #and ava.text != None:
        #print "'%s' : '%s', /" % (tld.get('name'), x.attrib['host']) 
        print "'%s' : '%s', /" % (tld.get('name'), ava.text) 
    except Exception, e:
        foo = e
        #print e
     