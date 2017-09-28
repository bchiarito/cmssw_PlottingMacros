from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys
import os
import glob
import fnmatch
import time

time_begin = time.time()

parser = OptionParser()
parser.add_option('--out', dest='out', default="output.root", help='output file')
parser.add_option('--file', dest='file', help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--tree', dest='treename', default="diphotonAnalyzer/fTree2", help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False, dest='dir', help='treat file option as a directory instead of a single file')
parser.add_option('--saveplot', dest='saveplot', help='')
parser.add_option('--reportevery', dest='reportevery', default=1000,help='')
parser.add_option('--title',dest="title", action='store')

parser.add_option('--lumi', dest='lumi', default=1.0,help='integrated lumi in pb^-1')
parser.add_option('--2016lumi', action='store_true', default=False, dest='lumi_set_to_2016', help='')
parser.add_option('--mcweight', action='store_true', default=False, dest='mcweight', help='')
parser.add_option('--smallrun',dest="smallrun", action='store')

parser.add_option('--tight', dest="tight", action='store_true', default=True)
parser.add_option('--cand', dest="tight", action='store_false')
(options, args) = parser.parse_args()

if options.lumi_set_to_2016:
  lumi = 41070.0
else:
  lumi = options.lumi

out_file = TFile(options.out, 'recreate')

if (not options.dir):
  chain = TChain(options.treename)
  chain.Add(options.file)
elif options.dir:
  chain = TChain(options.treename)
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

# book histos
hvm = TH2F('hvm' ,'high vs mid', 20,0,1, 20,0,1)
hvl = TH2F('hvl' ,'high vs low', 20,0,1, 20,0,1)
mvl = TH2F('mvl' ,'mid vs low', 20,0,1, 20,0,1)
pvl = TH2F('pvl' ,'photon vs larger', 20,0,1, 20,0,1)
pvs = TH2F('pvs' ,'photon vs smaller', 20,0,1, 20,0,1)
double = TH2F('double' ,'pT asymmetry', 20,0,1, 20,0,1)
triple = TH2F('triple' ,'pT asymmetry', 20,0,1, 20,0,1)

count = 0
total = chain.GetEntries()
for event in chain:
  if count % int(options.reportevery) == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  xs = 1.0
  N = 1.0
  if options.mcweight:
    xs = event.mcXS
    N = event.mcN
    if not options.smallrun == None:
      N = min(N, float(options.smallrun))

  for i in range(len(event.TwoProng_pt)):
    pt_photon = event.TwoProng_photon_pt[i]
    pt_track1 = event.TwoProng_CHpos_pt[i]
    pt_track2 = event.TwoProng_CHneg_pt[i]
    norm = pt_photon + pt_track1 + pt_track2
    ptg = pt_photon / norm
    pt1 = pt_track1 / norm
    pt2 = pt_track2 / norm

    high = max(ptg, pt1, pt2)
    low = min(ptg, pt1, pt2)
    if pt1 < high and pt1 > low:
      mid = pt1
    elif pt2 < high and pt2 > low:
      mid = pt2
    elif ptg < high and ptg > low:
      mid = ptg
    else:
      mid = low

    hvm.Fill(mid, high, xs*lumi/N)
    hvl.Fill(low, high, xs*lumi/N)
    mvl.Fill(low, mid, xs*lumi/N)

    pvl.Fill(max(pt1, pt2), ptg, xs*lumi/N)
    pvs.Fill(min(pt1, pt2), ptg, xs*lumi/N)

double.Add(pvl)
double.Add(pvs)
triple.Add(hvm)
triple.Add(hvl)
triple.Add(mvl)

time_end = time.time()
print "Elapsed Time: ", (time_end - time_begin)

c1 = TCanvas()
c1.cd()
double.GetYaxis().SetTitle('normalized photon pT')
double.GetXaxis().SetTitle('normalized smaller track pT, larger track pT')
double.SetStats(0)
if not options.title == None:
  double.SetTitle(options.title)
double.Draw('Colz')

c2 = TCanvas()
c2.cd()
triple.GetYaxis().SetTitle('normalized pT: high, high, mid')
triple.GetXaxis().SetTitle('normalized pT: mid, low, low')
triple.SetStats(0)
if not options.title == None:
  triple.SetTitle(options.title)
triple.Draw('Colz')

if not options.saveplot == None:
  c.SaveAs(options.saveplot)
else:
  raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
