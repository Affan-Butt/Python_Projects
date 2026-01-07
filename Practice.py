# num = 5
# result = num + 5
# result = result * 2
# result = result - 3
# print(result)


# a = 10
# b = 20

# print("The sum of a and b is:", a + b)
# print("The difference of b and a is:", b - a)
# print("The product of a and b is:", a * b)
# print("The quotient of b and a is:", b / a)


# Number = 5
# square = Number ** 2
# cube = Number ** 3
# print("The square of", Number, "is:", square)
# print("The cube of", Number, "is:", cube)


# num1 = 3.45
# num2 = 5.50
# num3 = 1.05

# print("The sum of num1, num2, and num3 is:", num1 + num2 + num3)
# print("The average of num1, num2, and num3 is:", (num1 + num2 + num3) / 3)


# x, y, z = 5, 10, 15
# print("The values are:", x, y, z)


# fruits = ["apple", "banana", "cherry", "mango", "orange"]
# # print(fruits[0])
# # print(fruits[1])
# # print(fruits[2])
# # print(fruits[3])
# # print(fruits[4])


# fruits[1] = "blueberry"
# print(fruits)


# fruits.append("kiwi")
# fruits.insert(0, "kiwi")
# print(fruits)


# del fruits[0]
# fruits.pop()
# fruits.remove("cherry")
# print(fruits)


# fruits = ["apple", "banana", "cherry", "mango", "orange"]
# print("before sort():", fruits)
# fruits.sort()
# print("after sort():", fruits)
# print("temporary sorted():", sorted(fruits))
# print("original list:", fruits)


# Destinations = ["Paris", "London", "New York", "Tokyo", "Sydney"]
# print("Original list:", Destinations)
# Destinations.sort()
# print("alphabetically sorted list:", (Destinations))
# Destinations.reverse()
# print("reverse alphabetically sorted list:", (Destinations))
# print("total number of destinations:", len(Destinations))


# guest_list = []
# guest_list.append("John Doe")
# guest_list.append("Jane Smith")
# guest_list.append("Alice Johnson")
# guest_list.insert(0, "Bob Brown")
# removed_guest = guest_list.pop()
# print("removed guest:", removed_guest)
# print("Final Invitation list:", guest_list)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# last_three = numbers[len(numbers) - 3: len(numbers)]
# print("The last three numbers are:", last_three)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)


# squares = []
# for num in range(1, 11):
#     squares.append(num ** 2)
# print("The squares of the numbers are:{i+1}", squares)


# movies = []

# for i in range(5):
#     movie = input(f"Enter favorite movie {i+1}: ")
#     movies.append(movie)

# movies.sort()

# print("Your favorite movies (sorted):")
# print(movies)


# name = input("Enter your name: ")
# movie = input("Enter your favorite movie: ")
# print(f"{name}'s favorite movie is {movie}.")


# word = input("Enter a word: ")
# print("Uppercase:", word.upper())
# print("Lowercase:", word.lower())
# print("Titlecase:", word.title())


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# sum_result = num1 + num2
# Difference = num1 - num2
# divide = num1 / num2
# multiply = num1 * num2

# print("Sum:", sum_result)
# print("Difference:", Difference)
# print("Product:", multiply)
# print("Quotient:", divide)


# friends = ["Ali", "Ahmed", "Sara", "Maya"]
# for friend in friends:
#     print("Hello,", friend)


# fruits = ["Apple", "Banana", "Mango"]
# print("Original list:", fruits)


# fruits[1] = "Strawberry"
# print("After replacing second fruit:", fruits)


# fruits.append("Pineapple")
# print("After appending a fruit at the end:", fruits)

# fruits.insert(0, "Cherry")
# print("After inserting a fruit at the beginning:", fruits)


# animals = []
# for i in range(5):
#     animal = input(f"Enter favorite animal {i+1}: ")
#     animals.append(animal)

# print("Total number of animals:", len(animals))

# print("First animal:", animals[0])
# print("Last animal:", animals[4])


# for i in range(1, 11):
#     print(i)


# for i in range(2, 21, 2):
#     print(i)


# for i in range(5, 51, 5):
#     print(i)


# for i in range(1, 11):
#     square = i ** 2
#     print("The square of", i, "is:", square)


# cubes = [i**3 for i in range(1, 6)]
# print(cubes)


# movies = []

# for i in range(5):
#     movie = input(f"Enter movie {i+1}: ")
#     movies.append(movie)

# print("Top 3 movies:", movies[0:3])

# print("Last 2 movies:", movies[3:5])


# students = []

# for i in range(5):
#     name = input(f"Enter student {i+1} name: ")
#     students.append(name)

# print("\nGreetings:")
# for student in students:
#     print(f"Hello, {student}!")

# print("\nTop 3 students:")
# print(students[:3])

# new_students = students[:]

# new_students.append("Hamza")
# new_students.append("Ayesha")

# print("\nOriginal students list:")
# print(students)

# print("\nNew students list (after adding 2 names):")
# print(new_students)


# places = ["Japan", "Turkey", "Italy", "Switzerland", "Maldives"]

# print("Original list:", places)

# print("Temporarily sorted list:", sorted(places))

# places.sort(reverse=True)
# print("Reverse alphabetical order:", places)

# places.reverse()
# print("After first reverse():", places)

# places.reverse()
# print("After second reverse():", places)


# name = input("Enter your name: ")

# char_list = list(name)

# print("\nCharacters in your name:")
# for char in char_list:
#     print(char)

# print("\nFirst 3 letters:", char_list[:3])

# print("Last 2 letters:", char_list[-2:])

# print("Total number of letters:", len(char_list))


# text = input("Enter a string: ")

# clean_text = text.replace(" ", "").lower()

# if clean_text == clean_text[::-1]:
#     print(f'"{text}" is a palindrome.')
# else:
#     print(f'"{text}" is not a palindrome.')


# items = [
#     ("Apple", 120.50),
#     ("Banana", 60.00),
#     ("Milk", 180.75),
#     ("Bread", 90.25)
# ]

# print("Complete items list:")
# print(items)

# print("\nFormatted Table:")
# print("S.No\tItem\tPrice")

# for index, item in enumerate(items, start=1):
#     name, price = item
#     print(f"{index}\t{name}\t{price}")


# sentence = input("Enter a sentence: ")

# print("Original sentence:", sentence)

# vowels = "aeiouAEIOU"

# count = 0
# for char in sentence:
#     if char in vowels:
#         count += 1

# print("Number of vowels:", count)


# prices = [19.99, 5.50, 100.0]

# discount_rate = 0.15

# discounted_prices = []

# for price in prices:
#     discounted_price = price - (price * discount_rate)
#     discounted_prices.append(discounted_price)

# print("Original prices:", prices)
# print("Discounted prices:", discounted_prices)

# print("\nOriginal\tDiscounted")
# for original, discounted in zip(prices, discounted_prices):
#     print(f"{original}\t\t{discounted}")


# numbers = ["03123456789", "03001234567"]

# print("Original\tFormatted")
# for num in numbers:

#     formatted = "+92-" + num[1:4] + "-" + num[4:]
#     print(f"{num}\t{formatted}")


# scores_tuple = (72, 85, 91, 58, 76)

# print("Scores Tuple:", scores_tuple)

# scores_list = list(scores_tuple)
# print("Scores List:", scores_list)

# minimum = min(scores_list)
# maximum = max(scores_list)
# average = sum(scores_list) / len(scores_list)

# print("Minimum Score:", minimum)
# print("Maximum Score:", maximum)
# print("Average Score:", average)


# sentence = "Hello World from Python"

# print("Original Sentence:", sentence)

# reversed_words = [word[::-1] for word in sentence.split()]
# formatted_sentence = " ".join(reversed_words)

# print("Formatted Sentence:", formatted_sentence)


# numbers = [2, 5, 3, 8, 1]

# print("Original List:", numbers)

# running_sum = []
# total = 0
# for num in numbers:
#     total += num
#     running_sum.append(total)

# print("Running Sum List:", running_sum)


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# interleaved = []

# for i in range(len(list1)):
#     interleaved.append(list1[i])
#     interleaved.append(list2[i])

# print("List 1:", list1)
# print("List 2:", list2)
# print("Interleaved List:", interleaved)


# text = input("Enter a string: ")

# repeated_text = ""
# for char in text:
#     repeated_text += char * 2

# print("Original string:", text)
# print("Repeated letters string:", repeated_text)
    