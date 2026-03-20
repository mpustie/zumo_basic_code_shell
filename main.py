# Function to Read Line Sensors to Detect Edge of Dohyo
def read_line(list2: List[number]):
    global s
    s = 0
    for value in list2:
        s = s + value
    return s

def on_on_event():
    zumo.clear()
    zumo.write_string_new_line("forward")
    zumo.run_motor(ZumoMotor.ALL, 92)
    zumo.write_num_new_line(sm)
    pause(10)
control.on_event(12, 3, on_on_event)

def on_button_d12_click():
    global timer, sm, collision
    music.play_melody("B A G A G F A C5 ", 250)
    timer = 0
    # Main Body
    while True:
        # Read Line Following Sensors to Detect Edge of Dohyo
        sm = read_line(zumo.read_line())
        collision = zumo.read_imu(ZumoIMUMode.ACC, ZumoIMUDirection.X)
        zumo.clear()
        zumo.write_num_new_line(sm)
        # Is Robot inside Dohyo?
        if sm > 500:
            zumo.stop_motor(ZumoMotor.ALL)
            control.raise_event(22, 2)
            pause(600)
        else:
            if collision < -4 or collision > 4:
                control.raise_event(10, 2)
                pause(10)
            else:
                control.raise_event(12, 3)
                pause(10)
input.button_d12.on_event(ButtonEvent.CLICK, on_button_d12_click)

def on_on_event2():
    zumo.clear()
    zumo.write_string_new_line("push hard")
    music.jump_up.play()
    # Yes Collision Detected
    zumo.stop_motor(ZumoMotor.ALL)
    zumo.run_motor(ZumoMotor.ALL, 100)
    pause(10)
    # Edge of Dohyo Detected, Stop and Turn Around
    zumo.stop_motor(ZumoMotor.ALL)
control.on_event(10, 2, on_on_event2)

def on_on_event3():
    zumo.clear()
    zumo.write_num_new_line(sm)
    zumo.write_string_new_line("see white space")
    # Edge of Dohyo Detected, Stop and Turn Around
    zumo.stop_motor(ZumoMotor.ALL)
    zumo.run_motor(ZumoMotor.ALL, -100)
    pause(200)
    zumo.turn_direction(ZumoMotor.RIGHT, 90)
    pause(200)
    # Edge of Dohyo Detected, Stop and Turn Around
    zumo.stop_motor(ZumoMotor.ALL)
control.on_event(22, 2, on_on_event3)

timer = 0
sm = 0
s = 0
collision = 0
collision = 0
zumo.create_i2c(pins.SCL, pins.SDA)
zumo.init(128, 64)
zumo.enable_imu()
zumo.initialization(Lightype.DIGITAL)
zumo.write_string_new_line("ready")
music.ba_ding.play()