from physics import distance
import config

def terminal_output(count):
    if(count%30 == 0): print("Distance btw Source and Listener:",distance(config.xS,config.xL,config.yS,config.yL))
    count+=1

def sound_out():
    pass