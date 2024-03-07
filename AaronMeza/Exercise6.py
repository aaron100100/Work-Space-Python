TAX_RATE = 0.05
TIP_RATE = 0.18

cost = float(input("Enter the cost of the meal: "))

#compute the tax and the tip
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip

#Display the result
print("The tax is %.2f and the tip is %.2f, making the total %.2f" %\
      (tax,tip,total))