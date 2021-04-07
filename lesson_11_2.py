class DivByZero(Exception):
    def __init__(self):
        print("You cannot divide by zero.")


division = False
while not division:
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
        if divisor == 0:
            raise DivByZero()
    except ValueError:
        print("Incorrect input.")
        continue
    except DivByZero:
        continue
    division = round(dividend / divisor, 10)
print(f"Result: {division}")
