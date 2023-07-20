## Load packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
from h5py import *

## Define coordinates
#returns num evenly spaced samples, calculated over the interval [start, stop]
#we want 40 for the x axis and 100 for the z axis
x = np.linspace(0,49,50)
z = np.linspace(0,109,110)

## Make grid and flatten
#create coordinate matrices from coordinate vectors
XX,ZZ = np.meshgrid(x,z)
#stack arrays in sequence vertically (row wise).
#create a copy of the array collapsed into one dimension
xz = pd.DataFrame(np.vstack((XX.flatten(), ZZ.flatten())).T)

## Define additional columns and rename them
xz['y'] = 0 # 2D grid
xz["zone"] = 0 #create empty column here
xz["zone"] = xz["zone"].astype("object")
xz.columns = ["x","z","y","zone"]
#print(xz)

## Filter for zones here
#df.loc[(condition1) & (condition2) & (condition N),"variable"] = value
#Zone0
xz.loc[(xz['z']<=99),'zone'] = 6

#Zone2
xz.loc[(xz['x']<=49) & (xz['z']<=99) &(xz['z']>=70),'zone'] = 2


#Zone 5
xz.loc[(xz['z']<=69),'zone'] = 5

# #Zone 1
xz.loc[(xz['x']>=10)& (xz['z']>= 97)& (xz['z']<= 99),'zone'] = 1
# xz.loc[(xz['x']>=30) & (xz['x']<=39) & (xz['z']<=78) & (xz['z']>=73),'zone'] = 1
# xz.loc[(xz['x']>=17) & (xz['x']<=29) & (xz['z']<=82) & (xz['z']>=81),'zone'] = 1
# xz.loc[(xz['x']>=16) & (xz['x']<=29) & (xz['z']<=87) & (xz['z']>=86),'zone'] = 1

#Zone 4
xz.loc[(xz['x']<=34)& (xz['z']<=72) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=26)& (xz['z']<=73) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=25)& (xz['z']<=74) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=22)& (xz['z']<=77) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=19)& (xz['z']<=78) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=18)& (xz['z']<=79) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=14)& (xz['z']<=80) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=13)& (xz['z']<=82) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=12)& (xz['z']<=84) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=11)& (xz['z']<=85) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=10)& (xz['z']<=87) & (xz['z']>=70),'zone'] = 4

# #Zone 3
xz.loc[(xz['x']<=19) &(xz['z']<=96) & (xz['z']>=93),'zone'] = 3
xz.loc[(xz['x']<=20) &(xz['z']<=94) & (xz['z']>=93),'zone'] = 3
xz.loc[(xz['x']<=21) &(xz['z']<=92) & (xz['z']>=88),'zone'] = 3
xz.loc[(xz['x']>=12) & (xz['x']<=22) &(xz['z']<=90) & (xz['z']>=88),'zone'] = 3
xz.loc[(xz['x']>=11) & (xz['x']<=23) &(xz['z']<=87) & (xz['z']>=86),'zone'] = 3
xz.loc[(xz['x']>=12) & (xz['x']<=23) &(xz['z']==85) ,'zone'] = 3
xz.loc[(xz['x']>=13) & (xz['x']<=23) &(xz['z']<=84) & (xz['z']>=83),'zone'] = 3
xz.loc[(xz['x']>=14) & (xz['x']<=24) &(xz['z']==82),'zone'] = 3
xz.loc[(xz['x']>=14) & (xz['x']<=25) &(xz['z']==81),'zone'] = 3
xz.loc[(xz['x']>=15) & (xz['x']<=25) &(xz['z']==80),'zone'] = 3
xz.loc[(xz['x']>=19) & (xz['x']<=26) &(xz['z']==79),'zone'] = 3
xz.loc[(xz['x']>=20) & (xz['x']<=26) &(xz['z']==78),'zone'] = 3
xz.loc[(xz['x']>=23) & (xz['x']<=32) &(xz['z']<=77)&(xz['z']>=75),'zone'] = 3
xz.loc[(xz['x']>=26) & (xz['x']<=34) &(xz['z']<=74)&(xz['z']>=73),'zone'] = 3
xz.loc[(xz['x']>=35) & (xz['x']<=36) &(xz['z']<=73)&(xz['z']>=70),'zone'] = 3
xz.loc[(xz['x']>=35) & (xz['x']<=36) &(xz['z']<=73)&(xz['z']>=70),'zone'] = 3
xz.loc[(xz['x']>=36) & (xz['x']<=37) &(xz['z']<=71)&(xz['z']>=70),'zone'] = 3
xz.loc[(xz['x']>=10) &(xz['x']<=19)&(xz['z']<=98)&(xz['z']>=97),'zone'] = 3
xz.loc[(xz['x']<=10)&(xz['z']>=97)&(xz['z']<=98),'zone'] = 3
xz.loc[(xz['x']<=9)&(xz['z']>=97)&(xz['z']<=99),'zone'] = 3
xz.loc[(xz['x']<=8)&(xz['z']>=97)&(xz['z']<=100),'zone'] = 3
xz.loc[(xz['x']<=7)&(xz['z']>=97)&(xz['z']<=101),'zone'] = 3
xz.loc[(xz['x']<=6)&(xz['z']>=97)&(xz['z']<=102),'zone'] = 3
xz.loc[(xz['x']<=5)&(xz['z']>=97)&(xz['z']<=103),'zone'] = 3
xz.loc[(xz['x']<=4)&(xz['z']>=97)&(xz['z']<=104),'zone'] = 3
xz.loc[(xz['x']<=3)&(xz['z']>=97)&(xz['z']<=105),'zone'] = 3
xz.loc[(xz['x']<=2)&(xz['z']>=97)&(xz['z']<=106),'zone'] = 3
xz.loc[(xz['x']<=1)&(xz['z']>=97)&(xz['z']<=108),'zone'] = 3
xz.loc[(xz['x']==0) & (xz['z']>=97)&(xz['z']>=109),'zone'] = 3

Regions_Elk = xz.copy() 

# ##create a elevation chanfe 
# top_elev = np.linspace(1.586,
#                2.775,
#                num = 40,
#                endpoint = True,
#                retstep = False,
#                dtype = None)

# top_elev =np.reshape(top_elev, (1, np.size(top_elev)), order="F")
# np.shape(top_elev)

def create_structred_grids(zz, DZ):  # nx, ny, and nz -- resolution, zz -- elevation or DEM
    [nx,ny] = np.shape(zz)
    #set the max elevation to 'zz'
    #The floor of the scalar x is the largest integer i, such that i <= x. 
    zz = np.floor(zz)
    #
    zz_max = np.max(zz[:])
    zz_min = np.min(zz[:])
    zz_min = zz_min - 10
    zz_col = np.arange(zz_min, zz_max ,DZ)
    nz = np.size(zz_col)
    mat_id  = np.ones((nx,ny,nz))
    mat_id= mat_id.astype('int')
    mat_id_1d = np.reshape(mat_id,(nx*ny*nz,1), order="F")
    cell_id = np.reshape(np.arange(1, (nx*ny*nz) +1),(nx,ny,nz),order="F")
    cell_id= cell_id.astype('int')
    cell_id_1d = np.reshape(cell_id,(nx*ny*nz, ),order="F")
    surface_cell_id = np.zeros((nx,ny)) # top most cells that are active
    surface_cell_id = surface_cell_id.astype('int')
    for ii  in range(0, nx):
        for jj in range(0, ny):
            for  kk  in range(0, nz):
                if (zz_col[kk] - zz[ii,jj] > 0):
                    mat_id[ii, jj, kk:np.size(zz_col)] = 0
                    surface_cell_id[ii,jj] = cell_id[ii,jj,kk-1] # (k-1) is tested
                    break
                else:
                    surface_cell_id[ii,jj] = cell_id[ii,jj,nz-1]
    mat_id_1d =  np.reshape(mat_id,(nx*ny*nz, ),order="F")
    return mat_id_1d, cell_id_1d, surface_cell_id, nx, ny, nz, zz_min




def identify_bounday_cell_ids(nx, ny, xidx, yidx, znode):
    # cell_ids_idfy = []
    boundary_cells_ids_whole_face_temp = []
    for mm in range(0, np.size(xidx)):
        for nn in range(0, np.size(znode)):
            cell_ids_idfy = find_cell_id(nx,ny, xidx[mm],yidx[mm],znode[nn])  #cell ids in the east side
            boundary_cells_ids_whole_face_temp.append(cell_ids_idfy)
        # boundary_cells_ids_whole_face_temp = [int(i) for i in sublist for sublist in boundary_cells_ids_whole_face_temp]  Chris
        for i in range(0, np.size(boundary_cells_ids_whole_face_temp)):
            boundary_cells_ids_whole_face_temp[i] = int(boundary_cells_ids_whole_face_temp[i])
    return boundary_cells_ids_whole_face_temp



def boundary_cells_ids_whole_face(nx, ny, nz, mat_id_1d, direction):
    if direction is "East":
        xidx = boundary_cells_ids(nx, ny, nz).E_xidx # calling boundary_cells_ids():
        yidx = boundary_cells_ids( nx, ny, nz).E_yidx
        face_ids_value = Face().W # East Bboundary region will be facing West

    elif direction is "West":
        xidx = boundary_cells_ids(nx, ny, nz).W_xidx
        yidx = boundary_cells_ids( nx, ny, nz).W_yidx
        face_ids_value = Face().E

    elif direction is "North":
        xidx = boundary_cells_ids(nx, ny, nz).N_xidx
        yidx = boundary_cells_ids( nx, ny, nz).N_yidx
        face_ids_value = Face().S

    elif direction is "South":
        xidx = boundary_cells_ids(nx, ny, nz).S_xidx
        yidx = boundary_cells_ids( nx, ny, nz).S_yidx
        face_ids_value = Face().N

    znode = boundary_cells_ids( nx, ny, nz).znode
    boundary_cells_ids_whole_face_temp = identify_bounday_cell_ids(nx, ny, xidx, yidx, znode)
    boundary_cells_ids_whole_face_temp = np.array(boundary_cells_ids_whole_face_temp)
    boundary_cells_ids_only_active_cells = np.where(mat_id_1d[(boundary_cells_ids_whole_face_temp -1)] == 1)  # inactive cells should be not be changed in mat ID
    boundary_cells_ids_whole_face_direction = boundary_cells_ids_whole_face_temp[boundary_cells_ids_only_active_cells[0]]
    face_ids = np.zeros([np.size(boundary_cells_ids_whole_face_direction),]) + face_ids_value

    return boundary_cells_ids_whole_face_direction, face_ids



class boundary_cells_ids():
    def __init__(self, nx, ny, nz):

        self.E_xidx = range(1, nx + 1) # rows are changing, column is fixed for the East Boundary
        self.W_xidx = range(1, nx + 1)
        self.N_xidx =  (np.ones(ny)) * 1
        self.S_xidx = (np.ones(ny)) * nx



        self.E_yidx = (np.ones(nx)) * ny
        self.W_yidx = (np.ones(nx)) * 1
        self.N_yidx = range(1, ny + 1)
        self.S_yidx = range(1, ny + 1)




        self.znode =  np.arange(1, nz + 1)


        
class Face:
    def __init__(self):
        self.E = 2 #FACE [WEST, EAST, SOUTH, NORTH, BOTTOM, TOP] # East Bboundary region will be facing West
        self.W = 1
        self.N = 4
        self.S = 3
        self.T = 6
        self.B = 5
# print Face().E
        


def find_cell_id(nx, ny, xnode, ynode, znode):
    find_cell_id = []
    if xnode > nx:
        print("xnode can not be greater than x")
    elif ynode > ny:
        print("ynode can not be greater than y")
    else:
        find_cell_id = (nx*ny)*(znode -1) + nx*(ynode -1) + xnode

        # find_cell_id = find_cell_id.astype('int')
    return find_cell_id

    

    
def finding_plane_from_top(nx, ny, nz, my_surface_cell_id, ranking):
    """ ranking is like counting from top, ranking = 1 is first active control volumes, ranking 2 is second active control volumes and so on """
    top_surface_region1 = np.reshape(my_surface_cell_id,(np.size(my_surface_cell_id), ),order="F") - ranking*nx*ny
    face_ids = np.zeros([np.size(top_surface_region1),]) + Face().T
    return top_surface_region1, face_ids

mat_id_1d, cell_id_1d, surface_cell_id, nx, ny, nz, zz_min = create_structred_grids(top_elev, 0.1)
# h5file.close()
mat_id_original = mat_id_1d.copy()
h5_file_name = "Model_info_Elkhorn_Slough_50x10_ext.h5"

h5file = File(h5_file_name, mode ='w')


######### --------------------- East Face ######### 
[east_boundary, face_ids ] = boundary_cells_ids_whole_face(nx, ny, nz, mat_id_1d, "East")
dataset_name1 = "/Regions/east_boundary/Cell Ids"
h5dset = h5file.create_dataset(dataset_name1, data = east_boundary, dtype = np.uint64);

dataset_name2 = "/Regions/east_boundary/Face Ids"
h5dset = h5file.create_dataset(dataset_name2, data = face_ids, dtype = np.uint64)

    
######### --------------------- West Face ######### 

[west_boundary, face_ids ] = boundary_cells_ids_whole_face(nx, ny, nz, mat_id_1d, "West")
dataset_name1 = "/Regions/west_boundary/Cell Ids"
h5dset = h5file.create_dataset(dataset_name1, data = west_boundary, dtype = np.uint64);

dataset_name2 = "/Regions/west_boundary/Face Ids"
h5dset = h5file.create_dataset(dataset_name2, data = face_ids, dtype = np.uint64)
    
    
######### --------------------- Top Boundary #########      
[top_surface, face_ids] = finding_plane_from_top(nx, ny, nz, surface_cell_id, 1)

dataset_name1 = "/Regions/top_surface/Cell Ids"
h5dset = h5file.create_dataset(dataset_name1, data = top_surface, dtype = np.uint64)

dataset_name2 = "/Regions/top_surface/Face Ids"
h5dset = h5file.create_dataset(dataset_name2, data = face_ids, dtype = np.uint64) #### this region is for rain    


######### --------------------- Zone 1 #########   
zone1 = Regions_Elk[Regions_Elk.zone==1].index + 1
zone1 = np.array(zone1)

dataset_name1 = "/Regions/zone1/Cell Ids"
h5dset = h5file.create_dataset(dataset_name1, data = zone1, dtype = np.uint64)



######### --------------------- Zone 2 #########   
zone2 = Regions_Elk[Regions_Elk.zone==2].index + 1
zone2 = np.array(zone2)

dataset_name1 = "/Regions/zone2/Cell Ids"
h5dset = h5file.create_dataset(dataset_name1, data = zone2, dtype = np.uint64)



######### --------------------- Zone 3 #########   
zone3 = Regions_Elk[Regions_Elk.zone==3].index + 1
zone3 = np.array(zone3)

dataset_name1 = "/Regions/zone3/Cell Ids"
h5dset = h5file.create_dataset(dataset_name1, data = zone3, dtype = np.uint64)


######### --------------------- Zone 4 #########   
zone4 = Regions_Elk[Regions_Elk.zone==4].index + 1
zone4 = np.array(zone4)

dataset_name1 = "/Regions/zone4/Cell Ids"
h5dset = h5file.create_dataset(dataset_name1, data = zone4, dtype = np.uint64)


######### --------------------- Zone 5 #########   
zone5 = Regions_Elk[Regions_Elk.zone==5].index + 1
zone5 = np.array(zone5)

dataset_name1 = "/Regions/zone5/Cell Ids"
h5dset = h5file.create_dataset(dataset_name1, data = zone5, dtype = np.uint64)

######### --------------------- Specify Mat ids   #########   

specify_mat_id  = [zone1, zone2, zone3, zone4, zone5]
#specify_mat_id  = [zone1, zone2, zone3, zone4, zone5, east_boundary, west_boundary, top_surface] 
ncount = 1
for id_spec in specify_mat_id:
    #print(id_spec)
    mat_id_1d[id_spec - 1] = ncount
    mat_id_1d = mat_id_1d *mat_id_original
    #print(ncount)
    ncount = ncount + 1
    
######### --------------------- Cell ids    ######### 
dataset_name = "/Materials/Cell Ids"
h5dset = h5file.create_dataset(dataset_name, data = cell_id_1d, dtype=np.uint64)
  
######### --------------------- Mat ids    ######### 
dataset_name = "/Materials/Material Ids"
h5dset = h5file.create_dataset(dataset_name, data = mat_id_1d, dtype=np.uint64)
     
h5file.close()
    
    
    