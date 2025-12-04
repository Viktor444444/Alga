# Fák, DP
# Szilágyi Viktor Dice Combinations megoldása

number_of_employees = int(input())
employees_and_their_bosses = list(map(int, input().split()))

#making 2D list
subordinates = []
for _ in range(number_of_employees + 1):
    subordinates.append([])

#a subordianes 2D lista, melyben minden boss-nak van egy listája benne a közvetlen alkalmazottaival
for employee_id, boss_id in enumerate(employees_and_their_bosses, start = 2):
    subordinates[boss_id].append(employee_id)

#num+1 element list with elements being zero
dp = [0] * (number_of_employees + 1)

stack = [(1, 0)]

#addit fut amíg van elem a stack-ben
while stack:
    employee, state = stack.pop()

    if state == 0:
        #először találkozunk vele
        stack.append((employee, 1))
        #végigmegyünk a beosztottakon
        for sub in subordinates[employee]:
            stack.append((sub, 0))
    else:
        #minden sub dp ki van számolva
        count = 0
        for sub in subordinates[employee]:
            count += 1 + dp[sub]
        dp[employee] = count

print(*dp[1:]) #* operator unpacks the list

#why dp: storing result in dp so you don’t recompute it