from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os

collor1 = (0.4, 0.8, 0.3)
yellow = (255, 255, 0)
collor2 = (0, 0.9, 0.9)
collor3 = (0.7, 0.1, 0.7)
collor4 = (0.1, 0.4, 0.2)
collor5 = (0.1, 0.1, 0.9)
collor6 = (0.7, 0.2, 0.2)
collor7 = (0.5, 0.6, 0.6)
yr = 0
param = 1
auto_val = False


# Function that makes the auto animation
def auto_run(val):
    global param, yr    # Global control variable
    global auto_val

    if auto_val:    # Check if the auto animation is enabled
        yr += (0.5 * param)     # making the auto animation
        glutPostRedisplay()     # The display needs to be redisplayed, changes in the screen to occur
        glutTimerFunc(5, auto_run, 1)   # calls the auto animation function again


# Function that draws the solar system
def sys_draw():
    glPushMatrix()      # Push in the matrix stack
    glColor3f(yellow[0], yellow[1], yellow[2])  # Colors of sphere in RGB
    glutSolidSphere(0.6, 20, 20)    # Draw a solid sphere
    glPopMatrix()   # pop in the matrix stack

    glPushMatrix()  # Push in the matrix stack
    glColor3f(collor1[0], collor1[1], collor1[2])   # Colors of sphere in RGB
    glRotatef(1.5 * yr, 0, 1, 0)    # Rotate the matrix
    glTranslatef(2.45, 0.1, 2)      # Translation matrix
    glutSolidSphere(0.09, 20, 20)   # Draw a solid sphere
    glPopMatrix()   # pop in the matrix stack

    glPushMatrix()  # Push in the matrix stack

    glColor3f(collor2[0], collor2[1], collor2[2])   # Colors of sphere in RGB
    glRotatef(yr, 0, 1.2, 0)    # Rotate the matrix
    glTranslatef(2, 0, 0)   # Translation matrix
    glutSolidSphere(0.2, 20, 20)    # Draw a solid sphere

    # Moon 1

    glColor3f(collor5[0], collor5[1], collor5[2])   # Colors of sphere in RGB
    glRotatef(1.7 * yr, 0, 1.1, 0)  # Rotate the matrix
    glTranslatef(0.3, 0, 0)     # Translation matrix
    glutSolidSphere(0.05, 20, 20)   # Draw a solid sphere

    # Moon 2

    glColor3f(collor7[0], collor7[1], collor7[2])   # Colors of sphere in RGB
    glRotatef(2.1 * yr, 1.1, 1.1, 0)    # Rotate the matrix
    glTranslatef(0.3, 0, 0)     # Translation matrix
    glutSolidSphere(0.03, 20, 20)   # Draw a solid sphere

    glPopMatrix()   # pop in the matrix stack

    glPushMatrix()  # Push in the matrix stack
    glColor3f(collor3[0], collor3[1], collor3[2])   # Colors of sphere in RGB
    glRotatef(0.2 * yr, 0, 1.3, 0)  # Rotate the matrix
    glTranslatef(3.45, 0, 0)    # Translation matrix
    glutSolidSphere(0.3, 20, 20)    # Draw a solid sphere
    glPopMatrix()   # pop in the matrix stack

    glPushMatrix()  # Push in the matrix stack
    glColor3f(collor4[0], collor4[1], collor4[2])   # Colors of sphere in RGB
    glRotatef(2 * yr, 0, 1.4, 0)    # Rotate the matrix
    glTranslatef(1.2, 0, 0)     # Translation matrix
    glutSolidSphere(0.1, 20, 20)    # Draw a solid sphere
    glPopMatrix()   # pop in the matrix stack

    glPushMatrix()  # Push in the matrix stack
    glColor3f(collor6[0], collor6[1], collor6[2])   # Colors of sphere in RGB
    glRotatef(3 * yr, 0, 1.5, 0)    # Rotate the matrix
    glTranslatef(3.1, 0, 0)     # Translation matrix
    glutSolidSphere(0.24, 20, 20)   # Draw a solid sphere
    glPopMatrix()   # pop in the matrix stack


def reshape(width, height):
    glViewport(0, 0, GLsizei(width), GLsizei(height))

    glMatrixMode(GL_MODELVIEW)      # Modelview matrix stack def
    glLoadIdentity()    # Replace the current matrix with identity matrix

    glMatrixMode(GL_PROJECTION)     # Projection matrix stack def
    gluPerspective(60, float(width / height), 1, 20)    # Perspective matrix def
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)    # Define the camera


# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)     # Clear buffer

    sys_draw()  # Function that draws the sun and planets

    glutSwapBuffers()   # Swap the buffers of display


# Program initialize function
def init():
    glClearColor(0, 0, 0, 0)    # RGBA
    glEnable(GL_DEPTH_TEST)     # Enable depth comparations and update depth buffer


# Keyboard events function
def key_f(key, x, y):
    global param, yr    # Global control variables
    global auto_val

    if key == b'y':     # Change speed and guidance
        param = 1
        yr += 1
        glutPostRedisplay()     # The display needs to be redisplayed, changes in the screen to occur
    elif key == b'Y':   # Change speed and guidance
        param = -1
        yr -= 1
        glutPostRedisplay()     # The display needs to be redisplayed, changes in the screen to occur
    elif key == b'\x1b':    # If 'esc' was pressed
        os._exit(0)
    elif key == b'a':   # Calls the auto animation
        auto_val = True
        glutTimerFunc(5, auto_run, 1)   # Calls the auto animation function
    elif key == b'd':   # Shut off the auto animation
        auto_val = False


if __name__ == '__main__':
    glutInit()  # Lib initialize
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)    # Define display mode
    glutInitWindowSize(800, 600)    # Define windows size
    glutInitWindowPosition(100, 100)    # (height, width)
    glutCreateWindow("Solar System")    # Window top text

    init()  # Program init function

    glutDisplayFunc(display)    # callback to function that draw in display
    glutReshapeFunc(reshape)    # callback to function that deals reshape
    glutKeyboardFunc(key_f)     # callback to function that handle keyboard events
    glutTimerFunc(5, auto_run, 1)   # callback function that deals the auto animation of solar system

    glutMainLoop()  # the main loop
