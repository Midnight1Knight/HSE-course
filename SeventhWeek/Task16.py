num = int(input())
dictin = dict()
for i in range(num):
    word1, word2 = map(str, input().split())
    dictin[word1] = word2
    dictin[word2] = word1
control = str(input())
print(dictin.get(control))
