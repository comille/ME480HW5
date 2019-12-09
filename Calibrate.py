#!/usr/bin/env python
# coding: utf-8

# In[48]:


from solid import *
from solid.utils import *
import viewscad

r = viewscad.Renderer(openscad_exec='C:\Program Files\OpenSCAD\openscad.exe')


# In[58]:


c1 = cylinder(r=5,h=5)
c2 = cylinder(r=2.5,h=5)
c3 = c1-c2
r.render(c3)


# In[13]:


def donut(r_lg,r_sm):
    if r_lg<r_sm or r_lg<0 or r_sm<0:
        print('large diameter first, positive values only')
    else:
        c1 = cylinder(r=r_lg,h=5)
        c2 = cylinder(r=r_sm,h=5)
        c3 = c1-c2
        r.render(c3)
    
donut(7,3)


# In[61]:


d = [1,2,3,4]
t = .5
def overlapcylinders(d,t):    
    c1=cylinder(r=d[0]/2+t,h=1)
    c2=cylinder(r=d[0]/2,h=1)
    final=c1-c2
    sep=0
    for i in range(1,len(d)):
        r1=d[i]/2+t
        r2=d[i]/2
        c1=cylinder(r=r1,h=1)
        c2=cylinder(r=r2,h=1)
        c3 = c1-c2
        sep=sep+d[i-1]/2+(d[i]/2)+3/2*t
        c = translate([0,sep,0])(c3)
        final= final+c
    r.render(final)
overlapcylinders(d,t)    


# In[ ]:




