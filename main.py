from item import  Item
from keyboard import Keyboard
from phone import Phone


Item.instantiate_from_csv()
print(Item.all)
item1 = Item("NewItem",750)
item1.name ="Rename"

item2 = Keyboard("Joystick",1000,3)

#polymorphism in action
item2.apply_discount()
print(item2.price)

item1.appy_increment(0.2)
#
item1.apply_discount()
print(item1.price)


