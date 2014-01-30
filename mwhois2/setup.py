from distutils.core import setup

version = '0.1.10a'

long_description = '''\
Multi-Whois is a small whois domain name search program capable of finding multiple available domains via a file or a list. 
It's a good way to search for domains that are available to buy.'''

setup( name='mwhois',
       version=version,
       long_description=long_description,
       author='Joel Cumberland',
	   author_email='joel_c@zoho.com',
	   url='http://jrosco.github.io/mwhois/',
       license='GPL',
       package_dir={'': 'src'},
       py_modules=['whoisconn', 'whoismap', 'whoissearch','const']
      )
