print("===== SIMPLE BILLING SYSTEM =====")

name = input("Enter Customer Name: ")

item1 = input("Enter Item 1: ")
price1 = float(input("Enter Price: "))
qty1 = int(input("Enter Quantity: "))

item2 = input("Enter Item 2: ")
price2 = float(input("Enter Price: "))
qty2 = int(input("Enter Quantity: "))

item3 = input("Enter Item 3: ")
price3 = float(input("Enter Price: "))
qty3 = int(input("Enter Quantity: "))

total1 = price1 * qty1
total2 = price2 * qty2
total3 = price3 * qty3

total = total1 + total2 + total3
gst = total * 0.05
grand_total = total + gst

print("\n========== BILL ==========")
print("Customer:", name)
print("--------------------------")
print(item1, "x", qty1, "=", total1)
print(item2, "x", qty2, "=", total2)
print(item3, "x", qty3, "=", total3)
print("--------------------------")
print("Total:", total)
print("GST (5%):", gst)
print("Grand Total:", grand_total)
print("==========================")
print("Thank You!")
