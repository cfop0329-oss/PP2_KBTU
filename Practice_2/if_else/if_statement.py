# Example 1: Simple condition
temperature = 30
if temperature > 25:
    print("It's a hot day!")
    print("Remember to drink water.")

# Example 2: Multiple statements in block
score = 85
if score >= 70:
    print("Passing grade!")
    print(f"Score: {score}")
    print("Well done!")

# Example 3: No else block (nothing happens if condition is False)
number = 4
if number % 2 == 0:
    print(f"{number} is even")

# Example 4: Nested if
age = 20
if age >= 18:
    print("You are an adult")
    if age >= 21:
        print("You can legally drink alcohol in some countries")