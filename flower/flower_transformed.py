from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import math

pi = 3.14159265
SIN_60 = 0.86602540378
spd_ang = float(pi/4)

petals_list = [(50, SIN_60 * 100),
               (-50, SIN_60 * 100),
               (100, 0),
               (50, -SIN_60 * 100),
               (-100, 0),
               (-50, -SIN_60 * 100)]

trunk_list = [(-5, 0),
              (5, 0),
              (-5, -200),
              (5, -200)]


# Function that changes speed of rotation
def vel(vell):
    global spd_ang

    spd_ang += vell * pi / 16  # The new speed

    if spd_ang < 0:
        spd_ang = 0.001


# Function that makes the animation of rotation
def rot(ang):
    i = 0
    while i < 6:
        j = i
        while j < i + 2:
            prev_x, prev_y = petals_list[j]  # Coordinates of the triangles vertices

            x = prev_x * math.cos(ang) - prev_y * math.sin(ang)  # Updating the values of the triangles vertices
            y = prev_y * math.cos(ang) + prev_x * math.sin(ang)  # Updating the values of the triangles vertices

            petals_list[j] = x, y    # Updating the values of the triangles vertices

            j += 1

        i += 2
    glutPostRedisplay()  # The display needs to be redisplayed, changes in the screen to occur


# Function that draw the flower trunk
def flower_petals():
    i = 0
    while i < 6:
        glBegin(GL_TRIANGLES)   # Delimit the vertices of triangles
        glColor3d(1.0, 0.0, 1.0)    # Defines the color of triangles
        glVertex2f(0.0, 0.0)    # The center of triangles is in the same point

        j = i
        while j < i + 2:
            try:
                x, y = petals_list[j]  # Coordinates of the triangles vertices

                glVertex2f(x, y)    # Draw the triangles
            except Exception as err:
                print("Failed: ", err)

            j += 1
        glEnd()  # specify where the "glBegin" parameters end

        i += 2


# Function that draw the flower trunk
def flower_trunk():
    i = 0
    while i < 2:
        glBegin(GL_TRIANGLES)   # Delimit the vertices of triangles
        glColor3d(0.0, 0.0, 0.0)    # Defines the color of triangles
        j = i
        while j < i + 3:
            try:
                x, y = trunk_list[j]  # Coordinates of the triangles vertices

                glVertex2i(x, y)    # Draw the triangles
            except Exception as err:
                print("Failed: ", err)

            j += 1
        glEnd()  # specify where the "glBegin" parameters end
        i += 1


# Function that handle display events like updates in images and color etc
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear buffer
    flower_trunk()  # Function that draw the flower trunk
    flower_petals()  # Function that draw the flower petals
    glutSwapBuffers()   # Swap the buffers of display


# Function that handle keyboard events
def key_f(key, x, y):
    # Esc
    if key == GLUT_KEY_END:
        os._exit(0)
    # Arrow Up
    if key == GLUT_KEY_UP:
        rot(spd_ang)
    # Arrow Down
    if key == GLUT_KEY_DOWN:
        rot(-spd_ang)
    # Arrow Right
    if key == GLUT_KEY_RIGHT:
        vel(1)
    # Arrow Left
    if key == GLUT_KEY_LEFT:
        vel(-1)


# Function to initialize
def init():
    glClearColor(1.0, 1.0, 0.0, 0.0)    # RGBA
    glutReshapeWindow(400, 400)  # Changes the size of the current window
    glMatrixMode(GL_PROJECTION)  # Initializes the type of matrix
    glLoadIdentity()    # Replace the current matrix with identity matrix
    gluOrtho2D(-400, 400, -400, 400)    # Defines a 2d orthographic projection matrix


if __name__ == '__main__':
    glutInit()  # Lib initialize
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) # Define display mode
    glutInitWindowSize(400, 400)    # (height, width)
    glutCreateWindow("April flower")

    init()  # Function to initialize the window

    glutDisplayFunc(display)    # callback to function that draw in display
    glutSpecialFunc(key_f)  # callback to function that handle display events
                            # like updates in images and color etc
    glutMainLoop()  # The main loop
