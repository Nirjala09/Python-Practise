try:
    x = 10 / 0  # This will cause an error
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This always runs.")



try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Success Result is:", result)
finally:
    print("okk")
