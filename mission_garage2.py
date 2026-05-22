from pysimverse import Drone
import time 

drone=Drone()
drone.connect()
drone.take_off()

drone.set_speed(100)
drone.move_forward(80)
drone.move_left(200)
time.sleep(1)
drone.move_forward(100)
drone.move_right(200)
time.sleep(1)
drone.move_forward(95)
drone.move_right(220)


drone.land()
time.sleep(1)