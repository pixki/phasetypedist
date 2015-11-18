#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: pixki
# @Date:   2015-11-11 12:07:40
# @Last Modified by:   Jairo Sánchez
# @Last Modified time: 2015-11-18 14:12:15

import numpy as np
from scipy.stats import expon, erlang
import matplotlib.pyplot as plt
import argparse
import sys


class hyperexp(rv_continuous):

    """ An HyperExponential Random Variable		
    """

    def _rvs(self):
        return

    def _pdf(self):
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

    plt.show()
if __name__ == '__main__':
    main()
