// Function to Read Line Sensors to Detect Edge of Dohyo
function read_line (list2: number[]) {
    s = 0
    for (let value of list2) {
        s = s + value
    }
    return s
}
input.buttonD12.onEvent(ButtonEvent.Click, function () {
    music.playMelody("B A G A G F A C5 ", 250)
    // Main Body
    while (true) {
        // Read Line Following Sensors to Detect Edge of Dohyo
        border_sensor = read_line(zumo.readLine())
        // Is Robot inside Dohyo?
        if (border_sensor > 500) {
            zumo.clear()
            zumo.writeStringNewLine("\"TURN AROUND\"")
            zumo.runMotor(ZumoMotor.All, -99)
            pause(0)
            zumo.TurnDirection(ZumoMotor.right, 99)
            pause(0)
        } else {
            ultrasound_sensor = zumo.HCSR04(pins.D0, pins.D1)
            if (ultrasound_sensor <= 0) {
                zumo.clear()
                zumo.writeStringNewLine("\"ATTACK\"")
                zumo.stopMotor(ZumoMotor.All)
                zumo.runMotor(ZumoMotor.All, 100)
                pause(0)
                zumo.stopMotor(ZumoMotor.All)
            } else {
                zumo.clear()
                zumo.writeStringNewLine("\"FORWARD\"")
                zumo.runMotor(ZumoMotor.All, 99)
                pause(0)
            }
        }
    }
})
let ultrasound_sensor = 0
let border_sensor = 0
let s = 0
zumo.createI2C(pins.SCL, pins.SDA)
zumo.init(128, 64)
zumo.enableIMU()
zumo.Initialization(Lightype.DIGITAL)
zumo.writeStringNewLine("ready 1.10")
music.baDing.play()
