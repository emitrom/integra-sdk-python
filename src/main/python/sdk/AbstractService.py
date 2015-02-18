'''

'''
import abc

class AbstractService(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create(self, entity):
        """Creates an entity and returns the persisted instance."""
        return
    
    @abc.abstractmethod
    def getAll(self):
        """Gets a collection of entities"""
        return
    
    @abc.abstractmethod
    def getById(self, entity_id):
        """Gets an entity given its id"""
        return
    
    @abc.abstractmethod
    def update(self, entity):
        """Updates an entity and returns the persisted/updated entity"""
        return
    
    @abc.abstractmethod
    def delete(self, entity_id):
        """Deletes an entity given its id"""
    
    