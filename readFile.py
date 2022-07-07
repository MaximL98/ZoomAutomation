from datetime import date
import calendar


# function that reads a given file
def read_file():
    flag = 0
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
                        link = file.readline()
                        link = link.strip('\n')
                    # getting the starting time of the Zoom call
                    if lines.startswith("StartTime:"):
                        start = file.readline()
                        start = start.strip('\n')
                    # getting the end time of the Zoom call
                    if lines.startswith("EndTime:"):
                        end = file.readline()
                        end = end.strip('\n')
        if not flag:
            print("No Lectures on " + curr_date)
            return None, None, None
    # closing the file
    file.close()
    # returning all the values needed from the file
    return link, start, end

# TODO
# def count_lec():
# count = 0
# with open('zoom_lec.txt', 'r') as file:
# for line in file:
# if(line.startswith())
