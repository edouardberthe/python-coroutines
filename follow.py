import time

from typing import Iterator

def follow(file) -> Iterator[str]:
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
        else:
            yield line


file_name = "messages.log"
with open(file_name) as file:
    f = follow(file)
    for line in f:
        print(line, end="")
