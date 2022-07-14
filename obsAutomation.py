import logging
import os
import sys
import time
import psutil

from obswebsocket import obsws, requests
from settings import HOST, PORT, PASSWORD, OBS_PATH


def open_obs():
    # checks if OBS not already running if not opens it
    if not "obs64.exe" in (p.name() for p in psutil.process_iter()):
        # opens OBS following the given path
        application = OBS_PATH
        os.startfile(application)
        time.sleep(5)


def close_obs():
    # checks if OBS is running, if yes, closes it
    if "obs64.exe" in (p.name() for p in psutil.process_iter()):
        # close OBS
        os.system("TASKKILL /F /IM obs64.exe")


def obs_connection():
    # opens OBS
    open_obs()
    time.sleep(1)
    # logs into OBS-WEBSOCKET
    logging.basicConfig(level=logging.INFO)
    sys.path.append('../')
    # host name
    host = HOST
    # port name given by user
    port = PORT
    # password given by user
    password = PASSWORD
    ws = obsws(host, port, password)
    return ws


# starts obs and making it the active window
def obs_start(ws):
    # connects to OBS websocket
    ws.connect()
    # starts recording
    ws.call(requests.StartRecording())
    print("OBS started recording")


def obs_end(ws):
    # stops recording
    ws.call(requests.StopRecording())
    print("OBS stopped recording")
    # disconnecting from OBS websocket
    ws.disconnect()
    # closes OBS
    close_obs()
