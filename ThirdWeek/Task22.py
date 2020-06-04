s = str(input())
pos1 = s. find("h")
pos2 = s.rfind("h")
st = s[pos1 + 1:pos2]
print(s[:pos1 + 1], st.replace("h", "H"), s[pos2:], sep="")
