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
import collections

def is_valkey_collection(value):
    return isinstance(value, (dict, set))

def is_ord_collection(value):
    return isinstance(value, (list, tuple))

def value_equals(value1, value2):
    if is_valkey_collection(value1) & is_valkey_collection(value2):
        return containers_differences(value1, value2, list(value1.keys()))
    elif is_ord_collection(value1) & is_ord_collection(value2):
        return containers_differences(value1, value2, range(0, len(value1)))
    else:
        return [value1 == value2]

import itertools
def flatten(list_to_flatten):
    return list(itertools.chain.from_iterable(list_to_flatten))

def containers_differences(container1, container2, keys_to_iterate):
    common_keys_different_values = []
    keys_only_in_first = []
    keys_only_in_second = []
    is_equal = True
    for x in keys_to_iterate:
        try:
            result = value_equals(container1[x], container2[x])
            if result[0] == False:
                common_keys_different_values.append(x)
                is_equal = False
            del(container1[x])
            del(container2[x])
            if len(result) == 1 :
                continue
            common_keys_different_values.append(result[1])
            keys_only_in_first.append(result[2])
            keys_only_in_second.append(result[3])
        except KeyError as e:
            is_equal = False
    if is_equal:
        is_equal = len(container2) == 0
    return(is_equal, 
    common_keys_different_values, 
    flatten(list(container1.keys()) + keys_only_in_first),
    flatten(list(container2.keys()) + keys_only_in_second))

#6#7?
print(value_equals({"a": "c", "b":"c", "d":{"e":"f"}}, {"a": "b", "d":{"f":"e"}, "z":"x"}))
exec("lambda *a, **k: print(a, k)")

import os
print(os.system("ls *.*"))