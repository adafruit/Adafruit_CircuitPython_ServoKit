"""Example that iterates through a servo on every channel, sets each to 180 and then back to 0."""
import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=8)

# Change range to the number of servos connected.
# They must be on channels within the specified range!
for i in range(8):
    kit.servo[i].angle = 180
    time.sleep(1)
    kit.servo[i].angle = 0
    time.sleep(1)
