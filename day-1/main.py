# Imports
# ---

# Function definition
def findTwoNumbers(inputArray):
     arrayResult = []
     i = 0
     while i < len(inputArray) - 1:
          j = 0
          while j < len(inputArray):
               if inputArray[i] + inputArray[j] == 2020:
                    result = [inputArray[i], inputArray[j]]
                    arrayResult.append(result)
                    print(inputArray[i], inputArray[j])
               j+=1
          i+=1

     result = str(arrayResult[0][0]) + " + " + str(arrayResult[0][1]) + " = " + str(arrayResult[0][0] * arrayResult[0][1])
     print("\n" + result)

     return arrayResult[0][0] * arrayResult[0][1]

def findThreeNumbers(inputArray):
     arrayResult = []
     i = 0
     while i < len(inputArray) - 1:
          j = 0
          while j < len(inputArray):
               n = 0
               while n < len(inputArray) - 1:
                    if inputArray[i] + inputArray[j] + inputArray[n] == 2020:
                         result = [inputArray[i], inputArray[j], inputArray[n]]
                         arrayResult.append(result)
                         print(inputArray[i], inputArray[j], inputArray[n])
                    n += 1
               j+=1
          i+=1

     result = str(arrayResult[0][0]) + " + " + str(arrayResult[0][1]) + " + " + str(arrayResult[0][2]) + " = " + str(arrayResult[0][0] * arrayResult[0][1] * arrayResult[0][2])
     print("\n" + result)

     return arrayResult[0][0] * arrayResult[0][1] * arrayResult[0][2]



# numbers are loaded into the following array.
inputNumbers = []
with open("input.txt", "r") as f:
     lines = f.readlines()
     for item in lines:
          inputNumbers.append(int(item.strip("\n")))




print(findTwoNumbers(inputNumbers))
print("\n\n")
print(findThreeNumbers(inputNumbers))

