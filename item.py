import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def appy_increment(self,i_v):
        self.__price = self.__price + self.__price * i_v
    @property
    def price(self):
        return self.__price
    
    @property
    #read only attribute
    def name(self):
        return self.__name
    
    
    
    @name.setter
    def name(self,val):
        if len(val) >=10:
            raise Exception("The name is too long")
        else:
            self.__name = val
    
    
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"




        """
        abstraction: We should hide unneccessary information from instances
        abstraction principles achievable by __ before method called thsoe 
        private method. 
        make the method unaccessible from outside of the class. 
        
        Inheritence: Inherit parent class attributes and methods on the child class
        
        
        Encapsulation: private attributes through getter(@poperty) and setter(@name.setter)
        
        
        polymorphism: refers to many forms, is the ability to have different scenario to have different power of function
        single function does know , how to handle different entity or objects
        """