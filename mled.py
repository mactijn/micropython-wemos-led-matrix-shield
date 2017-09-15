from machine import Signal, Pin

class driver:

    OFF = 0
    ON  = 1

    framebuffer = 0x00
    intensity = 0
    invert = 0

    def __init__(self, dataPin, clockPin):
        self.dataPin  = Signal(dataPin,  Pin.OUT, invert=False)
        self.clockPin = Signal(clockPin, Pin.OUT, invert=False)

        self.dataPin.on()
        self.clockPin.on()

    def setIntensity(self, intensity):
        self.intensity = 7 if intensity > 7 else intensity

    def display(self):
        self.sendData(0, self.framebuffer, 64)

        self.dataPin.off()
        self.clockPin.off()
        self.clockPin.on()
        self.dataPin.on()

        self.sendCommand(0x88|self.intensity)

    def clear(self):
        self.fill(0x00)

    def fill(self, val):
        self.framebuffer = 0x00
        for lineno in range(0, 8):
            self.framebuffer = self.framebuffer | ((val & 0xff) << (lineno * 8))

    def sendCommand(self, cmd):
        self.dataPin.off()
        self.send(cmd, 8)
        self.dataPin.on()

    def sendData(self, address, data, len):
        self.sendCommand(0x44)
        self.dataPin.off()
        self.send(0xC0 | address, 8)
        self.send(data, len)
        self.dataPin.on()

    def send(self, data, bits):
        for pixel in range(0, bits):
            self.clockPin.off()
            if data >> pixel & 1:
                self.dataPin.on()
            else:
                self.dataPin.off()

            self.clockPin.on()

    def pixel(self, x, y, val):
        if val:
            self.framebuffer = self.framebuffer | (1 << ((y * 8) + x))
        else:
            self.framebuffer = self.framebuffer ^ (1 << ((y * 8) + x))


    def frame(self, frame):
        self.framebuffer = frame


class animation:
    import utime

    def __init__(self, matrix):
        self.matrix = matrix

    def animate(self, sleep_ms, animation):
        for intensity, frame in animation:
            self.matrix.setIntensity(intensity)
            if frame != None:
                self.matrix.frame(frame)

            self.matrix.display()
            self.utime.sleep_ms(sleep_ms)

    def loop(self, times, sleep_ms, animation):
        if times > 0:
            for i in range(0, times):
                self.animate(sleep_ms, animation)
        else:
            while True:
                self.animate(sleep_ms, animation)
