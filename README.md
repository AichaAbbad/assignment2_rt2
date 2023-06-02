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
```
