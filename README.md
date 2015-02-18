# integra-sdk-python

- The Integra Python SDK can be used to seemelessly communicate with an Integra reactor.
- The Integra REST documentation and additional SDKs can be obtained at [Integra REST](http://docs.emitrom.com/docs/integra/1.0.0/downloads.html).
- The Integra documentation can be found at [Integra Docs](http://wiki.emitrom.com/wiki/index.php/Integra).

# Dependencies

- python 2.6+
- lxml
- [requests](http://docs.python-requests.org/en/latest/)
- integra_major_minor_build

# Build your own integra_major_minor_build

- Download the [Integra XSD](http://docs.emitrom.com/docs/integra/1.0.0/ns0.xsd).
- Install [pip](https://pip.pypa.io/en/latest/)
- pip install lxml
- pip install generateDS
- generateDS.py -o integra_major_minor_build.py integra.xsd 

#License

The Integra Python SDK is Open Source software released under the [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0.html).
