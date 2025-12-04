# DP
# Szilágyi Viktor Dice Combinations megoldása

# O(n) idő

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1

#feladat szt. így kell megadni, h ne legyenek túl nagy számok
MOD = 10**9 + 7

#elmegyek n-ig
for i in range (1 , n+1):
    #megnézem 1-6 a dobási lehetőségeket
    for j in range (1, 7):
        #ha az adott tobott érték nem nagyobb, mint i vagyis a jelenlegi n
        if i-j >= 0:
            #dp[i]: hányféleképp lehet i-t dobni
            #dp i-edik eleme legyen 0 + plusz az i-j-edik elem lehetőségeinek száma
            dp[i] = (dp[i] + dp[i - j]) % MOD

#vagyis végigmegyünk a számokon n-ig, megnézzük mind a 6 dobási lehetőséggel, hogy lehet-e i-t kirakni, és amelyikkel igen, akkor hozzáadjuk az összes olyan esetet, amelyet egy korábbi i-hez 1-6 számokat hozzáadva kaphatunk


print(dp[n])