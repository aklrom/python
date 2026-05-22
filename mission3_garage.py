from pysimverse import Drone
import time 

drone=Drone()
drone.connect()
drone.take_off(10)

drone.set_speed(100)
drone.move_left(225)
drone.move_forward(350)
time.sleep(1)
drone.move_right(480)
drone.move_backward(175)




drone.land()
time.sleep(1)