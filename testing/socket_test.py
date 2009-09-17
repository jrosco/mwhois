import MySQLdb

    
def db_conn(user, passwd, host, database, table, wordlist):
   
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)
    query = db.cursor()
    query.execute("SELECT * FROM %s" % (table) ) 
    result = query.fetchall()
    wordlist = open(wordlist, 'w')
    count = 0
    for record in result:
            print record[0]
            

     

