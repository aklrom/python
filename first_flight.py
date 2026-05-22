from pysimverse import Drone
import time 

drone=Drone()
drone.connect()
drone.take_off()

# go up and down
drone.move_forward(200)
time.sleep(1)
drone.rotate(90)
drone.set_speed(100)
drone.move_forward(200)
time.sleep(1)







drone.land()
time.sleep(1)

