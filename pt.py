#!/usr/bin/env python
"""
Periodic table from command line :)
also, search and  print details of an element
using its name or symbol or atomic number.

Author: iconxicon@me.com
"""

import argparse
import csv

# Command line praser
#----------------------------
parser = argparse.ArgumentParser(description='Periodic table from command line.')
parser.add_argument('-N', action="store", default=None, dest="name",
                    help='Name of the element.')
parser.add_argument('-S', action="store", default=None, dest="symbol",
                    help='Symbol of the element.')
parser.add_argument('-n', action="store", default=None, dest="number",
                    help='Atomic number of the element.')
prm = parser.parse_args()

# Read in data
with open('pt_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        data.append(row)

# convert csv data to a list of dictionaries
# list index corresponds to atomic number
data_list = []
for i in range(1,len(data)):
    data_tmp = {}
    for j in range(20):
        data_tmp[data[0][j]] = data[i][j]
    data_list.append(data_tmp)

# do we want to print table or details of one element?
if prm.name == None and prm.symbol == None and prm.number == None:
    details = False
    print ""
    print "                        Periodic Table of Elements  "
    print ""
    print "    1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |"
    print "  -----                                                               -----"
    print "1 | H |                                                               |He |"
    print "  |---+----                                       --------------------+---|"
    print "2 |Li |Be |                                       | B | C | N | O | F |Ne |"
    print "  |---+---|                                       |---+---+---+---+---+---|"
    print "3 |Na |Mg |                                       |Al |Si | P | S |Cl |Ar |"
    print "  |---+---+---------------------------------------+---+---+---+---+---+---|"
    print "4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |"
    print "  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|"
    print "5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |"
    print "  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|"
    print "6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |"
    print "  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|"
    print "7 |Fr |Ra |ACT|Rf |Db |Sb |Bh |Hs |Mt |Ds |Rg |Cn |Nh |Fl |Mc |Lv |Ts |Og |"
    print "  -------------------------------------------------------------------------"
    print ""
    print "              -------------------------------------------------------------"
    print "   Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |"
    print "              |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|"
    print "   Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |"
    print "              -------------------------------------------------------------"
    print ""

# details
elif prm.name != None and prm.symbol == None and prm.number == None:
    details = True
    # find index by name
    a = [i['name'].lower() for i in data_list]
    try:
        index = a.index(prm.name.lower())
    except ValueError:
        print("Name not found")
        exit()

elif prm.name == None and prm.symbol != None and prm.number == None:
    details = True
    # find index by symbol
    a = [i['symbol'].lower() for i in data_list]
    try:
        index = a.index(prm.symbol.lower())
    except ValueError:
        print("symbol not found")
        exit()

elif prm.name == None and prm.symbol == None and prm.number != None:
    details = True
    # index starts from 0
    index = prm.number - 1

else:
    print "\n** ERROR: Please only use one search parameter.[name | symbol | atomic number]"


if details == True:
    # use index to print data
    print "%-28s %s %s" %("AtomicNumber",            ":",  data_list[index]["atomicNumber"])
    print "%-28s %s %s" %("Symbol",                  ":",  data_list[index]["symbol"])
    print "%-28s %s %s" %("Name",                    ":",  data_list[index]["name"])
    print "%-28s %s %s" %("AtomicMass",              ":",  data_list[index]["atomicMass"])
    print "%-28s %s %s" %("CpkHexColor",             ":",  data_list[index]["cpkHexColor"])
    print "%-28s %s %s" %("ElectronicConfiguration", ":",  data_list[index]["electronicConfiguration"])
    print "%-28s %s %s" %("Electronegativity",       ":",  data_list[index]["electronegativity"])
    print "%-28s %s %s" %("AtomicRadius",            ":",  data_list[index]["atomicRadius"])
    print "%-28s %s %s" %("IonRadius",               ":",  data_list[index]["ionRadius"])
    print "%-28s %s %s" %("VanDelWaalsRadius",       ":",  data_list[index]["vanDelWaalsRadius"])
    print "%-28s %s %s" %("IonizationEnergy",        ":",  data_list[index]["ionizationEnergy"])
    print "%-28s %s %s" %("ElectronAffinity",        ":",  data_list[index]["electronAffinity"])
    print "%-28s %s %s" %("OxidationStates",         ":",  data_list[index]["oxidationStates"])
    print "%-28s %s %s" %("StandardState",           ":",  data_list[index]["standardState"])
    print "%-28s %s %s" %("BondingType",             ":",  data_list[index]["bondingType"])
    print "%-28s %s %s" %("MeltingPoint",            ":",  data_list[index]["meltingPoint"])
    print "%-28s %s %s" %("BoilingPoint",            ":",  data_list[index]["boilingPoint"])
    print "%-28s %s %s" %("Density",                 ":",  data_list[index]["density"])
    print "%-28s %s %s" %("GroupBlock",              ":",  data_list[index]["groupBlock"])
    print "%-28s %s %s" %("YearDiscovered",          ":",  data_list[index]["yearDiscovered"])
