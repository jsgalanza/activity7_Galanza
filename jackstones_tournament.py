scores = []

for i in range(1, 6):
    while True:
        score = int(input(f"Enter Score {i}: "))
            scores.append(score)

backup_scores = scores.copy()

print(f"Original Scores: {backup_scores}")
print("Backup successfully created")

y = True

while y:
    print("===== JACKSTONES SCORES MENU =====")
    print("1. Display Scores")
    print("2. Add Score")
    print("3. Insert Score")
    print("4. Remove Score")
    print("5. Remove Last Score")
    print("6. Search Score")
    print("7. Generate Statistics")
    print("8. Sort Scores")
    print("9. Reverse Scores")
    print("10. Clear Scores")
    print("11. Restore Original Scores")
    print("12. Exit")

    choice = int(input("Enter your choice (1-12): "))

    if choice == 1:
        print(f"Scores: {scores}")

    elif choice == 2:
        add_score = int(input("Enter score to add: "))
        if add_score < 0 or add_score > 10:
            print("Invalid score! Enter a score from 0 to 10.")
        else:
            scores.append(add_score)
            print(f"Updated Scores: {scores}")

    elif choice == 3:
        insert_score = int(input("Enter score to insert: "))
        if insert_score < 0 or insert_score > 10:
            print("Invalid score! Enter a score from 0 to 10.")
        else:
            index = int(input(f"Enter index (0 to {len(scores)}): "))
            if index < 0 or index > len(scores):
                print(f"Invalid index! Enter an index from 0 to {len(scores)}.")
            else:
                scores.insert(index, insert_score)
                print(f"Updated Scores: {scores}")

    elif choice == 4:
        if len(scores) == 0:
            print("Scores list is empty")
        else:
            remove_score = int(input("Enter score to remove: "))
            if remove_score not in scores:
                print("Score not found in the list.")
            else:
                scores.remove(remove_score)
                print(f"Updated Scores: {scores}")

    elif choice == 5:
        if len(scores) == 0:
            print("Scores list is empty")
        else:
            removed_score = scores.pop()
            print(f"Removed Score: {removed_score}")
            print(f"Updated Scores: {scores}")

    elif choice == 6:
        search_score = int(input("Enter score to search: "))
        occurrences = scores.count(search_score)
        if occurrences == 0:
            print("Score not found in the list.")
        else:
            first_index = scores.index(search_score)
            print(f"Number of Occurrences: {occurrences}")
            print(f"First Index: {first_index}")

    elif choice == 7:
        if len(scores) == 0:
            print("Scores list is empty")
        else:
            count = len(scores)
            total = sum(scores)
            average = total / count
            highest = max(scores)
            lowest = min(scores)
            print("===== SCORE STATISTICS =====")
            print(f"Scores: {scores}")
            print(f"Number of Scores: {count}")
            print(f"Total Score: {total}")
            print(f"Average Score: {average:.2f}")
            print(f"Highest Score: {highest}")
            print(f"Lowest Score: {lowest}")

    elif choice == 8:
        if len(scores) == 0:
            print("Scores list is empty")
        else:
            print("Select a choice:")
            print("(A) Ascending")
            print("(D) Descending")
            order = input("Enter sorting order: ").strip().upper()
            if order == "A":
                scores.sort()
                print(f"Sorted Scores: {scores}")
            elif order == "D":
                scores.sort(reverse=True)
                print(f"Sorted Scores: {scores}")
            else:
                print("Invalid sorting order! Enter (A) for Ascending or (D) for Descending.")

    elif choice == 9:
        if len(scores) == 0:
            print("Scores list is empty")
        else:
            scores.reverse()
            print(f"Reversed Scores: {scores}")

    elif choice == 10:
        scores.clear()
        print("All scores have been cleared.")
        print(f"Current Scores: {scores}")

    elif choice == 11:
        scores = backup_scores.copy()
        print("Original scores successfully restored.")
        print(f"Current Scores: {scores}")

    elif choice == 12:
        print("Thank you for using the system!")
        y = False

    else:
        print("Invalid choice! Please enter a number from 1 to 12.")
