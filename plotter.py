#!/usr/bin/env python
from __future__ import print_function
import os
import glob
import fnmatch
import math
import ROOT
import string
import sys
import time
from optparse import OptionParser
from optparse import OptionGroup
from optparse import SUPPRESS_HELP

time_begin = time.time()
usage = "Usage 1 (multiple samples): %prog [options] sample1 sample2 ... -v VAR -b BINNING -c CUT\n       Usage 2 (multiple variables): %prog [options] sample --var1 VAR1 --var2 VAR2 ... -b BINNING -c CUT\n       Usage 3 (mutliple samples from txt file input): %prog [options] samples.plot -v VAR -b BINNING -c CUT\nA sample arugment must be a root file, a directory which will be scanned for rootfiles, or a .dat file.\nEach line of the .dat file must be --sample xs N--.\nTo see the required format of .plot files, use <unfinised> command."
parser = OptionParser(usage=usage)

# Basic options
parser.add_option('-v', '--var', '--varx', type='string', action='store', dest='var', help='')
parser.add_option('-b', '--bin', '--bins', '--binsx', '--binx', type='string', metavar='NUM,LOW,HIGH', action='store', default='100,0,100', dest='binning', help='')
parser.add_option('-c', '--cut', type='string', action='store', default='', dest='cut', metavar='CUT_STRING', help='')
parser.add_option('--tree', type='string', action='store', dest='treename', default='Events', metavar='PATH', help='path to tree in rootfiles')
parser.add_option('--noplot', action='store_true', default=False, dest='noplot', help='do not plot anything, just gives cutflow')
parser.add_option('--savehist', type='string',action='store', dest='save', metavar='FILE.root', help='saves histograms')
parser.add_option('--save', type='string',action='store', dest='saveplot', metavar='FILE.ext', help='saves canvas')
parser.add_option('-q','--quiet', action='store_true', default=False, dest='quiet', help='less output')
parser.add_option('--verb', '--verbose', action='store_true', dest='verbose', help='more output')
parser.add_option('-n', '--num', type='int', action='store', default=-1, dest='nentries', metavar='MAX', help='max entries')
parser.add_option('--printevents', action='store_true', default=False, dest='printevents', help='print events that pass cut')

# multivar options
multivar_options = OptionGroup(parser, 'Multi-Variable Options', 'Setting --var1 --var2 ... --varN puts plotter in mutli-variable mode')
multivar_options.add_option('--var1', type='string', action='store', dest='var1', help=SUPPRESS_HELP)
multivar_options.add_option('--var2', type='string', action='store', dest='var2', help=SUPPRESS_HELP)
multivar_options.add_option('--var3', type='string', action='store', dest='var3', help=SUPPRESS_HELP)
multivar_options.add_option('--var4', type='string', action='store', dest='var4', help=SUPPRESS_HELP)
multivar_options.add_option('--var5', type='string', action='store', dest='var5', help=SUPPRESS_HELP)
multivar_options.add_option('--var6', type='string', action='store', dest='var6', help=SUPPRESS_HELP)
multivar_options.add_option('--var7', type='string', action='store', dest='var7', help=SUPPRESS_HELP)
multivar_options.add_option('--var8', type='string', action='store', dest='var8', help=SUPPRESS_HELP)

# 2D options
twod_options = OptionGroup(parser, '2D Plot Options', '')
twod_options.add_option('--vary', type='string', action='store', dest='vary', help='')
twod_options.add_option('--biny', '--binsy', type='string', action='store', dest='binningy', help='')
#twod_options.add_option('--scatter', action='store_true', default=False, dest='scatter', help='make a scatter plot in 2D instead of a histogram')
twod_options.add_option('--profile', default=False, action='store_true', dest='profile', help='make a profile plot instead of a 2D histogram')

# Visual options
visual_options = OptionGroup(parser, 'Visual Options', '')
visual_options.add_option('--title', type='string', action='store', dest='title', help='title')
visual_options.add_option('--xaxis', type='string', action='store', dest='xaxis', help='xaxis label')
visual_options.add_option('--yaxis', type='string', action='store', dest='yaxis', help='yaxis label')
visual_options.add_option('--legoff', action='store_true', default=False, dest='legoff', help='turns off the legend')
visual_options.add_option('--legleft', action='store_true', default=False, dest='legleft', help='legend on upper left instead of upper right')
visual_options.add_option('--stacked', action='store_true', default=False, dest='stacked', help='stacked histograms using THStack')
visual_options.add_option('--sidebyside', action='store_true', default=False, dest='sidebyside', help='stacked histograms using THStack and Draw("nostackb")')
visual_options.add_option('--noline', action='store_true', default=False, dest='noline', help='do not connect histogram with line')
visual_options.add_option('--errors', '--error',action='store_true', default=False, dest='errors', help='calls Sumw2() on all histograms')
visual_options.add_option('--logz', action='store_true', default=False, dest='logz', help='log scale on z')
visual_options.add_option('--logy', action='store_true', default=False, dest='logy', help='log scale on y')
visual_options.add_option('--logx', action='store_true', default=False, dest='logx', help='log scale on x')
visual_options.add_option('--scaled', action='store_true', default=False, dest='scale', help='scale to integral = 100')
visual_options.add_option('--mcweight', action='store_true', default=False, dest='mcweight', help='weight entries by XS and Ngen')
visual_options.add_option('--smallrun', action='store', dest='smallrun', metavar='N', help='correct mcN if small run')
visual_options.add_option('--lumi', type='float', action='store', dest='lumi', default=1.0, help='integrated luminosity to scale to (pb^1)')
visual_options.add_option('--2016lumi', action='store_true', default=False, dest='lumi_set_to_2016', help='set integreated luminiosity to 2016 total')
visual_options.add_option('--2015lumi', action='store_true', default=False, dest='lumi_set_to_2015', help='set integreated luminiosity to 2015 total')
visual_options.add_option('--vertical', type='float', action='store', dest='vertical', metavar='COOR', help='draw a vertical line')
visual_options.add_option('--horizontal', type='float', action='store', dest='horizontal', metavar='COOR', help='draw a horizontal line')
visual_options.add_option('--lega', type='string', action='store', dest='legenda', help=SUPPRESS_HELP)
visual_options.add_option('--legb', type='string', action='store', dest='legendb', help=SUPPRESS_HELP)

# Individual sample options
sample_options = OptionGroup(parser, 'Individual Sample Options', 'Set individual sample options with --treeN --errorN --legN --colorN.')
sample_options.add_option('--tree1', type='string', action='store', dest='treename1', help=SUPPRESS_HELP)
sample_options.add_option('--tree2', type='string', action='store', dest='treename2', help=SUPPRESS_HELP)
sample_options.add_option('--tree3', type='string', action='store', dest='treename3', help=SUPPRESS_HELP)
sample_options.add_option('--tree4', type='string', action='store', dest='treename4', help=SUPPRESS_HELP)
sample_options.add_option('--tree5', type='string', action='store', dest='treename5', help=SUPPRESS_HELP)
sample_options.add_option('--tree6', type='string', action='store', dest='treename6', help=SUPPRESS_HELP)
sample_options.add_option('--tree7', type='string', action='store', dest='treename7', help=SUPPRESS_HELP)
sample_options.add_option('--tree8', type='string', action='store', dest='treename8', help=SUPPRESS_HELP)
sample_options.add_option('--error1', action='store_true', dest='error1', help=SUPPRESS_HELP)
sample_options.add_option('--error2', action='store_true', dest='error2', help=SUPPRESS_HELP)
sample_options.add_option('--error3', action='store_true', dest='error3', help=SUPPRESS_HELP)
sample_options.add_option('--error4', action='store_true', dest='error4', help=SUPPRESS_HELP)
sample_options.add_option('--error5', action='store_true', dest='error5', help=SUPPRESS_HELP)
sample_options.add_option('--error6', action='store_true', dest='error6', help=SUPPRESS_HELP)
sample_options.add_option('--error7', action='store_true', dest='error7', help=SUPPRESS_HELP)
sample_options.add_option('--error8', action='store_true', dest='error8', help=SUPPRESS_HELP)
sample_options.add_option('--leg', '--leg1', type='string', action='store', dest='legend1', help=SUPPRESS_HELP)
sample_options.add_option('--leg2', type='string', action='store', dest='legend2', help=SUPPRESS_HELP)
sample_options.add_option('--leg3', type='string', action='store', dest='legend3', help=SUPPRESS_HELP)
sample_options.add_option('--leg4', type='string', action='store', dest='legend4', help=SUPPRESS_HELP)
sample_options.add_option('--leg5', type='string', action='store', dest='legend5', help=SUPPRESS_HELP)
sample_options.add_option('--leg6', type='string', action='store', dest='legend6', help=SUPPRESS_HELP)
sample_options.add_option('--leg7', type='string', action='store', dest='legend7', help=SUPPRESS_HELP)
sample_options.add_option('--leg8', type='string', action='store', dest='legend8', help=SUPPRESS_HELP)
sample_options.add_option('--color', '--color1', type='string', action='store', dest='color1', help=SUPPRESS_HELP)
sample_options.add_option('--color2', type='string', action='store', dest='color2', help=SUPPRESS_HELP)
sample_options.add_option('--color3', type='string', action='store', dest='color3', help=SUPPRESS_HELP)
sample_options.add_option('--color4', type='string', action='store', dest='color4', help=SUPPRESS_HELP)
sample_options.add_option('--color5', type='string', action='store', dest='color5', help=SUPPRESS_HELP)
sample_options.add_option('--color6', type='string', action='store', dest='color6', help=SUPPRESS_HELP)
sample_options.add_option('--color7', type='string', action='store', dest='color7', help=SUPPRESS_HELP)
sample_options.add_option('--color8', type='string', action='store', dest='color8', help=SUPPRESS_HELP)
sample_options.add_option('--xs1', type='float', action='store', dest='xs1', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--xs2', type='float', action='store', dest='xs2', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--xs3', type='float', action='store', dest='xs3', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--xs4', type='float', action='store', dest='xs4', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--xs5', type='float', action='store', dest='xs5', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--xs6', type='float', action='store', dest='xs6', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--xs7', type='float', action='store', dest='xs7', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--xs8', type='float', action='store', dest='xs8', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--num1', type='float', action='store', dest='num1', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--num2', type='float', action='store', dest='num2', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--num3', type='float', action='store', dest='num3', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--num4', type='float', action='store', dest='num4', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--num5', type='float', action='store', dest='num5', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--num6', type='float', action='store', dest='num6', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--num7', type='float', action='store', dest='num7', default=-1.0, help=SUPPRESS_HELP)
sample_options.add_option('--num8', type='float', action='store', dest='num8', default=-1.0, help=SUPPRESS_HELP)

parser.add_option_group(visual_options)
parser.add_option_group(twod_options)
parser.add_option_group(multivar_options)
parser.add_option_group(sample_options)
# get options
(options, args) = parser.parse_args()
# prevents ROOT from also reading options
sys.argv = []
# import colors
from ROOT import kRed
from ROOT import kWhite
from ROOT import kBlack
from ROOT import kGray
from ROOT import kRed
from ROOT import kGreen 
from ROOT import kBlue 
from ROOT import kYellow 
from ROOT import kMagenta 
from ROOT import kCyan 
from ROOT import kOrange 
from ROOT import kSpring 
from ROOT import kTeal 
from ROOT import kAzure 
from ROOT import kViolet 
from ROOT import kPink 

# check options
ind_treenames = False
if (not options.treename1==None) or \
   (not options.treename2==None) or \
   (not options.treename3==None) or \
   (not options.treename4==None) or \
   (not options.treename5==None) or \
   (not options.treename6==None) or \
   (not options.treename7==None) or \
   (not options.treename8==None):
  ind_treenames = True

ind_errors = False
if (not options.error1==None) or \
   (not options.error2==None) or \
   (not options.error3==None) or \
   (not options.error4==None) or \
   (not options.error5==None) or \
   (not options.error6==None) or \
   (not options.error7==None) or \
   (not options.error8==None):
  ind_errors = True

twod_mode = False
if (not options.vary==None) or \
   (not options.binningy==None):
  twod_mode = True

#if twod_mode and not options.profile:
#  options.legoff = True

multivar_mode = False
if (not options.var1==None) or \
   (not options.var2==None) or \
   (not options.var3==None) or \
   (not options.var4==None) or \
   (not options.var5==None) or \
   (not options.var6==None) or \
   (not options.var7==None) or \
   (not options.var8==None):
  multivar_mode = True

if multivar_mode and twod_mode:
  print("Multi-variable mode and 2D mode are not compatible")
  sys.exit()

if not multivar_mode and not twod_mode and not options.printevents and options.var == None:
  print("Must supply the name of the variable to be plotted with --var")
  sys.exit()

if twod_mode and (options.var==None or options.vary==None or options.binning==None or options.binningy==None):
  print("Must supply options --varx, --vary, --binsx, --binsy for use with 2D plotting mode")
  sys.exit()

if options.quiet and options.verbose:
  print("Output levels --quiet and --verbose cannot both be set")
  sys.exit()

# debug level  
debug = 1
if options.quiet:
  debug = 0
if options.verbose:
  debug = 2

# lumi
if options.lumi_set_to_2015:
  lumi = 2320.0
elif options.lumi_set_to_2016:
  lumi = 41010.0
else:
  lumi = options.lumi

# collection of samples
samples = []
if (args[0])[-5:len(args[0])] == ".plot":
  if debug >= 1:
    print("Grabbing input samples from", args[0])
  inputfile = open(args[0], 'r')
  for line in inputfile:
    line_list = line.split()
    sample = {}
    sample['tree'] = options.treename
    sample['error'] = options.errors
    sample['var'] = options.var
    sample['path'] = line_list[0]
    sample['label'] = line_list[1]
    sample['xs'] = float(line_list[2])
    sample['N'] = float(line_list[3])
    sample['color'] = None
    samples.append(sample)
elif not multivar_mode:
  for i in range(len(args)):
    sample = {}
    sample['path'] = args[i]
    if not ind_treenames:
      sample['tree'] = options.treename
    else:
      sample['tree'] = eval("options.treename"+str(i+1))
    if not ind_errors:
      sample['error'] = options.errors
    else:
      sample['error'] = eval("options.error"+str(i+1))
    sample['label'] = eval("options.legend"+str(i+1))
    sample['color'] = eval("options.color"+str(i+1))
    sample['var'] = options.var
    sample['xs'] = eval("options.xs"+str(i+1))
    sample['N'] = eval("options.num"+str(i+1))
    samples.append(sample)
else:
  if len(args) > 1:
    print("Can only use one sample if plotting multiple variables (with --var1, --var2, etc)")
    sys.exit()
  variables = []
  variables.append([options.var1, options.legend1, options.color1, options.xs1, options.num1])
  variables.append([options.var2, options.legend2, options.color2, options.xs2, options.num2])
  variables.append([options.var3, options.legend3, options.color3, options.xs3, options.num3])
  variables.append([options.var4, options.legend4, options.color4, options.xs4, options.num4])
  variables.append([options.var5, options.legend5, options.color5, options.xs5, options.num5])
  variables.append([options.var6, options.legend6, options.color6, options.xs6, options.num6])
  variables.append([options.var7, options.legend7, options.color7, options.xs7, options.num7])
  variables.append([options.var8, options.legend8, options.color8, options.xs8, options.num8])
  for var in variables:
    variable = {}
    variable['path'] = args[0]
    variable['tree'] = options.treename
    variable['error'] = options.errors
    if not var[1] == None:
      variable['label'] = var[1]
    else:
      variable['label'] = var[0]
    variable['color'] = var[2]
    variable['var'] = var[0]
    variable['test'] = '123'
    if not var[3] == None:
      variable['xs'] = var[3]
    else:
      variable['xs'] = -1.0
    if not var[4] == None:
      variable['N'] = var[4]
    else:
      variable['N'] = -1.0
    if not var[0] == None:
      samples.append(variable)

if len(samples) == 0:
  print("Must specify at least one sample as arugment")
  sys.exit()

# Make collection of TChains
for sample in samples:
  path = sample['path']
  ISrootfile = False
  ISdirectory = False
  ISinputfile = False
  if fnmatch.fnmatch(path, "*.root"):
    if debug >= 2:
      print("It appears", path, "is a rootfile")
    ISrootfile = True
  elif fnmatch.fnmatch(path, "*/"):
    if debug >= 2:
      print("It appears", path, "is a directory to traverse")
    ISdirectory = True
  elif fnmatch.fnmatch(path, "*.dat"):
    if debug >= 2:
      print("It appears", path, "is a text file of inputs")
    ISinputfile = True
  else:
    print("Can not recognize input", path, ", must end with /, .root, or .dat")
    sys.exit()

  if ISrootfile:
    chain = ROOT.TChain(sample['tree'])
    chain.Add(path)
    sample['entries'] = [[chain, -1.0, -1.0]]

  if ISdirectory:
    chain = ROOT.TChain(sample['tree'])
    rootfiles = []
    for root, dirnames, filenames in os.walk(path):
      for filename in fnmatch.filter(filenames, '*.root'):
        if (root[-6:len(root)] != 'failed'):
          rootfiles.append(os.path.join(root, filename))
    for rootfile in rootfiles:
      chain.Add(rootfile)
    sample['entries'] = [[chain, -1.0, -1.0]]

  if ISinputfile:
    sample['entries'] = []
    inputfile = open(path, 'r')
    for line in inputfile:
      line_list = line.split()
      # Get name, xs, and num from line
      if len(line_list) == 1:
        path_to_file = line_list[0]
        xs = -1.0
        N = -1.0
        treename = sample['tree']
      if len(line_list) == 2:
        path_to_file = line_list[0]
        xs = -1.0
        N = float(line_list[1])
        treename = sample['tree']
      if len(line_list) == 3:
        path_to_file = line_list[0]
        xs = float(line_list[1])
        N = float(line_list[2])
        if not options.nentries == -1:
          N = min(N, options.nentries)
        treename = sample['tree']
      if len(line_list) == 4:
        path_to_file = line_list[0]
        xs = float(line_list[1])
        N = float(line_list[2])
        if not options.nentries == -1:
          N = min(N, options.nentries)
        treename = line_list[3]
      if len(line_list) == 0 or len(line_list) > 4:
        print("couldn't parse this line from input file", path)
        print(line)
        continue
      # add files to chain
      chain = ROOT.TChain(treename)      
      if fnmatch.fnmatch(path_to_file, "*.root"):
        chain.Add(path_to_file)
      elif fnmatch.fnmatch(path_to_file, "*/"):
        rootfiles = []
        for root, dirnames, filenames in os.walk(path_to_file):
          for filename in fnmatch.filter(filenames, '*.root'):
            rootfiles.append(os.path.join(root, filename))
        for rootfile in rootfiles:
          chain.Add(rootfile)
      else:
        # line doesn't make sense
        print("couldn't parse this line from input file", path)
        print(line)
      sample['entries'].append([chain, xs, N])
     
# Print matching events
if options.printevents:
  num_selected_events = 0
  num_selected_events_dumped = 0
  continue_dumping_events = True
  for entry in sample['entries']:
    chain = entry[0]
    selected_tree = chain.CopyTree(options.cut)
    num_selected_events += selected_tree.GetEntries()
    for event in selected_tree:
      if continue_dumping_events:
        #print("", "run ", event.runNum, " lumi ", event.lumiNum, " event", event.eventNum)
        print("", "run ", event.run, " lumi ", event.luminosityBlock, " event", event.event)
        #print("  ", eval("event.event"))
        twoprongvec = ROOT.Math.PtEtaPhiMVector(event.TwoProng_pt[event.CBL_RecoPhi_twoprongindex], event.TwoProng_eta[event.CBL_RecoPhi_twoprongindex], event.TwoProng_phi[event.CBL_RecoPhi_twoprongindex], event.TwoProng_mass[event.CBL_RecoPhi_twoprongindex])
        photonvec = ROOT.Math.PtEtaPhiMVector(event.Photon_pt[event.CBL_RecoPhi_photonindex], event.Photon_eta[event.CBL_RecoPhi_photonindex], event.Photon_phi[event.CBL_RecoPhi_photonindex], event.Photon_mass[event.CBL_RecoPhi_photonindex])
        print("  ", event.CBL_RecoPhi_mass, event.Photon_pt[event.CBL_RecoPhi_photonindex], event.TwoProng_pt[event.CBL_RecoPhi_twoprongindex])
        print("  ", event.CBL_RecoPhi_mass, photonvec.Pt(), twoprongvec.Pt())
        print("  ", ROOT.Math.VectorUtil.DeltaR(twoprongvec, photonvec))
        print("  Phi:", event.CBL_RecoPhi_pt, event.CBL_RecoPhi_eta, event.CBL_RecoPhi_phi, event.CBL_RecoPhi_mass)
        print("  photon:", photonvec.Pt(), photonvec.Eta(), photonvec.Phi(), photonvec.M())
        print("  photon:", event.CBL_RecoPhi_Photon_pt, event.CBL_RecoPhi_Photon_eta, event.CBL_RecoPhi_Photon_phi, event.CBL_RecoPhi_Photon_mass)
        print("  twoprong:", twoprongvec.Pt(), twoprongvec.Eta(), twoprongvec.Phi(), twoprongvec.M())
        print("  twoprong:", event.CBL_RecoPhi_TwoProng_pt, event.CBL_RecoPhi_TwoProng_eta, event.CBL_RecoPhi_TwoProng_phi, event.CBL_RecoPhi_TwoProng_mass)
        print("  twoprong index:", event.CBL_RecoPhi_twoprongindex)
        print("  ntwoprong:", event.nTwoProng)
        print("  :", event.CBL_Region)
        for n in range(event.nTwoProng):
          print("    twoprong:", n, event.TwoProng_isTight[n], event.TwoProng_pt[n])
          
        num_selected_events_dumped += 1
        if num_selected_events_dumped % 20 == 0:
          inp = 'q'
          #inp = raw_input("[Enter] to continue printing events, 'q' to quit: ")
          if inp == 'q':
            continue_dumping_events = False
      else:
        break
  if debug>=1:
    print("Events matching cut: ", num_selected_events)
  time_end = time.time()
  if debug>=1:
    print("Elapsed Time: ", "%.1f" % (time_end - time_begin), "sec")
  sys.exit() 
    
# Draw into histograms from Chain
if debug>=2:
  print("Drawing into histogram...")

i1 = string.index(options.binning,',')
i2 = string.rindex(options.binning,',')
bins = int(options.binning[0:i1])
low = float(options.binning[i1+1:i2])
high = float(options.binning[i2+1:len(options.binning)])
if twod_mode:
  i1x = string.index(options.binning,',')
  i2x = string.rindex(options.binning,',')
  binsx = int(options.binning[0:i1x])
  lowx = float(options.binning[i1x+1:i2x])
  highx = float(options.binning[i2x+1:len(options.binning)])

  i1y = string.index(options.binningy,',')
  i2y = string.rindex(options.binningy,',')
  binsy = int(options.binningy[0:i1y])
  lowy = float(options.binningy[i1y+1:i2y])
  highy = float(options.binningy[i2y+1:len(options.binningy)])

count = 0
sumcount = 0
for sample in samples:
  sumcount += 1
  if not twod_mode:
    hist_sum = ROOT.TH1D("hist"+"_sum_"+str(sumcount), "hist", bins, low, high)
  elif options.profile:
    hist_sum = ROOT.TProfile("hist"+"_sum_"+str(sumcount), "hist", bins, low, high, lowy, highy)
  else:
    hist_sum = ROOT.TH2D("hist"+"_sum_"+str(sumcount), "hist", binsx, lowx, highx, binsy, lowy, highy)
  for entry in sample['entries']:
    chain = entry[0]
    xs = entry[1]
    N = entry[2]
    # if xs and N not specified from .dat input, try to take from command line options
    if (xs == -1.0 and N == -1.0):
      xs = sample['xs']
      N = sample['N']
    count += 1
    if not twod_mode:
      hist = ROOT.TH1D("hist"+"_"+str(count), "hist", bins, low, high)
    elif options.profile:
      hist = ROOT.TProfile("hist"+"_"+str(count), "hist", binsx, lowx, highx, lowy, highy)
    else:
      hist = ROOT.TH2D("hist"+"_"+str(count), "hist", binsx, lowx, highx, binsy, lowy, highy)
    draw_string = options.vary+":"+options.var if twod_mode else \
                  sample['var']
    draw_string = draw_string + ">>"+"hist"+"_"+str(count)
    cut_string = "1" if (options.cut=="" or options.cut==None) else options.cut
    option_string = "goff"
    if options.profile: option_string += " prof"
    if options.mcweight and not options.smallrun == None:
      cut_string = "("+cut_string+")*(mcXS*"+str(lumi)+"/"+str(int(options.smallrun))+")"
    elif options.mcweight and options.smallrun == None:
      cut_string = "("+cut_string+")*(mcXS*"+str(lumi)+"/mcN)"
    if options.nentries == -1:
      chain.Draw(draw_string, cut_string, option_string)
      if debug>=2:
        print("Draw String: ", draw_string, cut_string, option_string)
    else:
      n = chain.Draw(draw_string, cut_string, option_string, options.nentries)
    entry.append(hist)
    if not(xs == -1.0 or N == -1.0):
      if debug>=2: print('scaling with', xs, lumi, N)
      hist.Scale(xs*lumi/N)
    hist_sum.Add(hist)
  sample['summed_hist'] = hist_sum
  #if options.scatter:
  #  sample['graph'] = ROOT.TGraph(n, chain.GetV1(), chain.GetV2())
 
# Print Summary
count = 1
for sample in samples:
  hist = sample['summed_hist']
  if debug>=1:
    print("Entries " + str(count) + "  : ", int(hist.GetEntries()), " , total : " + str(hist.Integral()), end='')
  if not twod_mode:
    if not int(hist.GetBinContent(0)) == 0:
      if debug>=1:
        print(" : Underflow " + " - ", int(hist.GetBinContent(0)), end='')
    if not int(hist.GetBinContent(bins+1)) == 0:
      if debug>=1:
        print(" : Overflow " + " - ", int(hist.GetBinContent(bins+1)), end='')
  if debug>=1:
    if options.noplot:
      print("\nTotal Integral " + str(count) + "  : ", int(hist.Integral(0,hist.GetNbinsX()+1)), "| Uncer : " + str(hist.GetBinError(1)), end='')
    print("")
  count += 1

if options.noplot:
  time_end = time.time()
  if debug>=1:
    print("Elapsed Time: ", "%.1f" % (time_end - time_begin), "sec")
  sys.exit()

if not options.save == None:
  outfilename = options.save
  if debug>=2:
    print("Writing histogram(s) to file " + outfilename + ".root...")
  outputfile = ROOT.TFile(outfilename+'.root',"recreate")
  outputfile.cd()
  for sample in samples:
    sample['summed_hist'].Write()
  if options.stacked or options.sidebyside:
    hs.Write()
  outputfile.Close()

  time_end = time.time()
  if debug>=1:
    print("Elapsed Time: ", "%.1f" % (time_end - time_begin), "sec")
  sys.exit()
  
if debug>=2:
  print("Plotting...")
c = ROOT.TCanvas()
c.cd()
if options.logz:
  c.SetLogz()
if options.logy:
  c.SetLogy()
if options.logx:
  c.SetLogx()
colorcount = 1
for sample in samples:
  hist = sample['summed_hist']
  # Color
  if sample['color'] == None:
    hist.SetLineColor(colorcount)
    hist.SetMarkerColor(colorcount)
    hist.SetFillColor(colorcount if (options.stacked or options.sidebyside) else 0)
    colorcount+=1
  else:
    exec('hist.SetLineColor(' + sample['color'] + ')')
    exec('hist.SetMarkerColor(' + sample['color'] + ')')
    if options.stacked or options.sidebyside:
      exec('hist.SetFillColor(' + sample['color'] + ')')
    else:
      hist.SetFillColor(0)
  # Width
  hist.SetLineWidth(1)
  # Stats
  #ROOT.gStyle.SetOptStat(110000)
  #hist.SetStats(1)
  hist.SetStats(0)
  # Scale
  if options.scale:
    if not hist.Integral() == 0:
      hist.Scale(100.0/hist.Integral())

if options.stacked or options.sidebyside:
  hs = ROOT.THStack('hs','')
  for sample in samples:
    hist = sample['summed_hist']
    hs.Add(hist)
  if options.save == None:
    if options.stacked:
      hs.Draw('hist')
    elif options.sidebyside:
      hs.Draw('hist nostackb')

# Maximum
maximum = 0
minimum = 1.0
for sample in samples:
  hist = sample['summed_hist']
  maximum = max(maximum, hist.GetMaximum())
  if not hist.GetMaximum() == 0: minimum = min(minimum, hist.GetMaximum())
for sample in samples:
  hist = sample['summed_hist']
  if options.logy:
    hist.SetMaximum(maximum*4)
    hist.SetMinimum(minimum/1000.0)
  else:
    hist.SetMaximum(maximum*1.15)
    hist.SetMinimum(0)

# Labels
for sample in samples:
  hist = sample['summed_hist']
  title = ''
  xaxis = ''
  yaxis = ''
  # Title
  if not options.title == None:
    title = options.title
  else:
    if not twod_mode and not multivar_mode:
      title = options.var
    elif not twod_mode and multivar_mode:
      title = sample['path']
    else:
      if options.cut == None or options.cut == '':
        title = options.var + " vs " + options.vary
      else:
        title = options.cut
  if not twod_mode:
    # X axis
    if multivar_mode:
      xaxis = ""
    else:
      xaxis = options.var + " w/ " + options.cut if options.cut==None else options.var
    if not options.xaxis == None:
      xaxis = options.xaxis
    # Y axis
    if not options.yaxis == None:
      yaxis = options.yaxis
    elif options.scale:
      yaxis = "Scaled to Integral 100"
    else:
      yaxis = "Events"
  else:
    # X axis
    if not options.xaxis == None:
      xaxis = options.xaxis
    else:
      xaxis = options.var
    # Y axis
    if not options.yaxis == None:
      yaxis = options.yaxis
    else:
      yaxis = options.vary
  hist.SetTitle(title)
  hist.GetXaxis().SetTitle(xaxis)
  hist.GetYaxis().SetTitle(yaxis)
  if options.stacked or options.sidebyside:
    hs.SetTitle(title)
    hs.GetXaxis().SetTitle(xaxis)
    hs.GetYaxis().SetTitle(yaxis)
    
# Draw()
if options.save == None:
  if twod_mode:
    ROOT.gStyle.SetPalette(55)
  if options.stacked or options.sidebyside:
    if options.stacked:
      hs.Draw('hist')
    elif options.sidebyside:
      hs.Draw('hist nostackb')
  else:
    for sample in samples:
      hist = sample['summed_hist']
      if options.noline:
        draw_option = 'same'
      else:
        draw_option = 'hist same'
      if twod_mode:
        draw_option += ' Colz'
      if twod_mode and options.profile:
        draw_option = ''
      if sample['error']:
        draw_option += ' e'
      hist.Draw(draw_option)
  # Legend
  legendtype = ""
  if options.stacked or options.sidebyside or twod_mode:
    legendtype = "f"
  else:
    legendtype = "l"
  if not options.legleft:
    leg = ROOT.TLegend(0.7, 0.9-(0.06*len(samples)), 0.9, 0.9)
  else:
    leg = ROOT.TLegend(0.1, 0.9-(0.1*len(samples)), 0.35, 0.9)
  extra = False
  for sample in samples:
    hist = sample['summed_hist']
    if sample['label'] == None:
      leg.AddEntry(hist, sample['path'], legendtype)
    else:
      leg.AddEntry(hist, sample['label'], legendtype)  
    if not extra:
      if not options.legenda == None:
        leg.AddEntry('', options.legenda, '')
      if not options.legendb == None:
        leg.AddEntry('', options.legendb, '')
      extra = True
  if not options.legoff:
    leg.Draw("same")
  c.Modified()
# optional lines
if not options.vertical == None:
  pos = options.vertical
  maxi = samples[0]['summed_hist'] if not (options.stacked or options.sidebyside) else hs
  vert_line = ROOT.TLine(pos, 0, pos, maxi)
  vert_line.Draw("same")
if not options.horizontal == None:
  pos = options.horizontal
  maxi = samples[0]['summed_hist'] if not (options.stacked or options.sidebyside) else hs
  horz_line = ROOT.TLine(0, pos, maxi, pos)
  horz_line.Draw("same")

time_end = time.time()
if debug>=1:
  print("Elapsed Time: ", "%.1f" % (time_end - time_begin), "sec")

if not options.saveplot == None:
  if debug>=2:
    print("Writing plot to file " + options.saveplot + "...")
  filename = options.saveplot
  c.SaveAs(filename)
  sys.exit()

# After plot Commands
draws = []
if options.stacked:
  draws.append([hs, 'hist same'])
elif options.sidebyside:
  draws.append([hs, 'hist same nostackb'])
else:
  for sample in samples:
    if twod_mode:
      draws.append([sample['summed_hist'],'same Colz'])
    else:
      draws.append([sample['summed_hist'],'same'])
if not options.legoff:
  draws.append([leg, 'same'])

if options.stacked or options.sidebyside:
  hist = hs
else:
  hist = samples[0]['summed_hist']

cmd = "start"
while not cmd == "":
  # parse input
  inp = raw_input("[Enter] to finish, 'options' to see options: ")
  i = string.find(inp,' ')
  if i==-1:
    cmd = inp
    opt = ""
  else:
    cmd = inp[0:i]
    opt = inp[i+1:len(inp)]

  # begin commands
  if cmd == "save" or cmd == "saveas":
    if opt=="":
      sys.stdout.write(' ')
      sys.stdout.flush()
      filename = raw_input("Enter filename: ")
      c.SaveAs(filename)
    else:
      c.SaveAs(opt)
  elif cmd == "savehist":
    if opt=="":
      sys.stdout.write(' ')
      sys.stdout.flush()
      filename = raw_input("Enter filename: ")
      rootfile = ROOT.TFile(filename, "CREATE")
      rootfile.cd()
    else:
      rootfile = ROOT.TFile(opt, "CREATE")
      rootfile.cd()
    for sample in samples:
      sample['summed_hist'].Write()
    rootfile.Close()
  elif cmd == "title":
    if opt=="":
      sys.stdout.write(' ')
      sys.stdout.flush()
      new_title = raw_input("Enter title for plot: ")
    else:  
      new_title = opt
    hist.SetTitle(new_title)
    c.Modified()
  elif cmd == "fit":
    if opt=="":
      print("Must supply second argument to", cmd)
      continue
    hist.Fit(opt)
    c.Modified()
    for draw in draws:
      draw[0].Draw(draw[1])
    if not options.legoff:
      leg.Draw("same")
  elif cmd == "vertical":
    if opt=="":
      print("Must supply second argument to", cmd)
      continue
    pos = float(opt)
    vert_line = ROOT.TLine(pos, 0, pos, hist.GetMaximum())
    vert_line.Draw("same")
    if not options.legoff:
      leg.Draw("same")
    draws.append(vert_line)
  elif cmd == "horizontal":
    if opt=="":
      print("Must supply second argument to", cmd)
      continue
    pos = float(opt)
    horz_line = ROOT.TLine(0, pos, high, pos)
    horz_line.Draw("same")
    if not options.legoff:
      leg.Draw("same")
    draws.append(horz_line)
  elif cmd == "integrate":
    low = opt.split()[0]
    high = opt.split()[1]
    print(low, high)
    
  elif cmd == "options":
    print("save FILENAME       saves current canvas, optionally with supplied name\n" +\
          "saveas              alias for save\n" +\
          "savehist FILENAME   saves histograms into file\n" +\
          "fit FIT             fits with supplied fitting function, only fits sample1\n" +\
          "vertical NUM        draws a vertical line at xvalue=NUM\n" +\
          "horizontal NUM      draws a horizontal line at yvalue=NUM\n" +\
          "title NEW_TITLE     changes plot title to NEW_TITLE\n" +\
          "integrate LOW HIGH  integrate from low to high\n" +\
          "")
  elif not cmd == "":
    print("Not a valid command------------------------X")
