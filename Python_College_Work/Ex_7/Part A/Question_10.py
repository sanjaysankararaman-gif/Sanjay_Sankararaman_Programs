pos_keywords = ['excellent', 'good', 'great', 'fast', 'easy', 'happy']
neg_keywords = ['bad', 'poor', 'slow', 'expensive', 'disappointing', 'worst']

pos_reviews,neg_reviews,neutral_reviews = [],[],[]

f = open('reviews.txt', 'r')
f1 = open('sentiment_report.txt', 'w')
a = f.readline()
while a:
    p,ne = 0,0
    a = a.rstrip('\n')
    for i in a.split():
        if i.lower() in pos_keywords:
            P += 1
        elif i.lower() in neg_keywords:
            ne += 1
    if p > ne:
        pos_reviews.append(a)
    elif ne > p:
        neg_reviews.append(a)

    elif ne == p:
        neutral_reviews.append(a)

    a = f.readline()


f1.write('Postive reviews:\n')
f1.write('Number of positive reviews: '+len(pos_reviews)+'\n')
print('Postive reviews: ')
for i in pos_reviews():
    f1.write(i+'\n')
    print(i)
print()

f1.write('Negative reviews:\n')
f1.write('Number of negative reviews: '+len(neg_reviews)+'\n')
print('Negative reviews: ')
for i in neg_reviews():
    f1.write(i+'\n')
    print(i)

print()
f1.write('Neutral reviews:\n')
f1.write('Number of neutral reviews: '+len(neutral_reviews)+'\n')
print("Neutral reviews: ")

for i in neutral_reviews():
    f1.write(i+'\n')
    print(i)

f.close()
f1.close()


