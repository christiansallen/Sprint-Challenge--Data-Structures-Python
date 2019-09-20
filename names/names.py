import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# This solution gives me a runtime of around 6 seconds O(n^2)
duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# This solution gives me a runtime of about 1.2 seconds O(n)
# duplicates = [name for name in names_1 if name in names_2]

# Need to sort so I can effectively cut half of list every time
names_1.sort()

for name in names_2:
    first = 0
    last = len(names_2)-1
    found = False

    while (first <= last and not found):
        # Find mid of names list and see if the potential duplicate name is higher or lower
        mid = (first + last) // 2
        if names_1[mid] == name:
            duplicates.append(name)
            found = True
        else:
            # Move the last or first pointer depending on name is higher or lower than mid.
            if name < names_1[mid]:
                last = mid - 1
            else:
                first = mid + 1

# This will make it an O(logn) time complexity

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
