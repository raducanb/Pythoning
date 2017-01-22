#1
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_list(n):
    return list(map(fibonacci, range(1,n+1)))

print(fibonacci_list(10))

#5
# def combinatios_of_len(list_c, len_k):
#     combinations = list()
#     for i in range(0, len_k):
#
# print(tuple("ABCD"))
        
#6
class Counter(dict):
    def __missing__(self, key):
        return 0

def elements_that_appear_x_times(times, *lists):
    elements_dict = Counter()
    for a_list in lists:
        for a_element in a_list:
            elements_dict[a_element] += 1
    return list({k:v for k, v in elements_dict.items() if v == times}.keys())
    
print(elements_that_appear_x_times(2, [1,2,3], [2,3,4], [4,5,6], [4,1,"test"]))

#test
a_list = [1, 9, 8, 4]
print([elem * 2 for elem in a_list])
print(list(map(lambda x:x*2, a_list)))
for x in "abcd":
    print(ord(x))

#8
def tuples_lists_from_lists(*input_lists):
    max_len = max([len(x) for x in input_lists])
    output_lists = []

    for x in range(0, max_len):
        output_lists.insert(x, ([input_list[x] if len(input_list) > x else None for input_list in input_lists]))
    return output_lists

print(tuples_lists_from_lists((1,2,3),(4,5,6),(7,8)))
