# ZoomAutomation <img src = "https://user-images.githubusercontent.com/107645094/180647786-0f834d5b-cbb4-401f-b872-9316dd6ebbc0.png" width = "35" height = "35">

*Python program, that automatically opens Zoom meetings, and using OBS to record them*.

The program gets the schedule from a text file, that will look something like this:
```
<day of the week>
Link:
<lectures link>
StartTime:
<lecture starting time>
EndTime:
<lecture ending time>
```
Example
```
Sunday

Link:
www.google.com
StartTime:
08:30:00
EndTime:
10:25:00
```
The recordings are recorded with Open Broadcaster Software AKA OBS  <img src = "https://user-images.githubusercontent.com/107645094/180647953-dbeb238d-b633-48de-a3ca-49325d4a9119.png" width = "20" height = "20">

## Python packages used
- obswebsocket
- webbrowser
- logging
- psutil
- os
- sys
- urllib
- time
- calendar
## Future ideas
- [ ] Read from Excel file instead of text file

Creator @MaximL98\
***recording only for user’s personal usage, with the permission of the host :bangbang:***
