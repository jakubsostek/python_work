from zadanie3_funkcje import reverse_string

numbers = [10, 25, 3, 47, 8]
numbers.append(99)
numbers.pop(3)

if 47 in numbers:
    print("jest")
else:
    print("nie ma")

def remove_duplicates(numbers):
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))


def find_second_largest(numbers):
    largest = numbers[0]
    second_largest = numbers[0]
    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
           second_largest = number
    return second_largest

print(find_second_largest([10, 25, 3, 47, 8]))

def is_palindrome(text):
    text = text.lower()
    text = text.replace(" ","")
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    else:
        return False

print(is_palindrome("A man a plan a canal Panama"))