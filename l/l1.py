#1
def cmmdc(*list_of_numbers):
    for i in reversed(range(2, min(list_of_numbers) + 1)):
        l = list(filter(lambda x:x%i==0, list_of_numbers))
        if len(l) < len(list_of_numbers):
            continue
        return i
print(cmmdc(10,20,30))
print(cmmdc(15,10,25))

#2
s = "sfdgaeb"
print(len(list(filter(lambda x:x in "aeiou", s))))

#9
import re
s = "ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda300fds"
s2 = "as10as"
r = re.compile("[A-Za-z+](\d+)[A-Za-z+]")

def is_prime(number):
    return len([x for x in range(2, number//2) if(number%x==0)]) == 0

def number_from_match(match):
    return int(match.group(1))

def biggest_prime(text):
    ints = list(map(number_from_match, r.finditer(text)))
    try:
        return max(list(filter(is_prime, ints)))
    except:
        return -1

print(biggest_prime(s2))
