import soundfile as sf
import numpy as np
import scipy

xS,yS = -100,-100
vx,vy = 0.1,0

xL,yL = 0,0

source_position = (xS,yS)
listener_position = (0,0)
source_velocity = (vx,vy)

c = 299792458

Intensity = 1

count = 0
dt = 0.1