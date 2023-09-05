import re

def split_camel_case(input_str, entity_type):
    input_str = input_str[1:-1] if input_str.endswith("()") else input_str

    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', input_str)
    lowercase_words = [word.lower() for word in words]
    
    if entity_type == 'M':
        return ' '.join(lowercase_words)
    elif entity_type == 'V':
        return ' '.join(lowercase_words)
    elif entity_type == 'C':
        return ' '.join(lowercase_words)
        
def combine_camel_case(input_str, entity_type):
    if entity_type == 'M':
        words = input_str.split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:]) + "()"
    elif entity_type == 'V':
        words = input_str.split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    elif entity_type == 'C':
        words = input_str.split()
        return ''.join(word.capitalize() for word in words)


while True:
    try:
        line = input()
        operation, entity_type, input_str = line.split(';')
        
        if operation == 'S':
            print(split_camel_case(input_str, entity_type))
        elif operation == 'C':
            print(combine_camel_case(input_str, entity_type))
                
    except EOFError:
        break
