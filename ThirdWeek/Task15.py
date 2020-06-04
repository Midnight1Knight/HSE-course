s = str(input())
pos1 = s.find("h")
pos2 = s.rfind("h")
print(s[:pos1], s[pos2 + 1:], sep="")
