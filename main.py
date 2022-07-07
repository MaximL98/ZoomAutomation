from readFile import read_file
from openLink import check_time, end_recording
from obsAutomation import obs_start, obs_end, open_obs


# main function to call all others functions
def main():

    # getting the link, time start of the lecture and end time from file
    link, start, end = read_file()
    if (link or start or end) is None:
        return
    open_obs()
    # checking if it lectures start time
    if check_time(link, start):
        obs_start()
    # checking if it lectures end time
    # TODO
    if end_recording(end):
        obs_end()


main()

# TODO change from reading a file to exel
