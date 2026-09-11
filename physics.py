from config import source_position,listener_position,source_velocity,c,Intensity,vx,vy,dt
import math

vector_source = (xS,yS) = source_position
vector_listener = (xL,yL) = listener_position

def distance(xS,xL,yS,yL):
    return math.hypot(xS-xL, yS-yL)

def radial_vel(source_velocity):
    d = math.hypot(xS - xL, yS - yL)
    r_hat_x = (xS - xL)/ d
    r_hat_y =  (yS - yL)/ d
    vx, vy = source_velocity
    vr = vx * r_hat_x + vy * r_hat_y
    return vr

def doppler_transform(f0,vr):
    fobs = f0*c/(c+vr)
    return fobs

def intensity_drop():
    new_intensity = Intensity/distance(xS,xL,yS,yL)**2
    return new_intensity

def distance_delay():
    return distance(xS,xL,yS,yL)/c

def update():
    return vx*dt,vy*dt,0,0