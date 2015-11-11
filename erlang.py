#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: pixki
# @Date:   2015-11-11 12:07:40
# @Last Modified by:   pixki
# @Last Modified time: 2015-11-11 12:25:02

import numpy as np
from scipy.stats import expon,erlang
import matplotlib.pyplot as plt
import sys, argparse



def main():
	parser=argparse.ArgumentParser()
	parser.add_argument('-s', '--stages', type=int, required=True, help='Etapas de la distribución')
	parser.add_argument('-l', '--lambdap', type=float, required=True, help='Parámetro lambda de cada distribución')
	parser.add_argument('-r', '--runs', type=int, required=True, help='Ejecuciones a realizar por cada simulación')
	args=parser.parse_args()
	print 'Simulando distribución Erlang con {0} etapas (lambda={1}) en {2} ejecuciones'.format(args.stages, args.lambdap, args.runs)


	for run in range(args.runs):
		print "Run no. {0}...".format(run)


if __name__ == '__main__':
	main()