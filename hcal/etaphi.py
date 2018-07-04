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
                  dest='file', default='/afs/cern.ch/work/b/bchiari1/work/hcal/samples/task9/first_sample/hcalTupleTree_1.root',
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

etas = TH1D('etas','etas',200,-99.5,99.5)
phis = TH1D('phis','phis',200,-0.5,100)

count = 0
total = chain.GetEntries()
for event in chain:
  count+=1
  percentDone = float(count) / float(total) * 100.0
  print('Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone ))

  for i in range(len(event.QIE11DigiIEta)):
    #print(' Depth : '+str(event.QIE11DigiDepth[i]))

    etas.Fill(event.QIE11DigiIEta[i])
    phis.Fill(event.QIE11DigiIPhi[i])

    #print(event.QIE11DigiIEta[i], event.QIE11DigiIPhi[i], event.QIE11DigiDepth[i])

  print()
  if count == 100: break 

print()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
