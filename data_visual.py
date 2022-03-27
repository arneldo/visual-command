import json #To read/manipulate the json
import plotext as plt

f = open('sam-user-activity.eu-west-1.elasticbeanstalk.com.json') #<--- To work with a new json file change this string
data = json.load(f)


def visual_plotter(x,y):
    """Used to handle the plotting of the graphs on the command line."""
    plt.plot(x, y,marker='smile')
    plt.clc() #To make the graph colourless.
    plt.plot_size(100,20)
    plt.title("CLI API")
    plt.xlabel("nth day of January 2022")
    plt.ylabel("Userbase count")
    plt.show()
    plt.clear_plot() #Clear the settings for the figure that was built last. If this was not present the same graph would be plotted even with different inputs.


def sieve(start,end):
    hor_axis = [] # x values (Relevant days in January)
    ver_axis = [] #y values (Userbase on those days in January)

    if start.isdigit() and end.isdigit() and 0 < int(start) < int(end) < len(data) + 1: #Check if inputs are digits and the start date is smaller than the end date.
            for key,value in data.items():
                if int(start)-1 < int(key[0:2]) < int(end)+1:# storing all dates that are within our desired range.
                    hor_axis.append(int(key[:2]))
                    ver_axis.append(int(value))
            visual_plotter(hor_axis,ver_axis) #Call to method that does the plotting
            # print("----------------------------")
            print("\n")

    elif (start.isdigit() and end.isdigit() and len(data)+ 1 > int(start) > int(end) > 0): #If end date is smaller than the start date the two dates are swopped.
        for key,value in data.items():
            if int(end)-1 < int(key[0:2]) < int(start)+1:
                hor_axis.append(int(key[:2]))
                ver_axis.append(int(value))
        visual_plotter(hor_axis,ver_axis)
        # print("----------------------------")
        print("\n")

    elif (start.isdigit() and end.isdigit()):
        print("That value is outside the available range. Pick numbers between 1 and ",len(data),".") #Message pops up if inputs are outside of range.
    
    else:
        print("Please only enter integers as inputs.")


# print(len(data))
if __name__ == "__main__":
    print("Hey, Let's have a look at how our userbase has been growing")
    print("The dates range from the 1st of Jan to the ",len(data)," of Jan at the moment.")
    print("To exit enter a negative start/end date or non digit value as input.")
    print("\n")
    start = input("Enter start date: ")
    end = input("Enter end date: ")
    while(start.isdigit() and end.isdigit()):
        sieve(start,end)
        start = input("Enter start date: ")
        end = input("Enter end date: ")
    print("Thank you for taking an interest in our business. Goodbye!")


