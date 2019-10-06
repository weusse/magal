# Parent
class GotCharacter:
    """
    This a class for all GOT characters.
    Attributes:
    -----------
    name: string
    position: string
    is_alive: bool
    Method:
    ------
    speak(message: string) : return string
    """
    def __init__(self, name, x):
        self.__name = name
        self.position = x
        self.__isalive = True

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def isalive(self):
        return "Locked"

    @isalive.setter
    def isalive(self, isalive):
        self.__isalive = isalive

    def speak(self, message):
        print(f"You know nothing {self.name}! {message}")

    # Special Methods
    def __add__(self, other):
        return f"{self.name} is in a relationship with {other.name}"
    
    def __repr__(self):
        return self.position
    
    def __str__(self):
        return f"{self.isalive}"

    def __getitem__(self, other):
        return f"{self.name} killed {other.name}"

# Child Classes
class Stark(GotCharacter):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.hair_color = "dark"

jon = Stark("Jon Snow", "The Wall")
daenerys = GotCharacter("Daenerys Targaryen", "Mereen")