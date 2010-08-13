#!/usr/bin/python
import time;

# a kovetkezo szam generalasa linear congruential method hasznalataval
def linConRandom(s = False):
  global values;
  values['seed'] = ((values['seed'] * values['b']) + 1) % values['mod'];
  if s: # ha csak a seed kell
    return values['seed'];
  else:
    # return (int(values['seed'] / values['mod1']) % values['iv']) + values['min']; # itt elter a megoldas a jegyzetben szereplotol
    return ((int((int(values['seed'] / values['mod1']) * values['iv']) / values['mod1']))) % values['iv'] + values['min']; # ez a jegzyetben szereplo megoldas
# end of linConRandom()

# tabla generalasa az additive congruential method szamara
def randTableInit(ts):
  a = [];
  for j in range(0, ts):
    a.append(linConRandom(True));
  return a;
# end of randTableInit()

def initTable():
  global j;
  global table;
  j = linConRandom() % values['ts']; # veletlen pointer az additiv modszerhez
  table = randTableInit(values['ts']); # tabla generalasa az additiv modszerhez
# end of initTable()

# a kovetkezo szam generalasa additive congruential method hasznalataval
def adConRandom():
  global j; # a fuggveny kivulrol kapja meg a 'j' pointer erteket, hogy azt akar veletlenszam-kent is meg lehessen adni
  global table;
  if not j:
    initTable();

  j = (j + 1) % values['ts'];
  # a = randInit(ts); # ezzel minden ujabb szamkeresnel ujrageneralja a teljes tablat, igy meg veletlenszerubb lehet az eredmeny, de sokkal lasabb lesz a program
  table[j] = (table[(j + (values['ts'] - values['fc'] - 1)) % values['ts']] + table[(j + values['ts'] - 1) % values['ts']]) % values['mod'];
  return (int(table[j] / values['mod1']) % values['iv']) + values['min'];
  # return int((int(a[j] / mod1) * max) / mod1) # ez a jegyzetben szereplo megoldas
# end of adConRandom()

# main
# alapertekek
# automatikusan megadva
values = {};
values['seed'] = 1234567; # alapszam
values['b'] = 31415821; # konstans, amivel szorzunk
values['mod'] = 100000000; # modulo
values['mod1'] = 1000; # a szamok vegenek (left bits) levagasara
values['ts'] = 55; # table size for additive congruential method
values['fc'] = 31; # feedback-ken hasznalt szomszed sorszama
values['max'] = 100;
values['min'] = 0;

values['iv'] = values['max'] - values['min']; # a max es min ertek kozotti intervallum
j = False;
table = [];

# UNIX ido alapjan generalunk nehany szamot, hogy a szekvencia veletlenszeru helyen kezdodjon
t = int(time.time() * 10000) % 1000;
for i in range(0, t):
  linConRandom();
