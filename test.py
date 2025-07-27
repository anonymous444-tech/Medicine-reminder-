import questionary

answer = questionary.select(
    "Choose your operation:",
    choices=["Add", "Subtract", "Multiply", "Divide", "Exit"]
).ask()

print(f"You selected: {answer}")
