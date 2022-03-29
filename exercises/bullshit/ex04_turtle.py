"""Turtle drawing -- modern art!"""

__author__ = '730449902'

from turtle import Turtle, colormode, done
from random import randrange


def main() -> None:
    """Main function."""
    leo: Turtle = Turtle()
    colormode(255)
    draw_cube(leo, 60, 100, 100)
    draw_square(leo, 60, randrange(0, 100), randrange(0, 100))
    draw_square(leo, 60, -100, 100)
    draw_triangle(leo, 60, -50, 20)
    draw_filled_hexagon(leo, 10, -40, -40)
    done()


def turtle_setup(a_turtle: Turtle, x_pos: float, y_pos: float) -> None:
    """Sets up turtle to go to position without drawing line."""
    a_turtle.penup()
    a_turtle.goto(x_pos, y_pos)
    a_turtle.pendown()


def draw_cube(a_turtle: Turtle, side_len: int, x_pos: float, y_pos: float) -> None:
    """Drawing a cube (wow)."""
    turtle_setup(a_turtle, x_pos, y_pos)
    draw_square(a_turtle, side_len, x_pos, y_pos)
    draw_square(a_turtle, side_len, x_pos + 25, y_pos + 25)
    # sorry for the spam below but you can't really loop a cube
    a_turtle.goto(x_pos, y_pos)
    a_turtle.goto(x_pos + side_len, y_pos)
    a_turtle.goto(x_pos + side_len + 25, y_pos + 25)
    a_turtle.goto(x_pos + side_len + 25, y_pos + side_len + 25)
    a_turtle.goto(x_pos + side_len, y_pos + side_len)
    a_turtle.goto(x_pos, y_pos + side_len)
    a_turtle.goto(x_pos + 25, y_pos + side_len + 25)


def draw_filled_hexagon(a_turtle: Turtle, side_len: int, x_pos: float, y_pos: float) -> None:
    """A hexagon but filled in."""
    turtle_setup(a_turtle, x_pos, y_pos)
    a_turtle.color(20, 30, 240)
    i: int = 0
    a_turtle.begin_fill()
    while (i < 6):
        a_turtle.forward(side_len)
        a_turtle.left(60)
        i += 1
    a_turtle.end_fill()


def draw_triangle(a_turtle: Turtle, side_len: int, x_pos: float, y_pos: float) -> None:
    """Ever seen a triangle before?"""
    turtle_setup(a_turtle, x_pos, y_pos)
    a_turtle.color(99, 204, 250)
    i: int = 0
    while (i < 3):
        a_turtle.forward(side_len)
        a_turtle.left(120)
        i += 1


def draw_square(a_turtle: Turtle, side_len: int, x_pos: float, y_pos: float) -> None:
    """It's a square."""
    turtle_setup(a_turtle, x_pos, y_pos)
    i: int = 0
    while (i < 4):
        a_turtle.forward(side_len)
        a_turtle.left(90)
        i += 1


if __name__ == '__main__':
    main()