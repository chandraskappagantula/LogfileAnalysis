# LogfileAnalysis
GUI Program to analyze long log files, saving valuable coding time. Users can input information about the structure of their log files, and the program will output information in `.csv` format regarding the execution time of methods, etc. 

Output includes mean runtime, median runtime, any outliers for method execution, and a distribution showing runtimes for visual analysis. Data can also be optionally exported to a `.csv` with the click of a button. 

For an example of the visual output shown in a GUI, look at `example_output.png`. 

---

# Motivations

This project was created for engineers at BrighTex Bio Photonics to more easily analyze the log files their system returns. These files can be thousands of lines long, and the key information wanted is often on very specific lines, easy to miss by the human eye. Additionally, when a multi-threaded server returns a log file, two instances of the same method being executed clash in the same file, further complicating any troubleshooting process. 

This program does all of the work, depending on the type of log files inputted, and the structure of said log files through GUI input. This program works with files that report the start of method execution, and the end, and returns statistics regarding the execution times of a specific method, and reports outliers. Thus, it is easy to troubleshoot and look for a lagging point in a particular system, and it is easy to summarize a particular session of running the servers without the tedious work. 

# Usage

`main.py` works in the cases where log files are written more cleanly, with spaces. It splices each line among spaces, although in the future this will be expanded with other characters. The program takes input for a "starting signature", or some symbol to indicate a method has begun execution. It similarly also takes an "ending" signature. You then enter a method for which you want statistics on runtime, and in the next window, a distribution is shown, along with a list of runtimes, and an option to export this data to a `.csv` file that is automatically created. The distribution is also exported as a standalone image in the same directory. 

`method_statistics.py` is a module created for this project, which takes an array of start timestamps and end timestamps of a particular method's execution, and returns the average, median, and standard deviation of the runtimes, and returns a distribution of runtimes for visual analysis. 

# Roadmap/Future Work

- Expand `main.py` to reduce the core assumptions made about log file structure, and allow the user to more easily specify the structure of the lines in the log files.
- ~~Create a standalone module for generating statistics.~~
- Create a system for retrieving line #'s in between method executions (starting and ending), and report that data according to the user's choosing.
- Improve the `.csv` file writing to work across multiple methods. 
