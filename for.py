for number in range(1,11):
    print(number)

for letter in "abcd":
    print(letter)


vowels = 0
consonants = 0

for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))


students = {
    "male" : ["Tom","Charlier","Harry","Frank","Ali"],
    "female": ["Sarah","Huda","Emily","Samantha","Elizabeth"]
    }

#print name which having "a" letter.

for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
