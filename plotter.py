import os
import glob
import fnmatch
import math
import ROOT
import string
from ROOT import *
import sys

from optparse import OptionParser

parser = OptionParser()

parser.add_option('--cut', metavar='F', type='string', action='store',
                  default='',
                  dest='cut',
                  help='')
parser.add_option('--var', metavar='F', type='string', action='store',
                  dest='var',
                  help='')
parser.add_option('--bins', metavar='F', type='string', action='store',
                  default='100,0,100',
                  dest='binning',
                  help='')
parser.add_option('--name', metavar='F', type='string', action='store',
    	    	      default = "plot",
                  dest='name',
                  help='name of file when saving')
parser.add_option('--logy', action='store_true', default=False,
                  dest='logy',
                  help='logy sacle on y')
parser.add_option('--logx', action='store_true', default=False,
                  dest='logx',
                  help='logx sacle on x')
parser.add_option('--scaled', action='store_true', default=False,
                  dest='scale',
                  help='scale to integral = 1')
parser.add_option('--sample', metavar='F', type='string', action='store',
                  dest='sample1',
                  help='')
parser.add_option('--sample1', metavar='F', type='string', action='store',
                  default='',
                  dest='sample1',
                  help='')
parser.add_option('--sample2', metavar='F', type='string', action='store',
                  default='',
                  dest='sample2',
                  help='')
parser.add_option('--sample3', metavar='F', type='string', action='store',
                  default='',
                  dest='sample3',
                  help='')
parser.add_option('--save', action='store_true', default=False,
                  dest='save',
                  help='save plot')
parser.add_option('--title', metavar='F', type='string', action='store',
	    	          default = '',
                  dest='title',
                  help='Title of histogram in canvas')
parser.add_option('--noplot', action='store_true', default=False,
                  dest='noplot',
                  help='Do not plot anything')
parser.add_option('--tree', metavar='F', type='string', action='store',
                  dest='treename1',
                  help='full path of TTree object in each file')
parser.add_option('--tree1', metavar='F', type='string', action='store',
  	      	      default = 'fTree2',
                  dest='treename1',
                  help='full path of TTree object in each file')
parser.add_option('--tree2', metavar='F', type='string', action='store',
  	      	      default = 'fTree2',
                  dest='treename2',
                  help='full path of TTree object in each file')
parser.add_option('--tree3', metavar='F', type='string', action='store',
  	      	      default = 'fTree2',
                  dest='treename3',
                  help='full path of TTree object in each file')
parser.add_option('--xaxis', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='xaxis',
                  help='xaxis label')
parser.add_option('--leg', metavar='F', type='string', action='store',
                  dest='legend1',
                  help='legend entry label')
parser.add_option('--leg1', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend1',
                  help='legend entry label')
parser.add_option('--leg2', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend2',
                  help='legend2 entry label')
parser.add_option('--leg3', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend3',
                  help='legend3 entry label')
parser.add_option('--dir', action='store_true', default=False,
                  dest='dir',
                  help='treat file option as a directory instead of a single file')
parser.add_option('--txt', action='store_true', default=False,
                  dest='txt',
                  help='treat file option as a .txt file with optional cross sections included')
parser.add_option('--quiet', action='store_true', default=False,
                  dest='quiet',
                  help='less output')
parser.add_option('--errors', action='store_true', default=False,
                  dest='errors',
                  help='calls Sumw2() on resulting histogram')
parser.add_option('--legoff', action='store_true', default=False,
                  dest='legoff',
                  help='Turns off legend')
parser.add_option('-n', '--num', type='int', action='store',
                  default=-1,
                  dest='nentries',
                  help='max number of entries to draw from files')
parser.add_option('--lumi', type='float', action='store',
  	      	      default = -1.0,
                  dest='lumi',
                  help='luminosity to scale to, if changd from default value')

(options, args) = parser.parse_args()

if not options.quiet:
  print "Begin."

multiple_samples = (not options.sample2 == "") or \
                   (not options.sample3 == "")

samples = []
sample = {}
sample['path'] = options.sample1
sample['tree'] = options.treename1
samples.append(sample)
if not options.sample2 == "":
  sample = {}
  sample['path'] = options.sample2
  sample['tree'] = options.treename2
  samples.append(sample)
if not options.sample3 == "":
  sample = {}
  sample['path'] = options.sample3
  sample['tree'] = options.treename3
  samples.append(sample)

# Make collection of TChains
for sample in samples:
  path = sample['path']
  ISrootfile = False
  ISdirectory = False
  ISinputfile = False
  if fnmatch.fnmatch(path, "*.root"):
    print "I think", path, "is a rootfile"
    ISrootfile = True
  if fnmatch.fnmatch(path, "*/"):
    print "I think", path, "is a directory to traverse"
    ISdirectory = True
  if fnmatch.fnmatch(path, "*.txt"):
    print "I think", path, "is a text file of inputs"
    ISinputfile = True

  if ISrootfile:
    chain = ROOT.TChain(sample['tree'])
    chain.Add(path)
    sample['entries'] = [[chain, 1, 1]]

  if ISdirectory:
    chain = ROOT.TChain(sample['tree'])
    rootfiles = []
    for root, dirnames, filenames in os.walk(options.file1):
      for filename in fnmatch.filter(filenames, '*.root'):
        rootfiles.append(os.path.join(root, filename))
    for rootfile in rootfiles:
      chain.Add(rootfile)
    sample['entries'] = [[chain, 1, 1]]

  if ISinputfile:
    sample['entries'] = []
    inputfile = open(path, 'r')
    print "Reading from ", path, "..."
    for line in inputfile:
      chain = ROOT.TChain(sample['tree'])      
      print line
      sample = line.split()
      print sample
      # Get name, xs, and num from line
      if len(sample) == 1:
        path = sample[0]
      if len(sample) == 3:
        xs = sample[1]
        N = sample[2]
      if len(sample) == 2 or len(sample) == 0 or len(sample) > 3:
        print "couldn't parse line from input file", path
        continue
      # add files to chain
      if fnmatch(path, "*.root"):
        chain.Add(path)
      elif fnmatch(path, "*/"):
        rootfiles = []
        for root, dirnames, filenames in os.walk(path):
          for filename in fnmatch.filter(filenames, '*.root'):
            rootfiles.append(os.path.join(root, filename))
        for rootfile in rootfiles:
          chain.Add(rootfile)
      else:
        # line doesn't make sense
        print "couldn't parse line from input file", path
      sample['entries'].append([chain, xs, N])
     
if not options.quiet:
  print "Drawing into histogram..."

i1 = string.index(options.binning,',')
i2 = string.rindex(options.binning,',')
bins = int(options.binning[0:i1])
low = float(options.binning[i1+1:i2])
high = float(options.binning[i2+1:len(options.binning)])

count = 0
for sample in samples:
  for entry in sample['entries']:
    chain = entry[0]
    xs = entry[1]
    N = entry[2]
    count += 1
    hist = ROOT.TH1F(options.name+"_"+str(count), options.name, bins, low, high)
    chain.Draw(options.var+">>"+options.name+"_"+str(count),""+options.cut, "goff")
    entry.append(hist)    
  
  
    

    # here we should add up all the constitent histograms for a particular sample,
    # and also scale them against each other
    # if lumi is set, scale them according to the lumi
    # if lumi is set but the sample has no xs and N listed, just leave it alone, arbitrary units
    # if lumi is not set, scale the sample against the sample with the median event content




# Print Summary
print "\nEntries    : ", int(newhist.GetEntries())
if not int(newhist.GetBinContent(0)) == 0:
  print "Underflow  - ", int(newhist.GetBinContent(0))
if not int(newhist.GetBinContent(bins+1)) == 0:
  print "Overflow   - ", int(newhist.GetBinContent(bins+1))

if not options.file2 == "":
  print "Entries 2  : ", int(newhist2.GetEntries())
  if not int(newhist2.GetBinContent(0)) == 0:
    print "Underflow 2- ", int(newhist2.GetBinContent(0))
  if not int(newhist2.GetBinContent(bins+1)) == 0:
    print "Overflow 2 - ", int(newhist2.GetBinContent(bins+1))

if not options.file3 == "":
  print "Entries 3  : ", int(newhist3.GetEntries())
  if not int(newhist3.GetBinContent(0)) == 0:
    print "Underflow 3- ", int(newhist3.GetBinContent(0))
  if not int(newhist3.GetBinContent(bins+1)) == 0:
    print "Overflow 3 - ", int(newhist3.GetBinContent(bins+1))
print ""

if not options.noplot:
  if not options.quiet:
    print "Plotting..."
  c = TCanvas()
  c.cd()
  # Stats
  newhist.SetLineColor(ROOT.kRed)
  newhist.SetFillColor(0)
  newhist.SetLineWidth(2)
  newhist.SetLineStyle(1)	
  newhist.SetStats(0)
  if not options.file2 == "":
    newhist2.SetLineColor(ROOT.kBlack)
    newhist2.SetFillColor(0)
    newhist2.SetLineWidth(2)
    newhist2.SetLineStyle(1)	
    newhist2.SetStats(0)
  if not options.file3 == "":
    newhist3.SetLineColor(ROOT.kTeal)
    newhist3.SetFillColor(0)
    newhist3.SetLineWidth(2)
    newhist3.SetLineStyle(1)	
    newhist3.SetStats(0)
  # Scale
  if options.errors:
    newhist.Sumw2()
    if not options.file2 == "":
      newhist2.Sumw2()
    if not options.file3 == "":
      newhist3.Sumw2()
  if options.scale:
    newhist.Scale(100.0/newhist.Integral())
    if not options.file2 == "":
      newhist2.Scale(100.0/newhist2.Integral())
    if not options.file3 == "":
      newhist3.Scale(100.0/newhist3.Integral())
  if options.logy:
    c.SetLogy()
  if options.logx:
    c.SetLogx()
  maximum = newhist.GetMaximum()
  if not options.file2 == "":
    maximum = max(maximum, newhist2.GetMaximum())
  if not options.file2 == "":
    maximum = max(maximum, newhist3.GetMaximum())
  if options.logy:
    newhist.SetMaximum(maximum*4)
    if not options.scale:
      newhist.SetMinimum(0.5)
  else:
    newhist.SetMaximum(maximum*1.15)
  # Title
  if not options.title == "":
    newhist.SetTitle(options.title)
  elif options.name == "plot":
    newhist.SetTitle(options.var)
  else:
    newhist.SetTitle(options.name)
  # X axis
  newhist.GetXaxis().SetTitle(options.var + " w/ " + options.cut)
  if options.cut == "":
    newhist.GetXaxis().SetTitle(options.var)
  if not options.xaxis == "":
    newhist.GetXaxis().SetTitle(options.xaxis)
  # Y axis
  newhist.GetYaxis().SetTitle("Events")
  if options.scale:
    newhist.GetYaxis().SetTitle("Scaled to Integral 100")
  # Draw()
  newhist.Draw()
  if not options.file2 == "":
    newhist2.Draw("same")
  if not options.file3 == "":
    newhist3.Draw("same")
  # Legend
  leg = ROOT.TLegend(0.55, 0.80, 0.9, 0.9)
  leg1 = options.legend1
  if leg1 == "":
    leg1 = options.file1
  leg.AddEntry(newhist, leg1, "l")
  if not options.file2 == "":
    leg2 = options.legend2
    if leg2 == "":
      leg2 = options.file2
    leg.AddEntry(newhist2, leg2, "l")
  if not options.file3 == "":
    leg3 = options.legend3
    if leg3 == "":
      leg3 = options.file3
    leg.AddEntry(newhist3, leg3, "l")
  if not options.legoff:
    leg.Draw("same")
  # Save
  if options.save == True:
    c.SaveAs(options.name + ".png")

if not options.quiet:
  print "Done."

# After plot Commands
if (not options.save) and (not options.noplot):
  cmd = "start"
  while not cmd == "":
    print "\nPress [Enter] to finish, type 'options' to see options"
    # parse input
    inp = raw_input()
    i = string.find(inp,' ')
    if i==-1:
      cmd = inp
      opt = ""
    else:
      cmd = inp[0:i]
      opt = inp[i+1:len(inp)]
    # begin commands
    if cmd == "save":
      sys.stdout.write(' ')
      sys.stdout.flush()
      if opt=="":
        c.SaveAs(options.name + ".png")
      else:
        c.SaveAs(opt + ".png")
    elif cmd == "saveas":
      sys.stdout.write(' ')
      sys.stdout.flush()
      if opt=="":
        filename = raw_input("Enter filename: ")
        c.SaveAs(filename + ".png")
      else:
        c.SaveAs(opt + ".png")
    elif cmd == "gaus":
      newhist.Fit("gaus")
      newhist.Draw("same")
    elif cmd == "fit":
      if opt=="":
        print "Must supply second argument to", cmd
        continue
      newhist.Fit(opt)
      newhist.Draw("same")
    elif cmd == "vertical":
      if opt=="":
        print "Must supply second argument to", cmd
        continue
      pos = float(opt)
      vert_line = ROOT.TLine(pos, 0, pos, newhist.GetMaximum())
      vert_line.Draw("same")
      if not options.legoff:
        leg.Draw("same")
    elif cmd == "horizontal":
      if opt=="":
        print "Must supply second argument to", cmd
        continue
      pos = float(opt)
      horz_line = ROOT.TLine(0, pos, high, pos)
      horz_line.Draw("same")
      if not options.legoff:
        leg.Draw("same")
    elif cmd == "options":
      print "save FILENAME    saves current canvas, optionally with supplied name\n" +\
            "saveas FILENAME  saves current canvas prompting for filename if not given\n" +\
            "gaus             fits to a gaussian\n" +\
            "fit FIT          fits with supplied fitting function\n" +\
            "vertical INT     draws a vertical line at xvalue=INT\n" +\
            "horizontal INT   draws a horizontal line at yvalue=INT\n" +\
            ""
    elif not cmd == "":
      print cmd,"not a valid command"
