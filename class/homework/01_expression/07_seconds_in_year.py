days_in_year : int = 365
hours_in_day : int = 24
minutes_in_hour : int = 60
seconds_in_min : int = 60

def main():
    print(f"There are {str(days_in_year * hours_in_day * minutes_in_hour * seconds_in_min)} second in a year")

if __name__ == '__main__':
    main()