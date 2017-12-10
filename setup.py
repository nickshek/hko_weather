from distutils.core import setup
setup(
  name = 'hko_weather',
  packages = ['hko_weather'], # this must be the same as the name above
  scripts=['bin/hko_weather'],
  version = '0.1',
  description = 'A HKO Weather Library',
  author = 'Nick Shek',
  author_email = 'alfshek@hotmail.com',
  url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['HKO','Weather'], # arbitrary keywords
  install_requires=[
      'requests==2.18'
  ],
  classifiers = [],
)