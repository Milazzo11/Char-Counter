def sort(arr1, arr2):  # sorts arrays on alphabetical order
    n = len(arr1)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr1[j] > arr1[j + 1]:  # when needed, arrays indexing character and value switch
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]

    return arr1, arr2


f = open("input.txt", "r")
data = f.read()
f.close()
# reads in file data

char_list = []
count = []

for char in data.upper():  # iterates through file data and counts characters
    if char in char_list:
        count[char_list.index(char)] += 1
    else:
        char_list.append(char)
        count.append(1)

char_list, count = sort(char_list, count)
# sorts data

for x in range(len(char_list)):  # iterates through data and prints
    if char_list[x] == " ":
        char_list[x] = "SPACE"
    elif char_list[x] == "\n":
        char_list[x] = "RETURN"

    print(char_list[x] + ":  " + str(count[x]))