from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import radians, sin, cos, tan, sqrt

from loadMap import load_map
'''

Raycasting engine, written in player_ython using OpenGl, GLU, and GLUT


'''

def FixAng(angle):
    return angle%360

# The map that player exists in

world, mapX, mapY = load_map("maps/aryantech123.txt")

# Map variables
mapS = 64 # Size of each square in the map

# Draws 2D map
def drawMap2d():
    for y in range(0, mapY):
        for x in range(0 , mapX):
            if(world[y*mapY+x] != 0):
                glColor(1, 1, 1)
            else:
                glColor(0, 0, 0)
            xo, yo = x*mapS, y*mapS
            glBegin(GL_QUADS)
            glVertex(xo, yo)
            glVertex(xo, mapS+yo)
            glVertex(mapS+xo, mapS+yo)
            glVertex(mapS+xo, yo)
            glEnd()

# Player position variables
player_x = 0 # Player x
player_y = 0 # Player y
player_angle = 0 # Player angle
player_delta_x = 0 # Player delta x
player_delta_y = 0 # Player delta y


# Handles keyboard input callbacks
def buttons(key, x, y):
    global player_x, player_y, player_angle, player_delta_x, player_delta_y
    if(ord(key) == ord('z')):
        player_x += player_delta_x*5
        player_y += player_delta_y*5
    elif(ord(key) == ord('q')):
        player_angle += 5
        player_angle = FixAng(player_angle)
        player_delta_x=cos(radians(player_angle))
        player_delta_y=-sin(radians(player_angle))
    elif(ord(key) == ord('d')):
        player_angle -= 5
        player_angle = FixAng(player_angle)
        player_delta_x=cos(radians(player_angle))
        player_delta_y=-sin(radians(player_angle))
    elif(ord(key) == ord('s')):
        player_x -= player_delta_x*5
        player_y -= player_delta_y*5
    elif(ord(key) == ord('a')):
        player_x = x
        player_y = y
    glutPostRedisplay()

# Drawing all the rays
def drawRays2d():
    # Draws sky
    glColor3f(0,1,1)
    glBegin(GL_QUADS)
    glVertex( 526,  0) # Bottom left
    glVertex(1006,  0) # Bottom right
    glVertex(1006, 160) # Top right
    glVertex( 526, 160) # Top left
    glEnd()

    #Draws floor
    glColor3f(0,0.7,0)
    glBegin(GL_QUADS)
    glVertex2i(526,160) # Bottom left
    glVertex2i(1006,160) # Bottom right
    glVertex2i(1006,320) # Top right
    glVertex2i(526,320) # Top lefts
    glEnd()

    #ra is the ray angle
    ra = FixAng(player_angle + 30)

    for r in range(1, 60): # We are drawing total 60 rays, for a 60 degree field of view

        # Checking vertical wall intercept
        dof = 0 # Distance of wall
        disV = 10000 # Distance to the vertical wall
        Tan = tan(radians(ra)) # Tangent of the ray angle
        if(cos(radians(ra)) > 0.001): # Looking leftwards
            rx = ((int(player_x) >> 6) << 6) + 64 # First x-intercept
            ry = (player_x - rx)*Tan+player_y
            xo = 64
            yo = -xo * Tan
        elif(cos(radians(ra)) < -0.001): # Looking rightwards
            rx = ((int(player_x) >> 6) << 6) - 0.001
            ry = (player_x - rx)*Tan+player_y
            xo = -64
            yo = -xo * Tan
        else: # No vertical hit
            rx=player_x 
            ry=player_y
            dof=8
        while(dof < 8):
            mx = int(rx) >> 6
            my = int(ry) >> 6
            mp = my*mapX + mx
            if(mp > 0 and mp < mapX*mapY and world[mp] != 0): # Is the intercept a wall?
                dof = 8
                # disV = cos(radians(ra))*(rx-player_x)-sin(radians(ra))*(ry-player_y)
                disV = sqrt((player_x-rx)**2 + (player_y-ry)**2) # Finding vertical distance
                
            else: # Else, check next intercept
                rx += xo
                ry += yo
                dof += 1
        vx = rx
        vy = ry

        # Checking Horizontal wall intercept
        dof = 0 # Distance of wall
        disH = 10000 # Distance to the horizontal wall
        Tan = 1/Tan # Reciprocal of the slope

        if(sin(radians(ra)) > 0.001): # Looking up
            ry = ((int(player_y) >> 6) << 6) - 0.0001
            rx = (player_y-ry)*Tan+player_x
            yo = -64
            xo = -yo*Tan
        elif(sin(radians(ra)) < -0.001): # Looking down
            ry = ((int(player_y) >> 6) << 6) + 64
            rx = (player_y-ry)*Tan+player_x
            yo = 64
            xo = -yo*Tan
        
        while(dof < 8):
            mx = int(rx) >> 6 # Map grid index	
            my = int(ry) >> 6 # Map grid index
            mp = my*mapX + mx # Map index
            if(mp > 0 and mp < mapX*mapY and world[mp] != 0): # Is intercept a wall?
                dof = 8 # If yes, then distance is 8
                # disH = cos(radians(ra)) * (rx-player_x) - sin(radians(ra))*(ry-player_y)
                disH = sqrt((player_x-rx)**2 + (player_y-ry)**2)
                hitVertical = False # Ray has hit a horizontal wall
            else: # Now check next intercept
                rx += xo # Next x-intercept
                ry += yo # Next y-intercept
                dof += 1 # Increment distance of wall
        hx, hy = rx, ry # Horizontal intercept

        if(disV < disH): # If a Vertical wall is hit first
            rx, ry = vx, vy # Then the intercept is the vertical intercept
            disH = disV # And the distance is the vertical distance
            hitVertical = True # Ray has hit a vertical wall
        else: # If a Horizontal wall is hit first
            rx, ry = hx, hy # Then the intercept is the horizontal intercept
            hitVertical = False # Is the ray hitting a vertical wall?
        
        
        # Drawing 2D rays
        glLineWidth(2)
        glBegin(GL_LINES)
        glVertex(player_x, player_y)
        glVertex(rx, ry)
        glEnd()

        # Drawing 3D scene
        ca = FixAng(player_angle - ra) # This is to correct for Fisheye effect, which looks unnatural
        disH = disH*cos(radians(ca))
        lineH = mapS*320/disH
        if(lineH > 320):
            lineH = 320
        lineOff = 160-(lineH // 2)

           
        glLineWidth(15)

        if(hitVertical):
            glColor(0.6, 0.6, 0.6)
        else:
            glColor(0.4, 0.4, 0.4)
            
        glBegin(GL_LINES)
        glVertex(r*8+530,lineOff)
        glVertex(r*8+530,lineOff+lineH)
     
        glEnd()
        # Looping to next ray
        ra = FixAng(ra -1)

# Initializing basic window player_anglerameters
def init():
    global player_x, player_y, player_angle, player_delta_x, player_delta_y
    glClearColor(0.3,0.3,0.3,0)
    gluOrtho2D(0,1024,510,0)
    player_x=150; player_y=400; player_angle=90.1
    player_delta_x=cos(radians(player_angle))
    player_delta_y=-sin(radians(player_angle))

# Display callback function
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    drawMap2d()
    drawRays2d()
    glutSwapBuffers()

# Defining all callbacks and windows.
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(1024, 510)
glutCreateWindow(b"player_yopengl raycater")
init()
glutDisplayFunc(display)
glutIdleFunc(display)
glutKeyboardFunc(buttons)

glutMainLoop()

