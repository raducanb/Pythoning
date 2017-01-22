s = "PythonExam"
print(s[0::3])
print(s.index("a"))

def multi_sum(x, *listOfNumbers):
    sum = 0
    for y in listOfNumbers:
        sum += y
    return sum + x

print (multi_sum(4, 1, 2, 3))

