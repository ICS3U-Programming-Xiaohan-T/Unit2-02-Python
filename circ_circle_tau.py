#!/usr/bin/env python3
# Created by: Xiaohan
# Created on Feb 27, 2025
# This module calculates the circumference of a circle by using tau.
# Import the constant from constants.py
import constants


def main():
    # get the radius from the user's input
    radius = float(input("Enter the radius of the circle (mm): "))
    # calculate the circumference by the equation
    circumference = constants.TAU * radius
    # print out the result of the circumference
    print("")
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
