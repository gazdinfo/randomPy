#!/usr/bin/python
import sys;

# file megnyitasa
try:
  f = open(sys.argv[1]);
except IndexError:
  print 'Error: meg kell adni egy ervenyes fajlnevet';
  sys.exit();
except IOError:
  print 'Error: a megadott file nem letezik, vagy nem olvashato';
  sys.exit();

# intervallum valtozo ertekadas
try:
  iv = int(sys.argv[2]);
except IndexError:
  print 'Error: meg kell adni a maximumerteket';
  sys.exit();
except ValueError:
  print 'Error: a maximumaerteknek egesz szamnak kell lennie';
  sys.exit();

N = 0;
l = {}; # ures dictionary letrehozasa
for i in range(0, iv):
  l[i] = 0;

nonIntWarning = 0; # szamlalo: ha a fajl egy sora nem alakithato egesz szamma

# sorok beolvasasa, ertekek kiszamolasa
while True:
  rnum = f.readline().strip();

  if len(rnum) == 0: # fajlvege
    break;

  try:
    rnum = int(rnum);
  except ValueError:
    nonIntWarning += 1;
    continue;

  l[rnum] += 1;
  N += 1;

f.close(); # fajl lezarasa

# statisztika szamitasa
t = 0;

for i in range(0, iv):
  t += l[i] * l[i];

print (float(iv * t / N) - N);

if nonIntWarning > 0:
  print 'Warning: ' + str(nonIntWarning) + ' sor kimaradt, mert nem alakithato egeszszamma.';
