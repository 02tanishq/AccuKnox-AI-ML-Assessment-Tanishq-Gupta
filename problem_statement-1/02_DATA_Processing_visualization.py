import random

from pathlib import Path
import requests
import matplotlib.pyplot as plt



API = "https://jsonplaceholder.typicode.com/users"

# Reolve database path relative to script location
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_IMAGE = BASE_DIR / "students_scores.png"

def fetch_student():
    response = requests.get(API , timeout=10)

    if response.status_code != 200 :
        print("Failed to fetch data from api")
        return []

    data = response.json()

    students_scores = []
    
    for i, score in enumerate(data[:5]):
        name = score.get("name")
        index = i + 1

        # we are building fake score to present as jsonholder api does
        # not give scores .
        random_number = random.uniform(0 , 10.7)
        score = round(35 + (random_number * 6),2 )

        students_scores.append((name , score))

    return students_scores
    
def calculate_avg(students_scores):
    if not students_scores:
        return 0
    total_score_sum = sum(student[1] for student in students_scores)
    avg = round(total_score_sum / len(students_scores),2)

    return avg


def display_score(avg,students_scores):

    print("\n TEST SCORES:")
    print("-" * 55)

    for student in students_scores:
        print(f"{student[0]}: {student[1]}")

    print("-"*55)
    print(f"Average Score : {avg}")

def create_chart(students, average):
    names = [student[0] for student in students]
    scores = [student[1] for student in students]

    plt.figure(figsize=(10, 6))

    plt.bar(names, scores , color = 'yellow')

    plt.axhline(
        average,
        linestyle="--",
        label=f"Average: {average:.2f}"
    )

    plt.title("Student Test Scores")
    plt.xlabel("Students")
    plt.ylabel("Score")

    plt.xticks(rotation=30, ha='right')

    plt.legend()
    plt.tight_layout()

    plt.savefig(OUTPUT_IMAGE)
    print(f"\nChart saved to: {OUTPUT_IMAGE}")

    # Only show interactively if a GUI backend is available
    try:
        if plt.get_backend().lower() != "agg":
            plt.show()
        else:
            plt.close()
    except Exception:
        plt.close()

def main() :
    students_scores= fetch_student()

    if not students_scores :
        print("No student data fetched.")
        return

    average = calculate_avg(students_scores)

    display_score(average,students_scores)
    create_chart(students_scores , average)


if __name__ == "__main__":
    main()
