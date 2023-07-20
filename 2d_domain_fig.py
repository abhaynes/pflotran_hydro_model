## Load packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
import seaborn as sns

## Define coordinates
#returns num evenly spaced samples, calculated over the interval [start, stop]
#we want 40 for the x axis and 100 for the z axis
x = np.linspace(0,45,46)
z = np.linspace(0,99,100)

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

#Zone2
xz.loc[(xz['x']<=45) & (xz['z']>=70),'zone'] = 2

#Zone 5
xz.loc[(xz['x']<=45) & (xz['z']<=69),'zone'] = 5

# #Zone 1
xz.loc[(xz['z']>= 97),'zone'] = 1
# xz.loc[(xz['x']>=30) & (xz['x']<=39) & (xz['z']<=78) & (xz['z']>=73),'zone'] = 1
# xz.loc[(xz['x']>=17) & (xz['x']<=29) & (xz['z']<=82) & (xz['z']>=81),'zone'] = 1
# xz.loc[(xz['x']>=16) & (xz['x']<=29) & (xz['z']<=87) & (xz['z']>=86),'zone'] = 1

#Zone 4
xz.loc[(xz['x']<=24)& (xz['z']<=72) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=16)& (xz['z']<=73) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=15)& (xz['z']<=74) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=12)& (xz['z']<=77) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=9)& (xz['z']<=78) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=8)& (xz['z']<=79) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=4)& (xz['z']<=80) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=3)& (xz['z']<=82) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=2)& (xz['z']<=84) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=1)& (xz['z']<=85) & (xz['z']>=70),'zone'] = 4
xz.loc[(xz['x']<=0)& (xz['z']<=87) & (xz['z']>=70),'zone'] = 4

# #Zone 3
xz.loc[(xz['x']<=9) &(xz['z']<=96) & (xz['z']>=93),'zone'] = 3
xz.loc[(xz['x']<=10) &(xz['z']<=94) & (xz['z']>=93),'zone'] = 3
xz.loc[(xz['x']<=11) &(xz['z']<=92) & (xz['z']>=88),'zone'] = 3
xz.loc[(xz['x']>=2) & (xz['x']<=12) &(xz['z']<=90) & (xz['z']>=88),'zone'] = 3
xz.loc[(xz['x']>=1) & (xz['x']<=13) &(xz['z']<=87) & (xz['z']>=86),'zone'] = 3
xz.loc[(xz['x']>=2) & (xz['x']<=13) &(xz['z']==85) ,'zone'] = 3
xz.loc[(xz['x']>=3) & (xz['x']<=13) &(xz['z']<=84) & (xz['z']>=83),'zone'] = 3
xz.loc[(xz['x']>=4) & (xz['x']<=14) &(xz['z']==82),'zone'] = 3
xz.loc[(xz['x']>=4) & (xz['x']<=15) &(xz['z']==81),'zone'] = 3
xz.loc[(xz['x']>=5) & (xz['x']<=15) &(xz['z']==80),'zone'] = 3
xz.loc[(xz['x']>=9) & (xz['x']<=16) &(xz['z']==79),'zone'] = 3
xz.loc[(xz['x']>=10) & (xz['x']<=16) &(xz['z']==78),'zone'] = 3
xz.loc[(xz['x']>=13) & (xz['x']<=22) &(xz['z']<=77)&(xz['z']>=75),'zone'] = 3
xz.loc[(xz['x']>=16) & (xz['x']<=24) &(xz['z']<=74)&(xz['z']>=73),'zone'] = 3
xz.loc[(xz['x']>=25) & (xz['x']<=26) &(xz['z']<=73)&(xz['z']>=70),'zone'] = 3
xz.loc[(xz['x']>=25) & (xz['x']<=26) &(xz['z']<=73)&(xz['z']>=70),'zone'] = 3
xz.loc[(xz['x']>=26) & (xz['x']<=27) &(xz['z']<=71)&(xz['z']>=70),'zone'] = 3

Regions_Elk = xz.copy() 
colors = ['#2ca02c', '#8c564b', '#ffbb78',
                   '#c7c7c7', '#7f7f7f']
cmap = matplotlib.colors.ListedColormap(colors)
plt.rcParams.update({'font.size': 19})
plt.rcParams['font.family'] = 'Futura'
# sns.set_palette("husl", colorblind=True)
fig, ax = plt.subplots()
scatter = plt.scatter(xz['x'], xz['z'], s = 400, c = xz['zone'], cmap = cmap, marker = 's', edgecolors = 'black')

plt.title ('2D Model Domain of Elkhorn Slough Subsurface Model')
plt.xlabel('Length (0.50 m/cell)')
plt.ylabel('Depth (0.10 m/cell)')
# plt.yticks(np.arange(0, 99))
plt.ylim(0, 100)
plt.axis()

legend1 = plt.legend(*scatter.legend_elements(), markerscale=5, 
                     loc="lower right", title="Layers")
#change the marker size manually for both lines

ax.add_artist(legend1)
plt.tight_layout()  # Adjust spacing for better layout
plt.show()
# # /Users/ahaynes/Library/CloudStorage/GoogleDrive-ahaynes1@ucsc.edu/My Drive/UC Santa Cruz/even_year_talk/2023/2d_domain_fig


