from sound_input import sound_input
from physics import distance,intensity_drop,distance_delay,update
#from config import xS,xL,yS,yL,Intensity,count
import config
from output import terminal_output,sound_out

#Select Audio File
sound_input()

#Run Infinitely
while(True):
    #prints every 30th run
    terminal_output(config.count)

    #intensity drop with distance(spherical source)
    intensity_drop()

    #delay with speed of sound
    distance_delay()

    #sound output
    sound_out()

    #update position
    dxS,dyS,dxL,dyL = update()
    config.xS += dxS
    config.yS += dyS
    config.xL += dxL
    config.yL += dyL