import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3 import disable_warnings
import cStringIO
import integra

class RestTemplate(object):

    ROOT                            = '/'
    PROVIDERS                       =   ROOT + 'providers'
    PROVIDER_ACTIONS                =   ROOT + 'provider_actions'
    WORKFLOW_ACTIONS                =   ROOT + 'workflow_actions'
    WORKFLOWS                       =   ROOT + 'workflows'
    SCHEDULES                       =   ROOT + 'schedules'
    SCHEDULES_RESULTS               =   ROOT + 'schedules_results'
    CONFIGURATIONS                  =   ROOT + 'configurations'
    LICENSES                        =   ROOT + 'licenses'

    TAGS                            =   ROOT + 'tags'
    PROVIDER_TAGS_FULLPATH          =   TAGS + '/' + 'provider_tags'
    WORKFLOW_ACTION_TAGS_FULLPATH   =   TAGS + '/' + 'workflow_actions_tags'
    WORKFLOW_TAGS_FULLPATH          =   TAGS + '/' + 'workflow_tags'
    SCHEDULE_TAGS_FULLPATH          =   TAGS + '/' + 'schedule_tags'
    
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        
    def init(self, url=None, username=None, password=None):
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
        r = requests.post(self.url + "/" + rest_resource, verify=False, auth=self.auth, headers=self.content_type, data=self.toxml(entity))
        return integra.parseString(r.content, True)
     
    def get_all(self, rest_resource):
        r = requests.get(self.url + "/" + rest_resource, verify=False, auth=self.auth, headers=self.accept_header)
        return integra.parseString(r.content, True)
     
    def get_by_id(self, rest_resource, entity_id):
        r = requests.get(self.url + "/" + rest_resource + "/" + str(entity_id), verify=False, auth=self.auth, headers=self.accept_header)
        return integra.parseString(r.content, True)
 
    def put(self, rest_resource, entity):
        r = requests.put(self.url + "/" + rest_resource, verify=False, auth=self.auth, headers=self.content_type, data=self.toxml(entity))
        return integra.parseString(r.content, True)
     
    def delete(self, rest_resource, entity_id):
        requests.delete(self.url + "/" + rest_resource + "/" + str(entity_id), verify=False, auth=self.auth, headers=self.accept_header)
        
    def toxml(self, entity):
        try:
            output = cStringIO.StringIO()
            entity.export(output, 0)
            return output.getvalue()
        except Exception:
            raise
        finally:
            output.close()
