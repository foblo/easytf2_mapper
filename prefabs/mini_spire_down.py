import os

def createTile(posx, posy, id_num, world_id_num, entity_num, placeholder_list):
    
    looplist = '1'
    values=[]#Values are all of the lines of a prefab that have the vertex coords
    f = open('prefab_template/mini_spire_down.txt', 'r+')
    lines = f.readlines() #gathers each line of the prefab and puts numbers them
    x1 = posx*512 + (512)
    y1 = posy*-512 + (-512)
    z1 = 64
    x2 = posx*512
    y2 = posy*-512 + (-512)
    z2 = 64
    x3 = posx*512
    y3 = posy*-512
    z3 = 64
    x4 = posx*512 + (512)
    y4 = posy*-512
    z4 = 0
    x5 = posx*512
    y5 = posy*-512
    z5 = 0
    x6 = posx*512
    y6 = posy*-512 + (-512)
    z6 = 0
    x7 = posx*512 + (512)
    y7 = posy*-512 + (-512)
    z7 = 0
    x8 = posx*512
    y8 = posy*-512 + (-512)
    z8 = 0
    x9 = posx*512
    y9 = posy*-512 + (-512)
    z9 = 64
    x10 = posx*512
    y10 = posy*-512
    z10 = 0
    x11 = posx*512 + (512)
    y11 = posy*-512
    z11 = 0
    x12 = posx*512 + (512)
    y12 = posy*-512
    z12 = 64
    x13 = posx*512
    y13 = posy*-512 + (-512)
    z13 = 0
    x14 = posx*512
    y14 = posy*-512
    z14 = 0
    x15 = posx*512
    y15 = posy*-512
    z15 = 64
    x16 = posx*512 + (512)
    y16 = posy*-512
    z16 = 0
    x17 = posx*512 + (512)
    y17 = posy*-512 + (-512)
    z17 = 0
    x18 = posx*512 + (512)
    y18 = posy*-512 + (-512)
    z18 = 64
    x19 = posx*512 + (448)
    y19 = posy*-512 + (-128)
    z19 = 192
    x20 = posx*512 + (384)
    y20 = posy*-512 + (-128)
    z20 = 192
    x21 = posx*512 + (384)
    y21 = posy*-512 + (-64)
    z21 = 192
    x22 = posx*512 + (448)
    y22 = posy*-512 + (-64)
    z22 = 176
    x23 = posx*512 + (384)
    y23 = posy*-512 + (-64)
    z23 = 176
    x24 = posx*512 + (384)
    y24 = posy*-512 + (-128)
    z24 = 176
    x25 = posx*512 + (448)
    y25 = posy*-512 + (-128)
    z25 = 176
    x26 = posx*512 + (384)
    y26 = posy*-512 + (-128)
    z26 = 176
    x27 = posx*512 + (384)
    y27 = posy*-512 + (-128)
    z27 = 192
    x28 = posx*512 + (384)
    y28 = posy*-512 + (-64)
    z28 = 176
    x29 = posx*512 + (448)
    y29 = posy*-512 + (-64)
    z29 = 176
    x30 = posx*512 + (448)
    y30 = posy*-512 + (-64)
    z30 = 192
    x31 = posx*512 + (384)
    y31 = posy*-512 + (-128)
    z31 = 176
    x32 = posx*512 + (384)
    y32 = posy*-512 + (-64)
    z32 = 176
    x33 = posx*512 + (384)
    y33 = posy*-512 + (-64)
    z33 = 192
    x34 = posx*512 + (448)
    y34 = posy*-512 + (-64)
    z34 = 176
    x35 = posx*512 + (448)
    y35 = posy*-512 + (-128)
    z35 = 176
    x36 = posx*512 + (448)
    y36 = posy*-512 + (-128)
    z36 = 192
    x37 = posx*512 + (128)
    y37 = posy*-512 + (-128)
    z37 = 192
    x38 = posx*512 + (64)
    y38 = posy*-512 + (-128)
    z38 = 192
    x39 = posx*512 + (64)
    y39 = posy*-512 + (-64)
    z39 = 192
    x40 = posx*512 + (128)
    y40 = posy*-512 + (-64)
    z40 = 176
    x41 = posx*512 + (64)
    y41 = posy*-512 + (-64)
    z41 = 176
    x42 = posx*512 + (64)
    y42 = posy*-512 + (-128)
    z42 = 176
    x43 = posx*512 + (128)
    y43 = posy*-512 + (-128)
    z43 = 176
    x44 = posx*512 + (64)
    y44 = posy*-512 + (-128)
    z44 = 176
    x45 = posx*512 + (64)
    y45 = posy*-512 + (-128)
    z45 = 192
    x46 = posx*512 + (64)
    y46 = posy*-512 + (-64)
    z46 = 176
    x47 = posx*512 + (128)
    y47 = posy*-512 + (-64)
    z47 = 176
    x48 = posx*512 + (128)
    y48 = posy*-512 + (-64)
    z48 = 192
    x49 = posx*512 + (64)
    y49 = posy*-512 + (-128)
    z49 = 176
    x50 = posx*512 + (64)
    y50 = posy*-512 + (-64)
    z50 = 176
    x51 = posx*512 + (64)
    y51 = posy*-512 + (-64)
    z51 = 192
    x52 = posx*512 + (128)
    y52 = posy*-512 + (-64)
    z52 = 176
    x53 = posx*512 + (128)
    y53 = posy*-512 + (-128)
    z53 = 176
    x54 = posx*512 + (128)
    y54 = posy*-512 + (-128)
    z54 = 192
    x55 = posx*512 + (384)
    y55 = posy*-512 + (-352)
    z55 = 64
    x56 = posx*512 + (384)
    y56 = posy*-512 + (-384)
    z56 = 64
    x57 = posx*512 + (448)
    y57 = posy*-512 + (-384)
    z57 = 64
    x58 = posx*512 + (384)
    y58 = posy*-512 + (-128)
    z58 = 192
    x59 = posx*512 + (384)
    y59 = posy*-512 + (-128)
    z59 = 176
    x60 = posx*512 + (448)
    y60 = posy*-512 + (-128)
    z60 = 176
    x61 = posx*512 + (384)
    y61 = posy*-512 + (-384)
    z61 = 64
    x62 = posx*512 + (384)
    y62 = posy*-512 + (-352)
    z62 = 64
    x63 = posx*512 + (384)
    y63 = posy*-512 + (-128)
    z63 = 176
    x64 = posx*512 + (448)
    y64 = posy*-512 + (-128)
    z64 = 192
    x65 = posx*512 + (448)
    y65 = posy*-512 + (-128)
    z65 = 176
    x66 = posx*512 + (448)
    y66 = posy*-512 + (-352)
    z66 = 64
    x67 = posx*512 + (448)
    y67 = posy*-512 + (-384)
    z67 = 64
    x68 = posx*512 + (384)
    y68 = posy*-512 + (-384)
    z68 = 64
    x69 = posx*512 + (384)
    y69 = posy*-512 + (-128)
    z69 = 192
    x70 = posx*512 + (448)
    y70 = posy*-512 + (-128)
    z70 = 176
    x71 = posx*512 + (384)
    y71 = posy*-512 + (-128)
    z71 = 176
    x72 = posx*512 + (384)
    y72 = posy*-512 + (-352)
    z72 = 64
    x73 = posx*512 + (64)
    y73 = posy*-512 + (-352)
    z73 = 64
    x74 = posx*512 + (64)
    y74 = posy*-512 + (-384)
    z74 = 64
    x75 = posx*512 + (128)
    y75 = posy*-512 + (-384)
    z75 = 64
    x76 = posx*512 + (64)
    y76 = posy*-512 + (-128)
    z76 = 192
    x77 = posx*512 + (64)
    y77 = posy*-512 + (-128)
    z77 = 176
    x78 = posx*512 + (128)
    y78 = posy*-512 + (-128)
    z78 = 176
    x79 = posx*512 + (64)
    y79 = posy*-512 + (-384)
    z79 = 64
    x80 = posx*512 + (64)
    y80 = posy*-512 + (-352)
    z80 = 64
    x81 = posx*512 + (64)
    y81 = posy*-512 + (-128)
    z81 = 176
    x82 = posx*512 + (128)
    y82 = posy*-512 + (-128)
    z82 = 192
    x83 = posx*512 + (128)
    y83 = posy*-512 + (-128)
    z83 = 176
    x84 = posx*512 + (128)
    y84 = posy*-512 + (-352)
    z84 = 64
    x85 = posx*512 + (128)
    y85 = posy*-512 + (-384)
    z85 = 64
    x86 = posx*512 + (64)
    y86 = posy*-512 + (-384)
    z86 = 64
    x87 = posx*512 + (64)
    y87 = posy*-512 + (-128)
    z87 = 192
    x88 = posx*512 + (128)
    y88 = posy*-512 + (-128)
    z88 = 176
    x89 = posx*512 + (64)
    y89 = posy*-512 + (-128)
    z89 = 176
    x90 = posx*512 + (64)
    y90 = posy*-512 + (-352)
    z90 = 64
    x91 = posx*512 + (384)
    y91 = posy*-512 + (-128)
    z91 = 192
    x92 = posx*512 + (128)
    y92 = posy*-512 + (-128)
    z92 = 192
    x93 = posx*512 + (128)
    y93 = posy*-512 + (-64)
    z93 = 192
    x94 = posx*512 + (384)
    y94 = posy*-512 + (-64)
    z94 = 176
    x95 = posx*512 + (128)
    y95 = posy*-512 + (-64)
    z95 = 176
    x96 = posx*512 + (128)
    y96 = posy*-512 + (-128)
    z96 = 176
    x97 = posx*512 + (384)
    y97 = posy*-512 + (-128)
    z97 = 176
    x98 = posx*512 + (128)
    y98 = posy*-512 + (-128)
    z98 = 176
    x99 = posx*512 + (128)
    y99 = posy*-512 + (-128)
    z99 = 192
    x100 = posx*512 + (128)
    y100 = posy*-512 + (-64)
    z100 = 176
    x101 = posx*512 + (384)
    y101 = posy*-512 + (-64)
    z101 = 176
    x102 = posx*512 + (384)
    y102 = posy*-512 + (-64)
    z102 = 192
    x103 = posx*512 + (128)
    y103 = posy*-512 + (-128)
    z103 = 176
    x104 = posx*512 + (128)
    y104 = posy*-512 + (-64)
    z104 = 176
    x105 = posx*512 + (128)
    y105 = posy*-512 + (-64)
    z105 = 192
    x106 = posx*512 + (384)
    y106 = posy*-512 + (-64)
    z106 = 176
    x107 = posx*512 + (384)
    y107 = posy*-512 + (-128)
    z107 = 176
    x108 = posx*512 + (384)
    y108 = posy*-512 + (-128)
    z108 = 192
    x109 = posx*512 + (384)
    y109 = posy*-512 + (-384)
    z109 = 256
    x110 = posx*512 + (128)
    y110 = posy*-512 + (-384)
    z110 = 256
    x111 = posx*512 + (128)
    y111 = posy*-512 + (-224)
    z111 = 256
    x112 = posx*512 + (128)
    y112 = posy*-512 + (-384)
    z112 = 192
    x113 = posx*512 + (128)
    y113 = posy*-512 + (-384)
    z113 = 256
    x114 = posx*512 + (384)
    y114 = posy*-512 + (-384)
    z114 = 256
    x115 = posx*512 + (128)
    y115 = posy*-512 + (-128)
    z115 = 192
    x116 = posx*512 + (128)
    y116 = posy*-512 + (-224)
    z116 = 256
    x117 = posx*512 + (128)
    y117 = posy*-512 + (-384)
    z117 = 256
    x118 = posx*512 + (384)
    y118 = posy*-512 + (-384)
    z118 = 192
    x119 = posx*512 + (384)
    y119 = posy*-512 + (-384)
    z119 = 256
    x120 = posx*512 + (384)
    y120 = posy*-512 + (-224)
    z120 = 256
    x121 = posx*512 + (384)
    y121 = posy*-512 + (-224)
    z121 = 256
    x122 = posx*512 + (128)
    y122 = posy*-512 + (-224)
    z122 = 256
    x123 = posx*512 + (128)
    y123 = posy*-512 + (-128)
    z123 = 192
    x124 = posx*512 + (128)
    y124 = posy*-512 + (-128)
    z124 = 192
    x125 = posx*512 + (128)
    y125 = posy*-512 + (-384)
    z125 = 192
    x126 = posx*512 + (384)
    y126 = posy*-512 + (-384)
    z126 = 192
    x127 = posx*512 + (320)
    y127 = posy*-512 + (-192)
    z127 = 64
    x128 = posx*512 + (192)
    y128 = posy*-512 + (-192)
    z128 = 64
    x129 = posx*512 + (192)
    y129 = posy*-512 + (-320)
    z129 = 64
    x130 = posx*512 + (320)
    y130 = posy*-512 + (-320)
    z130 = 192
    x131 = posx*512 + (192)
    y131 = posy*-512 + (-320)
    z131 = 192
    x132 = posx*512 + (192)
    y132 = posy*-512 + (-192)
    z132 = 192
    x133 = posx*512 + (320)
    y133 = posy*-512 + (-320)
    z133 = 64
    x134 = posx*512 + (192)
    y134 = posy*-512 + (-320)
    z134 = 64
    x135 = posx*512 + (192)
    y135 = posy*-512 + (-320)
    z135 = 192
    x136 = posx*512 + (192)
    y136 = posy*-512 + (-192)
    z136 = 64
    x137 = posx*512 + (320)
    y137 = posy*-512 + (-192)
    z137 = 64
    x138 = posx*512 + (320)
    y138 = posy*-512 + (-192)
    z138 = 192
    x139 = posx*512 + (192)
    y139 = posy*-512 + (-320)
    z139 = 64
    x140 = posx*512 + (192)
    y140 = posy*-512 + (-192)
    z140 = 64
    x141 = posx*512 + (192)
    y141 = posy*-512 + (-192)
    z141 = 192
    x142 = posx*512 + (320)
    y142 = posy*-512 + (-192)
    z142 = 64
    x143 = posx*512 + (320)
    y143 = posy*-512 + (-320)
    z143 = 64
    x144 = posx*512 + (320)
    y144 = posy*-512 + (-320)
    z144 = 192
    var_count = 144
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

    return values, id_num, world_id_num
