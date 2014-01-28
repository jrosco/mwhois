Multi Whois Client
=====
*** 

Multi-Whois is a small whois domain name search program capable of finding multiple available domains via a file or a MySQL query. It's a good way to search for domains that are available to buy. (http://jrosco.github.io/mwhois)


Install 
====
***

Dependencies:
* Python >= 2.7.3 (Python 3 not supported yet) Download from http://www.python.org/download/
* Python Module wx (can still run mwhois without this module, but only with command line support)

1. Download zip file mwhois.zip https://github.com/jrosco/mwhois/archive/master.zip
2. Unzip mwhois.zip 
3. Windows Only. Ensure that python is in your environment variables e.g C:\Python27 
3. Run run.bat (windows) or run.sh (linux)

Note: For help run 'python mwhois.py --help' via the command line (without quotes). 

How to use
====

* * * 

Run with GUI: 
---
<code> Run run.bat (windows) or run.sh (Linux) </code>

You can either search for a single domain or use a list of names to search for and provide a tld to use e.g .com. A sample file can be found in files/wordlist-sample from the download. To search multiple domains select the "Multi Search" tab and open the file to use, don't worry about selecting a save file this will be done for you, but if you would like to specify a file for saving the the output use the save file function. Now select a tld to use (ATM only a few to choose from) then hit the begin button. Now you'll see all available domains from the wordlist you selected to search.  


Run via command line: 
---
<pre>
Usage: mwhois.py [options] -i [file-to-read-from] -o [file-to-write-too] 
 
Examples:
mwhois -t net -i /tmp/wordlist -o /tmp/domains
mwhois -s sourceforge.net

Options:
  -h, --help            show this help message and exit
  -t TLD, --tld=TLD     --tld com/net/org/biz/edu/info - Search for these
                        TLD's (Only use one of these tlds for each whois
                        search
  -s, --single          Single domain search
  -a, --advance         Advanced domain search
  -i FILEIN, --file-in=FILEIN
                        File to read from
  -o FILEOUT, --file-out=FILEOUT
                        File to write to
  --sql                 Connect to a MySQL database
  --host=HOST           Host address for MySQL database connection (Default
                        127.0.0.1)
  --port=PORT           Port to use for MySQL database connection (Default
                        3306)
  --user=USER           User to use for MySQL database connection
  -p, --passwd          Prompt for a password to use with MySQL database
                        connection
  --database=DATABASE   Database to use for MySQL database query
  --table=TABLE         Table to use for MySQL database query
  --column=COLUMN       Column to use for MySQL database query
  -g, --gui             Start GUI Interface

</pre>

Contact
===
***

joel_c at zoho dot com
