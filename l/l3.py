#1
def differences(a, b):
    intersection = []
    reunion = sorted(set(tuple(a+b)))
    for letter in a:
        if letter in b:
            intersection.append(letter)
            a = a.replace(letter, "")
            b = b.replace(letter, "")
    return [intersection, reunion, tuple(a), tuple(b)]

print(differences("abcd", "bcdef"))

#3
import types
def value_equals(value1, value2):
    if isinstance(value1, (dict, set)) & isinstance(value2, (dict, set)):
        return equals_containers(value1, value2, set(list(value1.keys()) + list(value2.keys())))
    elif isinstance(value1, (list, tuple)) & isinstance(value2, (list, tuple)):
        return equals_containers(value1, value2, range(0, max(len(value1), len(value2))))
    else:
        return value1 == value2

def equals_containers(container1, container2, keys_to_iterate):
    for x in keys_to_iterate:
        try:
            if value_equals(container1[x], container2[x]) == False:
                return False
        except:
            return False
    return True

print(value_equals({"a": "b", "b":("a", "b", "c")}, {"a": "b", "b":("a", "b", "c")}))

