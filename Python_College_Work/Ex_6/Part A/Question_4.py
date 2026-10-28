import math
songs = ["Shape of You", "Believer", "Perfect", "Memories"]
duration = [4.2, 3.4, 4.4, 3.1]

d = dict(zip(songs, duration))
print(d)

for i in d:
    print('Song:', i)
    print("Duration:", d[i])

a = math.inf
s = ''
for i in d:
    if d[i] < a:
        a = d[i]
        s = i
print()
print("Shortest Song: ", s)
print("Duration: ", a)

print()

print("Songs whose duration is less than 4 minutes")

for i in d:
    if d[i] < 4:
        print("Song: ", i)
        print("Duration: ", d[i])

print()

print("Total playlist duration: ", sum(d.values()))


    
