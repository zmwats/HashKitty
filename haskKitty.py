from collections import Counter
from os import system
import time
import sys

def main():

    def textappearance(text, wait=0.5, cr=True):
            for letter in text:
                print('\033[92m'+letter+'\033[0m', end="", flush=True)
                time.sleep(0.02)
            if cr:
                print()
            time.sleep(wait)

    def intro():
        textappearance("Welcome to HaskKitty")
        textappearance("This is a simple program that will help you find the most common masks in a file")

    def create_mask(strings):
        masks = []
        for string in strings:
            mask = ""
            for char in string:
                if str.isalpha(char):
                    if str.isupper(char):
                        mask += "?u"
                    else:
                        mask += "?l"
                elif str.isdigit(char):
                    mask += "?d"
                else:
                    mask += "?s"
            masks.append(mask)
        return masks

    def extractStrings(path):
        with open (path, 'r') as file:
            strings = file.read().splitlines()
        return strings


    path = '/home/user/Documents/filename.txt' # Change this to the path of your file
    strings = extractStrings(path)

    intro()

    if strings:
        masks = create_mask(strings)
        enumeratedmasks = Counter(masks)
        top3masks = enumeratedmasks.most_common(3)
        textappearance(" Top 3 Correlated Masks:")
        for mask, count in top3masks:
            print(mask, "Count:", count)

    def export():
        answer = input("Would you like to export the results to a file? (y/n): ")
        if answer == "y":
            with open('results.txt', 'w') as file:
                for mask, count in top3masks:
                    file.write(str(mask) + " Count: " + str(count) + "\n")
            textappearance("Results have been exported to results.txt")
        if answer == "n":
            sys.exit()
    export()
    

main()



