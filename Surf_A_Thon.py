scores  = []
names = []

highest_score = 0

result_f = open("results.txt")

for line in result_f:
    (name, score) = line.split()
    scores.append(float(score))
    names.append(name)
result_f.close()
scores.sort()
scores.reverse()

print("The Highest Scores were:")
print(scores[0])
print(scores[1])
print(scores[2])
