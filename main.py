import csv
class Item:
    #class attribute
    pay_rate = 0.8 # The pay rate afer 20% discount
    all = []
    
    
    def __init__(self, name: str,  price: int,quantity = 0):
        # Run validation to the recieved arguments
        assert price >= 0,f"Price {price}is not greater than or equal to zero"
        assert quantity >= 0
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actinos to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.quantity * self.price
    
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        

    #decorator for class method
    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=float(item.get("quantity")),

            )
    #control objects 
    def __repr__(self) -> str:
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

  

Item.instanciate_from_csv()
print(Item.all)


# print(Item.all)

# # print(item1.calculate_total_price())

# item2.apply_discount()
# print(item2.price)

# item1.pay_rate = 0.7
# item1.apply_discount()
# print(item1.price)


# print(Item.__dict__)# magic attributes for class level
# print(item1.__dict__) # magic attributes for instance level
