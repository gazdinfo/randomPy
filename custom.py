#!/usr/bin/python
import sys;
from randgen import *;

# help
if '-h' in sys.argv:
  print 'A kovetkezo opciok hasznalhatoak';
  print '  -a   kivalaszthato, melyik algoritmust hasznalja';
  print '  -c   minden kiinduloertek kezi valo megadasa';
  print '  -n   a generalt szamok mennyisegenek megadasa (alapertelmezes: 1)';
  print '  -m   maximum- es minimumertek kezi megadasa (alapertelmezes: 100 es 0)';
  print '  -h   megjeleniti a sugot';
  sys.exit();

# alapertekek kezzel megadva
if '-c' in sys.argv:
  values['seed'] = int(input('seed = '));
  values['b'] = int(input('b = '));
  values['mod'] = int(input('modulo = '));
  values['mod1'] = int(input('mod1 = '));
  values['ts'] = int(input('additiv modszer tablamerete: '));
  values['fc'] = int(input('feedback elem sorszama: '));

N = 1;
if '-n' in sys.argv:
  N = int(input('N = '));

if '-m' in sys.argv:
  values['max'] = int(input('max (ezt az erteket nem mar nem erheti el a veletlen szam) = '));
  values['min'] = int(input('min = '));
  values['iv'] = values['max'] - values['min']; # a max es min ertek kozotti intervallum

alg = 2;
if '-a' in sys.argv:
  alg = int(input('Algoritmus: linearis (1), additiv (2) '));

# main
for i in range(0, N):
  if alg == 2:
    print adConRandom();
  else:
    print linConRandom();
