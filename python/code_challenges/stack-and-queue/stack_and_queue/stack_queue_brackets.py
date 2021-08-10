
def validate_brackets(string):
    
    round_brackets = 0
    square_brackets = 0
    curly_brackets = 0
    
    for item in string:
        if item == '(':
            round_brackets += 1
        elif item == ')':
            round_brackets -= 1         
        elif item == '[':
            square_brackets += 1
        elif item == ']':
            square_brackets -= 1         
        elif item == '{':
            curly_brackets += 1
        elif item == '}':
            curly_brackets -= 1 
    if round_brackets == 0 and square_brackets == 0 and curly_brackets == 0:
        return True
    return False


print(validate_brackets('(Nawal)'))
print(validate_brackets('{{()}})'))
print(validate_brackets('({()})'))
print(validate_brackets('{[[]}]}'))
print(validate_brackets('{}(){}'))
