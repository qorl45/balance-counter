import os
import time
from datetime import datetime
import json

transactions = []
balance = 0
a = 1

def main_menu():
    global balance
    global transactions
    global a

    nowtime = datetime.now()
    formatted = nowtime.strftime("%Y-%m-%d %H:%M:%S")

    print("Welcome to balance counter!")
    print(" ")
    print("1) add income")
    print("2) add expense")
    print("3) see balance")
    print("4) exit")
    print("5) transaction history")
    print("6) dump to json")
    print("7) load json transactions")

    op = int(input(">"))

    if op == 1:
        income_added = int(input("Enter an amount of money to add to balance: "))
        balance += income_added
        print(f"Updated balance: {balance}")
        transactions.append((f"{a})", income_added, formatted))
        a += 1

    elif op == 2:
        income_deduced = int(input("Enter an amount of money to deduct from balance: "))
        balance -= income_deduced
        print(f"Updated balance: {balance}")
        transactions.append((f"{a})", -income_deduced, formatted))
        a += 1

    elif op == 3:
        print(f"Current balance: {balance}")
        time.sleep(6)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif op == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Exiting...")
        time.sleep(3)
        quit()

    elif op == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("TRANSACTION HISTORY:")
        print(" ")
        for transaction in transactions:
            print(transaction)
        time.sleep(15)
        os.system('cls' if os.name == 'nt' else 'clear')

    elif op == 6:
        namejs = input("Enter a json filename (where to dump): ")
        with open(namejs, "w") as file:
            json.dump(transactions, file)
        print(f"data  dumped at {namejs}! you can confirm by accessing the file ")
        time.sleep(2)

    elif op == 7:
        name2js = input("json file to load data from it: ")
        try:
            with open(name2js, 'r') as file:
                loaded_data = json.load(file)



            cleaned = []
            for index, amount, timestamp in loaded_data:
                if isinstance(amount, str):
                    amount = int(amount.replace("+", ""))
                cleaned.append((index, amount, timestamp))



            transactions.clear()
            transactions.extend(cleaned)
            balance = sum(t[1] for t in transactions)
            

            print("transaction history loaded successfully and balance was updated.")
            time.sleep(3)
            
        except Exception as e:
            print(f"an error occured: {e}")
            time.sleep(3)

























while True:
    main_menu()
