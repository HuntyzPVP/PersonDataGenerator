import random

while True:
    try:
        number_of_people = int(input("Please select the number of people you would like to create values for between 2-8 people: "))
        if number_of_people < 2 or number_of_people > 8:
            print("Woah! You have to select a number between 2-8\n")
        else:
            break
    except ValueError:
        print("Must provide an integer value.\n")
        continue

human_types = ('Male', 'Female', 'Kid')

def personal_details():
    total_baggage_weight = 0

    for number in range(1, number_of_people + 1):
        number_of_person, human_type = number, random.choice(human_types)
        if human_type == 'Male':
            weight = random.randint(170, 240)
            baggage_weight = random.randint(10, 50)
            total_baggage_weight += baggage_weight
        elif human_type == 'Female':
            weight = random.randint(115, 160)
            baggage_weight = random.randint(10, 50)
            total_baggage_weight += baggage_weight
        else:
            weight = random.randint(75, 125)
            baggage_weight = random.randint(0, 30)
            total_baggage_weight += baggage_weight
        print("Person: {}\nHuman Type: {}\nWeight: {} Pounds\nBaggage Weight: {} Pounds\n".format(number_of_person, human_type, weight, baggage_weight))
    print("Total Baggage Weight:", total_baggage_weight, "Pounds\n")

personal_details()