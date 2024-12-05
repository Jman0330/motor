let leftMotor = 0
let rightMotor = 0

// Initialize motors
basic.forever(function () {
    // Map pin outputs to motors
    pins.digitalWritePin(DigitalPin.P0, leftMotor)
    pins.digitalWritePin(DigitalPin.P1, rightMotor)
})

// Button A moves the car forward
input.onButtonPressed(Button.A, function () {
    leftMotor = 1
    rightMotor = 1
    basic.showArrow(ArrowNames.North)
})

// Button B moves the car backward
input.onButtonPressed(Button.B, function () {
    leftMotor = 0
    rightMotor = 0
    basic.showArrow(ArrowNames.South)
})

// Press A+B to stop the car
input.onButtonPressed(Button.AB, function () {
    leftMotor = 0
    rightMotor = 0
    basic.clearScreen()
})

// Tilt left to turn left
input.onGesture(Gesture.TiltLeft, function () {
    leftMotor = 0
    rightMotor = 1
    basic.showArrow(ArrowNames.West)
})

// Tilt right to turn right
input.onGesture(Gesture.TiltRight, function () {
    leftMotor = 1
    rightMotor = 0
    basic.showArrow(ArrowNames.East)
})

