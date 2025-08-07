from inputs import get_two_numbers
from calculator import add_and_print

while True:
    num1, num2 = get_two_numbers()
    add_and_print(num1, num2)
    again = input("Do you want to add more numbers? (yes/no) ").strip().lower()
    if again == "no":
        break
