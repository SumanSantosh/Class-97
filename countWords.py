introString = input("Enter Your Introduction : ")
charecterCount = 0
wordCount = 1

for i in introString:
    charecterCount = charecterCount + 1
    if i ==" " : 
        wordCount = wordCount + 1

print("Number of word in the string")
print(wordCount)

print("Number of charecters in the string")
print(charecterCount)