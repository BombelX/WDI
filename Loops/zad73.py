import random

def has_duplicate_birthdays(birthdays):
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return True
    return False

def birthday_paradox_simulation(num_people, num_trials=10000):
    same_birthday_count = 0

    for _ in range(num_trials):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if has_duplicate_birthdays(birthdays):
            same_birthday_count += 1

    probability = same_birthday_count / num_trials
    return probability

# Zakres wartości N od 20 do 40
for N in range(20, 41):
    probability = birthday_paradox_simulation(N)
    print(f"Liczba osób: {N}, Prawdopodobieństwo: {probability:.4f}")
