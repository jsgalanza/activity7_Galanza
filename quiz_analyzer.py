scores = []

for i in range(1, 6):
    score = int(input(f"Enter Score {i}: "))
    scores.append(score)

print("====QUIZ SCORE REPORT=====")
print(f"Quiz Scores: {scores}")
print("Number of Quizzes: 5")
print(f"Total Score: {sum(scores)}")
print(f"Average Score: {sum(scores) / len(scores):.2f}")
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Ascending: {(sorted(scores))}")
print(f"Descending: {(sorted(scores, reverse=True))}")
print(f"Original Scores: {scores}")