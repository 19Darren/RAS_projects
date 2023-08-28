# RAS_projects
Two projects (Tello Project and Open Project)

# For Tello Project:
### Simulated Implementation of Tello Drone Automatically Passing Through Gates
Our drone successfully navigated through single or dual gates positioned at various initial locations and angles (90 degrees and 60 degrees). 
This was achieved by detecting the gates in captured images, drawing the smallest rectangular outline and identifying the center of the gate, and subsequently calculating the outline's area to determine the flight direction.
https://github.com/19Darren/RAS_projects/blob/main/Tello_project/Gatepass_1.mp4
https://github.com/19Darren/RAS_projects/blob/main/Tello_project/Gatepass_2.mp4

# For Open Project:
### Implementation of Autonomous Driving Along a Track for the Turtlebot Waffle and Real-time Communication with Tello Drone
In simulation experiments, we designed the turtlebot waffle to automatically drive along the drawn trajectory, and make the turtlebot waffle subscribe to the camera of the DJI Tello drone to broadcast the car in real-time.

Our Tello drone model and turtlebot waffle model need to be installed in ros1 and ros2 systems respectively, so let the two models run in different systems and communicate with each other by subscribing to topics.
https://github.com/19Darren/RAS_projects/blob/main/Open_project/project.mp4
