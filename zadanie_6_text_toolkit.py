def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ","")
    reversed_text = text[::-1]
    if text == reversed_text:
        return "is"
    else:
        return "is not"

def count_vowels(text):
    total=0
    for letter in text:
        if letter in "aeiou":
            total += 1
    return total

def word_count(text):
    words = text.split()
    return len(words)

def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

name = input(f"What's your name?")
user_text = input(f"Please insert your word {name} :) : ")

while True:
    print("Choose option")
    print("1. Palindrom")
    print("2. Count vowels")
    print("3. Count words")
    print("4. Reverse word")
    print("5. Exit")
    choice = input()
    if choice == "1":
        result = is_palindrome(user_text)
        print(f"{user_text} {result} a palindrome")
    elif choice == "2":
        result = count_vowels(user_text)
        print(f"{user_text} has {result} vowels.")
    elif choice == "3":
        result = word_count(user_text)
        print(f"{user_text} has {result} words")
    elif choice == "4":
        result = reverse_words(user_text)
        print(f"{user_text} spelled backwards is {result}!")
    elif choice == "5":
        break
    else:
        print("Invalid option, try again :)")
