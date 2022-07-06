the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'banana']
change = [1, 'small', 2, 'regular', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruits of type: {fruits}")

for i in change:
    print(f"I got {i}")

elements = []
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")                