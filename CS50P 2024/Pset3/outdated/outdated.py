# Maimoona Aziz

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Get input from user
while True:
    try:
        date = input("Date: ")

        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if month > 12 or day > 31:
                continue

        elif "," in date:
            month, day, year = date.replace(",", "").split(" ")

            day = int(day)
            year = int(year)

            if month not in months or day > 31:
                continue
            month = (months.index(month)) + 1

        else:
            continue

    except ValueError:
        pass
    else:
        break

print(f"{year}-{month:02}-{day:02}")

