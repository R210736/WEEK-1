try:
    x=(input("Enter the numerator"))
    y=(input("Enter the denominator"))
    division=float(x)/float(y)
    print("The Division of two numbers is",division)
except valueError:
    print("Enter either integers or floats(decimals)")
