valid_r = 0
low = 0
mid = 0
high = 0

while True:
    movie_r = int(input("Enter a movie rating: "))

    if movie_r == -1:
        break

    if movie_r < 1 or movie_r > 5:
        print("The movie name must be between 1 and 5")
        continue

    if movie_r == 1 or movie_r == 2:
        low += 1
        valid_r += 1
    elif movie_r == 3:
        mid += 1
        valid_r += 1
    elif movie_r == 4 or movie_r == 5:
        high += 1
        valid_r += 1

print("Valid ratings", valid_r)
print("Low (1-2)", low)
print("Middle (1-3)", mid)
print("High (4-5)", high)
