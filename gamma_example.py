#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: pixki
# @Date:   2015-11-11 12:40:52
# @Last Modified by:   pixki
# @Last Modified time: 2015-11-11 14:04:25

import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

#Calculate a few first moments:

a = 5
lambdap=2
mean, var, skew, kurt = gamma.stats(a, scale=lambdap, moments='mvsk')
print "E[X]={0}, var(X)={1}".format(mean, var)
#Display the probability density function (pdf):

x = np.linspace(gamma.ppf(0.00001, a, scale=lambdap), gamma.ppf(0.99999, a, scale=lambdap), num=1000)
ax.plot(x, gamma.pdf(x, a, scale=lambdap), 'r-', lw=5, alpha=0.6, label='gamma pdf')

#Alternatively, the distribution object can be called (as a function) to fix the shape, location and scale parameters. This returns a “frozen” RV object holding the given parameters fixed.
#Freeze the distribution and display the frozen pdf:

rv = gamma(a, scale=lambdap)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#Check accuracy of cdf and ppf:
#vals = gamma.ppf([0.001, 0.5, 0.999], a, scale=lambdap)
#np.allclose([0.001, 0.5, 0.999], gamma.cdf(vals, a, scale=lambdap))

#Generate random numbers:
r = gamma.rvs(a, size=100000, scale=lambdap)

#And compare the histogram:
ax.hist(r, bins=50, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()

