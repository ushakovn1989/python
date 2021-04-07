import re


class NotNumber(Exception):
    def __init__(self, string):
        print(f"{string} is not number")


is_number = re.compile(r"^[-+]?\d+[\.]?\d*$")

numbers = []
while True:
    try:
        user_input = input("Enter the number: ")
        if user_input.lower() == "stop":
            break
        elif re.search(is_number, user_input):
            numbers.append(float(user_input) if user_input.count(".") else int(user_input))
        else:
            raise NotNumber(user_input)
    except NotNumber:
        continue
print(numbers)
