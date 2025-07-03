import tkinter
import math 
import csv
import statistics
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

window = tkinter.Tk()
window.title("Method statistics from chosen log files")
window.geometry("800x800")

query_frame = tkinter.Frame(window, height = 800, width = 800)
query_frame.pack()

analysis = tkinter.Frame(window, height = 800, width = 800)
analysis.pack()
analysis.pack_forget()

text1 = tkinter.Label(query_frame, text = "Input the method for which you want statistics in the textbox below. ", bd = 2, relief = "solid")
text2 = tkinter.Label(query_frame, text = "Include parentheses after the method's name. This query is case sensitive. ", bd = 2, relief = "solid")
text1.place(relx = 0.5, rely = 0.2, anchor = "center")
text2.place(relx = 0.5, rely = 0.23, anchor = "center")

e = tkinter.Entry(query_frame)
e.place(relx = 0.5, rely = 0.28, anchor = "center")

text3 = tkinter.Label(query_frame, text = "Input the starting signature \nthe log files use in the textbox below. The starting signature \nindicates the method beginning in execution. ", borderwidth=2, relief = "solid")
text3.place(relx = 0.25, rely = 0.45, anchor = "center")
e2 = tkinter.Entry(query_frame)
e2.place(relx = 0.25, rely = 0.53, anchor = "center")
text4 = tkinter.Label(query_frame, text = "Input the ending signature \nthe log files use in the textbox below. The ending signature \nindicates that the method has finished execution. ", borderwidth=2, relief = "solid")
text4.place(relx = 0.75, rely = 0.45, anchor = "center")
e3 = tkinter.Entry(query_frame)
e3.place(relx = 0.75, rely = 0.53, anchor = "center")

text5 = tkinter.Label(query_frame, text = "Select the log file from the file explorer below. ", bd = 2, relief = "solid")
text5.place(relx = 0.5, rely = 0.6, anchor = "center")

def ask():
    global file_path
    file_path = askopenfilename()
button1 = tkinter.Button(query_frame, text = "Select file", command = ask)
button1.place(relx = 0.5, rely = 0.65, anchor = "center")

submit_button = tkinter.Button(query_frame, text = "Get Method Statistics", command = lambda: get_method_statistics(e.get(), e2.get(), e3.get(), file_path))
submit_button.place(relx = 0.5, rely = 0.74, anchor = "center")

def get_method_statistics(method_name, starting_signature, ending_signature, file_path):
    global analysis, FREQUENCY, MIN_DURATION, MAX_DURATION, RANGE_DURATION, AVG_DURATION, MEDIAN_DURATION, STDDEV_DURATION, DURATIONS

    METHOD_NAME = str(method_name)

    FILE_PATH = str(file_path)
    SIGNATURES = [str(starting_signature), str(ending_signature)]

    # statistical variables below
    FREQUENCY = 0
    START_TIMES = []
    END_TIMES = []
    SIGNS = []
    LINES = []
    DURATIONS = []

    with open(FILE_PATH, "r") as r:
        for item in r.readlines():
            item = item.strip()
            splice = item.split(" ")
            if splice[-1] == METHOD_NAME:
                SIGNS.append(splice[3])
                LINES.append(splice)

    for i in range(len(SIGNS)): 
        if SIGNS[i] == SIGNATURES[0]:
            new = ""
            count = len(LINES[i][0]) - 3
            for n in range(len(LINES[i][0])):
                if n < count:
                    new += LINES[i][0][n]
                elif n == count:
                    break
            
            START_TIMES.append(new + " " + LINES[i][1])
            FREQUENCY += 1
        elif SIGNS[i] == SIGNATURES[1]:
            new = ""
            count = len(LINES[i][0]) - 3
            for n in range(len(LINES[i][0])):
                if n < count:
                    new += LINES[i][0][n]
                elif n == count:
                    break
            
            END_TIMES.append(new + " " + LINES[i][1])

    # subtract the times here and update the DURATIONS list

    for i in range(len(END_TIMES)):
        try: 
            d1 = datetime.strptime(END_TIMES[i], "%m-%d %H:%M:%S")
            d2 = datetime.strptime(START_TIMES[i], "%m-%d %H:%M:%S")
            DURATIONS.append(d1.microsecond - d2.microsecond)
        except IndexError: # if one execution starting is not ended in the log files
            DURATIONS.append(0)

    MIN_DURATION = min(DURATIONS)
    MAX_DURATION = max(DURATIONS)
    RANGE_DURATION = MAX_DURATION - MIN_DURATION
    AVG_DURATION = statistics.mean(DURATIONS) 
    MEDIAN_DURATION = statistics.median(DURATIONS)
    STDDEV_DURATION = statistics.stdev(DURATIONS)

    query_frame.pack_forget()
    query_frame.lower()
    analysis.pack(fill = "both", expand = True)
    analysis.tkraise()
    window.update()

    fig = plt.hist(DURATIONS)
    plt.savefig(f"distribution_of_runtimes_{METHOD_NAME}.png")

    phot_1 = tkinter.PhotoImage(file = f"distribution_of_runtimes_{METHOD_NAME}.png")
    phot_1 = phot_1.subsample(1)
    image_1 = tkinter.Label(analysis, image = phot_1)
    image_1.photo = phot_1
    image_1.place(relx = 0.5, rely = 0.64, anchor = "center")

    stat_1 = tkinter.Label(analysis, text = f"The average duration {METHOD_NAME} took to execute: {AVG_DURATION} ms.")
    stat_2 = tkinter.Label(analysis, text = f"{METHOD_NAME} was executed {FREQUENCY} times. ")
    stat_3 = tkinter.Label(analysis, text = f"The maxmimum execution time is: {MAX_DURATION}. ")
    stat_4 = tkinter.Label(analysis, text = f"The minimum execution time is: {MIN_DURATION}. ")
    stat_5 = tkinter.Label(analysis, text = f"The median execution time is: {MEDIAN_DURATION}. ")
    stat_6 = tkinter.Label(analysis, text = f"The standard deviation of all execution times is: {STDDEV_DURATION}. ")
    title_1 = tkinter.Label(analysis, text = "Distribution of method execution durations", font = ("Helvetica", 15, "underline"))

    stat_1.place(relx = 0.5, rely = 0.05, anchor = "center")
    stat_2.place(relx = 0.5, rely = 0.08, anchor = "center")
    stat_3.place(relx = 0.5, rely = 0.13, anchor = "center")
    stat_4.place(relx = 0.5, rely = 0.15, anchor = "center")
    stat_5.place(relx = 0.5, rely = 0.2, anchor = "center")
    stat_6.place(relx = 0.5, rely = 0.23, anchor = "center")
    title_1.place(relx = 0.5, rely = 0.31, anchor = "center")

    def get_csv(name, freq, minimum, maximum, avg, med, stdev):
        data = [
            ["Name of Method", "Frequency", "Minimum Execution Time", "Maximum Execution Time", "Average Execution Time", "Median Execution Time", "Standard Deviation of Execution Times"], 
            [name, freq, minimum, maximum, avg, med, stdev]
        ]
        with open("methods_data.csv", "w", newline = "") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    csv_button = tkinter.Button(analysis, text = "Get CSV file with data", command = lambda: get_csv(METHOD_NAME, FREQUENCY, MIN_DURATION, MAX_DURATION, AVG_DURATION, MEDIAN_DURATION, STDDEV_DURATION))
    csv_button.place(relx = 0.16, rely = 0.15, anchor = "center")

    durations_label = tkinter.Label(analysis, text = "List of Execution Times: Check for outliers", font = ("Helvetica", 9, "underline"))
    durations_label.place(relx = 0.8, rely = 0.08, anchor = "center")

    durations_list = tkinter.Listbox(analysis)
    durations_list.place(relx = 0.86, rely = 0.2, anchor = "center")

    scrollbar = tkinter.Scrollbar(analysis, orient = "vertical", command = durations_list.yview)
    scrollbar.place(relx = 0.92, rely = 0.2, anchor = "center")

    durations_list.config(yscrollcommand = scrollbar.set)

    # for i in range(len(DURATIONS)):
    #    durations_list.insert(i + 1, DURATIONS[i])

    for i in range(100):
        durations_list.insert(i, i)

    return [FREQUENCY, MIN_DURATION, MAX_DURATION, RANGE_DURATION, AVG_DURATION, MEDIAN_DURATION, STDDEV_DURATION, DURATIONS]


window.mainloop()