x = "Nepal"
reverse = ""
for char in x:
    reverse = char + reverse
    print(reverse)
    if "peN" in reverse:
        break
print(reverse)





x = x[::-2]
print(x)




x = "Nepal"
reverse = ""
for char in x:
    if char == "e":
        continue
    reverse = char + reverse
    #print(reverse)
       
print(reverse)