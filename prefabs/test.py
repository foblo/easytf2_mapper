import os
import math

def rotatePoint(centerPoint,point,angle):
    angle = math.radians(angle)
    temp_point = point[0]-centerPoint[0] , point[1]-centerPoint[1]
    temp_point = ( temp_point[0]*math.cos(angle)-temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)+temp_point[1]*math.cos(angle))
    temp_point = temp_point[0]+centerPoint[0] , temp_point[1]+centerPoint[1]
    return temp_point

def createTile(posx, posy, id_num, world_id_num, entity_num, placeholder_list, rotation, level):
    
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template/test.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them

    if rotation == 0:

        x1 = posx*1*512
        y1 = posy*-1*512
        z1 = level*512 + 64
        x2 = posx*1*512 + (512)
        y2 = posy*-1*512
        z2 = level*512 + 64
        x3 = posx*1*512 + (512)
        y3 = posy*-1*512 + (-512)
        z3 = level*512 + 64
        x4 = posx*1*512
        y4 = posy*-1*512 + (-512)
        z4 = level*512 + 0
        x5 = posx*1*512 + (512)
        y5 = posy*-1*512 + (-512)
        z5 = level*512 + 0
        x6 = posx*1*512 + (512)
        y6 = posy*-1*512
        z6 = level*512 + 0
        x7 = posx*1*512
        y7 = posy*-1*512
        z7 = level*512 + 64
        x8 = posx*1*512
        y8 = posy*-1*512 + (-512)
        z8 = level*512 + 64
        x9 = posx*1*512
        y9 = posy*-1*512 + (-512)
        z9 = level*512 + 0
        x10 = posx*1*512 + (512)
        y10 = posy*-1*512
        z10 = level*512 + 0
        x11 = posx*1*512 + (512)
        y11 = posy*-1*512 + (-512)
        z11 = level*512 + 0
        x12 = posx*1*512 + (512)
        y12 = posy*-1*512 + (-512)
        z12 = level*512 + 64
        x13 = posx*1*512 + (512)
        y13 = posy*-1*512
        z13 = level*512 + 64
        x14 = posx*1*512
        y14 = posy*-1*512
        z14 = level*512 + 64
        x15 = posx*1*512
        y15 = posy*-1*512
        z15 = level*512 + 0
        x16 = posx*1*512 + (512)
        y16 = posy*-1*512 + (-512)
        z16 = level*512 + 0
        x17 = posx*1*512
        y17 = posy*-1*512 + (-512)
        z17 = level*512 + 0
        x18 = posx*1*512
        y18 = posy*-1*512 + (-512)
        z18 = level*512 + 64
#INSERT_ROT_0_PY_LIST

    elif rotation == 1:
        x1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[0])
        y1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[1])
        z1 = level*512 + level*512 + 64
        x2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z2 = level*512 + level*512 + 64
        x3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z3 = level*512 + level*512 + 64
        x4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z4 = level*512 + level*512 + 0
        x5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z5 = level*512 + level*512 + 0
        x6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z6 = level*512 + level*512 + 0
        x7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[0])
        y7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[1])
        z7 = level*512 + level*512 + 64
        x8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z8 = level*512 + level*512 + 64
        x9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z9 = level*512 + level*512 + 0
        x10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z10 = level*512 + level*512 + 0
        x11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z11 = level*512 + level*512 + 0
        x12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z12 = level*512 + level*512 + 64
        x13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[0])
        y13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 270)[1])
        z13 = level*512 + level*512 + 64
        x14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[0])
        y14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[1])
        z14 = level*512 + level*512 + 64
        x15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[0])
        y15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 270)[1])
        z15 = level*512 + level*512 + 0
        x16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[0])
        y16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 270)[1])
        z16 = level*512 + level*512 + 0
        x17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z17 = level*512 + level*512 + 0
        x18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[0])
        y18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 270)[1])
        z18 = level*512 + level*512 + 64
#INSERT_ROT_1_PY_LIST

    elif rotation == 2:
        x1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[0])
        y1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[1])
        z1 = level*512 + level*512 + 64
        x2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z2 = level*512 + level*512 + 64
        x3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z3 = level*512 + level*512 + 64
        x4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z4 = level*512 + level*512 + 0
        x5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z5 = level*512 + level*512 + 0
        x6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z6 = level*512 + level*512 + 0
        x7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[0])
        y7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[1])
        z7 = level*512 + level*512 + 64
        x8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z8 = level*512 + level*512 + 64
        x9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z9 = level*512 + level*512 + 0
        x10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z10 = level*512 + level*512 + 0
        x11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z11 = level*512 + level*512 + 0
        x12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z12 = level*512 + level*512 + 64
        x13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[0])
        y13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 180)[1])
        z13 = level*512 + level*512 + 64
        x14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[0])
        y14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[1])
        z14 = level*512 + level*512 + 64
        x15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[0])
        y15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 180)[1])
        z15 = level*512 + level*512 + 0
        x16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[0])
        y16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 180)[1])
        z16 = level*512 + level*512 + 0
        x17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z17 = level*512 + level*512 + 0
        x18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[0])
        y18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 180)[1])
        z18 = level*512 + level*512 + 64
#INSERT_ROT_2_PY_LIST

    elif rotation == 3:
        x1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[0])
        y1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[1])
        z1 = level*512 + level*512 + 64
        x2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y2 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z2 = level*512 + level*512 + 64
        x3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y3 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z3 = level*512 + level*512 + 64
        x4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y4 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z4 = level*512 + level*512 + 0
        x5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y5 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z5 = level*512 + level*512 + 0
        x6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y6 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z6 = level*512 + level*512 + 0
        x7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[0])
        y7 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[1])
        z7 = level*512 + level*512 + 64
        x8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y8 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z8 = level*512 + level*512 + 64
        x9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y9 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z9 = level*512 + level*512 + 0
        x10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y10 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z10 = level*512 + level*512 + 0
        x11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y11 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z11 = level*512 + level*512 + 0
        x12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y12 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z12 = level*512 + level*512 + 64
        x13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[0])
        y13 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512), 90)[1])
        z13 = level*512 + level*512 + 64
        x14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[0])
        y14 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[1])
        z14 = level*512 + level*512 + 64
        x15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[0])
        y15 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512), 90)[1])
        z15 = level*512 + level*512 + 0
        x16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[0])
        y16 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (512), posy*-1*512 + (-512)), 90)[1])
        z16 = level*512 + level*512 + 0
        x17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y17 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z17 = level*512 + level*512 + 0
        x18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[0])
        y18 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512, posy*-1*512 + (-512)), 90)[1])
        z18 = level*512 + level*512 + 64
#INSERT_ROT_3_PY_LIST

    var_count = 18
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
    
    for i in range(ogvalues.count("world_idnum")):
        values = values.replace('world_idnum', str(world_id_num), 1)
        world_id_num += 1
    
    for var in ["x", "y", "z"]:
        for count in range(1,var_count+1):
            string = var + str(count)
            string_var = str(eval(var + str(count)))

            if var == "z":
                values = values.replace(string + ")",string_var + ")") #we need to do this or else it will mess up on 2 digit numbers
            else:
                values = values.replace(string + " ",string_var + " ")

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1
        if "ROTATION_RIGHT" in values:
            if rotation == 0:
                values = values.replace("ROTATION_RIGHT","0 0 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_RIGHT","0 270 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_RIGHT","0 180 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_RIGHT","0 90 0",1)
        if "ROTATION_UP" in values:
            if rotation == 0:
                values = values.replace("ROTATION_UP","0 90 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_UP","0 0 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_UP","0 270 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_UP","0 180 0",1)
        if "ROTATION_LEFT" in values:
            if rotation == 0:
                values = values.replace("ROTATION_LEFT","0 180 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_LEFT","0 90 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_LEFT","0 0 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_LEFT","0 270 0",1)
        if "ROTATION_DOWN" in values:
            if rotation == 0:
                values = values.replace("ROTATION_DOWN","0 270 0",1)
            elif rotation == 1:
                values = values.replace("ROTATION_DOWN","0 180 0",1)
            elif rotation == 2:
                values = values.replace("ROTATION_DOWN","0 90 0",1)
            elif rotation == 3:
                values = values.replace("ROTATION_DOWN","0 0 0",1)

    values = values.replace('"[0 0 0 1] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[0 0 1 0] 0.25"','"[1 1 1 1] 0.25"')
    values = values.replace('"[0 1 0 0] 0.25"','"[1 1 1 1] 0.25"')       
    values = values.replace('"[1 0 0 0] 0.25"','"[1 1 1 1] 0.25"')
        

    g = open('prefab_template/test_entities.txt', 'r+')
    lines_ent = g.readlines()

    if rotation == 0:

        px1 = posx*1*512 + (256)
        py1 = posy*-1*512 + (-256)
        pz1 = level*512 + 64
#INSERT_ROT_0_PY_LIST

    elif rotation == 1:
        px1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (256), posy*-1*512 + (-256)), 270)[0])
        py1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (256), posy*-1*512 + (-256)), 270)[1])
        pz1 = level*512 + level*512 + 64
#INSERT_ROT_1_PY_LIST

    elif rotation == 2:
        px1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (256), posy*-1*512 + (-256)), 180)[0])
        py1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (256), posy*-1*512 + (-256)), 180)[1])
        pz1 = level*512 + level*512 + 64
#INSERT_ROT_2_PY_LIST

    elif rotation == 3:
        px1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (256), posy*-1*512 + (-256)), 90)[0])
        py1 = int(rotatePoint((posx*512+256,posy*-1*512-256), (posx*1*512 + (256), posy*-1*512 + (-256)), 90)[1])
        pz1 = level*512 + level*512 + 64
#INSERT_ROT_3_PY_LIST
    ent_var_count = 1
    ent_values = "".join(lines_ent)
    ent_values_split = ent_values.split("\"")
    valcount = "".join(lines_ent)

    for item in ent_values_split:
        if "entity_name" in item or "parent_name" in item or "door_large" in item:
            placeholder_list.append(item)

    for i in range(valcount.count('world_idnum')):
        ent_values = ent_values.replace('world_idnum', str(world_id_num), 1)
        world_id_num += 1

    for var in ["px", "py", "pz"]:
        for count in range(1,ent_var_count+1):
            string = var + str(count)
            string_var = str(eval(var + str(count)))

            if var == "pz":
                ent_values = ent_values.replace(string + "\"",string_var + "\"") #we need to do this or else it will mess up on 2 digit numbers
            else:
                ent_values = ent_values.replace(string + " ",string_var + " ")
                
    for var in ["x", "y", "z"]:
        for count in range(1,var_count+1):
            try:
                string = var + str(count)
                string_var = str(eval(var + str(count)))
                if var == "z":
                    ent_values = ent_values.replace(string + ")",string_var + ")") #we need to do this or else it will mess up on 2 digit numbers
                else:
                    ent_values = ent_values.replace(string + " ",string_var + " ")
            except:
                pass

    for i in range(valcount.count('id_num')):
        ent_values = ent_values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    for i in range(valcount.count("entity_name")):
        try:
            ent_values = ent_values.replace("entity_name", "entity" + str(entity_num), 1)
            ent_values = ent_values.replace("entity_same", "entity" + str(entity_num), 1)
            if "parent_name" in placeholder_list[entity_num]:
                ent_values = ent_values.replace("parent_name", "entity" + str(entity_num), 1)
                placeholder_list.remove(placeholder_list[entity_num])
            
            if "door_large" in ent_values:
                ent_values = ent_values.replace("door_large", "door_large" + str(entity_num), 4)
            if "\"respawn_name\"" in ent_values:
                ent_values = ent_values.replace("\"respawn_name\"", "\"respawn_name" + str(entity_num) + "\"", 2)
            if "ROTATION_RIGHT" in ent_values:
                if rotation == 0:
                    ent_values = ent_values.replace("ROTATION_RIGHT","0 0 0",1)
                elif rotation == 1:
                    ent_values = ent_values.replace("ROTATION_RIGHT","0 270 0",1)
                elif rotation == 2:
                    ent_values = ent_values.replace("ROTATION_RIGHT","0 180 0",1)
                elif rotation == 3:
                    ent_values = ent_values.replace("ROTATION_RIGHT","0 90 0",1)
            if "ROTATION_UP" in ent_values:
                if rotation == 0:
                    ent_values = ent_values.replace("ROTATION_UP","0 90 0",1)
                elif rotation == 1:
                    ent_values = ent_values.replace("ROTATION_UP","0 0 0",1)
                elif rotation == 2:
                    ent_values = ent_values.replace("ROTATION_UP","0 270 0",1)
                elif rotation == 3:
                    ent_values = ent_values.replace("ROTATION_UP","0 180 0",1)
            if "ROTATION_LEFT" in ent_values:
                if rotation == 0:
                    ent_values = ent_values.replace("ROTATION_LEFT","0 180 0",1)
                elif rotation == 1:
                    ent_values = ent_values.replace("ROTATION_LEFT","0 90 0",1)
                elif rotation == 2:
                    ent_values = ent_values.replace("ROTATION_LEFT","0 0 0",1)
                elif rotation == 3:
                    ent_values = ent_values.replace("ROTATION_LEFT","0 270 0",1)
            if "ROTATION_DOWN" in ent_values:
                if rotation == 0:
                    ent_values = ent_values.replace("ROTATION_DOWN","0 270 0",1)
                elif rotation == 1:
                    ent_values = ent_values.replace("ROTATION_DOWN","0 180 0",1)
                elif rotation == 2:
                    ent_values = ent_values.replace("ROTATION_DOWN","0 90 0",1)
                elif rotation == 3:
                    ent_values = ent_values.replace("ROTATION_DOWN","0 0 0",1)
            
            entity_num += 1
        except:
            pass



    return values, id_num, world_id_num, entity_num, ent_values, placeholder_list