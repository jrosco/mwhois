from distutils.core import setup

version = '0.1.0b'

long_description = '''\
Whois cleint capable of finding multiple available domains via a file or list type. 
It's a good way to search for domains that are available to buy.'''

setup( name='mwhois-cleint',
       version=version,
       long_description=long_description,
       author='jrosco',
       author_email='joel_c@zoho.com',
       license='GPL',
       package_dir={'mwhois-client': 'src'},
       packages=['mwhois-client'],
       #py_modules=['whois', 'whoconnect', 'whomap', 'whosearch','const']
      )
