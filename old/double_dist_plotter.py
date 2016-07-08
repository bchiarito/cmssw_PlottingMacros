import os
import glob
import fnmatch
import math
import ROOT
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
parser.add_option('-b', '--bins', metavar='F', type='int', action='store',
                  default=100,
                  dest='bins',
                  help='')
parser.add_option('--min', metavar='F', type='float', action='store',
                  dest='min',
                  help='')
parser.add_option('--max', metavar='F', type='float', action='store',
                  dest='max',
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
parser.add_option('--scale', action='store_true', default=False,
                  dest='scale',
                  help='scale to integral = 1')
parser.add_option('--file', metavar='F', type='string', action='store',
                  default='',
                  dest='file',
                  help='')
parser.add_option('--file2', metavar='F', type='string', action='store',
                  default='',
                  dest='file2',
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
  	      	      default = 'diphotonAnalyzer/fTree2',
                  dest='treename',
                  help='full path of TTree object in each file')
parser.add_option('--legend', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend',
                  help='')
parser.add_option('--dir', action='store_true', default=False,
                  dest='dir',
                  help='treat file option as a directory instead of a single file')
parser.add_option('--input', action='store_true', default=False,
                  dest='input',
                  help='treat file option as a text file listing inputs and weights')
parser.add_option('--inputdir', action='store_true', default=False,
                  dest='dirinput',
                  help='treat file option as a text file listing inputs directories and weights')
parser.add_option('--quiet', action='store_true', default=False,
                  dest='quiet',
                  help='less output')
parser.add_option('--error', action='store_true', default=False,
                  dest='error',
                  help='calls Sumw2() on resulting histogram')
(options, args) = parser.parse_args()

print "Begin."
chain = ROOT.TChain(options.treename)
print "Adding files to TChain..."
if (not options.dir) and (not options.input) and (not options.dirinput):
  chain.Add(options.file)
elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)
print "Booking histogram..."
newhist = ROOT.TH1F(options.name, options.name, options.bins, options.min, options.max)	
print "Drawing into histogram..."
chain.Draw(options.var+">>"+options.name,""+ options.cut, "goff")
if options.scale:
  newhist.Scale(1/newhist.Integral())
newhist.SetLineColor(ROOT.kBlue)
newhist.SetFillColor(0)
newhist.SetLineWidth(2)
newhist.SetLineStyle(1)	
newhist.SetStats(0)
if not options.noplot:
  print "Plotting..."
  c = TCanvas()
  c.cd()
  if options.title == "" and options.name == "plot":
    newhist.SetTitle(options.var)
  elif options.title == "":
    newhist.SetTitle(options.name)
  else:
    newhist.SetTitle(options.title)
  newhist.GetXaxis().SetTitle(options.var + " w/ " + options.cut)
  if options.cut == "":
    newhist.GetXaxis().SetTitle(options.var)
  newhist.GetYaxis().SetTitle("Events")
  if options.scale:
    newhist.GetYaxis().SetTitle("Scaled to Integral 1")
  if options.logy:
    c.SetLogy()
  if options.logx:
    c.SetLogx()
  if options.error:
    newhist.Sumw2()
  newhist.Draw()
  leg = ROOT.TLegend(0.55, 0.85, 0.9, 0.9)
  leg.AddEntry(newhist, options.file, "l")
  leg.Draw("same")
  if options.save == True:
    c.SaveAs(options.name + ".png")
print "Done."

if not options.quiet:
  print "Entries: ", int(newhist.GetEntries())
  print "Underflow: ", int(newhist.GetBinContent(0))
  print "Overflow : ", int(newhist.GetBinContent(options.bins+1))
if options.save == False and options.noplot == False:
  cmd = "start"
  while not cmd == "":
    print "Press [Enter] to finish, type 'options' to see options"
    cmd = raw_input()
    if cmd == "save":
      c.SaveAs(options.name + ".png")
    elif cmd == "fit":
      newhist.Fit("gaus")
      newhist.Draw("same")
    elif cmd == "options":
      print "save     saves current canvas\nfit      fits to a gaussian"
