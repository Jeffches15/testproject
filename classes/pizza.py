# 1. Instance Methods
    # The most common type of method.
    # Take self as the first argument.
    # Can access and modify instance-level data.

# 2. Class Methods
    # Use the @classmethod decorator.
    # Take cls (the class itself) as the first argument.
    # Can access and modify class-level data (shared across instances).

# 3. Static Methods
    # Use the @staticmethod decorator.
    # Don’t take self or cls as the first argument.
    # Act like regular functions but live inside a class for logical grouping.

# A class variable is shared across all instances of the class. 
    # It’s defined directly inside the class, outside any methods.

# An instance variable is specific to each object (instance) 
    # and is usually set inside the __init__ method with self..


class Pizza:
    # Class attribute
    default_size = "Medium"

    def __init__(self, toppings):
        self.toppings = toppings  # instance attribute

    # Instance Method
    def describe(self):
        return f"This pizza has {', '.join(self.toppings)}."

    # Class Method
    @classmethod
    def change_default_size(cls, new_size):
        cls.default_size = new_size

    # Static Method
    @staticmethod
    def oven_temperature():
        return "Bake at 425°F for 15 minutes"
