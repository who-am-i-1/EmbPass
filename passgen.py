import random

def generate_embarrassing_password(num_words=3, separator='-', capitalize=True):
    # List of embarrassing words
    embarrassing_words = [
        'booger', 'diaper', 'wedgie', 'snot', 'burp',
        'fart', 'sneeze', 'belch', 'zit', 'drool',
        'toilet', 'pimple', 'potty', 'underwear', 'spit',
        'nosehair', 'earwax', 'mucus', 'itch', 'wedge',
        'flab', 'freckle', 'dandruff', 'sweat', 'wheeze'
    ]

    # Shuffle the list of embarrassing words
    random.shuffle(embarrassing_words)

    # Select a random subset of words
    selected_words = embarrassing_words[:num_words]

    # Capitalize words if specified
    if capitalize:
        selected_words = [word.capitalize() for word in selected_words]

    # Join the words with the separator
    password = separator.join(selected_words)
    password1= 'your'+password

    return password1

if __name__ == "__main__":
    num_words = int(input("Enter the number of words for the password: "))
    separator = input("Enter the separator character (e.g., '-', '_', '.'): ")
    capitalize = input("Capitalize the words? (yes/no): ").lower() == 'yes'

    password = generate_embarrassing_password(num_words, separator, capitalize)
    print("Embarrassing Password:", password)
