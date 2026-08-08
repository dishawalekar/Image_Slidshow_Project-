# Abtraction 
""" fidine sound how iy works """
from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound (self):
        pass

class dog(Animal):
    pass
a= Animal()    