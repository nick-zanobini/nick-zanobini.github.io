---
layout: single
title:  NASA Sample Return Challenge
excerpt: "Details on autonomously mapping a simulated environment and searching for and collecting samples of interest"
date:   2017-08-10 05:00
comments:   true
tags: 
  - python
  - unity
  - OpenCV
  - control
  - Programming
  - Robotics
header:
  teaser: /assets/images/rover_project_best_run_th.jpg
  image: /assets/images/rover_project_best_run.jpg
---

{% include toc title="Project Steps" icon="file-text" %}
<!-- sidebar:
  - title: "Role"
    image: /assets/images/
    image_alt: "logo"
    text: "Designer, Front-End Developer"
  - title: "Responsibilities"
    text: "Reuters try PR stupid commenters should isn't a business model" -->

## Goal
For the Udacity Robotics Nanodegree our first project was to develop the perception and control algorithms for a rover in a simulated world similar to the NASA Sample Return Challenge. We were provided an unknown environment in Unity simulation and asked to generate a map of the navigable terrain and identify samples of interest (gold rocks) from 30 FPS video stream.

Here were the requirements:

* The rover must map at least 40% of the environment with 60% fidelity (accuracy) against the ground truth. You must also find (map) the location of at least one rock sample.

I decided that if I could find and collect all 6 rock samples I would have to be over the 40% mapped, so I set off to collect all 6 rock samples. Here is my best run:

<figure>
	<a href="/assets/images/rover_project_best_run.jpg"><img src="/assets/images/rover_project_best_run.jpg"></a>
	<figcaption>The results of my best run</figcaption>
</figure>


## Solution
The first thing I did was convert the color space to HSV in order to segment out the 3 specific regions I was looking for: The samples of interest (gold rocks), the navigable terrain (sand) and the obstacles (gray and brown rocks). In order to generate a top-down map view of the area I applied a perspective transform on the camera image and then thresholded the transformed image to get the various regions of interest. In order to better detect the small rock samples after thresholding the transformed image to find the gold rock samples I dilated each image enlarging any detected gold rocks. 

<figure class="half">
    <a href="/assets/images/rover_project_example_rock1.jpg"><img src="/assets/images/rover_project_example_rock1.jpg"></a>
    <a href="/assets/images/rover_project_warped.jpg"><img src="/assets/images/rover_project_warped.jpg"></a>
    <figcaption>The segmented rock image and the three segmented images combined</figcaption>
</figure>

<figure class="half">
    <a href="/assets/images/rover_project_rock_threshed.jpg"><img src="/assets/images/rover_project_rock_threshed.jpg"></a>
    <a href="/assets/images/rover_project_color_img.jpg"><img src="/assets/images/rover_project_color_img.jpg"></a>
    <figcaption>The segmented rock image and the three segmented images combined</figcaption>
</figure>

From the navigable terrain image the pixel coordinates are converted to rover-centric coordinates. The rover-centric coordinates are used to calculate the angle and distance of each pixel from the rover to deterine which way to navigate. The rover-centric coordinates are also converted to world coordinates to update the world map.

<figure>
	<a href="/assets/images/rover_project_calc_path.jpg"><img src="/assets/images/rover_project_calc_path.jpg"></a>
	<figcaption>Calculating the optimal direction to move</figcaption>
</figure>

In order to filter the data from the rover the world coordinates are only used to update the world map if the pitch and roll of the rover are within 0.0 +/- 0.5 degrees. This is because when the rover isn't sitting flat the transformed image provides inaccurate data. Since the values returned to update the world map are used to determine percentage mapped and the fidelity of the mapping it is important to only update the map when the data is accurate.


### Rover States
With the data from the images I was able to develop a control algorithm. My control algorithm has 5 modes:  
   * **Forward**: Checks navigable angles to make sure they are over the minimum threshold, if they are then it
     checks the rover's speed. If the speed is less than the max velocity it accelerates otherwise it just 
     coasts. If the rover is in forward mode and its speed is stuck below 0.05 for more than a second then
      the rover changes its mode to turn. If the navigable angles is below the minimum threshold then the 
      enters stop mode.  
   * **Stop**: In this mode if the rover's speed isn't 0 then it brakes. If it is 0 then it sets its steering
    angle to -15 degrees and turns. I tried checking which way the average navigable angles were pointing but
    this caused it to get stuck in a corner turning back and forth.  
   * **Turn**: This mode is very similar to stop except it is called after the rover's speed is stuck at 0 when
    the rover is supposed to be moving.  
   * **Pickup**: This is a non-explicit mode that checks if there are any angles to the rocks. If there are the
    robot either stops or slows down as it navigates to the rock. In order to prevent over shooting the rock if 
    the robot is traveling fast it slams on the brakes and slowly moves to the rock.  
   * **Home**: This mode is untested but is meant to navigate the rover back to its starting place while avoiding
    obstacles.


## Accomplishments:
1. Rover was able to successfully navigate around the world and pick up the rocks  
    1. Converting the image to HSV let me isolate the rock easier without false positives like I was getting using the default BGR color-space.  
    1. By eroding the detected rock I was able to make it stand out more. This allowed me to wander in the middle of the path more and still make it to the rocks.  
2. Added turn mode to get the rover unstuck when it drove into a rock. Detects when it is trying to go forward but it not making any progress successful.
3. When my rover is going fast (velocity > 0.8) It slams on the brakes and then turns to the rock in order to prevent over shooting the rock

This project gave me more experience with OpenCV, Feedback Control, Python, Object Recognition, Mapping, OOP.

## Full Source Code
Full code and description available [here](https://github.com/nick-zanobini/RoboND-Rover-Project)