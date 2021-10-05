letter = ''' Dear <|Name|>
You are selected
<|Date|>'''

Name = (input("enter your name: " ))
Date = (input("enter date: "))

letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)

print(letter)