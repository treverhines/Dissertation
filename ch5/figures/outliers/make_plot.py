import numpy as np
import matplotlib.pyplot as plt
import pygeons
from matplotlib import colors

def trend(u1,t1):
  idx = np.isfinite(u1)
  u2 = u1[idx]
  t2 = t1[idx]
  G = np.array([np.ones(t2.shape[0]),t2]).T
  m = np.linalg.inv(G.T.dot(G)).dot(G.T).dot(u2)
  return m
  
xtick_dates = ['2011-01-01','2012-01-01','2013-01-01','2014-01-01']
xticks = [pygeons.mjd.mjd(i,'%Y-%m-%d') for i in xtick_dates]
xtick_labels = ['2011-01-01','2012-01-01','2013-01-01','2014-01-01']

c1 = colors.to_rgb('C0')
c1t = tuple(0.6 + 0.4*np.array(colors.to_rgb('C0')))
c2 = colors.to_rgb('C1')
c2t = tuple(0.6 + 0.4*np.array(colors.to_rgb('C1')))

# plot raw data
fig,ax = plt.subplots(figsize=(7,3.0))
pygeons.plot.plot._setup_ts_ax([ax])
ax.set_xticks(xticks)
ax.set_xticklabels(xtick_labels)
ax.tick_params(labelsize=10)
ax.set_xlim((55378.0,56839.0))
ax.set_ylim((-10.0,15.0))
ax.grid()

data = pygeons.io.io.dict_from_hdf5('data-2017-05-17.h5')
idx = (data['id'] == 'SC03').nonzero()[0][0]
lon = data['longitude'][idx]
lat = data['latitude'][idx]

t = data['time']
u = 1000*data['east'][:,idx]
us = 1000*data['east_std_dev'][:,idx]
m = trend(u,t)
u = u - m[0] - m[1]*t
ax.errorbar(t,u,us,marker='.',linestyle='None',color=c2,ecolor=c2t,ms=4.99)

data = pygeons.io.io.dict_from_hdf5('data.final.h5')
idx = (data['id'] == 'SC03').nonzero()[0][0]
t = data['time']
u = 1000*data['east'][:,idx]
us = 1000*data['east_std_dev'][:,idx]
u = u - m[0] - m[1]*t
ax.errorbar(t,u,us,marker='.',linestyle='None',color=c1,ecolor=c1t,ms=5.0)
ax.set_title('station SC03 (%.1f$^\mathregular{\circ}$W, %.1f$^\mathregular{\circ}$N)' % 
                 (-lon,lat),fontsize=10)
ax.set_ylabel('displacement [mm]',fontsize=10)
fig.tight_layout()
plt.savefig('outliers.pdf',format='pdf')
plt.show()
