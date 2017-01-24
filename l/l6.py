import re
#1
def words_from_text(text):
    return re.split("[^a-z']+", text, flags = re.IGNORECASE)

print(words_from_text("ana are mere"))

#2
def results_from_text(reg, text):
    results = re.finditer(reg, text)
    return [result.group(1) for result in results]

def results_from_text_max_length(reg, text, maxlen):
    return [result for result in results_from_text(reg, text) if len(result) <= maxlen]

print(results_from_text_max_length("\s*(\w+)\s*", "ana are mere", 3))
    
#test
s = "Today I'm having a python course"
print (re.sub("having\s+a\s+(\w+)\s+course",
              r"not doing the \1 course",
              s))

#6
def censor_word(word):
    new_word = ""
    for index, letter in enumerate(word):
        if index % 2 == 1:
            letter = "*"
        new_word += letter
    return new_word

def censor_match(word_match):
    new_word = censor_word(word_match.group(1))
    for x in range(2, word_match.lastindex+1):
        new_word += word_match.group(x)
    return new_word

def censor_words(text):
    return re.sub("([aeiou]+[a-zA-Z']*[aeiou]+)($|\s|\.+)", censor_match, text)

print(censor_words("atesta atest itesta."))