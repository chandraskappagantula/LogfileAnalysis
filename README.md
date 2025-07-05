# LogfileAnalysis
GUI Program to analyze long log files, saving valuable coding time. Users can input information about the structure of their log files, and the program will output information in `.csv` format regarding the execution time of methods, etc. 

Output includes mean runtime, median runtime, any outliers for method execution, and a distribution showing runtimes for visual analysis. Data can also be optionally exported to a `.csv` with the click of a button. 

For an example of the visual output shown in a GUI, look at `example_output.png`. 
---
# Motivations

This project was created for engineers at BrighTex Bio Photonics to more easily analyze the log files their system returns. These files can be thousands of lines long, and the key information wanted is often on very specific lines, easy to miss by the human eye. Additionally, when a multi-threaded server returns a log file, two instances of the same method being executed clash in the same file, further complicating any troubleshooting process. 

This program does all of the work, depending on the type of log files inputted, and the structure of said log files through GUI input. This program works with files that report the start of method execution, and the end, and returns statistics regarding the execution times of a specific method, and reports outliers. Thus, it is easy to troubleshoot and look for a lagging point in a particular system, and it is easy to summarize a particular session of running the servers without the tedious work. 

# Usage

