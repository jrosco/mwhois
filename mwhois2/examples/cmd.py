import getpass
from optparse import OptionParser
import sys

import const as CONST
from whosearch import WhoisSearch
from exception import WhoException

class CLDisplay:
    
    def __init__(self):
       """Used by the progress_bar() to keep track of the percentage being used"""
       self.already = 0
    
    """Used by the advanced search, so the user can be shown the program is still running :) """
    def progress_bar(self, number, total,  char):
       percentage = int(100 - round(number*100.0/total))
       if percentage > 0:
           xchar = char * (percentage-self.already)
           self.already = percentage 
           sys.stdout.write(xchar)
           sys.stdout.flush()                                      
                
                
    """Counts the number of lines in a file for the progress_bar()"""
    def count_lines(self, file):
        linecount = 0
        f = open(file)
        it = iter(f)
        try: 
            while it.next():
                linecount += 1
        except StopIteration:
                    pass
        return linecount
    
    """Indents the command line CLDisplay to make it look pretty"""
    def format_this(self, word, indent):
        wcount = len(word)
        num = (indent - wcount)
        whitespace = " "
        format = whitespace * num
        return format
    
    def remove_whitespace(self, str):
        self.str = re.sub("\s+", "", str)
        return self.str
        
    def format_output(self,output):
         
         if output[0] == CONST.DOMAIN_ALIVE:
              show_this = CONST.FAIL+CONST.DOMAIN_FOUND+CONST.ENDC
         elif output[0] == CONST.DOMAIN_DEAD:
              show_this = CONST.OKBLUE+CONST.DOMAIN_NOT_FOUND+CONST.ENDC
         else:
              show_this = "Error"
          
         domain_txt = output[1]
         tab_space = self.format_this(domain_txt,30)
         
         return CONST.HEADER+domain_txt+CONST.ENDC + tab_space + show_this 
     
    def file_format_output(self,output):
         
         if output[0] == CONST.DOMAIN_ALIVE:
              show_this = CONST.DOMAIN_FOUND
         elif output[0] == CONST.DOMAIN_DEAD:
              show_this = CONST.DOMAIN_NOT_FOUND
         else:
              show_this = "Error"
          
         domain_txt = output[1]
         
         return domain_txt + "," + show_this 


def main():
    usage = "usage: %prog [options] -i [file-to-read-from] -o [file-to-write-too]\n \n Examples:\n mwhois -t net -i /tmp/wordlist -o /tmp/domains\n mwhois -s sourceforge.net\n mwhois --gui \n\nWordlists Found @ http://www.packetstormsecurity.org/Crackers/wordlists/"
    parser = OptionParser(usage=usage)

    try:
        parser.add_option("-t", "--tld", action="store", type="string", dest="tld",
                          help="--tld com/net/org/biz/edu/info - Search for these TLD's (Only use one of these tlds for each whois search")
        parser.add_option("-s", "--single", action="store_true", dest="single", help="Single domain search")
        parser.add_option("-a", "--advance", action="store_true", dest="advance", help="Advanced domain search")
        parser.add_option("-i", "--file-in", dest="filein",  type="string", help="File to read from")
        parser.add_option("-o", "--file-out", dest="fileout", type="string",  help="File to write to (csv format)")
#        parser.add_option("--sql", action="store_true", dest="sql", help="Connect to a MySQL database")
        
        parser.add_option("-d", action="store_true", dest="dead", help="Only display dead domains")
        
#         parser.add_option("--host", dest="host", type="string", help="Host address for MySQL database connection (Default 127.0.0.1)")
#         parser.add_option("--port", dest="port", type="int", help="Port to use for MySQL database connection (Default 3306)")
#         parser.add_option("--user", dest="user", type="string", help="User to use for MySQL database connection")
#         parser.add_option("-p", "--passwd", action='store_true', dest="passwd",  help="Prompt for a password to use with MySQL database connection")
#         parser.add_option("--database", dest="database", type="string", help="Database to use for MySQL database query")
#         parser.add_option("--table", dest="table", type="string", help="Table to use for MySQL database query")
#         parser.add_option("--column", dest="column", type="string", help="Column to use for MySQL database query")
#        parser.add_option("-g", "--gui", action="store_true", dest="gui", help="Start GUI Interface")

        (options, args) = parser.parse_args()
        
#         if len(sys.argv) == 1 or options.gui == True:
#             window = StartGUI()
#             window.main()
        
        if options.single == True:
            search = WhoisSearch(dname=sys.argv[2]).whois_search()
            print(search)
           
        else:
#             if options.sql == True:
#                 options.filein = options.fileout + ".tmp"
#                 if options.passwd == True:
#                     options.passwd = getpass.getpass()
#                 conn = WhoisServer()
#                 DBConnection().connection(options.user, options.passwd, options.host, options.port, options.database, options.table, \
#                                         options.column, options.filein)
            
            w = WhoisSearch(tld=options.tld,wordlist=options.filein,deadonly=options.dead)
            
            cl = CLDisplay()
            
            if options.advance == True:
                multi_search = w.deeper_search()
            else:
                multi_search = w.whois_multi_search()
            
            for i in multi_search:
                if options.fileout:
                    file_output = cl.file_format_output(i)
                    write_to_file = open(options.fileout, 'a').write(file_output+"\n")
                    #write_to_file.close()
                #cl_txt = cl.format_this(i,30)
                print(cl.format_output(i))

    except IOError as (errno, strerror):
        print("\nI/O error({0}): {1}".format(errno, strerror) +"\n")
        print(parser.get_usage())
        sys.exit()
    
    except KeyboardInterrupt:
        sys.exit()
   
    except WhoException as e:
        print("\nParameter Error %s\n" % (e))
        print(parser.get_usage())
        sys.exit()
        
        
if __name__ == "__main__":
        main()