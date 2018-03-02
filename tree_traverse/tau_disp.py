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
                  dest='treename', default="diphotonAnalyzer/fTree2",
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

spread = TH1F("spread","spread",200,0,1000)
reco_high_spread = TH1F("reco_high_spread","spread",200,0,1000)
reco_low_spread = TH1F("reco_low_spread","spread",200,0,1000)


count = 0
total = chain.GetEntries()
for event in chain:
  if count % 10000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone)
  count += 1

  pts = []
  for i in range(len(event.GenTau_pt)):
    pts.append(event.GenTau_pt[i])
  etas = []
  for i in range(len(event.GenTau_pt)):
    etas.append(event.GenTau_eta[i])

  mineta = 99999.9
  maxeta = 0.0
  minpt = 99999999.9
  maxpt = 0.0
  for pt in pts:
    if pt < minpt:
      minpt = pt
    if pt > maxpt:
      maxpt = pt

  for eta in etas:
    if eta < mineta:
      minpt = pt
    if eta > maxeta:
      maxpt = pt
  
  ptspread = maxpt - minpt
  etaspread = maxeta - mineta
  spread.Fill(etaspread)

  if not event.nTwoProngs==1:
    continue
  
  lowspread = event.TwoProng_pt[0] - minpt
  highspread = event.TwoProng_pt[0] - maxpt
  reco_high_spread.Fill(lowspread)
  reco_low_spread.Fill(highspread)
  
# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
