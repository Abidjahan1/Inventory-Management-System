# Inventory Management System with OOP in Python

This project demonstrates a basic **Inventory Management System** built using **Object-Oriented Programming (OOP)** principles in Python. It reads item data from a CSV file and handles different item types such as generic items, phones, and keyboards.

## 📁 Project Structure

├── items.csv # CSV file with item data
├── item.py # Base Item class (encapsulation, abstraction)
├── keyboard.py # Keyboard subclass (inheritance & polymorphism)
├── phone.py # Phone subclass with additional attributes
├── main.py # Entry point demonstrating usage


## 📌 Key Features

- Read items from a CSV file
- Calculate total prices and apply discounts
- Create multiple item types (`Item`, `Phone`, `Keyboard`)
- Use of private attributes and getter/setter methods
- Apply object-oriented principles: Encapsulation, Abstraction, Inheritance, and Polymorphism

## 🧠 OOP Principles Used

### ✅ Encapsulation
- Attributes like `__name` and `__price` are private
- Accessed and modified using `@property` and `@name.setter`

### ✅ Abstraction
- Internal logic of validation and price calculation is hidden
- Private methods and attributes are not accessible outside

### ✅ Inheritance
- `Phone` and `Keyboard` classes inherit from `Item` class
- Can override attributes like `pay_rate`

### ✅ Polymorphism
- `apply_discount()` behaves differently based on the item type due to class-specific `pay_rate`

## 📦 Requirements

- Python 3.x
- No third-party libraries required

## 📊 CSV File Format (`items.csv`)

```csv
name,price,quantity
Phone,100,1
Laptop,1000,3
Cable,10,5
Mouse,50,5
Keyboard,75,5
