#print message based on your age......
age = int(input("Enter your age:"))
if age < 18:
    print("You are a minor right now !")
elif age>18 and age<65:
    print("You are a Adult!")
else:
    print("You are a senior citizen !")


#use of triple uotes....
letter = """Dear Deepak,
This pyton Course is nice,
Thanks!"""
print(letter)