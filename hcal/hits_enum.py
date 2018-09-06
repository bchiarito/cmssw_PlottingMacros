from __future__ import print_function
from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys
import os
import glob
import fnmatch

parser = OptionParser()
parser.add_option('--out',
                  dest='out', default="output.root",
                  help='output file')
parser.add_option('--file',
                  dest='file',
                  help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--tree',
                  dest='treename', default="hcalTupleTree/tree",
                  help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False,
                  dest='dir',
                  help='treat file option as a directory instead of a single file')
(options, args) = parser.parse_args()

out_file = TFile(options.out, 'recreate')

chain = TChain(options.treename)
if (not options.dir):
  chain.Add(options.file)
elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

count = 0
total = chain.GetEntries()
for event in chain:
  count+=1
  percentDone = float(count) / float(total) * 100.0
  print('Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone ))

 # print('QIE11DigiIEta :')
 # for i in range(len(event.QIE11DigiIEta)):
 #   print(event.QIE11DigiIEta[i], end=' ')
 # print()
 # print ('QIE11DigiIPhi :')
 # for i in range(len(event.QIE11DigiIPhi)):
 #   print(event.QIE11DigiIPhi[i], end=' ')

  
  for i in range(len(event.QIE11DigiIEta)):
    print("Hit "+str(i+1)+":")
    print(' IEta : '+str(event.QIE11DigiIEta[i]))
    print(' IPhi : '+str(event.QIE11DigiIPhi[i]))
    print(' CapIDError : '+str(event.QIE11DigiCapIDError[i]))
    print(' Subdet : '+str(event.QIE11DigiSubdet[i]))
    print(' Depth : '+str(event.QIE11DigiDepth[i]))
    print(' RawID : '+str(event.QIE11DigiRawID[i]))
    print(' LinkError : '+str(event.QIE11DigiLinkError[i]))
    print(' Flags : '+str(event.QIE11DigiFlags[i]))
    print(' NTDC : '+str(event.QIE11DigiNTDC[i]))
    print(' TimeFC : '+str(event.QIE11DigiTimeFC[i]))
    print(' TimeTDC : '+str(event.QIE11DigiTimeTDC[i]))
    print(' TotFC : '+str(event.QIE11DigiTotFC[i]))
    print('CapIDs : ',end=' ')
    for j in range(len(event.QIE11DigiCapID[i])):
      print(event.QIE11DigiCapID[i][j],end=' ')
    print()
    print('ADCs : ',end=' ')
    for j in range(len(event.QIE11DigiADC[i])):
      print(event.QIE11DigiADC[i][j],end=' ')
    print()
    print('FCs : ',end=' ')
    for j in range(len(event.QIE11DigiFC[i])):
      print(event.QIE11DigiFC[i][j],end=' ')
    print()
    print('TDCs : ',end=' ')
    for j in range(len(event.QIE11DigiTDC[i])):
      print(event.QIE11DigiTDC[i][j],end=' ')
    print()
    print('SOIs : ',end=' ')
    for j in range(len(event.QIE11DigiSOI[i])):
      print(event.QIE11DigiSOI[i][j],end=' ')
    print()
    print()

    if i == 10: break
  
  break

print()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
