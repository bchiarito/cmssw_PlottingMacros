import os
import glob
import fnmatch
import math
import ROOT
import string
from ROOT import *
import sys
import time

from optparse import OptionParser

time_begin = time.time()

parser = OptionParser()

# Variable options
parser.add_option('--varx', metavar='F', type='string', action='store',
                  dest='varx',
                  help='')
parser.add_option('--vary', metavar='F', type='string', action='store',
                  dest='vary',
                  help='')
parser.add_option('--binx', metavar='F', type='string', action='store',
                  default='100,0,100',
                  dest='binningx',
                  help='')
parser.add_option('--biny', metavar='F', type='string', action='store',
                  default='100,0,100',
                  dest='binningy',
                  help='')
parser.add_option('--cut', metavar='F', type='string', action='store',
                  default='',
                  dest='cut',
                  help='')

# Input files options
parser.add_option('--sample', metavar='F', type='string', action='store',
                  default='',
                  dest='sample1',
                  help='')
parser.add_option('--tree', metavar='F', type='string', action='store',
                  default='fTree2',
                  dest='treename1',
                  help='full path of TTree object in each file')

# Histogram drawing options
parser.add_option('--logy', action='store_true', default=False,
                  dest='logy',
                  help='log sacle on y')
parser.add_option('--logx', action='store_true', default=False,
                  dest='logx',
                  help='log sacle on x')
parser.add_option('--logz', action='store_true', default=False,
                  dest='logz',
                  help='log sacle on z')
parser.add_option('--scaled', action='store_true', default=False,
                  dest='scale',
                  help='scale to integral = 1')
parser.add_option('--lumi', type='float', action='store',
  	      	      default = -1.0,
                  dest='lumi',
                  help='luminosity to scale to, if changed from default value')
parser.add_option('--title', metavar='F', type='string', action='store',
	    	          default = '',
                  dest='title',
                  help='Title of histogram in canvas')
parser.add_option('--xaxis', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='xaxis',
                  help='xaxis label')
parser.add_option('--yaxis', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='yaxis',
                  help='yaxis label')
parser.add_option('--noplot', action='store_true', default=False,
                  dest='noplot',
                  help='Do not plot anything')
parser.add_option('--errors', action='store_true', default=False,
                  dest='errors',
                  help='calls Sumw2() on resulting histogram')
parser.add_option('--legoff', action='store_true', default=False,
                  dest='legoff',
                  help='Turns off legend')
parser.add_option('--leg', metavar='F', type='string', action='store',
                  dest='legend1',
                  help='legend entry label')

# Other options
parser.add_option('--save', action='store_true', default=False,
                  dest='save',
                  help='save plot')
parser.add_option('--name', metavar='F', type='string', action='store',
    	    	      default = "plot",
                  dest='name',
                  help='name of file when saving')
parser.add_option('--quiet', action='store_true', default=False,
                  dest='quiet',
                  help='less output')
parser.add_option('-n', '--num', type='int', action='store',
                  default=-1,
                  dest='nentries',
                  help='max number of entries to draw from files')

(options, args) = parser.parse_args()

if not options.quiet:
  print "Begin."

samples = []
sample = {}
sample['path'] = options.sample1
sample['tree'] = options.treename1
sample['label'] = options.legend1
samples.append(sample)

# Make collection of TChains
for sample in samples:
  path = sample['path']
  ISrootfile = False
  ISdirectory = False
  ISinputfile = False
  if fnmatch.fnmatch(path, "*.root"):
    #print "It appears ", path, "is a rootfile"
    ISrootfile = True
  if fnmatch.fnmatch(path, "*/"):
    #print "It appears", path, "is a directory to traverse"
    ISdirectory = True
  if fnmatch.fnmatch(path, "*.txt"):
    #print "It appears", path, "is a text file of inputs"
    ISinputfile = True

  if ISrootfile:
    chain = ROOT.TChain(sample['tree'])
    chain.Add(path)
    sample['entries'] = [[chain, 1, 1]]

  if ISdirectory:
    chain = ROOT.TChain(sample['tree'])
    rootfiles = []
    for root, dirnames, filenames in os.walk(path):
      for filename in fnmatch.filter(filenames, '*.root'):
        rootfiles.append(os.path.join(root, filename))
    for rootfile in rootfiles:
      chain.Add(rootfile)
    sample['entries'] = [[chain, 1, 1]]

  if ISinputfile:
    sample['entries'] = []
    inputfile = open(path, 'r')
    for line in inputfile:
      line_list = line.split()
      # Get name, xs, and num from line
      if len(line_list) == 1:
        path_to_file = line_list[0]
        xs = 1
        N = 1
        treename = sample['tree']
      if len(line_list) == 3:
        path_to_file = line_list[0]
        xs = float(line_list[1])
        N = float(line_list[2])
        treename = sample['tree']
      if len(line_list) == 4:
        path_to_file = line_list[0]
        xs = float(line_list[1])
        N = float(line_list[2])
        treename = line_list[3]
      if len(line_list) == 2 or len(line_list) == 0 or len(line_list) > 4:
        print "couldn't parse line from input file", path
        continue
      # add files to chain
      chain = ROOT.TChain(treename)      
      if fnmatch.fnmatch(path, "*.root"):
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
        print "couldn't parse line from input file", path
      sample['entries'].append([chain, xs, N])
     
if not options.quiet:
  print "Drawing into histogram..."

i1x = string.index(options.binningx,',')
i2x = string.rindex(options.binningx,',')
binsx = int(options.binningx[0:i1x])
lowx = float(options.binningx[i1x+1:i2x])
highx = float(options.binningx[i2x+1:len(options.binningx)])

i1y = string.index(options.binningy,',')
i2y = string.rindex(options.binningy,',')
binsy = int(options.binningy[0:i1y])
lowy = float(options.binningy[i1y+1:i2y])
highy = float(options.binningy[i2y+1:len(options.binningy)])

count = 0
sumcount = 0
for sample in samples:
  sumcount += 1
  hist_sum = ROOT.TH2F(options.name+"_sum_"+str(sumcount), options.name, binsx, lowx, highx, binsy, lowy, highy)
  for entry in sample['entries']:
    chain = entry[0]
    xs = entry[1]
    N = entry[2]
    count += 1
    hist = ROOT.TH2F(options.name+"_"+str(count), options.name, binsx, lowx, highx, binsy, lowy, highy)
    chain.Draw(options.vary+":"+options.varx+">>"+options.name+"_"+str(count),""+options.cut, "goff")
    entry.append(hist)
    hist.Scale(xs/N)
    hist_sum.Add(hist)
  sample['summed_hist'] = hist_sum
  
# Print Summary
print ""
for sample in samples:
  hist = sample['summed_hist']
  print "Entries " + str(count) + "   : ", int(hist.GetEntries())
print ""
  
if not options.noplot:
  if not options.quiet:
    print "Plotting..."
  c = TCanvas()
  c.cd()
  if options.logy:
    c.SetLogy()
  if options.logx:
    c.SetLogx()
  if options.logz:
    c.SetLogz()
  for sample in samples:
    hist = sample['summed_hist']
    # Stats
    hist.SetStats(0)
    # Scale
    if options.errors:
      hist.Sumw2()
    if options.scale:
      hist.Scale(100.0/hist.Integral())

  # Title
  for sample in samples:
    hist = sample['summed_hist']
    if not options.title == "":
      hist.SetTitle(options.title)
    elif options.name == "plot":
      hist.SetTitle(options.varx + " vs " + options.vary)
    else:
      hist.SetTitle(options.name)
    # X axis
    hist.GetXaxis().SetTitle(options.varx + " w/ " + options.cut)
    if options.cut == "":
      hist.GetXaxis().SetTitle(options.varx)
    if not options.xaxis == "":
      hist.GetXaxis().SetTitle(options.xaxis)
    # Y axis
    hist.GetYaxis().SetTitle(options.vary + " w/ " + options.cut)
    if options.cut == "":
      hist.GetYaxis().SetTitle(options.vary)
    if not options.xaxis == "":
      hist.GetYaxis().SetTitle(options.xaxis)

  # Draw()
  count = 0
  for sample in samples:
    hist = sample['summed_hist']
    if count == 0:
      hist.Draw("Colz")
    else:
      hist.Draw("same")
    count += 1

  # Save
  if options.save == True:
    c.SaveAs(options.name + ".png")

if not options.quiet:
  print "Done."

time_end = time.time()

print "Elapsed Time: ", (time_end - time_begin)

# After plot Commands
if (not options.save) and (not options.noplot):
  hist = samples[0]['summed_hist']
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
      hist.Fit("gaus")
      hist.Draw("same")
    elif cmd == "fit":
      if opt=="":
        print "Must supply second argument to", cmd
        continue
      hist.Fit(opt)
      hist.Draw("same")
    elif cmd == "vertical":
      if opt=="":
        print "Must supply second argument to", cmd
        continue
      pos = float(opt)
      vert_line = ROOT.TLine(pos, 0, pos, hist.GetMaximum())
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
