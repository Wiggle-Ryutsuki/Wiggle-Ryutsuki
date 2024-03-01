from cs50 import SQL
import csv

db = SQL("sqlite:///roster.db")

data = []

# Opening and reading CSV
try:
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            data.append(row)

except FileNotFoundError:
    print("File could not be opened ")

students_table = "students"
houses_table = "houses"
assign_table = "assign"

# Inserting data into students table
existing_students = set()
for row in data:
    student_name = row["student_name"]
    if student_name not in existing_students:
        student_query = "INSERT INTO students (name) VALUES (?)"
        db.execute(student_query, student_name)
        existing_students.add(student_name)

# Inserting data into houses table
# Insert data into houses table (avoiding duplicates)
existing_houses = set()
for row in data:
    house_name = row["house"]
    if house_name not in existing_houses:
        house_query = "INSERT INTO houses (house, head) VALUES (?, ?)"
        db.execute(house_query, house_name, row["head"])
        existing_houses.add(house_name)



# Create a mapping of house names to IDs
house_id_map = {}
houses = db.execute("SELECT id, house FROM houses")
for house in houses:
    house_id_map[house["house"]] = house["id"]

# Insert data into assign table

# Create a mapping of student names to IDs
student_id_map = {}
students = db.execute("SELECT id, name FROM students")
for student in students:
    student_id_map[student["name"]] = student["id"]

# Insert data into assign table
for row in data:
    student_name = row["student_name"]
    house_name = row["house"]

    # Get the corresponding IDs from the mappings
    student_id = student_id_map[student_name]
    house_id = house_id_map[house_name]

    # Insert data into the assign table
    assign_query = "INSERT INTO assign (student_id, house_id) VALUES (?, ?)"
    db.execute(assign_query, student_id, house_id)