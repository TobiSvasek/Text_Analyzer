"""
projekt_1.py: První projekt do blablabla

author: Tobias Svasek
email: 1143@student.itgymnazium.cz
"""
from collections import Counter

valid_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

texts = [
    "This is the first text bruzz. It has some rizzy words and numbers like 1234.",
    "Here is the second text (sigma). It also has words and numbers like 456.",
    "Finally, this is the third text, did I mention I hate minorities???. It contains words and numbers like 789."
]

def verify_login(username, password):
    if username in valid_users and valid_users[username] == password:
        print ("\nHi " + username + ", we have 3 texts to be analyzed.")
        return True
    else:
        print ("\nUsername or password is incorrect, terminating")
        return False


def text_analyzer(text):
    word_count = len(text.split())
    title_count = sum(1 for c in text if c.istitle())
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    num_count = sum(1 for c in text if c.isdigit())
    sum_count = sum(int(c) for c in text if c.isdigit())
    print("\nThere are", word_count, "words in the selected text.")
    print("There are", title_count, "title case characters in the selected text.")
    print("There are", upper_count, "upper case characters in the selected text.")
    print("There are", lower_count, "lower case characters in the selected text.")
    print("There are", num_count, "numeric characters in the selected text.")
    print("The sum of all the numbers is:", sum_count)

    word_lengths = [len(word) for word in text.split()]
    length_counts = Counter(word_lengths)

    print("\nWord Length Occurrences:")
    for length, count in sorted(length_counts.items()):
        print(f"{length}| {'*' * count} |{count}")

username = input("Enter username: ")
password = input("Enter password: ")


if verify_login(username, password):
    for i, text in enumerate(texts, 1):
        print(f"{i}. {text}")
    choice = int(input("Enter the number of the text you want to analyze (1-3): "))
    if 1 <= choice <= 3:
        text_analyzer(texts[choice - 1])
    else:
        print("Invalid choice, terminating")

