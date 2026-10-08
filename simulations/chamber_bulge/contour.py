"""Bulged chamber contour, reproduced from puffsat_impact_simulation @ 69d1f40
(crates/sweep --shape-40c / --efficiency-r3 and euler2d::vessel). make(0.075) returns
the wall radius r(z), the throat position, cylinder length, throat radius and volume."""
import math
R_PORT=None
def make(r_port):
    r_c,head,r_t=1.4,0.7,math.sqrt(106/160/math.pi)
    nose=(1.4-r_t)/math.tan(math.radians(12))
    def base(z,L):
        z_c,z_hi=head+L,head+L+nose
        if z<head:
            u=1-max(z,0)/head; return r_port+(r_c-r_port)*math.sqrt(1-u*u)
        if z<=z_c: return r_c
        s=min(max((z-z_c)/(z_hi-z_c),0),1); return r_t+(r_c-r_t)*(1-s)
    def vol(f,z_hi,n=4000):
        dz=z_hi/n; return sum(math.pi*f((k+.5)*dz)**2*dz for k in range(n))
    lo,hi=0,40
    for _ in range(80):
        mid=(lo+hi)/2
        if vol(lambda z:base(z,mid),head+mid+nose)<40: lo=mid
        else: hi=mid
    L=(lo+hi)/2; z_hi=head+L+nose
    def bulge(z,dr=1.6,z0=1.4,z1=2.8,ramp=0.5,ro=3.0):
        x=1-(z0-z)/ramp if z<z0 else (1-(z-z1)/ro if z>z1 else 1)
        x=min(max(x,0),1); return dr*0.5*(1-math.cos(math.pi*x))
    f=lambda z: base(z,L)+bulge(z)
    return f,z_hi,L,r_t,vol(f,z_hi)
