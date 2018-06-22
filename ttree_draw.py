import os
import glob
import fnmatch
import math
import ROOT
import string
import sys
import time
from optparse import *

# command line options
time_begin = time.time()
usage = "%prog [options] sample -v VAR -b BINNING -c CUT."
parser = OptionParser(usage=usage)
parser.add_option('-v', '--var', '--varx', type='string', action='store', dest='var', help='')
parser.add_option('-b', '--bin', '--bins', type='string', metavar='NUM,LOW,HIGH', action='store', default='100,0,100', dest='binning', help='')
parser.add_option('-c', '--cut', type='string', action='store', default='', dest='cut', metavar='CUT_STRING', help='')
parser.add_option('--tree', type='string', action='store', dest='treename', default='diphotonAnalyzer/fTree2', metavar='PATH', help='path to tree in rootfiles')
parser.add_option('--mcweight', action='store_true', default=False, dest='mcweight', help='weight entries by XS and Ngen found in ttree as mcXS and mcN')
parser.add_option('--lumi', type='float', action='store', dest='lumi', default=1.0, help='integrated luminosity to scale to (pb^1)')
(options, args) = parser.parse_args()
sys.argv = [] # prevents ROOT from also reading options

# check args
if len(args) == 0:
  print "Must specify at least one sample as arugment"
  sys.exit()

# make TChain
path = args[0]
chain = ROOT.TChain(options.treename)
if fnmatch.fnmatch(path, "*.root"):
  chain.Add(path)
elif fnmatch.fnmatch(path, "*/"):
  rootfiles = []
  for root, dirnames, filenames in os.walk(path):
    for filename in fnmatch.filter(filenames, '*.root'):
      if (root[-6:len(root)] != 'failed'):
        rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

# make histogram
i1 = string.index(options.binning,',')
i2 = string.rindex(options.binning,',')
bins = int(options.binning[0:i1])
low = float(options.binning[i1+1:i2])
high = float(options.binning[i2+1:len(options.binning)])
hist = ROOT.TH1F("hist", "hist", bins, low, high)

lumi = options.lumi
draw_string = options.var + ">>"+"hist"
cut_string = "1" if (options.cut=="" or options.cut==None) else options.cut
if options.mcweight:
  cut_string = "("+cut_string+")*(mcXS*"+str(lumi)+"/mcN)"
chain.Draw(draw_string, cut_string, "goff")

# draw the histogram
c = ROOT.TCanvas()
c.cd()
hist.Draw()

# hold until user input
time_end = time.time()
print "Elapsed Time: ", "%.1f" % (time_end - time_begin), "sec"
raw_input("Press Enter to finish")
