def main():
    time = input("Enter the time (in 24-hour format): ")
    timeinhrs = convert(time)
    if 7 <= timeinhrs <= 8:
        print("It's breakfast time.")
    elif 12 <= timeinhrs <= 13:
        print("It's lunch time.")
    elif 18 <= timeinhrs <= 19:
        print("It's dinner time.")
    else:
        pass

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return hours + minutes

if _name_ == "_main_":
    main()
