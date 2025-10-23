# Word

word = str(input())

count_upper = 0
count_lower = 0

for c in word:
    if ord(c) > 90:
        count_lower += 1
    else:
        count_upper += 1

if count_upper > count_lower:
    print(word.upper())
else:
    print(word.lower())

# AAR: Empty