import os

ItemName = ["cola can", "sprite can", "mango drink", "sour patch", "skittles", "gummy bears"]
ItemPin = ["11", "22", "33", "44", "55", "66"]

while True: 
    print(" ~Hello!~ ")
    print(" ~Welcome to MA Vending Machine!~ ")
    print(" ~Our drinks selection consists of: ")

    print(f"{'Item':<30} {'Pin':<5}")
    print("-" * 40)

    for name, pin in zip(ItemName, ItemPin):
        dash_count = 30 - len(name) - 2
        dashes = "-" * dash_count
        print(f"{name} {dashes} {pin}")
        
    print("-"*40)
    
    while True:
            InputPin = input("Please enter the Pin of the item you want!: ")
            if InputPin in ItemPin:
                index = ItemPin.index(InputPin)
                print(f"Here is your Item!: {ItemName[index]}")
            else:
                print("This item Pin does not exist! Please try Again!")
                
            NewItem = input("\nWould you like to Get another item? (yes/no): ").lower()
            if NewItem != "yes":
                print("Thank you for using MA Vending Machine. Please enjoy yourself and have a good time!")
                break

    break
