# Why are there two files?

During testing, I was worried my code had hung. Do check this, I added a simple status indicator that can be enabled with `-p` after the trial counts. However, doing this cleanly required the use of a couple non-booksite output functions (specifically `sys.stdout.flush()` and `sys.stdout.write()`) to rewrite over the previously-printed line. To make sure I am only submitting code for grading that uses the booksite library when required, I moved that functionality into a separate file. Thus, `dice.py` uses booksite only and `dice-with-progress.py` uses booksite + `sys.stdout` for the progress bar. The line numbers that contain the non-booksite output functions are listed in the footer of `dice-with-progress.py`.