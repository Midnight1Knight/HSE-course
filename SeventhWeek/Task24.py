def is_upper(x):
    num = 0
    for i in x:
        if i.isupper():
            num += 1
    if num == 1:
        return True
    else:
        return False


numOfWords = int(input())
dict1_ = set()
dict2_ = set()
mistakes = 0
for i in range(numOfWords):
    w = input()
    dict1_.add(w)
    dict2_.add(w.lower())
sentence = list(input().split())
for word in sentence:
    if word.lower() in dict2_:
        if word in dict1_:
            dict1_.add(word)
            dict2_.add(word.lower())
            continue
        else:
            mistakes += 1
            continue
    elif is_upper(word) is False:
        mistakes += 1
        continue
    elif word.islower():
        mistakes += 1
        continue
print(mistakes)
