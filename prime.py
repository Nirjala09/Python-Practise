def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False  

    return True 


number =int(input("Enter a number: ")) 
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
