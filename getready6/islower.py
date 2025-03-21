def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())  # Count uppercase letters
    lower_count = sum(1 for char in s if char.islower())  # Count lowercase letters
    
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

# Example usage
text = input("Enter a string: ")
count_case(text)