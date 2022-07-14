from readFile import read_file
from openLink import check_time, end_recording
from obsAutomation import obs_start, obs_end, obs_connection


# main function to call all others functions
def main():
    # getting the link, time start of the lecture and end time from file
    links, starts, ends = read_file()
    # if there is no link or lecture start or end time program ends
    if (links or starts or ends) is None:
        print("Wrong input for lecture link or start/end time")
        print("Please make sure the text file contains all the needed information")
        return
    if not (len(links) == len(starts) == len(ends)):
        print("Bad text file input")
        print("Make sure every link has it start time and end time")
        return
    # in a loop run check_time and end_recording to open OBS and record the lectures on user given times and links
    for i in range(len(links)):
        # opens OBS and loggings to obs software to run commands
        ws = obs_connection()
        if check_time(links[i], starts[i]):
            # connecting to OBS and starts recording
            obs_start(ws)
        if end_recording(ends[i]):
            # stops recording and closes OBS
            obs_end(ws)


# run main
main()

# TODO change from reading a file to exel
