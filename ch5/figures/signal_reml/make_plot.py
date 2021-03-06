import numpy as np
from pygeons.io.parser import _get_field
import os
import matplotlib.pyplot as plt

def iqr(x):
  return np.subtract(*np.percentile(x,[75.0,25.0],interpolation='linear'))

msg = 'cov. function & direction & $\\lambda$  & $\\phi$   & $\\theta$  & diff. REML \\\\ \\hline\n'
#####################################################################
files = os.listdir('se-se-results')
sese_like = {'east':[],'north':[],'vertical':[]}
params0 = {'east':[],'north':[],'vertical':[]}
params1 = {'east':[],'north':[],'vertical':[]}
params2 = {'east':[],'north':[],'vertical':[]}
for f in files:
  buff = open('se-se-results/%s' % f,'r')
  content = buff.read()
  buff.close()
  content = content[content.find('REML RESULTS'):]
  content = content[content.find('network :'):]
  units = _get_field('parameter units',content).strip().split(',')
  for dir in ['east','north','vertical']:
    params = _get_field('optimal %s parameters' % dir,content).strip().split(',')
    if np.isfinite(float(params[0])):
      params0[dir] += [float(params[0])]

    if np.isfinite(float(params[1])):
      params1[dir] += [float(params[1])]

    if np.isfinite(float(params[2])):
      params2[dir] += [float(params[2])]

    likelihood_content = content[content.find('likelihood :'):]
    sese_like[dir] += [float(_get_field(dir,likelihood_content))]
    
east_p0 = params0['east']
north_p0 = params0['north']
vertical_p0 = params0['vertical']

east_p1 = params1['east']
north_p1 = params1['north']
vertical_p1 = params1['vertical']

east_p2 = params2['east']
north_p2 = params2['north']
vertical_p2 = params2['vertical']

msg += 'SE-SE & east   & %.5g $\pm$ %.5g km  & %.5g $\pm$ %.5g mm  & %.5g $\pm$ %.5g yr & 0.0 \\\\\n' % (
                                                                                      np.median(east_p2),iqr(east_p2),
                                                                                      np.median(east_p0),iqr(east_p0),
                                                                                      np.median(east_p1),iqr(east_p1))
msg += 'SE-SE & north  & %.5g $\pm$ %.5g km  & %.5g $\pm$ %.5g mm  & %.5g $\pm$ %.5g yr & 0.0 \\\\\n' % (
                                                                                       np.median(north_p2),iqr(north_p2),
                                                                                       np.median(north_p0),iqr(north_p0),
                                                                                       np.median(north_p1),iqr(north_p1))
#####################################################################
files = os.listdir('se-wen-results')
like = {'east':[],'north':[],'vertical':[]}
params0 = {'east':[],'north':[],'vertical':[]}
params1 = {'east':[],'north':[],'vertical':[]}
params2 = {'east':[],'north':[],'vertical':[]}
for f in files:
  buff = open('se-wen-results/%s' % f,'r')
  content = buff.read()
  buff.close()
  content = content[content.find('REML RESULTS'):]
  content = content[content.find('network :'):]
  units = _get_field('parameter units',content).strip().split(',')
  for dir in ['east','north','vertical']:
    params = _get_field('optimal %s parameters' % dir,content).strip().split(',')
    if np.isfinite(float(params[0])):
      params0[dir] += [float(params[0])]

    if np.isfinite(float(params[1])):
      params1[dir] += [float(params[1])]

    if np.isfinite(float(params[2])):
      params2[dir] += [float(params[2])]

    likelihood_content = content[content.find('likelihood :'):]
    like[dir] += [float(_get_field(dir,likelihood_content))]

east_p0 = params0['east']
north_p0 = params0['north']
vertical_p0 = params0['vertical']

east_p1 = params1['east']
north_p1 = params1['north']
vertical_p1 = params1['vertical']

east_p2 = params2['east']
north_p2 = params2['north']
vertical_p2 = params2['vertical']

east_like = np.array(like['east']) - np.array(sese_like['east'])
north_like = np.array(like['north']) - np.array(sese_like['north'])

plt.hist(east_like,50)
#plt.hist(north_like)
plt.show()

msg += 'SE-WEN & east   & %.5g $\pm$ %.5g km  & %.5g $\pm$ %.5g mm  & %.5g $\pm$ %.5g yr & %.5g $\pm$ %.5g \\\\\n' % (
                                                                                      np.median(east_p2),iqr(east_p2),
                                                                                      np.median(east_p0),iqr(east_p0),
                                                                                      np.median(east_p1),iqr(east_p1),
                                                                                      np.median(east_like),iqr(east_like))
msg += 'SE-WEN & north  & %.5g $\pm$ %.5g km  & %.5g $\pm$ %.5g mm  & %.5g $\pm$ %.5g yr & %.5g $\pm$ %.5g \\\\\n' % (
                                                                                       np.median(north_p2),iqr(north_p2),
                                                                                       np.median(north_p0),iqr(north_p0),
                                                                                       np.median(north_p1),iqr(north_p1),
                                                                                       np.median(north_like),iqr(north_like))
#####################################################################
files = os.listdir('se-ibm-results')
like = {'east':[],'north':[],'vertical':[]}
params0 = {'east':[],'north':[],'vertical':[]}
params1 = {'east':[],'north':[],'vertical':[]}
params2 = {'east':[],'north':[],'vertical':[]}
for f in files:
  buff = open('se-ibm-results/%s' % f,'r')
  content = buff.read()
  buff.close()
  content = content[content.find('REML RESULTS'):]
  content = content[content.find('network :'):]
  units = _get_field('parameter units',content).strip().split(',')
  for dir in ['east','north','vertical']:
    params = _get_field('optimal %s parameters' % dir,content).strip().split(',')
    if np.isfinite(float(params[0])):
      params0[dir] += [float(params[0])]

    if np.isfinite(float(params[1])):
      params1[dir] += [float(params[1])]

    if np.isfinite(float(params[2])):
      params2[dir] += [float(params[2])]

    likelihood_content = content[content.find('likelihood :'):]
    like[dir] += [float(_get_field(dir,likelihood_content))]

east_p0 = params0['east']
north_p0 = params0['north']
vertical_p0 = params0['vertical']

east_p1 = params1['east']
north_p1 = params1['north']
vertical_p1 = params1['vertical']

east_p2 = params2['east']
north_p2 = params2['north']
vertical_p2 = params2['vertical']

east_like = np.array(like['east']) - np.array(sese_like['east'])
north_like = np.array(like['north']) - np.array(sese_like['north'])

msg += 'SE-IBM & east   & %.5g $\pm$ %.5g km  & %.5g $\pm$ %.5g mm/yr$^{0.5}  & - & %.5g $\pm$ %.5g \\\\\n' % (
                                                                                      np.median(east_p2),iqr(east_p2),
                                                                                      np.median(east_p0),iqr(east_p0),
                                                                                      np.median(east_like),iqr(east_like))
msg += 'SE-IBM & north  & %.5g $\pm$ %.5g km  & %.5g $\pm$ %.5g mm/yr$^{0.5} & - & %.5g $\pm$ %.5g \\\\\n' % (
                                                                                      np.median(north_p2),iqr(north_p2),
                                                                                      np.median(north_p0),iqr(north_p0),
                                                                                      np.median(north_like),iqr(north_like))
print(msg)
