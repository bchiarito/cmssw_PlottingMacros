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
parser.add_option('--file', metavar='F', type='string', action='store',
                  dest='file1',
                  help='')
parser.add_option('--file1', metavar='F', type='string', action='store',
                  default='',
                  dest='file1',
                  help='')
parser.add_option('--file2', metavar='F', type='string', action='store',
                  default='',
                  dest='file2',
                  help='')
parser.add_option('--file3', metavar='F', type='string', action='store',
                  default='',
                  dest='file3',
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
parser.add_option('--quiet', action='store_true', default=False,
                  dest='quiet',
                  help='less output')
parser.add_option('--errors', action='store_true', default=False,
                  dest='errors',
                  help='calls Sumw2() on resulting histogram')
parser.add_option('--legoff', action='store_true', default=False,
                  dest='legoff',
                  help='Turns off legend')
(options, args) = parser.parse_args()

if not options.quiet:
  print "Begin."

chain = ROOT.TChain(options.treename1)
if not options.file2 == "":
  chain2 = ROOT.TChain(options.treename2)
if not options.file3 == "":
  chain3 = ROOT.TChain(options.treename3)

if not options.quiet:
  print "Adding files to TChain..."

if (not options.dir):
  chain.Add(options.file1)
  if not options.file2 == "":
    chain2.Add(options.file2)
  if not options.file3 == "":
    chain3.Add(options.file3)  

elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file1):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)
  if not options.file2 == "":
    rootfiles = []
    for root, dirnames, filenames in os.walk(options.file2):
      for filename in fnmatch.filter(filenames, '*.root'):
        rootfiles.append(os.path.join(root, filename))
    for rootfile in rootfiles:
      chain2.Add(rootfile)
  if not options.file3 == "":
    rootfiles = []
    for root, dirnames, filenames in os.walk(options.file3):
      for filename in fnmatch.filter(filenames, '*.root'):
        rootfiles.append(os.path.join(root, filename))
    for rootfile in rootfiles:
      chain3.Add(rootfile)

if not options.quiet:
  print "Booking histograms..."

i1 = string.index(options.binning,',')
i2 = string.rindex(options.binning,',')
bins = int(options.binning[0:i1])
low = float(options.binning[i1+1:i2])
high = float(options.binning[i2+1:len(options.binning)])
newhist = ROOT.TH1F(options.name, options.name, bins, low, high)
if not options.file2 == "":
  newhist2 = ROOT.TH1F(options.name + "_2", options.name, bins, low, high)
if not options.file3 == "":
  newhist3 = ROOT.TH1F(options.name + "_3", options.name, bins, low, high)

if not options.quiet:
  print "Drawing into histogram..."

chain.Draw(options.var+">>"+options.name,""+ options.cut, "goff")
if not options.file2 == "":
  chain2.Draw(options.var+">>"+options.name+"_2",""+ options.cut, "goff")
if not options.file3 == "":
  chain3.Draw(options.var+">>"+options.name+"_3",""+ options.cut, "goff")

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

if not options.noplot:
  print "\nPlotting..."
  c = TCanvas()
  c.cd()
  # Stats
  newhist.SetLineColor(ROOT.kBlack)
  newhist.SetFillColor(0)
  newhist.SetLineWidth(2)
  newhist.SetLineStyle(1)	
  newhist.SetStats(0)
  if not options.file2 == "":
    newhist2.SetLineColor(ROOT.kBlue)
    newhist2.SetFillColor(0)
    newhist2.SetLineWidth(2)
    newhist2.SetLineStyle(1)	
    newhist2.SetStats(0)
  if not options.file3 == "":
    newhist3.SetLineColor(ROOT.kRed)
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
if options.save == False and options.noplot == False:
  cmd = "start"
  while not cmd == "":
    print "\nPress [Enter] to finish, type 'options' to see options"
    cmd = raw_input()
    if cmd == "save":
      c.SaveAs(options.name + ".png")
    if cmd == "saveas":
      filename = raw_input("Enter filename: ")
      c.SaveAs(filename + ".png")
    elif cmd == "gaus":
      newhist.Fit("gaus")
      newhist.Draw("same")
    elif cmd == "options":
      print "save     saves current canvas\n" +\
            "saveas   saves current canvas prompting for filename" +\
            "gaus     fits to a gaussian\n"
