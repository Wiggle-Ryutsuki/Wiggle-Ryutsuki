# Maimoona Aziz

# Ask user for input
file = input("File name: ")

# Remove whitespaces and make all lowercase
file = file.lower().strip()

# Extract extension
exten = file[file.rfind('.'):]

# Compare extensions
if exten == ".gif" or exten == ".png":
    print(f"image/{exten[1:]}")
elif exten == ".jpg" or exten == ".jpeg":
    print("image/jpeg")
elif exten ==".pdf" or exten == ".zip":
    print(f"application/{exten[1:]}")
elif exten == ".txt":
    print("text/plain")
else:
    print("application/octet-stream")
