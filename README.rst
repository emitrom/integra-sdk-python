==================
integra-sdk-python
==================

* The Integra Python SDK can be used to seemelessly communicate with an Integra reactor.
* The Integra REST documentation and additional SDKs can be obtained at `Integra REST`_.
* The Integra documentation can be found at `Integra Docs`_.

.. _Integra REST: http://docs.emitrom.com/docs/integra/1.0.0/downloads.html
.. _Integra Docs: http://wiki.emitrom.com/wiki/index.php/Integra

Dependencies
============

* python 2.6+
* lxml
* requests
* integra_major_minor_build

Build your own integra_major_minor_build
========================================

* Download the `Integra XSD`_.
* Install `pip`_
* pip install lxml
* pip install requests
* pip install generateDS
* generateDS.py -o integra_major_minor_build.py integra.xsd
 
.. _Integra XSD: http://docs.emitrom.com/docs/integra/1.0.0/ns0.xsd
.. _pip: https://pip.pypa.io/en/latest/

Usage
=====

1- Init RestTemplate::

 RestTemplate().init('https://localhost:8443/rest', 'admin', 'integra')

2- Invoke RestTemplate REST methods:

* post  
* get_all  
* get_by_id  
* put  
* delete  

RestTemplate contains a static list of REST resource end points. Example putting it all together; creating a provider::

 class ProviderServiceTest(unittest.TestCase):

  description = 'test desc'
  hostname = 'localhost'
  name = 'test name'
  password = 'password'
  port = 9999
  timeout = 1000
    
  def setUp(self):
   RestTemplate().init('https://localhost:8443/rest', 'admin', 'integra')

  def test_create(self):
   prov = self._get_provider()
        
   prov = RestTemplate().post(RestTemplate.PROVIDERS, prov)
   self.assertIsNotNone(prov, 'Unable to create provider')
   self.assertIsNotNone(prov.get_id())
      
  def _get_provider(self):
   prov = provider()
   prov.set_description(self.description)
   prov.set_hostname(self.hostname)
   prov.set_name(self.name)
   prov.set_password(self.password)
   prov.set_port(self.port)
   prov.set_secured(True)
   prov.set_timeout(self.timeout)
      
   return prov
      
 if __name__ == "__main__":
  unittest.main()

License
=======

The Integra Python SDK is Open Source software released under the `Apache 2.0 license`_.

.. _Apache 2.0 license: http://www.apache.org/licenses/LICENSE-2.0.html
