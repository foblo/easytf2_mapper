import os

def createSkyboxLeft(gridx,gridy,skyboxz,id_num,world_id_num):
    values = []
    f = open('prefab_template/skybox_worldgeo/skybox_side.txt','r+')
    lines = f.readlines()
    values = "".join(lines)#converting list to string
    ogvalues = "".join(lines)
    values = values.replace("world_idnum", str(world_id_num))
    world_id_num += 1
    values = values.replace("skyboxz",str(skyboxz))
    values = values.replace("ynum",str(gridy*-512))

    for i in range(ogvalues.count('id_num')):
        values = values.replace('id_num', str(id_num), 1)
        id_num = id_num+1

    return values, id_num, world_id_num
