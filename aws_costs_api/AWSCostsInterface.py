import abc

class AWSCostsInterface(abc.ABC):

    @abc.abstractmethod
    def getCosts(self):
        pass
