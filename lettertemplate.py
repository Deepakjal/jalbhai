letter = f"""Dear <NAME>,
You are selected!
<DATE>"""

name = input("Enter your name:")
date =input("Enter the date:")

letter = letter.replace("<NAME>",name)
letter = letter.replace("<DATE>",date)

print(letter)  