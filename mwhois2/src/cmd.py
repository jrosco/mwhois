from optparse import OptionParser
import sys
import getpass

from whoissearch import WhoisSearch

def main():
    usage = "usage: %prog [options] -i [file-to-read-from] -o [file-to-write-too]\n \n Examples:\n mwhois -t net -i /tmp/wordlist -o /tmp/domains\n mwhois -s sourceforge.net\n mwhois --gui \n\nWordlists Found @ http://www.packetstormsecurity.org/Crackers/wordlists/"
    parser = OptionParser(usage=usage)

    try:
        parser.add_option("-t", "--tld", action="store", type="string", dest="tld",
                          help="--tld com/net/org/biz/edu/info - Search for these TLD's (Only use one of these tlds for each whois search")
        parser.add_option("-s", "--single", action="store_true", dest="single", help="Single domain search")
        parser.add_option("-a", "--advance", action="store_true", dest="advance", help="Advanced domain search")
        parser.add_option("-i", "--file-in", dest="filein",  type="string", help="File to read from")
        parser.add_option("-o", "--file-out", dest="fileout", type="string",  help="File to write to")
        parser.add_option("--sql", action="store_true", dest="sql", help="Connect to a MySQL database")
        
        parser.add_option("-d", action="store_true", dest="dead", help="Only display dead domains")
        
        parser.add_option("--host", dest="host", type="string", help="Host address for MySQL database connection (Default 127.0.0.1)")
        parser.add_option("--port", dest="port", type="int", help="Port to use for MySQL database connection (Default 3306)")
        parser.add_option("--user", dest="user", type="string", help="User to use for MySQL database connection")
        parser.add_option("-p", "--passwd", action='store_true', dest="passwd",  help="Prompt for a password to use with MySQL database connection")
        parser.add_option("--database", dest="database", type="string", help="Database to use for MySQL database query")
        parser.add_option("--table", dest="table", type="string", help="Table to use for MySQL database query")
        parser.add_option("--column", dest="column", type="string", help="Column to use for MySQL database query")
        parser.add_option("-g", "--gui", action="store_true", dest="gui", help="Start GUI Interface")

        (options, args) = parser.parse_args()
        
#         if len(sys.argv) == 1 or options.gui == True:
#             window = StartGUI()
#             window.main()
            
        if options.single == True:
            search = WhoisSearch(dname=sys.argv[2]).single_search()
            print(search)
           
        else:
#             if options.sql == True:
#                 options.filein = options.fileout + ".tmp"
#                 if options.passwd == True:
#                     options.passwd = getpass.getpass()
#                 conn = WhoisServer()
#                 DBConnection().connection(options.user, options.passwd, options.host, options.port, options.database, options.table, \
#                                         options.column, options.filein)
#             w = WhoisSearch(None, options.tld, options.filein, options.fileout, None)
            
            if options.advance == True:
                w.advance_search()
            else:
                print options.dead
                basic = WhoisSearch(tld=options.tld, wordlist=options.filein, deadonly=options.dead).basic_search()
#                 
#         try: os.remove(options.fileout + ".tmp")
#         except Exception, e: pass
#         
    except IOError as (errno, strerror):
        print "\nI/O error({0}): {1}".format(errno, strerror) +"\n"
        print parser.get_usage()
        sys.exit()
    
    except KeyboardInterrupt:
        sys.exit()
   
    except:
        print "\nParameter Error\n"
        print parser.get_usage()
        sys.exit()
        


if __name__ == "__main__":
        main()