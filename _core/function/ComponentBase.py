import abc


class Component(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def set(): 
        raise NotImplemented

    @abc.abstractmethod
    def load(): 
        raise NotImplemented

    @abc.abstractmethod
    def create(): 
        raise NotImplemented

    @abc.abstractmethod
    def delete():
        raise NotImplemented
