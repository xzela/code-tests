'''
MARS ROVERS

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

OUTPUT
The output for each rover should be its final co-ordinates and heading.

INPUT AND OUTPUT

Test Input:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

Expected Output:
1 3 N
5 1 E
'''
import re

position = {}

def init(command):
    """
    We assume the first command from NASA is the rover
    position. Assumetions are bad. We know that the
    command conists of two numbers seperated by a space.

    Parse the number so it matches D D
    """
    if re.match('^[0-9]\s[0-9]\s[a-zA-Z]$', command):
        pos = command.split(" ");
        position['x'] = pos[0]
        position['y'] = pos[1]
        position['heading'] = pos[2]
        print position
        return position
    return False

def update_position(position):
    if position['heading'] == 'N':
        position['y'] = int(position['y']) + 1
    elif position['heading'] == 'S':
        position['y'] = int(position['y']) - 1
    elif position['heading'] == 'E':
        position['x'] = int(position['x']) + 1
    elif position['heading'] == 'W':
        position['x'] = int(position['x']) - 1

def update_heading(m):
    headings = ['N', 'E', 'S', 'W']
    index = headings.index(position['heading'])
    if m == "L":
        if index == 0:
            index = 3
        else:
            index = index - 1
    if m == "R":
        if index == 3:
            index = 0
        else:
            index = index + 1
    position['heading'] = headings[index]


def move(command):
    """
    Movement commands come down as long strings of alpha characters
    There are only three movement characters, L, R, and M
    L updates the rovers heading by 90deg to the left
    R updates the rovers heading by 90deg to the right
    M moves the rover forward one unti (towards its heading)
    """
    instructions = list(command)
    for m in instructions:
        if m == "M":
            update_position(position)
        if m == "R" or m == "L":
            update_heading(m)
    print position


init("1 2 N")
move("LMLMLMLMM")
