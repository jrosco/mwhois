import MySQLdb
import whois

"""Create a wordlist from a mysql database"""
def db_conn(user, passwd, host, port, database, table, column, wordlist):

    if port == None:
        port = 3306

    if host == None:
        host = '127.0.0.1'

    try:
        db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=database)
        query = db.cursor()
        query.execute("SELECT %s FROM %s" % (column, table) ) 
        result = query.fetchall()
        wordlist = open(wordlist, 'w')
        for record in result:
                print >>wordlist, record[0]
    except Exception, e:
        print e
        
return wordlist


