import random

def randomize(items):
    newList = []
    for i in range(0, len(items)):
        randomNum = random.randint(0, len(items)-1)
        newList.append(items[randomNum])
        items.pop(randomNum)
    return newList

def question(fråga, options, correct):
    options = randomize(options)
    print("")
    print(fråga)
    i = 0
    for option in options:
        i += 1
        print(f"{i}. {option}")
    
    chosen = int(input("Ditt val: "))
    if options[chosen-1] == correct:
        print("Rätt!")
        return 1
    else:
        print(f"Fel, rätt svar var: {correct}")
        return 0

def run_quiz():
    quiz = [
        question(fråga="Vilken huvudstad har Sverige?", options=["Oslo", "Stockholm", "Köpenhamn"], correct="Stockholm"),
        question(fråga="Vilket år började andrav ärldskriget?", options=["1914", "1939", "1945"], correct="1939")
    ]
    
    print("")
    print(f"Du fick {sum(quiz)} av {len(quiz)} rätt")

run_quiz()