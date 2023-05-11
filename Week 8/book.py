class Book:
    """
    A class to represent a book.

    Attributes:
        name (str): The name of the book.
        author (str): The author of the book.
        genre (str): The genre of the book.
        year (int): The year the book was published.
    """
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


# python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
# everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

# print(f"{python.author}: {python.name} ({python.year})")
# print(f"The genre of the book {everest.name} is {everest.genre}")

class Checklist:
    """
    Represents a checklist with a header and a list of entries.
    """

    def __init__(self, header: str, entries: list):
        self.header = header
        self.entries = entries

        

class Customer:
    """
    Represents a customer object with an ID, balance, and discount percentage.

    Attributes:
    - id (str): A string representing the customer's unique ID.
    - balance (float): A float representing the customer's balance.
    - discount (int): An integer representing the customer's discount percentage.
    """
    def __init__(self, id: str, balance: float, discount: int) -> None:
        self.id = id
        self.balance = balance
        self.discount = discount
        
class Cable:
    """A class representing a cable.

    Attributes:
    -----------
    string : str
        The type of cable.
    length : float
        The length of the cable.
    max_speed : int
        The maximum speed that can be transmitted through the cable.
    bidirectional : bool
        A boolean indicating whether the cable is bidirectional or not.
    """
    
    def __init__(self, string: str, length: float, max_speed: int, bidirectional: bool) -> None:
        self.string =  string
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional

    

        
