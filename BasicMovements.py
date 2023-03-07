from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 50, 0, 0)
sleep(2)
# To avoid drone from going forward while landing
me.send_rc_control(0, 0, 0, 0)
sleep(2)
me.land()


