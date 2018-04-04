from setuptools import setup

try:
    unicode
    def u8(s):
        return s.decode('unicode-escape').encode('utf-8')
except NameError:
    def u8(s):
        return s.encode('utf-8')

setup(name='nobug',
      version='0.3.0',
      description=u8('no bug no bug'),
      author='Les1ie',
      author_email = 'iansmith@qq.com',
      url="https://github.com/IanSmith123/nobug",
      packages=['nobug'],
      )

