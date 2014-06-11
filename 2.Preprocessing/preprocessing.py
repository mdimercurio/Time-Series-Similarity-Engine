import numpy as np
import csv
from numpy.lib.recfunctions import append_fields

d = np.genfromtxt('../data/USGOVT.csv', delimiter=','
                     , skip_header=1, dtype=[('date', 'S10'), ('val', 'f8')]) 

d = d[d['date']>'2004-01-00']

## Compute z-score

mean = np.mean(d['val'])

std = np.std(d['val'])

zscore = (d['val']-mean)/std

d = append_fields(d, 'z', data=zscore)

d = d.data
