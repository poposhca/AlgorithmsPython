# Dynamic Window
# Algorith takes O(n)
s = "bbbbb"
charSet = set()
left = 0
res = 0
for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[left])
        left += 1
    charSet.add(s[r])
    res = max(res, r - left + 1)
print(res)
