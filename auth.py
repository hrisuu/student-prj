import os

class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role

def authenticate(username, password):
    try:
        with open("data/passwords.txt", "r") as file:
            for line in file:
                fields = line.strip().split(",")
                if len(fields) != 3:  # Validate the number of fields
                    print(f"Invalid line format in passwords.txt: {line.strip()}")
                    continue
                stored_username, stored_password, role = fields
                if username == stored_username and password == stored_password:
                    return role  # Return the role (admin or student)
    except FileNotFoundError:
        print("Error: passwords.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_user_details(username):
    try:
        with open("data/users.txt", "r") as file:
            for line in file:
                stored_username, full_name, role = line.strip().split(",")
                if username == stored_username:
                    return User(username, full_name, role)
    except FileNotFoundError:
        print("Error: users.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_student_grades(username):
    try:
        with open("data/grades.txt", "r") as file:
            for line in file:
                stored_username, *grades = line.strip().split(",")
                if username == stored_username:
                    return grades  # Return the grades as a list
    except FileNotFoundError:
        print("Error: grades.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_student_eca(username):
    try:
        with open("data/eca.txt", "r") as file:
            for line in file:
                stored_username, *activities = line.strip().split(",")
                if username == stored_username:
                    return activities  # Return the activities as a list
    except FileNotFoundError:
        print("Error: eca.txt file not found.")
    except Exception as e:
        print(f"Error: {e}")
    return None

def update_student_profile(username, full_name):
    try:
        updated = False
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        with open("data/users.txt", "w") as file:
            for line in lines:
                stored_username, _, role = line.strip().split(",")
                if username == stored_username:
                    file.write(f"{username},{full_name},{role}\n")
                    updated = True
                else:
                    file.write(line)
        return updated
    except Exception as e:
        print(f"Error: {e}")
        return False