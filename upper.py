def capitalize_words(text):
    return text.title()   #title is builtin function to Convert the first character of each word to upper case


user_input = input("Enter a sentence: ")

capitalized = capitalize_words(user_input)
print("Capitalized sentence:", capitalized)
