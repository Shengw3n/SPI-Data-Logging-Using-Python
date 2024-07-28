import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import sys, time, math
import serial

xsize = 100

# Configure the serial port
ser = serial.Serial(
    port='/dev/cu.usbserial-D30A7ZO1',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.EIGHTBITS
)
ser.isOpen()

def data_gen():
    t = data_gen.t
    while True:
        t += 1
        val = int(ser.readline())
        yield t, val

def run(data):
    # update the data
    t, y = data
    if t > -1:
        xdata.append(t)
        ydata.append(y)
        if t > xsize:  # Scroll to the left.
            ax.set_xlim(t - xsize, t)

        # Change line color based on the temperature
        if y > 20:
            line.set_color('red')
            update_text(t, y, "Hot")
        elif y < 10:
            line.set_color('blue')
            update_text(t, y, "Cold")
        else:
            line.set_color('green')
            update_text(t, y, "Normal")
            
        line.set_data(xdata, ydata)
        update_avg_temp()  # Update the average temperature display

    return line,


def update_text(t, y, status):
    # Remove the previous text
    for txt in ax.texts:
        txt.set_visible(False)
    # Add new text
    ax.text(t, y, f"{status}", fontsize=12, color='black')

def on_close_figure(event):
    sys.exit(0)

def change_background(event):
    current_color = ax.get_facecolor()
    if current_color == (1.0, 1.0, 1.0, 1.0):  # matplotlib's default white background
        new_color = 'lightgreen'  # Change to green
    else:
        new_color = 'white'  # Change back to white
    ax.set_facecolor(new_color)
    fig.canvas.draw_idle()
def update_avg_temp():
    avg_temp = sum(ydata) / len(ydata) if ydata else 0
    # Check if the average temperature text box already exists
    if hasattr(update_avg_temp, 'text_box'):
        # Update the text box with the new average temperature
        update_avg_temp.text_box.set_text(f"Average Temperature: {avg_temp:.2f}°C")
    else:
        # Create the text box and save it as an attribute of the function
        update_avg_temp.text_box = ax.text(0.02, 0.95, f"Average Temperature: {avg_temp:.2f}°C", transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='none'))

# Make sure to call update_avg_temp() within your run(data) function to update the average temperature display with each new data point.


data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=2)
ax.set_ylim(-10, 100)
ax.set_xlim(0, xsize)
ax.grid()
xdata, ydata = [], []

# Button for changing background color
axcolor = 'lightgoldenrodyellow'
axbutton = plt.axes([0.1, 0.01, 0.1, 0.075])
button = Button(axbutton, 'Change Background', color=axcolor, hovercolor='0.975')

# Connect the button to its callback
button.on_clicked(change_background)

# Text box for displaying average temperature
avg_temp_display = ax.text(0.5, 0.95, '', transform=ax.transAxes, ha='center')

# Animation
ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100, repeat=False)

plt.show()
