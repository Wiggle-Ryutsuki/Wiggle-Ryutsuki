# Maimoona Aziz
import inflect

p = inflect.engine()
# Initialise name list
names = []

while True:
    try:
        # Prompt for user input
        name = input("Name: ")
        # Add input into a list and keep prompting until CTRL-D
        names.append(name)

    # When CTRL-D is pressed, join the names in the list than print
    except EOFError:
        names = p.join((names))
        print(f"Adieu, adieu, to {names}")
        break
