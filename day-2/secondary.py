

# numbers are loaded into the following array.
inputLines = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for item in lines:
        inputLines.append(item.strip("\n"))

splittedLines = []

for items in inputLines:
    splittedLines.append(items.split(" "))


# print(splittedLines)

letters = []
minmaxLetters = []
codeLetters = []

i = 0
while i < len(splittedLines):
    letters.append(splittedLines[i][1].strip(":"))
    minmaxLetters.append(splittedLines[i][0].split("-"))
    codeLetters.append(splittedLines[i][2])
    i += 1


# print(letters)
# print(minmaxLetters)
# print(codeLetters)


def check4Char(letter, minmaxLetter, codeLetter):
    print(minmaxLetter, letter, codeLetter)
    if len(codeLetter) >= int(minmaxLetter[0]) - 1:

        #print(letter, codeLetter[int(minmaxLetter[0])], codeLetter[int(minmaxLetter[1])])
        
        if letter == codeLetter[int(minmaxLetter[0]) - 1] and letter != codeLetter[int(minmaxLetter[1]) - 1]:  
            return True
        else:
            return False


i = 0
n = 0
while i < len(letters):
    availableCode = check4Char(letters[i], minmaxLetters[i], codeLetters[i])

    if availableCode == True:
        print("Found one!")
        n += 1
    i += 1

print("A total of " + str(n) + " codes work!")

# Returns 319 but that isn't the answer.