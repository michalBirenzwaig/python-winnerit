day = input("Enter day:  ")
match day.lower():
    case ("Monday" | "Tuesday" | "Wednesday" | "Thursday" ):
        print("Weekday")
    case ("Saturday" | "Sunday"):
        print("weekend")
    case _:
        print("Invalid day")
