from test.ServiceTest import ServiceTest
from main.python.sdk.RestTemplate import RestTemplate
from main.python.sdk.integra import provider

class ProviderServiceTest(ServiceTest):

    description = 'test desc'
    hostname = 'localhost'
    name = 'test name'
    password = 'password'
    port = 9999
    timeout = 1000
    
    def tearDown(self):
        providers = RestTemplate().get_all(RestTemplate.PROVIDERS)
        for provider in providers.provider:
            if provider.name == self.name:
                RestTemplate().delete(RestTemplate.PROVIDERS, provider.id)
    
    def test_create(self):
        prov = self._get_provider()
        
        prov = RestTemplate().post(RestTemplate.PROVIDERS, prov)
        self.assertIsNotNone(prov, 'Unable to create provider')
        self.assertIsNotNone(prov.get_id())
        
    def test_get_all(self):
        providers = RestTemplate().get_all(RestTemplate.PROVIDERS)
        self.assertIsNotNone(providers, 'Unable to retrieve providers')

    def test_get_by_id(self):
        prov = self._get_provider()
        prov = RestTemplate().post(RestTemplate.PROVIDERS, prov)
        self.assertIsNotNone(prov, 'Unable to create provider')
        self.assertIsNotNone(prov.get_id())
        
        prov = RestTemplate().get_by_id(RestTemplate.PROVIDERS, prov.get_id())
        self.assertIsNotNone(prov, 'Unable to create provider')
        self.assertIsNotNone(prov.get_id())
 
    def test_update(self):
        prov = self._get_provider()
        
        prov = RestTemplate().post(RestTemplate.PROVIDERS, prov)
        self.assertIsNotNone(prov, 'Unable to create provider')
        self.assertIsNotNone(prov.get_id())

        prov.description = 'new desc'
        prov = RestTemplate().put(RestTemplate.PROVIDERS, prov)
        
        self.assertIsNotNone(prov, 'Unable to create provider')
        self.assertIsNotNone(prov.get_id())
        self.assertTrue(prov.description == 'new desc', 'Unable to update provider')

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
