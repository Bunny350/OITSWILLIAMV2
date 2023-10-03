import time
from digitalio import DigitalInOut, Direction, Pull
import board
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

print ("waking")

# USB device
consumer = ConsumerControl(usb_hid.devices)

pinns = (
    board.GP9,
    board.GP8,
    board.GP7
    )

keys = {
    (0): (ConsumerControlCode.VOLUME_INCREMENT),
    (1): (ConsumerControlCode.VOLUME_DECREMENT),
    (2): (ConsumerControlCode.MUTE)
    }
altkeys = {
    (0): (ConsumerControlCode.BRIGHTNESS_INCREMENT),
    (1): (ConsumerControlCode.BRIGHTNESS_DECREMENT),
    (2): ()
    }

button = []
for i in range(len(pinns)):
    buttona = DigitalInOut(pinns[i])
    buttona.direction = Direction.INPUT
    buttona.pull = Pull.UP
    button.append(buttona)
    
keies = [0, 0, 0]

ispressingmute = 0
ispressingbright = 0
brightnessmode = 0
disengaging = 0

# loop
while True:
    for buttonb in range(2):
        if ispressingmute == 0 and disengaging == 0:
            if keies[buttonb] == 0:
                if not button[buttonb].value:
                    try:
                        consumer.press(keys[buttonb])
                    except ValueError:  # deals w six key limit
                        pass
                    keies[buttonb] = 1
                
            if keies[buttonb] == 1:
                if button[buttonb].value:
                    if brightnessmode == 0 and disengaging == 0:
                        try:
                            consumer.send(keys[buttonb])
                        except ValueError:
                            pass
                        keies[buttonb] = 0
                    elif disengaging == 1:
                        disengaging = 0
                    # end of volume mode
        elif ispressingmute == 0 and disengaging == 1 and ispressingbright == 0:
            print("ERR", brightnessmode, ispressingmute, disengaging, ispressingbright)
            disengaging = 0
        if ispressingmute == 1:
            if keies[buttonb] == 0:
                if not button[buttonb].value:
                    brightnessmode = 1
                    ispressingbright = 1
                    print ("brightnessmode engaged!1")
                    if brightnessmode == 1:
                        try:
                            consumer.press(altkeys[buttonb])
                        except ValueError:  # deals w six key limit
                            pass
                        keies[buttonb] = 1
                
            if keies[buttonb] == 1:
                if button[buttonb].value:
                    ispressingbright = 0
                    try:
                        consumer.send(altkeys[buttonb])
                    except ValueError:
                        pass
                    keies[buttonb] = 0
        elif disengaging == 1:
            if keies[buttonb] == 1:
                if button[buttonb].value:
                    print ("prepare to disengage in the second way")
                    try:
                        consumer.send(altkeys[buttonb])
                    except ValueError:
                        pass
                    keies[buttonb] = 0
                    disengaging = 0
                # end line of brightness mode
    for buttonC in range(1):
            if keies[buttonC + 2] == 0:
                if not button[buttonC + 2].value:
                    ispressingmute = 1
                    try:
                        if keies[buttonC + 2] == 0 and ispressingmute == 1:
                            print ("mute pressed")
                    except ValueError:  # deals w six key limit
                        pass
                    keies[buttonC + 2] = 1
                
            if keies[buttonC + 2] == 1:
                if button[buttonC + 2].value:
                    try:
                        if brightnessmode == 0:
                            consumer.send(keys[buttonC + 2])
                            print("mute switch mode")
                        else:
                            brightnessmode = 0
                            disengaging = 1
                            print ("disengaging", disengaging)
                            print ("brightnessmode disengaged")
                    except ValueError:
                        pass
                    ispressingmute = 0
                    keies[buttonC + 2] = 0
    time.sleep(0.01)
