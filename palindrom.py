def reverse(word):
    return word[::-1]

user_input = input("Enter the word:")
reverse = reverse(user_input)
if user_input == reverse:
        print("Yes")
else:
    print("No")
#print(reverse)