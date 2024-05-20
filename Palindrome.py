def palindrome(string):
    s = string.lower()

    new_string = ''
    for char in s:
        if char.isalnum(): # isalnum is a method in that checks if characters in a string are alphanumeric
            new_string += char 

    reversed_string = new_string[::1]  

    return new_string == reversed_string

test_cases = [
    ("A man, a plan, a canal, Panama!", True), 
    ("Radar", True),                          
    (12321, True),                             
    ("Python", False),                       
]

for i in range(len(test_cases)):
    input_data, expected_output = test_cases[i]
    result = palindrome(str(input_data))
    print(f"Test Case {i+1}: {result == expected_output}")


