thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)




























































def reverse_word(word):
    if len(word) == 0:
        return word
    return reverse_word(word[1:]) + word[0]

print(reverse_word("Python")) 