from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os


actx = 0
acty = 0

color_dict = {20: (255, 255, 0), 100: (0, 0, 205), 180: (0.9, 0.4, 0.8),
              260: (0.9, 0.2, 1), 340: (0.3, 0.5, 0.8)}

squares = [[(20, 80,  20, 80), (255, 255, 0)], [(100, 160, 20, 80), (0, 0, 205)],
           [(180, 240, 20, 80), (0.9, 0.4, 0.8)], [(260, 320, 20, 80), (0.9, 0.2, 1)],
           [(340, 400, 20, 80), (0.3, 0.5, 0.8)]]


# Function to initialize
def init():
    glClearColor(0.7, 0.7, 0.7, 1.0)  # RGBA
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Cleaning buffers
    glLoadIdentity() # Reset the matrix

    gluOrtho2D(0, 500, 0, 500)  # left, right, bottom, top

    global actx, acty
    actx, acty = 20, 80

    # the calls for the display func initializes the squares
    display((20, 80,  20, 80), (255, 255, 0))
    display((100, 160, 20, 80), (0, 0, 205))
    display((180, 240, 20, 80), (0.9, 0.4, 0.8))
    display((260, 320, 20, 80), (0.9, 0.2, 1))
    display((340, 400, 20, 80), (0.3, 0.5, 0.8))

    glutSwapBuffers()


# Function to animate the ola
def re_display():
    # Cleaning buffers again to redraw squares
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    global actx, acty

    # checking square that is going up
    for c in squares:
        if c[0][0] == actx:
            display((c[0][0], c[0][1], 100, 160), c[1])
        else:
            display((c[0][0], c[0][1], c[0][2], c[0][3]), c[1])


# Function to draw squares
def display(pos, color):
    glColor3d(color[0], color[1], color[2])  # RGB

    glBegin(GL_POLYGON)
    glVertex2i(pos[0], pos[2])
    glVertex2i(pos[1], pos[2])
    glVertex2i(pos[1], pos[3])
    glVertex2i(pos[0], pos[3])

    glEnd()

    glFlush()  # Updates window draw


# Function to deal with keyboard events
def ola_make(key, x, y):
    global actx, acty
    global color_dict

    # The end key closes the program
    if key == GLUT_KEY_END:
        os._exit(0)

    # Left arrow
    elif key == GLUT_KEY_LEFT:
        if actx <= 20 and acty <= 80:
            re_display()
            actx, acty = 340, 400
            re_display()
        else:
            re_display()
            actx -= 80
            acty -= 80
            re_display()

    # Right arrow
    elif key == GLUT_KEY_RIGHT:
        if actx >= 340 and acty >= 400:
            re_display()
            actx, acty = 20, 80
            re_display()
        else:
            re_display()
            actx += 80
            acty += 80
            re_display()

    # Redefines squares to start position
    elif key == GLUT_KEY_HOME:
        init()


glutInit()  # Lib initialize
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) # Define display mode

glutInitWindowSize(500, 500)  # (height, width)
glutInitWindowPosition(100, 100)  # (x pos, y pos)

glutCreateWindow("Hello World!")

glutDisplayFunc(init)   # Callback function of init function
glutSpecialFunc(ola_make)   # Function to deal with keyboard events
glutMainLoop()  # The mainloop
