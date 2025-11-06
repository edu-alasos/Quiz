def question(fråga, options, correct):
    print(fråga)
    i = 0
    for option in options:
        i += 1
        print(f"{i}. {option}")
    
    chosen = int(input("Ditt val: "))
    if options[chosen-1] == correct:
        print("Rätt!")
    else:
        print("Fel.")
    
question(fråga="Vilken huvudstad har Sverige?", options=["Oslo", "Stockholm", "Köpenhamn"], correct="Stockholm")