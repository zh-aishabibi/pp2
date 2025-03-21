try:
    t = tuple(map(int,input("elements of tuple: ").split()))
    print(all(t))

except ValueError:
    print("Error: Please enter only numbers.")
