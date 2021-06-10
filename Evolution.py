import random
import string
import time


def guesser():
    possible_characters = string.ascii_lowercase + string.digits
    target = input(">>> Enter your target text: ")
    print()
    target.lower()
    start = time.time()
    attempt_this = ''.join(random.choice(possible_characters) for i in range(len(target)))
    completed = False
    generation = 0

    while not completed:
        print(">>>> ", attempt_this, " <<<<")
        attempt_next = ""
        completed = True
        for i in range(len(target)):
            if attempt_this[i] != target[i]:
                completed = False
                attempt_next += random.choice(possible_characters)
            else:
                attempt_next += target[i]
        generation += 1
        attempt_this = attempt_next

    end = time.time()
    print(f"\n- {target} took {generation:d} generation(s) and {end - start:.3f} seconds.")


guesser()
