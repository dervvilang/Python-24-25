print("Hi! Guess a number from 0 to 1000 (inclusive), and I'll try to guess it.")
min = 0
max = 1000


while min <= max:

    step = 0
    mid = (min + max) // 2
    answ = input(f"If your number is {mid}, then write \"yes\", otherwise write \"more\" or \"less\".\n")


    if answ == "more":
        step += 1
        min = mid + 1
    elif answ == "less":
        step += 1
        max = mid - 1
    elif answ == "yes":
        step += 1
        print(f"Hah, I win.. Only {step} steps.")
        break
    else:
        print("You wrote something... strange. Try again.")
