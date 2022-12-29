# If area of room is 144 sq m. Then how many tiles of size 12*12 sq cm will be required to cover the flooring of room.
'''
area =  144 sq.m
tile = 1.44     # 12*12 sq. cm = 144 sq.cm i.e. 1.44 sq.m
total_tiles = area/tile
print("Total tiles required to cover the flooring of room: ",total_tiles)

'''
# Input from user
area = float(input("Enter area of room in sq.m: "))
tile_l = float(input("Enter tile length in cm: "))
tile_b = float(input("Enter tile breadth in cm: "))

print("Area of room: ",area,"sq.m")

tile_area = tile_l * tile_b / 100 # cm to m 
print("Single Tile dimension: ",tile_l,"*",tile_b,"sq.cm","\n i.e. Single tile area", tile_area,"sq.m")

total_tiles = area/tile_area
print("Total tiles required to cover the flooring of room: ",int(total_tiles))



