# Write a program to accept Item Name,Quantity, Rate.
# Calculate Total Cost as Quantity * Rate
# Calculate discount as following
# if Total Cost >=10000, Discount = 7.5%
# if Total Cost >=7500, Discount = 6.15%
# if Total Cost >=5000, Discount = 4.95%
# else discount is 3.25%
# Display Item name, Total cost and Discount

item_name = input("Enter Item Name : ")
quantity = int(input("Enter the Quantity : "))
rate = float(input("Enter Rate : "))

total_cost = quantity * rate

if total_cost >= 10000 :
    discount_amount = total_cost * 0.075
elif total_cost >= 7500 :
    discount_amount = total_cost * 0.0615
elif total_cost >= 5000 :
    discount_amount = total_cost * 0.0495
else :
    discount_amount = total_cost * 0.0325

print ("The item is :",item_name)
print ("The Total cost is : ", total_cost)
print ("The Discount amount is : ", discount_amount)