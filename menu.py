menu={
    'Pizza':40,
    'Burger':60,
    'Pasta':50,
    'Salad':70,
    'Coffee':80,
}
print('Welcome to python Cafe')
print("Pizza: Rs40\nBurger: Rs60\nPasta: Rs50\nSalad: Rs70\nCoffee: Rs80")
orderTotal=0
item1=input("Enter the name of item you want to order: ")
if item1 in menu:
    orderTotal+=menu[item1]
    print(f"{item1} added to your order")
    
else:
    print(f"{item1} is not available yet")
anotherItem=input("Do you want to order another item? (yes/no): ")
if anotherItem=='yes':
    item2=input("Enter the name of item you want to order: ")
    if item2 in menu:
        orderTotal+=menu[item2]
        print(f"{item2} added to your order")
    else:
        print(f"{item2} is not available yet")
print(f"Your total order amount is: {orderTotal}")
print("Thank you for ordering from Python Cafe")