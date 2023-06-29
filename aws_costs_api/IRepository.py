import abc

class IRepository(abc.ABC):
    @abc.abstractmethod
    def setConnectionString(self, connectionString: str):
        pass
    
    @abc.abstractmethod
    def dataExists(self, key) -> bool:
        pass
    
    @abc.abstractmethod
    def store(self, key, value):
        pass
    
    @abc.abstractmethod
    def get(self, key):
        pass
    
    @abc.abstractmethod
    def all(self):
        pass

