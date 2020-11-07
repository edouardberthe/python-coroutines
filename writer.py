import time
import random as rd

file_name = "messages.log"
alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = " "
n = len(alphabet)

while True:
    with open(file_name, "a") as file:
        message = rd.choice(alphabet).upper() + "".join(rd.choice(alphabet + symbols) for _ in range(rd.randint(5, 30)))
        print(f"Printing message {message}")
        file.write(f"{message}\n")
        time.sleep(2)
