import time
import random as rd

from constants import file_name


alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = " "
n = len(alphabet)

while True:
    with open(file_name, "a") as file:
        message = rd.choice(alphabet).upper() + "".join(rd.choice(alphabet + symbols) for _ in range(rd.randint(5, 30)))
        print(f"Printing message {message}")
        file.write(f"{message}\n")
    time.sleep(rd.randint(500, 3000) / 1000)
