# visual-command

Welcome to my application. 

This implementation was made and tested on a linux machine using pyhton.

The terminal plotting was done using plotext (https://github.com/piccolomo/plotext).

To run the app locally plotext needs to be installed.

The app can be run in 2 ways. The API endpoint needs to be in the same directory as the 2 python files.

1. Run on terminal: python3 data_visual.py
	You will then be prompted to input a start date and an end date for which you would 
	like to see a plot for. 
	After each start-end pair the data will be plotted on the terminal. You will then be 	prompted to enter another start end pair.
	This will continue until an exit condition is met (e.g a negative start/end value)
	
2. Run on Terminal: python3 data_visual_test.py
	All the tests will run and all outputs will be on the terminal.
