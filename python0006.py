number = int(input("Enter a number: "))
low = int(input("Enter the lower limit: "))
high = int(input("Enter the upper limit: "))

if low <= number <= high:
    print("The number lies within the range.")
else:
    print("The number does not lie within the range.")
