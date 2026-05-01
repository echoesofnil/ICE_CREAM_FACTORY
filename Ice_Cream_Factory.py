from reportlab.lib.pagesizes import A6
from reportlab.pdfgen import canvas
from datetime import datetime

print("''' WELCOME TO THE ICECREAM FACTORY '''")

flavours = {
    "vanilla" : {
        "ingredients" : {
            "milk" : 200, 
            "sugar" : 100, 
            "flavour" : 50,
                },
                "cost" : 55,},

    "chocolate" : {
        "ingredients" : {
            "milk" : 250,
            "sugar" : 150,
            "flavour" : 100,
                 },
                "cost" : 70,},

    "butterscotch" : {
        "ingredients" : {
            "milk" : 300,
            "sugar" : 200,
            "flavour" : 150,
                 },
                "cost" : 80,},

    "strawberry" : {
        "ingredients" : {
            "milk" : 350,
            "sugar" : 250,
            "flavour" : 200,
                 },
                "cost" : 50,},

    "blueberry" : {
        "ingredients" : {
            "milk" : 400,
            "sugar" : 300,
            "flavour" : 250,
                 },
                "cost" : 60,
    },
    "pineapple" :{
        "ingredients" : {
            "milk" : 450,
            "sugar" : 350,
            "flavour" : 300,
                 },
                "cost" : 35,},

    "mango" : {
        "ingredients" : {
            "milk" : 500,
            "sugar" : 400,
            "flavour" : 350,
                 },
                "cost" : 45,},
    }

resources = {
    "milk" : 2000,
    "sugar" : 1500,
    "flavour" : 500,
    "money" : 0,
    }

def check_resources(flavour):
    """Check if enough resources are available"""
    for item in flavours[flavour]["ingredients"]:
        if flavours[flavour]["ingredients"][item] > resources[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def deduct_resources(flavour):
    for item in flavours[flavour]["ingredients"]:
        resources[item] -= flavours[flavour]["ingredients"][item]

def print_receipt(flavour, price, cash, change):
    file_name = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    c = canvas.Canvas(file_name, pagesize=A6)
    width, height = A6

    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(width / 2, height - 30, "Nilakshi's ICECREAM FACTORY")

    c.setFont("Helvetica", 10)
    c.drawString(20, height - 60, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}")

    c.line(20, height - 70, width - 20, height - 70)

    c.drawString(20, height - 90, f"Flavour: {flavour.title()}")
    c.drawString(20, height - 105, f"Price: {price} rs")
    c.drawString(20, height - 120, f"Paid: {cash} rs")
    c.drawString(20, height - 135, f"Change: {change} rs")

    c.line(20, height - 150, width - 20, height - 150)

    c.drawCentredString(width / 2, height - 170, "Thank You! Visit Again!")

    c.save()
    import os
    os.startfile(file_name)   # Windows
    print(f"Receipt generated: {file_name}")

def ice_cream_factory():
    profit = 0
    is_on = True
    while is_on:
        choices = input("Which flavour of Icecream do you like:\n").lower()
        if choices in flavours:
            if check_resources(choices):
                price = flavours[choices]["cost"]
                cash = int(input(f"your total bill is {price}rs., please pay:\n"))
        
                if cash >= price:
                    deduct_resources(choices)
                    change = cash - price
                    profit += price
                    resources["money"] += price
                    print(f"Here is your 🍨 {choices} icecream, enjoy!")
                    print_receipt(choices, price, cash, change)

                    if change > 0:
                        print(f"Here is your change {change}rs.")
                else:
                    print("Not enough money, money refunded.")

        elif choices == "menu":
            print("\n--- PRICE LIST ---")
            for flavour in flavours:
                print(f"{flavour.title()}: {flavours[flavour]['cost']} rs.")
            print("\n--- RESOURCES ---")
            for item in resources:
                print(f"{item.title()}: {resources[item]}")
            print(f"\nTotal Profit: {profit} rs.\n")

        elif choices == "off":
            is_on = False
            print("Thank you for visiting the Icecream Factory! 🍨")

        else:
            print("Sorry! This flavour is not available right now.")

ice_cream_factory()
