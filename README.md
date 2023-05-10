# Husky_motion_plan
Husky Motion Planning : Contains instructions to run the planning and control code

To run the code, you need all the required dependencies for Husky -ROS. These have been compiled in the form of a docker container.
One the PC connected on the Husky ROS Network, install Docker and run :

```
docker pull asalvi179/husky_base_demo:motion_planning_v2
```
Once the container is pulled, run an instance using standard Docker running tools. 

### Important files
1. pub_vel.py : This files publishes a manuver like fishook which has been fit to the gps coordinates realized by the A* planner
2. gps_viz.py : This file visualizes live GPS readings as the Husky is executing the manuever

