# Anton and Danik

games = int(input())
results = str(input())

anton = results.count('A')
danik = results.count('D')

if anton > danik:
    print('Anton')
elif danik > anton:
    print('Danik')
else:
    print("Friendship")

# AAR: Empty