import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3 import disable_warnings

class RestTemplate(object):

    def __init__(self, url=None, username=None, password=None):
        self.url = url
        self.username = username
        self.password = password
        self.auth = HTTPBasicAuth(username, password)
        self.content_type = {'Content-Type': 'application/xml'}
        self.accept_header = {'Accept': 'application/xml'}
        disable_warnings()
        
    def set_base_ur(self, url):
        self.url = url
        
    def get_base_url(self):
        return self.url
    
    def post(self, rest_resource, entity):
        r = requests.post(self.url + "/" + rest_resource, verify=False, self.auth, headers=self.content_type, data=entity)
        return r.text
    
    def get_all(self, rest_resource):
        r = requests.get(self.url + "/" + rest_resource, verify=False, self.auth, headers=self.accept_header)
        return r.text
    
    def get_by_id(self, rest_resource, entity_id):
        r = requests.get(self.url + "/" + rest_resource + "/" + entity_id, verify=False, self.auth, headers=self.accept_header)
        return r.text

    def put(self, rest_resource, entity):
        r = requests.put(self.url + "/" + rest_resource, verify=False, self.auth, headers=self.content_type, data=entity)
        return r.text
    
    def delete(self, rest_resource, entity_id):
        requests.delete(self.url + "/" + rest_resource + "/" + entity_id, verify=False, self.auth, headers=self.accept_header)