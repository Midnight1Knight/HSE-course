s = str(input())
i = 0
new = s[0]
while i != len(s) - 1:
    new = s[i] + "*"
    i += 1
    print(new, end="")
print(s[i], end="")
