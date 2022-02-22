from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

defaultPos = 90

kit.servo[0].angle = defaultPos
kit.servo[1].angle = defaultPos
kit.servo[2].angle = defaultPos
kit.servo[3].angle = defaultPos

time.sleep(1)

# Lower the arm
kit.servo[2].angle = 30
kit.servo[3].angle = 160

# Open the Claw and Grab the object
kit.servo[1].angle = 130
time.sleep(1)
kit.servo[1].angle = 50
time.sleep(1)

# Make the arm go to the default position
kit.servo[3].angle = defaultPos
kit.servo[2].angle = defaultPos
kit.servo[1].angle = defaultPos

# Rotate the arm
kit.servo[0].angle = 180
time.sleep(1)

# Drop the object
kit.servo[1].angle = 130
time.sleep(1)

# Close the Claw
kit.servo[1].angle = defaultPos