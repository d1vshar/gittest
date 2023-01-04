import sys
from os.path import exists

print("Dictionary Generator Console Tool")
file="dict.txt"

def print_menu():
    print("""
1 - Enter Word-Meaning pair
2 - Search Meaning
3 - Remove Word
4 - Exit""")

def dexists():
    return exists(file)

def add_word(word, meaning):
    result = search_word(word)
    if result == None:
        with open(file, "a") as f:
            f.write(f"{word}={meaning}\n")
    else:
        add_meaning(word, meaning)

def add_meaning(word, meaning):
    if (not dexists()):
        return None
    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            parts = line.strip("\n").split("=")
            if parts[0] == word:
                f.write(f"{parts[0]}={parts[1]},{meaning}\n")


def remove_word(word):
    if (not dexists()):
        return None
    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            if line.strip("\n").split("=")[0] != word:
                f.write(line)

def search_word(word):
    if (not dexists()):
        return None
    with open(file, "r") as f:
        line = f .readline()
        if not line:
            return None
        parts = line.strip("\n").split("=")
        if parts[0] == word:
            return parts[1]

while(True):
    print_menu()
    print("\nEnter choice: ")
    choice=int(input())
    if choice == 1:
        word=input()
        meaning=input()
        add_word(word, meaning)
    elif choice == 2:
        word=input()
        meaning = search_word(word)
        if meaning != None:
            print(meaning)
        else:
            print("Word doesn't exist")
    elif choice == 3:
        word=input()
        remove_word(word)
    elif choice == 4:
        sys.exit()
    else:
        print("invalid")
