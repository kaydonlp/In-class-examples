 # Working with Data, Cash Register Activities
#Kaydon Payne
#Programming Python 1 & 2
# September, 9th 2019


#Starting Amounts / information
numItems = 4
costPerItem = 15.75
subTotal = numItems * costPerItem
taxRate = 0.08
taxAmount = subTotal * taxRate
totalPrice = subTotal  + taxAmount


#Making easier print functions, rather than converting more numbers to string and convivinces
items = "Number of items: " + str(numItems)
cost = "Cost Per Item: " + "$" + str(costPerItem)
sub = "SubTotal: " + "$" + str(subTotal)
rate = "Tax Rate: " + str(taxRate)
tax = "Tax Amount: " + "$" + str(taxAmount)
total = "Total Price" + "$" + str(totalPrice)


print ("     Sale  Receipt     ")
print ("______________")
print(items)
print(cost)
print(sub)
print(rate)
print(tax)
print(total)
