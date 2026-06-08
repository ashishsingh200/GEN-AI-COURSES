# Assignment 7 — Object Oriented Programming (OOP)

## Overview

All tasks in Assignment 7 have been successfully completed. This assignment covered all four pillars of Object Oriented Programming — Encapsulation, Inheritance, Polymorphism, and Abstraction — along with Magic Methods and a Mini Inventory System project.

---

## Tasks Completed

### Task 1 — Basic Class with Attributes and Methods
- Created a `Product` class with attributes: `name`, `price`, `category`, `discount` (default = 0)
- Implemented `get_info()` — prints product details
- Implemented `apply_discount()` — calculates and prints price after discount
- **Extra:** Added `discount` as a default parameter set to 0
- Created two objects `obj1` (no discount) and `obj2` (15% discount) and tested both methods

### Task 2 — Encapsulation (Getters and Setters)
- Created a `Product` class with `_price` as a **protected attribute**
- Implemented `get_price()` — getter to read price
- Implemented `set_price(new_price)` — setter with validation (rejects negative values)
- Demonstrated setting invalid price (`-43`) and valid price (`50`)

### Task 3 — Inheritance
- Created `ElectronicProduct` class inheriting from `Product`
- Added `warranty_years` attribute
- Overrode `get_info()` to include discount and warranty info
- Used `super().__init__()` to call parent constructor
- Used `super().get_info()` to call parent method

### Task 4 — Polymorphism
- Created `Laptop` and `Mobile` classes both inheriting from `Product`
- Both override `get_info()` with different output — same method, different behavior
- Created a list containing both `Laptop` and `Mobile` objects
- Looped through the list calling `get_info()` — demonstrates polymorphism

### Task 5 — Abstraction
- Imported `ABC` and `abstractmethod` from `abc` module
- Created abstract class `Payment` with abstract method `process_payment(amount)`
- Implemented `CreditCardPayment` — prints credit card payment message
- Implemented `UPIPayment` — prints UPI payment message
- Tested both classes with different amounts

### Task 6 — Magic Methods (Operator Overloading)
- Created `Product1` class with `__str__` and `__add__` magic methods
- `__str__` — returns formatted product details when `print(obj)` is called
- `__add__` — combines two products' names and sums their prices
- Tested with `prod1 + prod2` returning a new combined `Product1` object

### Task 7 — Mini Project: Simple Inventory System
- Created three classes — `Product`, `Inventory`, `Store`
- `Product` — stores name, price, category with `__str__` and `__add__`
- `Inventory` — manages a list of products with:
  - `add_product(product)` — adds a Product object
  - `remove_product(name)` — removes by name
  - `get_total_value()` — sums all prices
  - `show_all_products()` — prints all products
- `Store` — wraps Inventory with:
  - `add_new_product()` — takes input and creates Product object
  - `show_summary()` — prints total items and total value
- Tested by creating a store, adding 3 products, showing summary, combining with `__add__`, and removing a product

---

## OOP Concepts Covered

| Concept | Used in |
|---|---|
| Class & Object | Task 1, all tasks |
| `__init__` constructor | Task 1, all tasks |
| Instance attributes | Task 1, all tasks |
| Default parameters | Task 1 |
| Encapsulation (`_protected`) | Task 2 |
| Getters & Setters | Task 2 |
| Single Inheritance | Task 3, Task 4 |
| `super()` | Task 3, Task 4 |
| Method Overriding | Task 3, Task 4 |
| Polymorphism | Task 4 |
| Abstraction (`ABC`) | Task 5 |
| `@abstractmethod` | Task 5 |
| `__str__` magic method | Task 6, Task 7 |
| `__add__` magic method | Task 6, Task 7 |
| Operator Overloading | Task 6, Task 7 |
| Composition (Store has Inventory) | Task 7 |

---

## File Structure

```
GEN AI Assignment-7(Ashish)/
│
├── README.md
├── Task1.ipynb
│
└── images/
    ├── task1.png
    ├── task2.png
    ├── task3.png
    ├── task4.png
    ├── task5.png
    ├── task6.png
    └── task7.png
```

---

## Notes

- No external libraries used — only built-in Python and `abc` module
- All four OOP pillars covered across tasks
- Magic methods `__str__` and `__add__` implemented and tested
- Mini project (Task 7) combines all OOP concepts into one working system
- Only OOP concepts used — no file handling, no exceptions, no packages

---

*Assignment 7 — Completed Successfully*
