# 1. Sum of all items in a list
lst = [10, 20, 30, 40]
print(sum(lst))

# 2. Largest number in a list
lst = [10, 50, 20, 80]
print(max(lst))

# 3. Smallest number in a list
lst = [10, 50, 20, 80]
print(min(lst))

# 4. Remove duplicate elements from a list
lst = [1, 2, 2, 3, 4, 4, 5]
print(list(set(lst)))

# 5. Clone or copy a list
lst = [1, 2, 3]
copy_lst = lst.copy()
print(copy_lst)

# 6. Reverse a list
lst = [1, 2, 3, 4, 5]
print(lst[::-1])

# 7. Create a list containing different data types
lst = [10, "Python", 3.14, True, None]
print(lst)

# 8. Remove empty elements from a list
lst = [1, "", 2, None, "Python", [], 3]
new_lst = [x for x in lst if x]
print(new_lst)

# 9. Append all elements of a second list to a first list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# 10. Select a random item from a list
import random
lst = [10, 20, 30, 40]
print(random.choice(lst))

# 11. Separate odd and even numbers from a list
lst = [1, 2, 3, 4, 5, 6]
even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]
print("Even:", even)
print("Odd:", odd)

# 12. Sort a list in ascending order
lst = [40, 10, 30, 20]
print(sorted(lst))

# 13. Sort a list in descending order
lst = [40, 10, 30, 20]
print(sorted(lst, reverse=True))

# 14. Count the number of elements in a list
lst = [10, 20, 30, 40, 50]
count = 0
for _ in lst:
    count += 1
print(count)

# 15. Average of numbers in a list
lst = [10, 20, 30, 40]
print(sum(lst) / len(lst))

# 16. Count how many times a specific element appears in a list
lst = [1, 2, 3, 2, 4, 2]
print(lst.count(2))

# 17. Check whether an element exists in a list
lst = [10, 20, 30, 40]
print(20 in lst)

# 18. Insert an element at a specific position in a list
lst = [10, 20, 40, 50]
lst.insert(2, 30)
print(lst)

# 19. Remove a specific element from a list
lst = [10, 20, 30, 40]
lst.remove(30)
print(lst)

# 20. Find the second largest number in a list
lst = [10, 50, 20, 80, 70]
unique = list(set(lst))
unique.sort()
print(unique[-2])

# 21. Merge two lists into a single list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# 22. Find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(list(set(list1) & set(list2)))

# 23. Create a new list containing only positive numbers
lst = [-2, 4, -5, 7, 0, 9]
positive = [x for x in lst if x > 0]
print(positive)

# 24. Replace all negative numbers in a list with 0
lst = [-2, 4, -5, 7, 0, 9]
result = [0 if x < 0 else x for x in lst]
print(result)

# 25. Find the index position of a given element in a list
lst = [10, 20, 30, 40]
print(lst.index(30))


# 26. Store 5 student names in a list and display them one by one
students = ["Arun", "Kavi", "Priya", "Ravi", "Meena"]
for name in students:
    print(name)

# 27. Store 10 marks in a list and find highest and lowest marks
marks = [78, 56, 91, 88, 67, 73, 95, 62, 84, 69]
print("Highest:", max(marks))
print("Lowest:", min(marks))

# 28. Store product prices in a list and calculate the total bill amount
prices = [120.5, 250.0, 89.75, 300.0]
print("Total bill:", sum(prices))

# 29. Store employee salaries in a list and find salaries greater than 25000
salaries = [18000, 25000, 32000, 45000, 22000, 28000]
high_salaries = [sal for sal in salaries if sal > 25000]
print(high_salaries)

# 30. Store attendance status in a list and count the number of present students
attendance = ["Present", "Absent", "Present", "Present", "Absent"]
print(attendance.count("Present"))