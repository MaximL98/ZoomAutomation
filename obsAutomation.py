import os
import time
import pygetwindow as gw
from pynput.keyboard import Controller
import psutil


def open_obs():
    if not "obs64.exe" in (p.name() for p in psutil.process_iter()):
        # opens OBS following the given path
        application = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio\OBS Studio (64bit).lnk"
        os.startfile(application)
        time.sleep(5)


# starts obs and making it the active window
def obs_start():
    # activating OBS
    win = gw.getWindowsWithTitle('OBS')[0]
    win.activate()
    time.sleep(10)
    # calling the hotkeys
    hotkey_e()


# TODO stop recording
def obs_end():
    win = gw.getWindowsWithTitle('OBS')[0]
    win.activate()
    time.sleep(2)
    hotkey_end()


# hotkeys
def hotkey_e():
    # calling the controller
    keyboard = Controller()
    # switch scenes hotkey
    switch_to_scene = "a"
    # start recording hotkey
    start_recording = "r"
    # presses and releases
    keyboard.press(switch_to_scene)
    time.sleep(0.05)
    keyboard.release(switch_to_scene)
    time.sleep(0.05)
    keyboard.press(start_recording)
    time.sleep(0.05)
    keyboard.release(start_recording)


def hotkey_end():
    keyboard = Controller()
    end_recording = "s"
    keyboard.press(end_recording)
    time.sleep(0.05)
    keyboard.release(end_recording)
# HOTKEY = [HotKey(HotKey.parse("a"), hotkey_e())]
