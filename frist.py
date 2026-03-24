import csv
import os
import re


def main():

    skills = save_skills_csv()

    print(f"--- ⚔️ Welcome back, Omar! You have {len(skills)} unfinished tasks ⚔️ ---")
    print(
        "What do you want to do?\n"
        "1: Add new task\n"
        "2: Remove completed task\n"
        "3: Show tasks list\n"
        "4: Exit"
    )

    while True:
        i = input("\nWhat do you want: ")
        os.system("cls" if os.name == "nt" else "clear")
        if i == "4":

            save_skills_csv(skills)
            print("Goodbye Hero! 🦸‍♂️")
            break
        elif i == "1":
            add(skills)
        elif i == "2":
            remove(skills)
        elif i == "3":
            show(skills)
        else:
            print("❌ Choose a valid option")


def add(skill):
    intr = input("Add new task: ")
    clean_text = re.sub(r"[^a-zA-Z0-9 ]", "", intr)
    skill.append(clean_text)
    print(f"✅ '{clean_text}' has been added!")


def remove(remskill):
    while True:
        if len(remskill) == 0:
            print("Your TODO list is empty!")
            break

        print("Current tasks:", remskill)
        revskill = input("Which task  do you want to remove (or 'q' to cancel): ")

        if revskill == "q":
            break

        try:
       
            remskill.remove(revskill)
            print(f"🗑️ '{revskill}' has been removed!")
            break
        except ValueError:
            print("⚠️ Enter a valid task please ☺️")


def show(skillsho):
    print("\n--- 📜 Your Tasks ---")
    print(skillsho)
    print("----------------------")


def save_skills_csv(tasks_list=None):
    if tasks_list is None:
        try:
            with open("my_todo.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader) 
                tasks_list = [row[0] for row in reader if row]
            return tasks_list
        except FileNotFoundError:
            return [] 
    else:
        with open("my_todo.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Task Name"])
            for s in tasks_list:
                writer.writerow([s])


if __name__ == "__main__":
    main()
