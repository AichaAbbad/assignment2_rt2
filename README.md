# Assignment2 | Research Track 02
---------------------------

Student: Aicha Manar ABBAD
Student ID: s5565902

---------------------------

The main goal of this assignment is to create a [Jupyter Notebook](https://github.com/AichaAbbad/assignment2_rt2/blob/fe2a387a12dd0a3801b56e4dda4704cdfcec83ba/src/assignment_2_2022/src/assignment_2_2022/Notebook/node_a.ipynb) that servers as a user interface for the control
a two wheeled mobile robot in a ROS environment starting from (node 'A') implemented in [assignment 02 of research track 01](https://github.com/AichaAbbad/assignment_2_2022.git).
It also shows the graphical feedback of the state of the robot and its behaviour using widgets.

---------------------------

# Node A
As described earlier, "Node A" implements an action client that allows the user to set or cancel the target goal. Moreover, it publishes and velocity as a costum message based the values published in "/odom" topic.

---------------------------

# Notebook Description
The notebook consists of 4 main parts:
1. Packages
2. Classes
3. Required functions
4. Controlling robot motion using buttons

---------------------------

# 1. Packages
In this part we import the necessary packages needed for our code.
```Python
import rospy
import actionlib
import geometry_msgs.msg
import nav_msgs.msg
import time
import assignment_2_2022.msg

import matplotlib.pyplot as plt
import jupyros as jr
import ipywidgets as widgets
import numpy as np

from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from assignment_2_2022.msg import position, PlanningActionGoal, PlanningActionResult
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
from matplotlib.patches import Arrow, Circle
from jupyros import ros3d
from ipywidgets import Button, Layout, ButtonStyle, GridBox, VBox, HBox, widgets
from IPython.display import display
from std_srvs.srv import Empty,EmptyResponse

from buttons import *
```
---------------------------

# 2. Classes
* Visualiser() : This class is responsible for handling the visualization of a robot's position, orientation, and sensor data.
* Goals() : This class is responsible for tracking and visualizing the progress of goals being reached or cancelled.
* Distance() : computes the distance between the current position and a desired position, and stores the computed distance in an instance variable.

---------------------------

# 3. Required Functions
* start_simulation" : This function is called when the "start" button is clicked.
* "stop_simulation" : This function is called when the "stop" button is clicked.
* "move_forward" : This function is called when the "up" button is clicked. 
* "move_backward" : This function is called when the "down" button is clicked.
* "turn_left" : This function is called when the "left" button is clicked.
* "turn_right" : This function is called when the "right" button is clicked.
* "stop_movement" : This function is called when the "stops" button is clicked. 
* "button_event" : This function sets up the event handling for the buttons. It assigns the appropriate functions to the on_click events of each button.
* The main() function is then defined, which serves as the entry point for the program. It initializes a ROS node, sets up ROS subscribers and publishers, creates and animates plots using matplotlib, and defines callback functions for handling received data.

---------------------------

# 4. Controlling robot motion using buttons

In this part we try to control the motion of the robot (Up, Down, Left, Right, Stop) using widget buttons.

1. Robot "start" or "stop" simulation:
```Python
HBox([start,stop])
```

2. Robot moves "up" or "down":
```Python
HBox([up,down])
```

3. Robot moves "left" or "right":
```Python
HBox([left,right])
```

3. Robot "stop":
```Python
display(stops)
```
