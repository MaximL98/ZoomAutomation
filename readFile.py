from datetime import date
import calendar


# function that reads a given file
def read_file():
    flag = 0
    # 3 arrays to store all the information from the file
    links = []
    start_times = []
    end_times = []
    # getting the current day name
    curr_date = date.today()
    curr_date = calendar.day_name[curr_date.weekday()]
    # opening the file
    with open('zoom_lec.txt', 'r') as file:
        # iterating line by line in the file
        for line in file:
            if line.startswith(curr_date):
                flag = 1
                for lines in file:
                    # getting the link of the Zoom call
                    if lines.startswith("Link:"):
                        links.append(file.readline().strip('\n'))
                        # getting the starting time of the Zoom call
                    if lines.startswith("StartTime:"):
                        start_times.append(file.readline().strip('\n'))
                    # getting the end time of the Zoom call
                    if lines.startswith("EndTime:"):
                        end_times.append(file.readline().strip('\n'))
        # if on current day user did not input any lectures, close program
        if not flag:
            print("No Lectures on " + curr_date)
            return None, None, None
    # storing the amount of lecture today
    count = len(links)
    # closing the file
    file.close()
    # printing information for user
    print_info(curr_date, count, start_times[0], max(end_times))
    # returning all the values needed from the file
    return links, start_times, end_times


# information printing function, giving user more details about his day
def print_info(curr_date, lec_count, start, end):
    print("Hello, Today is " + curr_date)
    print("Today you have", lec_count, "lectures")
    print("first lecture starting at " + start)
    print("last lecture ending at " + end)
    print("hopefully all lecture gonna be opened and recorded without problems")
    print("Good Luck, Enjoy!")
