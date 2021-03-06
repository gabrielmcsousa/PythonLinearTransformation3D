import numpy as np
import matplotlib.pyplot as plt

#ROTATION MATRIX FOR X AXIS
def rotateX(p, ang):
    m_rot = np.array([ 
        [1,0,0],
        [0, np.cos(np.deg2rad(ang)), -np.sin(np.deg2rad(ang))],
        [0, np.sin(np.deg2rad(ang)), np.cos(np.deg2rad(ang))]
    ])

    rot = m_rot @ p

    return rot

#ROTATION MATRIX FOR Y AXIS
def rotateY(p, ang):
    m_rot = np.array([ 
        [np.cos(np.deg2rad(ang)), 0, -np.sin(np.deg2rad(ang))],
        [0,1,0],
        [np.sin(np.deg2rad(ang)), 0, np.cos(np.deg2rad(ang))]
    ])

    rot = m_rot @ p

    return rot

#ROTATION MATRIX FOR Z AXIS
def rotateZ(p, ang):
    m_rot = np.array([ 
        [np.cos(np.deg2rad(ang)), -np.sin(np.deg2rad(ang)),0],
        [np.sin(np.deg2rad(ang)), np.cos(np.deg2rad(ang)),0],
        [0,0,1]
    ])

    rot = m_rot @ p

    return rot

#ROTATING EVERY VECTOR IN THE FIGURE, ON THE Z AXIS
#IF YOU WISH TO CHANGE THE DIRECTION, CHANGE THE ROTATE FUNCTION IN LINE 44
def rotate_figure(figure, _angulo_rotacao):
    for i in range(len(figure)):
        vetor = rotateZ(figure[i], _angulo_rotacao)
        ax.plot(vetor[0], vetor[1], vetor[2], 'k-')
        figure[i] = vetor

#CONNECT TWO VECTORS AND PLOT THE LINE
def connectPoints(p_0, p_1):
    x1, x2 = p_0[0], p_1[0]
    y1, y2 = p_0[1], p_1[1]
    z1, z2 = p_0[2], p_1[2]

    #Random Collored Lines
    ax.plot([x1, x2], [y1, y2], [z1, z2], 'k-')
    #Black Lines
    #ax.plot([x1, x2], [y1, y2], [z1, z2], 'k-')

def createCube():
    #CENTRALIZED CUBE
    connectPoints(cube[0], cube[1])
    connectPoints(cube[0], cube[3])
    connectPoints(cube[0], cube[4])
    connectPoints(cube[1], cube[2])
    connectPoints(cube[1], cube[5])
    connectPoints(cube[2], cube[3])
    connectPoints(cube[2], cube[6])
    connectPoints(cube[3], cube[7])
    connectPoints(cube[4], cube[5])
    connectPoints(cube[4], cube[7])
    connectPoints(cube[5], cube[6])
    connectPoints(cube[6], cube[7])

    #DECENTRALIZED CUBE
    #connectPoints(cube[0], cube[1])
    #connectPoints(cube[0], cube[2])
    #connectPoints(cube[0], cube[4])
    #connectPoints(cube[1], cube[5])
    #connectPoints(cube[1], cube[3])
    #connectPoints(cube[2], cube[3])
    #connectPoints(cube[2], cube[6])
    #connectPoints(cube[3], cube[7])
    #connectPoints(cube[4], cube[5])
    #connectPoints(cube[4], cube[6])
    #connectPoints(cube[5], cube[7])
    #connectPoints(cube[6], cube[7])

def createTesseract():
    #TESSERACT
    #EXTERNAL CUBE
    connectPoints(tesseract[0], tesseract[1])
    connectPoints(tesseract[0], tesseract[3])
    connectPoints(tesseract[0], tesseract[4])
    connectPoints(tesseract[1], tesseract[2])
    connectPoints(tesseract[1], tesseract[5])
    connectPoints(tesseract[2], tesseract[3])
    connectPoints(tesseract[2], tesseract[6])
    connectPoints(tesseract[3], tesseract[7])
    connectPoints(tesseract[4], tesseract[5])
    connectPoints(tesseract[4], tesseract[7])
    connectPoints(tesseract[5], tesseract[6])
    connectPoints(tesseract[6], tesseract[7])
    #INTERNAL CUBE
    connectPoints(tesseract[0+8], tesseract[1+8])
    connectPoints(tesseract[0+8], tesseract[3+8])
    connectPoints(tesseract[0+8], tesseract[4+8])
    connectPoints(tesseract[1+8], tesseract[2+8])
    connectPoints(tesseract[1+8], tesseract[5+8])
    connectPoints(tesseract[2+8], tesseract[3+8])
    connectPoints(tesseract[2+8], tesseract[6+8])
    connectPoints(tesseract[3+8], tesseract[7+8])
    connectPoints(tesseract[4+8], tesseract[5+8])
    connectPoints(tesseract[4+8], tesseract[7+8])
    connectPoints(tesseract[5+8], tesseract[6+8])
    connectPoints(tesseract[6+8], tesseract[7+8])
    #CONNECTION
    connectPoints(tesseract[0], tesseract[8])
    connectPoints(tesseract[1], tesseract[9])
    connectPoints(tesseract[2], tesseract[10])
    connectPoints(tesseract[3], tesseract[11])
    connectPoints(tesseract[4], tesseract[12])
    connectPoints(tesseract[5], tesseract[13])
    connectPoints(tesseract[6], tesseract[14])
    connectPoints(tesseract[7], tesseract[15])

#DECENTRALIZED CUBE
#cube = [
#    [1, 1, 1], #0
#    [1, 6, 1], #1
#    [6, 1, 1], #2
#    [6, 6, 1], #3
#    [1, 1, 6], #4
#    [1, 6, 6], #5
#    [6, 1, 6], #6
#    [6, 6, 6]  #7
#]

#CENTRALIZED CUBE
cube = [
    [2, -2, -2], #0
    [-2, -2, -2], #1
    [-2, 2, -2], #2
    [2, 2, -2], #3
    [2, -2, 2], #4
    [-2, -2, 2], #5
    [-2, 2, 2], #6
    [2, 2, 2]  #7
]

#CENTRALIZED TESSERACT
tesseract = [
    [2, -2, -2], #0
    [-2, -2, -2], #1
    [-2, 2, -2], #2
    [2, 2, -2], #3
    [2, -2, 2], #4
    [-2, -2, 2], #5
    [-2, 2, 2], #6
    [2, 2, 2],  #7
    [1, -1, -1], #8
    [-1, -1, -1], #9
    [-1, 1, -1], #10
    [1, 1, -1], #11
    [1, -1, 1], #12
    [-1, -1, 1], #13
    [-1, 1, 1], #14
    [1, 1, 1]  #15
]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_zlim([-5,5])

createTesseract()
#createCube()
#plt.show()


'''
    THIS PART KEEPS DRAWING AND ROTATING THE CUBE/TESSERACT
    IF YOU WISH DO DRAW ONE OR THE OTHER, COMMENT THE LINES REGARDING TO EACH
    AS OF NOW, THE LINES REGARDING TO THE SIMPLE CUBE AR COMMENTED
'''
while True:
    #rotate_figure(cube, 5)
    #createCube()

    rotate_figure(tesseract, 5)
    createTesseract()
    plt.draw()
    
    #FOR Cube
    #for i in range(len(ax.lines)-13, 0, -1):
    #    ax.lines.remove(ax.lines[i])

    #FOR TESSERACT
    for i in range(len(ax.lines)-33, 0, -1):
        ax.lines.remove(ax.lines[i])
    
    plt.pause(0.00001)

