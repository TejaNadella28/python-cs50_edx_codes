def main():
    time_input = input("What time is it? ")
    meal_time = check_meal_time(time_input)
    if meal_time:
        print(meal_time)

def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60

def check_meal_time(time_str):
    time = convert(time_str)
    if 7.0 <= time < 8.0:
        return "breakfast time"
    elif 12.0 <= time <=13.0:
        return "lunch time"
    elif 18.0 <= time < 19.0:
        return "dinner time"

    else:
        return None

if __name__ == "__main__":
    main()
