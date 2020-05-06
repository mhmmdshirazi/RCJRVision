# RCJRVision (Robocup Junior Rescue Vision)
# Table of Contents
1. [Overview](#Overview)
2. [Instalation](#Installation)
3. [Usage](#Usage)
4. [Dependencies](#Dependencies)


## Overview
RCJRVision is a fast and simple method for **Robocup** Junior rescue maze and Robocup Junior Rescue simulation leagues
to Detect H, S, and U Letters in an image.
This package converts raw image to a solid black and white image, finds contours in the picture, chooses the most proper
contour, and finally check it with pre defined letter contours to find the best match.


## Instalation

## Usage
#### Use with predefined contours
1. Import **RCJRVision**

2. Make an object from HSUVision Class

`my_vision = RCJRVision.HSUVision()`

3. Convert your image to an opencv image

4. Use find_HSU method

`letter, center = my_test_vision.find_HSU(img)`

This method returns two variables:

- letter:

    >Key of the predefined contour dictionary.
    In this case: 'H' or 'S' or 'U'
- center: 

    >A 2 element list that represent the center of discover contour
## Dependencies
Click on the link below to see dependencies and their status:

[![Requirements Status](https://requires.io/github/mhmmdshirazi/RCJRVision/requirements.svg?branch=master)](https://requires.io/github/mhmmdshirazi/RCJRVision/requirements/?branch=master)