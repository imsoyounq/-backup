from gpiozero import MotionSensor
pir = MotionSensor(15)
while True:
    if pir.motion_detected:
        print "You moved!"
