import mled, animations

class Example:

    boards = {
        'd1_mini': (13, 14),
        'mh_et_live_minikit': (23, 18)
    }

    def main(self, model):
        self.matrix = mled.driver(self.boards[model][0], self.boards[model][1])
        self.test()
        self.animate()

    def test(self):
        self.matrix.clear()
        self.matrix.setIntensity(7)
        for y in range(0, 8):
            for x in range(0, 8):
                self.matrix.pixel(x, y, self.matrix.ON)
                self.matrix.display()

        for y in range(0, 8):
            for x in range(0, 8):
                self.matrix.pixel(x, y, self.matrix.OFF)
                self.matrix.display()

    def animate(self):
        ani = mled.animation(self.matrix)
        ani.loop(0, 33, animations.ani_heart_pulse + animations.ani_pacman_pulse + animations.ani_ghost_pulse)


app = Example()
app.main('d1_mini')
