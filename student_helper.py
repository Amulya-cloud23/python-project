print("Welcome to Python Student Helper!")

name = input("Enter your name: ")

print("Hello", name)
print("How can I help you today?")

print("1. Study Tips")
print("2. Python Practice")
print("3. Motivation")

choice = input("Enter your choice: ")

if choice == "1":
    print("Make a daily study timetable!")

elif choice == "2":
    print("Practice Python coding every day!")

elif choice == "3":
    print("Believe in yourself. Keep learning!")

else:
    print("Invalid choice!")
