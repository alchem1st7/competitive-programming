# Team

problems = int(input())
solution = 0


for i in range(problems):
    num_problems = map(int, input().split())
    if sum(num_problems) > 1:
        solution += 1

print(solution)