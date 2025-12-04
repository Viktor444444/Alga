# Oszd meg és uralkodj, Rendezés, Keresés
# Szilágyi Viktor Factory Machines megoldása

n, t = map(int, input().split()) # a map intté forceol

time_in_second_for_each_machine = list(map(int, input().split()))

machines_number = n
products_number = t

#bináris keresés:

left = 1 #fastest possibility
right = t * min(time_in_second_for_each_machine) #slowest: the fastest machine does all the work

while left < right:
    mid = (left + right) // 2 #lekerekítve osztás operátor

    # hány terméket tud az összes gép mid idő alatt
    products_made_already = sum(mid // k for k in time_in_second_for_each_machine) #syntax:

    if products_made_already >= products_number:
        #mid bőven elég idő
        right = mid
    else:
        #mid kevés idő
        left = mid + 1

print(left)