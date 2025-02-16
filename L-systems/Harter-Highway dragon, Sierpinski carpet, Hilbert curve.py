from turtle import *


class LSystem2D:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.t = t
        self.rules = {}
        self.t.pensize(self.width)

    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

    def draw_turtle(self, start_pos, start_angle):

        tracer(1, 0)
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()

        for move in self.state:
            if move == 'F':
                self.t.forward(self.length)
            elif move == 'S':
                self.t.up()
                self.t.forward(self.length)
                self.t.down()
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)

        done()


width = 500
height = 500
screen = Screen()
screensize(10000, 10000)
screen.setup(width, height, 0, 0)

t = Turtle()
t.ht()

t.screen.bgcolor("#000006")
t.color('#4f1c38')
# t.color('#b92c2d')
pen_width = 2
f_len = 5
angle = 90
axiom = 'FX'

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
l_sys.add_rules(('FX', 'FX+FY+'), ('FY', '-FX-FY'))
l_sys.generate_path(12)
print(l_sys.state)
l_sys.draw_turtle((0, 0), 0)