n = int(input("Enter a decimal number: "))

b = bin(n)
h = hex(n)

print("Binary =", b[2:])
print("Hexadecimal =", h[2:])