import urllib.request
#https://adventofcode.com/2022/day/2/input

##need to implement login stuff

def readLinesFromFile(fileName="input.txt"):
    file = open(fileName, 'r')
    lines = file.read().splitlines()
    return lines

def readAOCinput(day):
    url = 'https://adventofcode.com/2022/day/' + str(day) +'/input'
    print(url)

    with urllib.request.urlopen(url) as f:
        print(f.read())

if __name__ == "__main__":
    readAOCinput("2")