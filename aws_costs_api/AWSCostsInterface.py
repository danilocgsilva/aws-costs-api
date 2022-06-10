import abc

class AWSCostsInterface(abc.ABC):

    @abc.abstractmethod
    def getCosts(self) -> dict:
        pass
    
    @abc.abstractmethod
    def setUniqueService(self, service: str):
        pass

