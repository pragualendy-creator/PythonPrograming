n = int(input("Enter a number: "))
square = n * n

if str(square).endswith(str(n)):
    print("Automorphic")
else:
    print("Not automorphic")
