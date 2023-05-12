
import threading


current_balance = 1000


def pasaload(from_number, to_number, amount):

    global current_balance

    if amount > current_balance:
        print("Error: Insufficient balance")
    else:

        print(f"Pasaload {amount} PHP from {from_number} to {to_number}")
        current_balance -= amount
        print(f"Current balance: {current_balance} PHP")


while True:
    from_number = input("Enter your phone number: ")
    to_number = input("Enter the recipient's phone number: ")
    amount = int(input("Enter the amount to pasaload: "))

    thread = threading.Thread(
        target=pasaload, args=(from_number, to_number, amount))
    thread.start()

    choice = input("Do you want to pasaload again? (Y/N) ")
    if choice.lower() != "y":
        break

print("Exiting...")
