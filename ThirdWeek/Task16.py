s = str(input())
pos1 = s.find("h")
pos2 = s.rfind("h")
print(s[:pos2], s[pos1 + 1:pos2], s[pos2:], sep="")
