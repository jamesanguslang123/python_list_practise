import random

languages = ["Python", "JavaScript", "Java", "C#", "C++"]

while True:
    # Display the languages with clean formatting
    for idx, lang in enumerate(languages):
        if idx == 0:
            print(f"First language: {lang}")
        elif idx == len(languages) - 1:
            print(f"Last language: {lang}")
        else:
            print(f"Language at index {idx}: {lang}")

    # Ask the user for a new language and replace a random entry
    new_lang = input("Enter a programming language to add (or press Enter to skip): ")
    if new_lang:
        replace_idx = random.randint(0, len(languages) - 1)
        languages[replace_idx] = new_lang
        print(f"Replaced language at position {replace_idx} with {new_lang}.")

    # Ask whether to continue
    cont = input("Do you want to continue? (yes/no): ").strip().lower()
    if cont == "no":
        print("Exiting the program. Goodbye!")
        break
    elif cont != "yes":
        print("Invalid input. Assuming you want to continue.")
        # loop continues
