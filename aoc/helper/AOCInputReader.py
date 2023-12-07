import urllib.request
from typing import List


def readLinesFromFile(fileName="input.txt") -> list[str]:
    file = open(fileName, 'r')
    lines = file.read().splitlines()
    return lines

def readAOCinput(day):
    url = 'https://adventofcode.com/2022/day/' + str(day) + '/input'
    print(url)

    with urllib.request.urlopen(url) as f:
        print(f.read())


if __name__ == "__main__":
    readAOCinput("2")
