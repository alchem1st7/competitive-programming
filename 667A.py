# Vanya and Friends

num_friends, height = map(int, input().split())

friends = list(map(int, input().split()))

solution = 0

for f in friends:
    if f > height:
        solution += 2
    else:
        solution +=1

print(solution)

# AAR: Empty