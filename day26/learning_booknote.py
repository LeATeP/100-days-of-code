import csv
import random
import pandas

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# y = True
# new_name = [n * 2 for n in range(1, 5) if y is True]
# print(new_name)

# names = ["wewrwy", "good", "SHooOK", "sfkhryu"]
# new = [name.upper() for name in names if len(name) > 5]
# print(new)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n * n for n in numbers]
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)


###############################################
# with open("./1.txt") as numbers:
#     lots1 = csv.reader(numbers)
#     w = [n for n in lots1]
#
# with open("./2.txt") as numbers:
#     lots2 = csv.reader(numbers)
#     q = [n for n in lots2 if n in w]
#
# e = []
# for n in q:
#     if n not in e:
#         e.append(int(n[0]))
#
# e.sort()
# print(e)
############
# Version n2
# with open("./1.txt") as numbers:
#     lots1 = numbers.readlines()
#
# with open("./2.txt") as numbers:
#     lots2 = numbers.readlines()
#
#
# result = [int(n) for n in lots2 if n in lots1]
# print(result)
###############################################

# students = ["jon", "josh", "smith", "deve", "kari", "smoth", "hosh"]
# students_score = {student: random.randint(1, 100) for student in students}
# passed_students = {student: score for (student, score) in students_score.items() if score > 40}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# w = {word: len(word) for word in words}
# print(w)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {name: (temp * 9/5 + 32) for (name, temp) in weather_c.items()}
# print(weather_f)

# dict1 = {
#     "students": ["josh", "nick"],
#     "scores": [25, 70]
# }
# dict_frame = pandas.DataFrame(dict1)
# for (index, row) in dict_frame.iterrows():
#     print(row.scores)



























