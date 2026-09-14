import random
import string

def generate_random_string(length):
    # Create a pool of letters and numbers (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
    characters = string.ascii_letters + string.digits
    
    # Randomly select 'length' number of characters and join them into a string
    return ''.join(random.choices(characters, k=length))




if __name__ == '__main__':
    # Example usage:
    print(generate_random_string(6))  # Outputs something like: eK9sv2XpZb
