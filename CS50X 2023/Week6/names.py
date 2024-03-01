import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]
name = input("Name: ")
for n in names:
    if n in name:
        print("Found")
        sys.exit(0)
print("Not found")
sys.exit(1)
