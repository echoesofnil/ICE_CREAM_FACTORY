# 🍦 Ice Cream Factory Simulator

A Python-based Ice Cream Factory Management System that allows users to order ice cream flavors, manage ingredient inventory, process payments, track profits, and automatically generate PDF receipts for each purchase.

## Features

> Multiple Ice Cream Flavors

> Inventory Management

> Resource Availability Checking

> Payment Processing

> Change Calculation

> Profit Tracking

> Automated PDF Receipt Generation

> Menu and Resource Reporting

> User-Friendly Command-Line Interface

---

## Available Flavors

| Flavor       | Price (Rs.) |
| ------------ | ----------- |
| Vanilla      | 55          |
| Chocolate    | 70          |
| Butterscotch | 80          |
| Strawberry   | 50          |
| Blueberry    | 60          |
| Pineapple    | 35          |
| Mango        | 45          |

---

## Technologies Used

* Python 3
* Dictionaries
* Functions
* ReportLab (PDF Generation)
* Datetime Module

---

## Project Structure

```python
flavours          # Ice cream menu with ingredients and prices
resources         # Available inventory

check_resources() # Verifies ingredient availability
deduct_resources()# Updates inventory after purchase
print_receipt()   # Generates PDF receipt
ice_cream_factory() # Main program loop
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ice-cream-factory.git
```

### Navigate to Project Folder

```bash
cd ice-cream-factory
```

### Install Required Library

```bash
pip install reportlab
```

### Run the Application

```bash
python ice_cream_factory.py
```

---

## Example Usage

```text
Which flavour of Icecream do you like:
chocolate

Your total bill is 70 rs., please pay:
100

Here is your 🍨 chocolate icecream, enjoy!

Receipt generated successfully.
Here is your change 30 rs.
```

---

## Commands

| Command      | Description                         |
| ------------ | ----------------------------------- |
| vanilla      | Order Vanilla Ice Cream             |
| chocolate    | Order Chocolate Ice Cream           |
| butterscotch | Order Butterscotch Ice Cream        |
| strawberry   | Order Strawberry Ice Cream          |
| blueberry    | Order Blueberry Ice Cream           |
| pineapple    | Order Pineapple Ice Cream           |
| mango        | Order Mango Ice Cream               |
| menu         | Display menu, resources, and profit |
| off          | Exit the application                |

---

## PDF Receipt Features

Each purchase automatically generates a PDF receipt containing:

* Factory Name
* Purchase Date & Time
* Selected Flavor
* Price
* Amount Paid
* Change Returned

---

## Learning Outcomes

This project helped me learn:

* Python Functions
* Dictionaries and Nested Data Structures
* Inventory Management Logic
* Payment Processing
* File Generation using ReportLab
* PDF Creation and Automation
* Resource Tracking
* Command-Line Application Development

---

## Future Improvements

* GUI Version using Tkinter
* Database Integration
* Sales Analytics Dashboard
* Customer Order History
* Inventory Refill System
* Online Ordering Support
* Employee Management Module

---

## Author

Developed by Nilakshi 🚀

A Python project focused on inventory management, billing automation, and PDF receipt generation.
