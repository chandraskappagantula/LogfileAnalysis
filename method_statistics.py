"""
This module works with the program written in the "LogfileAnalysis" GitHub repository. 

Given an array of start times and end times for a specific method's execution, among other input, this module will return 
the mean and median runtime for that method, using the datetime module's implementation to calculate durations. It will also 
return the standard deviation, range, and a distribution of runtimes. 
"""

from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import statistics
import tkinter

def return_statistics(START_TIMES, END_TIMES, METHOD_NAME, MASTER_WINDOW, COORDS):
    """
    START_TIMES: an array containing all the start times of the chosen method's execution
    END_TIMES: an array containing all the ending times of the chosen method's execution
    METHOD_NAME: the chosen method
    MASTER_WINDOW: the main window in which you want the distribution to be placed. It will also be saved to the root directory
    COORDS: relative coordinates, in decimal, of where the image should be placed (example: (0.5, 0.5) is perfectly in the middle)
    """
    DURATIONS = []
    for i in range(len(END_TIMES)):
        try: 
            d1 = datetime.strptime(END_TIMES[i], "%m-%d %H:%M:%S")
            d2 = datetime.strptime(START_TIMES[i], "%m-%d %H:%M:%S")
            DURATIONS.append(d1.microsecond - d2.microsecond)
        except IndexError:
            DURATIONS.append(0)
    
    MASTER_WINDOW.pack()

    MIN_DURATION = min(DURATIONS)
    MAX_DURATION = max(DURATIONS)
    RANGE_DURATION = MAX_DURATION - MIN_DURATION
    AVG_DURATION = statistics.mean(DURATIONS) 
    MEDIAN_DURATION = statistics.median(DURATIONS)
    STDDEV_DURATION = statistics.stdev(DURATIONS)

    fig = plt.hist(DURATIONS)
    plt.savefig(f"distribution_of_runtimes_{METHOD_NAME}.png")

    phot_1 = tkinter.PhotoImage(file = f"distribution_of_runtimes_{METHOD_NAME}.png")
    phot_1 = phot_1.subsample(1)
    image_1 = tkinter.Label(MASTER_WINDOW, image = phot_1)
    image_1.photo = phot_1
    image_1.place(relx = COORDS[0], rely = COORDS[1], anchor = "center")

    return MIN_DURATION, MAX_DURATION, RANGE_DURATION, AVG_DURATION, MEDIAN_DURATION, STDDEV_DURATION