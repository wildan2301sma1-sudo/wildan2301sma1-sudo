import turtle

t = turtle.Turtle()
t.speed(0)

# Persegi panjang
def persegi_panjang(p, l):
    for i in range(2):
        t.forward(p)
        t.right(90)
        t.forward(l)
        t.right(90)

# Segitiga
def segitiga(s):
    for i in range(3):
        t.forward(s)
        t.left(120)

# Trapesium
def trapesium(a, b, tgl):
    t.forward(a)
    t.left(120)
    t.forward(tgl)
    t.left(60)
    t.forward(b)
    t.left(60)
    t.forward(tgl)

# Jajar genjang
def jajar_genjang(p, l):
    t.forward(p)
    t.left(60)
    t.forward(l)
    t.left(120)
    t.forward(p)
    t.left(60)
    t.forward(l)

# Belah ketupat
def belah_ketupat(s):
    for i in range(2):
        t.forward(s)
        t.left(60)
        t.forward(s)
        t.left(120)


# Gambar berjejer
t.penup(); t.goto(-300,100); t.pendown(); persegi_panjang(120,70)
t.penup(); t.goto(-120,100); t.pendown(); segitiga(100)
t.penup(); t.goto(60,100); t.pendown(); trapesium(120,80,70)
t.penup(); t.goto(-200,-80); t.pendown(); jajar_genjang(120,70)
t.penup(); t.goto(40,-80); t.pendown(); belah_ketupat(70)
