import json
import tkinter as tk
from tkinter import messagebox

from person import Person

# Hidden Tkinter root
root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)

class Learner(Person):

    def __init__(self):
        super().__init__()

        self.learners = []
        self.marks_list = []

    # ---------------- CALCULATE AVERAGE ----------------
    def calculate_average(self, marks):
        if len(marks) == 0:
            return 0
        return sum(marks) / len(marks)

    # ---------------- SEARCH LEARNER ----------------
    def search_learner(self, learner_id):

        for learner in self.learners:
            if learner["id"] == learner_id:
                return learner

        return None

    # ---------------- LOAD DATA ----------------
    def load_data(self):

        try:
            with open("learners.json", "r") as file:
                self.learners = json.load(file)

        except FileNotFoundError:
            self.learners = []

        except json.JSONDecodeError:
            self.learners = []

    # ---------------- SAVE DATA ----------------
    def save_data(self):

        with open("learners.json", "w") as file:
            json.dump(self.learners, file, indent=4)
            
    def safe_info(self, title, msg):
        try:
            messagebox.showinfo(title, msg)
        except:
            print(msg)

    def safe_error(self, title, msg):
        try:
            messagebox.showerror(title, msg)
        except:
            print(msg)

    def safe_confirm(self, title, msg):
        try:
            return messagebox.askyesno(title, msg)
        except:
            return input(msg + " (y/n): ").lower() == "y"        

    # ---------------- RUN SYSTEM ----------------
    def run_system(self):

        emp_password = "3456"
        logged_in = False

        enter_password = input("Enter password: ")

        if enter_password == emp_password:

            logged_in = True
            print("Login Successful")

            self.load_data()

        else:
            print("Incorrect password")

        while logged_in:

            print("\n===== LPTS MENU =====")
            print("1. Add New Learner")
            print("2. View Learners")
            print("3. Update Learner")
            print("4. Remove Learner")
            print("5. Add Marks")
            print("6. Search Learner")
            print("7. Show Learner Result")
            print("8. Exit")

            try:
                option = int(input("Select option (1-8): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            # ---------------- ADD LEARNER ----------------
            if option == 1:

                learner = {
                    "id": int(input("Enter student ID: ")),
                    "name": input("Enter name: "),
                    "age": int(input("Enter age: ")),
                    "course": input("Enter course: "),
                    "marks": []
                }

                self.learners.append(learner)

                self.safe_info(
                    "Success",
                    "Learner added successfully!"
                )

            # ---------------- VIEW LEARNERS ----------------
            elif option == 2:

                if len(self.learners) == 0:

                    self.safe_error(
                        "Error",
                        "No learners found."
                    )

                else:

                    for learner in self.learners:

                        print("\n--------------------")
                        print("ID:", learner["id"])
                        print("Name:", learner["name"])
                        print("Age:", learner["age"])
                        print("Course:", learner["course"])
                        print("Marks:", learner["marks"])

            # ---------------- UPDATE LEARNER ----------------
            elif option == 3:

                search_id = int(
                    input("Enter learner ID to update: ")
                )

                learner = self.search_learner(search_id)

                if learner:

                    learner["id"] = int(input("New ID: "))
                    learner["name"] = input("New Name: ")
                    learner["age"] = int(input("New Age: "))
                    learner["course"] = input("New Course: ")

                    self.safe_info(
                        "Success",
                        "Learner updated successfully!"
                    )

                else:

                    self.safe_error(
                        "Error",
                        "Learner not found."
                    )

            # ---------------- REMOVE LEARNER ----------------
            elif option == 4:

                search_id = int(
                    input("Enter learner ID to remove: ")
                )

                learner = self.search_learner(search_id)

                if learner:

                    confirm = self.safe_confirm(
                        "Confirm Removal",
                        "Are you sure you want to remove this learner?"
                    )

                    if confirm:

                        self.learners.remove(learner)

                        self.safe_info(
                            "Success",
                            "Learner removed successfully!"
                        )

                else:

                    self.safe_error(
                        "Error",
                        "Learner not found."
                    )

            # ---------------- ADD MARKS ----------------
            elif option == 5:

                search_id = int(
                    input("Enter learner ID to add marks: ")
                )

                learner = self.search_learner(search_id)

                if learner:

                    while True:

                        mark = int(
                            input("Enter mark (-2 to stop): ")
                        )

                        if mark == -2:
                            break

                        learner["marks"].append(mark)

                    self.safe_info(
                        "Success",
                        "Marks added successfully!"
                    )

                else:

                    self.safe_error(
                        "Error",
                        "Learner not found."
                    )

            # ---------------- SEARCH LEARNER ----------------
            elif option == 6:

                search_id = int(
                    input("Enter learner ID to search: ")
                )

                learner = self.search_learner(search_id)

                if learner:

                    avg = self.calculate_average(
                        learner["marks"]
                    )

                    print("\n===== SEARCH RESULT =====")
                    print("ID:", learner["id"])
                    print("Name:", learner["name"])
                    print("Age:", learner["age"])
                    print("Course:", learner["course"])
                    print("Marks:", learner["marks"])
                    print("Average:", round(avg, 2))

                    if avg >= 75:
                        print(
                            "Certificate: QUALIFIED WITH DISTINCTION"
                        )

                    elif avg >= 50:
                        print(
                            "Certificate: QUALIFIED"
                        )

                    else:
                        print(
                            "Certificate: NOT QUALIFIED"
                        )

                else:

                    self.safe_error(
                        "Error",
                        "Learner not found."
                    )

            # ---------------- SHOW RESULT ----------------
            elif option == 7:

                search_id = int(
                    input("Enter learner ID: ")
                )

                learner = self.search_learner(search_id)

                if learner:

                    avg = self.calculate_average(
                        learner["marks"]
                    )

                    print(
                        f"\nResult of {learner['name']}"
                    )

                    print(
                        "Average:",
                        round(avg, 2)
                    )

                    if avg >= 75:
                        print("Performance: Passed with distinction")
                        self.safe_info(
                            "Performance:","PASS / QUALIFIED WITH DISTINCTION"
                        )

                    elif avg >= 50:
                        print("Performance: Passed")
                        self.safe_info(
                            "Performance:","PASS / QUALIFIED"
                        )

                    else:
                        print("Performance: Failed")
                        self.safe_info(
                            "Performance:","FAIL / NOT QUALIFIED"
                        )

                else:

                    self.safe_error(
                        "Error",
                        "Learner not found."
                    )

            # ---------------- EXIT ----------------
            elif option == 8:

                confirm = self.safe_confirm(
                    "Exit System",
                    "Do you want to save data and exit?"
                )

                if confirm:

                    self.save_data()

                    self.safe_info(
                        "Success",
                        "Data saved successfully!"
                    )

                    print("Exiting system...")
                    break

            else:
                print("Invalid option.")