#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
first= float(input("enter the amount: "))
second=float(input("enter the amount: "))
third= float(input("enter the amount: "))
fourth=float(input("enter the amount: "))
fifth= float(input("enter the amount: "))
subtotal= (first)+(second)+(third)+(fourth)+(fifth)
taxes=subtotal*0.12
total = subtotal+taxes
taxes=round(taxes,2)
total=round(total,2)
print(f"your subtotal is ${subtotal} and your taxes total ${taxes} of a total of ${total}")