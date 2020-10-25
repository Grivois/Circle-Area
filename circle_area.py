import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import animation
import numpy as np




fig, ax = plt.subplots(2, 2, figsize=(9, 8.5))

topend = 50
angle_list = []
int_angle = []
count = []
sidelengths = []
area_list = []

for x in range(3,topend):    #finds regular angle of an n-gon (where n = 3-topend)
    degrees = 180*(x-2)
    angle = degrees/x
    angle_list.append(angle)
    
    if angle.is_integer():    #checks if angle is an integer
        int_angle.append(angle)
        count.append(x)
        
    length = 2*np.cos(angle*np.pi/(180*2))
    height = np.sin(angle*np.pi/(180*2))
    sidelengths.append(length)
    area = 2*x*(1/2 * length/2 * height)
    area_list.append(area)
    
    if x == topend-1:    #approximates pi using the area of the largest n-gon
        print('pi is approx: ' + str(area))
    
#creates circle    
circle = mpatches.Circle([0.5,0.5], 0.5, 
                         ec="none", 
                         facecolor = 'r', 
                         alpha = 0.7
                         )
#creates polygon (triangle)
polygon = mpatches.RegularPolygon([0.5,0.5],3,0.5)

#Creates each frame for bottom right graph
def update_vector(i, polygon):
    ax[1,1].clear()
    polygon = mpatches.RegularPolygon([0.5,0.5],i+3,
                                      0.5, 
                                      alpha=0.5
                                      )
    ax[1,1].add_patch(circle)
    ax[1,1].add_patch(polygon)

    return polygon,

#hides x,y axis ticks for bottom right graph
ax[1,1].axes.xaxis.set_visible(False)
ax[1,1].axes.yaxis.set_visible(False)

#animates bottom right frame
anim = animation.FuncAnimation(fig, update_vector,
                               fargs = (polygon,),
                               frames=20,    #sets max n-gon in animation
                               interval=650,
                               ) 

#creates each graph    
ax[0,0].scatter(range(3,topend),angle_list)
ax[0,0].scatter(count,int_angle)
ax[0,0].set(xlabel='Number of Sides', ylabel= 'Degree of Angle')
ax[0,1].scatter(range(3,topend),area_list)
ax[0,1].set(xlabel='Number of Sides', ylabel= 'Area')
ax[1,0].scatter(range(3,topend),sidelengths)
ax[1,0].set(xlabel='Number of Sides', ylabel= 'Lenght of Side')
#sets title
fig.suptitle('Approaching the Area of a Circle', fontsize = 20)

plt.show()

# #**Uncomment to save file as mp4 or gif**
# import matplotlib
# matplotlib.use("Agg")
# # Set up formatting for the movie files
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=6, metadata=dict(artist='Me'), bitrate=1800)

   
# anim.save('app_circle_graphic.mp4', writer=writer)  #save as mp4, requires ffmpeg
# anim.save('app_circle_graphic.gif', writer='imagemagick', fps=6)  # save as gif requries, imagemagick and wand

