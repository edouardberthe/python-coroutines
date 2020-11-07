from constants import file_name
from follow import follow

def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

logfile = open(file_name)
loglines = follow(logfile)
pylines = grep("p", loglines)

if __name__ == "__main__":
    for line in pylines:
        print(line, end="")