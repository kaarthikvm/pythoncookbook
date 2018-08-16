from distutils.core import setup, Extension
setup(name='hellocppext', version='1.0',  \
      ext_modules=[Extension('hellocppext', ['hello.cpp'])])
