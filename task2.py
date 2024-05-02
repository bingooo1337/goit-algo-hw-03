import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)


def main():
    size = 300
    order = 2

    try:
        order = int(input("Input recursion level: "))
    except:
        print("Can not parse value - using default level = 2")

    wn = turtle.Screen()
    wn.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")

    # move to start position
    t.penup()
    t.goto(-size / 2, size / 4)
    t.pendown()

    # draw triangle
    for i in range(3):
        koch_snowflake(t, order, size)
        # rotate
        t.right(120)

    wn.mainloop()


if __name__ == "__main__":
    main()
