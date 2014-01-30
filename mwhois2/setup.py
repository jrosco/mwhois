from distutils.core import setup

setup(  name='mwhois',
        version='0.1.10b',
        author='Joel Cumberland',
        license='GPL',
        package_dir={'': 'src'},
        py_modules=['whoisconn', 'whoismap', 'whoissearch','const']
      )