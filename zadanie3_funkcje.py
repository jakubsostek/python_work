#Zadanie 1
def sum_of_evens(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number
    return total

result = sum_of_evens([3, 8, 12, 7, 4, 15, 6])
#Zadanie 2
print(result)
def count_names(names_list):
    counts = {}
    for name in names_list:
        if name in counts:
            counts[name]+= 1
        else:
            counts[name] = 1
    return counts

result =  count_names(["Ala", "Bartek", "Ala", "Celina", "Bartek", "Ala"])
print(result)
#Zadanie 3
def double(n):
    return n * 2
result = double(5)
print(result)
#Zadanie 4
def add(a, b):
    return a + b
result = add(3,4)
print(result)
#Zadanie 5
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))
#Zadanie 6
def average(numbers):
    return sum(numbers) / len(numbers)
result = average([2, 4, 6, 8])

print(result)
#Zadanie 7
def max_of_two(a,b):
    if a > b:
        return a
    else:
        return b

result = max_of_two(7,3)
print(result)
#Zadanie 8
def is_even_sum(a,b):
    total = a + b
    return is_even(total)
result = is_even_sum(3,5)
print(result)
#Zadanie 8
def calculate_tip(bill, percent):
    tip = (bill / 100) * percent
    return  bill + tip

result = calculate_tip(50, 20)
print(result)

#Zadanie 9
def grade_to_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >=70:
        return "C"
    else:
        return "D"

result = grade_to_letter(95)
print(result)
result = grade_to_letter(85)
print(result)
result = grade_to_letter(72)
print(result)
result = grade_to_letter(50)
print(result)

#Zadanie 10
def reverse_string(text):
    return text[::-1]
result = reverse_string("kod")
print(result)