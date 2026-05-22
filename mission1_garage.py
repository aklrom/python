from pysimverse import Drone
import time 

drone=Drone()
drone.connect()
drone.take_off()


drone.set_speed(100)
drone.move_forward(250)
time.sleep(1)
drone.move_right(190)
time.sleep(1)

drone.land()
time.sleep(1)
