from distutils.core import setup

setup(
    name='integra-sdk',
    version='0.1.0',
    author='Emitrom Inc.',
    author_email='support@emitrom.com',
    packages=['integra'],
    url='http://pypi.python.org/pypi/integra-sdk/',
    license='LICENSE.txt',
    description='Integra SDK',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests == 2.5.1",
        "lxml == 3.4.2",
    ],
)