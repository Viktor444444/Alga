# Rendezés, Mohó
# Szilágyi Viktor Movie Festival megoldása

class Movie:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start} {self.end}"

movies = []
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    movies.append(Movie(a,b))

movies.sort(key=lambda movie: movie.end)

current_time = 0
output = 0

for movie in movies:
    if(current_time <= movie.start):
        output += 1
        current_time = movie.end

print(output)