#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: pixki
# @Date:   2015-11-11 12:07:40
# @Last Modified by:   jairo
# @Last Modified time: 2015-11-24 23:05:40

import numpy as np
from scipy.stats import expon, erlang, rv_continuous
import matplotlib.pyplot as plt
import argparse
import sys

import numpy.random as mtrand


class hyperexp(rv_continuous):

    """An HyperExponential Random Variable		
    """

    def __init__(self, alpha=0.5, lambda1=1.0, lambda2=1.0):
        self.alpha = alpha
        self.lambda1 = lambda1
        self.lambda2 = lambda2

    def rvs(self, size=1):
        st="Generando {0} muestras con dist. HypExp([{1},{2}],[{3},{4}])"
        print st.format(size, self.alpha, 1-self.alpha, 
                        self.lambda1, self.lambda2)
        vsample = np.vectorize(self._single_sample)
        return np.fromfunction(vsample, (size,))

    def _single_sample(self, size):
        U1=mtrand.random()
        if U1 >= self.alpha:
            scale = self.lambda1
        else:
            scale = self.lambda2
        U2 = mtrand.random()
        return -np.log(U2) / scale

    def pdf(self, x):
        a = self.alpha*self.lambda1*np.exp(self.lambda1*-x)
        b = (1-self.alpha)*self.lambda2*np.exp(self.lambda2*-x)
        return a + b

    def ppf(self):
        return

    




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--stages', type=int, required=False,
                        help='Etapas de la distribución')
    parser.add_argument('-l', '--lambdap', type=float, required=True,
                        help='Parámetro lambda de cada distribución')
    parser.add_argument('-r', '--runs', type=int, required=True,
                        help='Ejecuciones a realizar por cada simulación')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='Archivo de salida para la grafica')
    parser.add_argument('-d', '--dist', type=str, required=True,
                        choices=['erlang', 'expon', 'hyperexp'],
                        help='Distribución a emplear para la simulación')
    args = parser.parse_args()
    msg = 'Distribución {3} con {0} etapas (lambda={1}) en {2} ejecuciones'
    print msg.format(args.stages, args.lambdap, args.runs, args.dist)
    fig, ax = plt.subplots(1, 1)
    if args.dist in 'erlang':
        if args.stages <= 0:
            print 'Error: se necesita un número válido de etapas'
            sys.exit(1)
        mean, var, skew, kurt = erlang.stats(args.stages, scale=args.lambdap,
                                             moments='mvsk')
        print "E[X]={0}, var(X)={1}".format(mean, var)
        x = np.linspace(erlang.ppf(0.00001, args.stages, scale=args.lambdap),
                        erlang.ppf(0.99999, args.stages, scale=args.lambdap),
                        num=1000)
        rv = erlang(args.stages, scale=args.lambdap)
        ax.plot(x, rv.pdf(x), 'r-', lw=5, alpha=0.6, label='Erlang PDF')
        # Generate random numbers with this distribution
        r = erlang.rvs(args.stages, scale=args.lambdap, size=args.runs)
        ax.hist(r, bins=20, normed=True, histtype='stepfilled', alpha=0.2)
    elif args.dist in 'expon':
        mean, var, skew, kurt = expon.stats(scale=args.lambdap, moments='mvsk')
        print "E[X]={0}, var(X)={1}".format(mean, var)
        x = np.linspace(expon.ppf(0.00001, scale=args.lambdap),
                        expon.ppf(0.99999, scale=args.lambdap),
                        num=1000)
        rv = expon(scale=args.lambdap)
        ax.plot(x, rv.pdf(x), 'r-', lw=5, alpha=0.6, label='Exponential PDF')
        # Generate random numbers with this distribution
        r = expon.rvs(scale=args.lambdap, size=args.runs)
        ax.hist(r, bins=20, normed=True, histtype='stepfilled', alpha=0.2)
    elif args.dist in 'hyperexp':
        print "HyperExponential RV"
        rv=hyperexp(0.5, 1.2, 1.3)
        values=rv.rvs(size=10)
        print values
        print "------------------------"
        x = np.linspace(0.00000001, 10.99999, num=1000)
        ax.plot(x, rv.pdf(x), 'r-', lw=5, alpha=0.6, label='HyperExponential PDF')

    plt.show()
if __name__ == '__main__':
    main()
