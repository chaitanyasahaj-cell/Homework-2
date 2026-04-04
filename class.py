# word = input("Enter a word: ")
# n = int(input("Enter a number: "))
# print(word[n-1])




# word = input("Enter a word: ")
# number = int(input("Enter a number: "))

# letter = word[(number - 1) % len(word)]
# print("Letter:", letter)



text = input("Enter a string: ")
result = ""

for i in range(0, len(text), 2):
    letter = text[i]
    count = int(text[i + 1])
    result = result + letter * count
print(result)