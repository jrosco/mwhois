from distutils.core import setup


setup(  name='mwhois',
        version='0.1.10b',
        author='Joel Cumberland',
	author_email='joel_c@zoho.com',
	url='http://jrosco.github.io/mwhois/',
        license='GPL',
        package_dir={'mwhois2': 'src'},
        py_modules=['whoisconn', 'whoismap', 'whoissearch','const']
      )
