import webbrowser
import time


# import pygetwindow as gw

# function to check if the time of the lecture is the current time
def check_time(link, alarm):
    # getting the current time
    current_time = time.strftime("%H:%M:%S")
    # while it's not lecture time keep waiting
    while current_time != alarm:
        current_time = time.strftime("%H:%M:%S")
        print("Waiting, the current time is " + current_time)
        time.sleep(1)
        # if it is lecture time open the link from the file
        if current_time == alarm:
            print("Starting Lecture")
            webbrowser.open(link)
            time.sleep(10)
            # maximize_zoom()
            return True


def end_recording(end):
    # getting current time
    current_time = time.strftime("%H:%M:%S")
    while current_time != end:
        current_time = time.strftime("%H:%M:%S")
    # checking if the lecture time came to an end
    if current_time == end:
        print("Lecture Ended")
        return True

# def maximize_zoom():
# zoom_window = gw.getWindowsWithTitle('Zoom Meeting')[0]
# zoom_window.activate()
# zoom_window.maximize()

# TODO close obs when last lecture ends
