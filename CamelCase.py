liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

s = "saveChangesInTheEditor"

def camelcase(s):
    count = 0
    for i in s:
        if i in liste:
            count += 1

    return count + 1

print(camelcase(s))