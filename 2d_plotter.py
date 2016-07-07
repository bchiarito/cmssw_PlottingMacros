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
parser.add_option('--varx', metavar='F', type='string', action='store',
                  default='',
                  dest='varx',
                  help='')
parser.add_option('--vary', metavar='F', type='string', action='store',
                  default='',
                  dest='vary',
                  help='')
parser.add_option('--binsx', metavar='F', type='string', action='store',
                  default='100,0,100',
                  dest='binningx',
                  help='')
parser.add_option('--binsy', metavar='F', type='string', action='store',
                  default='100,0,100',
                  dest='binningy',
                  help='')
parser.add_option('--name', metavar='F', type='string', action='store',
    	    	      default = "plot",
                  dest='name',
                  help='name of file when saving')
parser.add_option('--logz', action='store_true', default=False,
                  dest='logz',
                  help='log scale on z')
parser.add_option('--logy', action='store_true', default=False,
                  dest='logy',
                  help='log scale on y')
parser.add_option('--logx', action='store_true', default=False,
                  dest='logx',
                  help='log scale on x')
parser.add_option('--scaled', action='store_true', default=False,
                  dest='scale',
                  help='scale to integral = 1')
parser.add_option('--file', metavar='F', type='string', action='store',
                  default = '',
                  dest='file',
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
                  default = 'fTree2',
                  dest='treename',
                  help='full path of TTree object in each file')
parser.add_option('--xaxis', metavar='F', type='string', action='store',
                  default = '',
                  dest='xaxis',
                  help='xaxis label')
parser.add_option('--yaxis', metavar='F', type='string', action='store',
                  default = '',
                  dest='yaxis',
                  help='yaxis label')
parser.add_option('--leg', metavar='F', type='string', action='store',
                  default = '',
                  dest='legend',
                  help='legend entry label')
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

chain = ROOT.TChain(options.treename)

if not options.quiet:
  print "Adding files to TChain..."

if (not options.dir):
  chain.Add(options.file)

elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

if not options.quiet:
  print "Booking histograms..."

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

newhist = ROOT.TH2F(options.name, options.name, binsx, lowx, highx, binsy, lowy, highy)

if not options.quiet:
  print "Drawing into histogram..."

chain.Draw(options.vary+":"+options.varx+">>"+options.name,""+options.cut, "goff")

# Print Summary
print "\nEntries    : ", int(newhist.GetEntries())

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
  # Scale
  if options.scale:
    newhist.Scale(1/newhist.Integral())
  # Title and Axes
  if not options.title == "":
    newhist.SetTitle(options.title)
  elif not options.name == "plot":
    newhist.SetTitle(options.name)
  else:
    newhist.SetTitle(options.cut)
  if not options.xaxis == "":
    newhist.GetXaxis().SetTitle(options.xaxis)
  else:
    newhist.GetXaxis().SetTitle(options.varx)
  if not options.yaxis == "":
    newhist.GetYaxis().SetTitle(options.yaxis)
  else:
    newhist.GetYaxis().SetTitle(options.vary)
  if options.logy:
    c.SetLogz()
  if options.logy:
    c.SetLogy()
  if options.logx:
    c.SetLogx()
  if options.errors:
    newhist.Sumw2()
  # Draw()
  newhist.Draw("Colz")
  # Legend
  leg = ROOT.TLegend(0.6, 0.80, 0.9, 0.9)
  leg1 = options.legend
  if leg1 == "":
    leg1 = options.file
  leg.AddEntry(newhist, leg1, "")
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
    elif cmd == "saveas":
      filename = raw_input("Enter filename: ")
      c.SaveAs(filename + ".png")
    elif cmd == "drawx":
      temphistx = ROOT.TH1F("temphistx", options.varx, binsx, lowx, highx)
      chain.Draw(options.varx+">>"+"temphistx",""+options.cut, "goff")
      c_x = TCanvas()
      c_x.cd()
      temphistx.Draw()
    elif cmd == "drawy":
      temphisty = ROOT.TH1F("temphisty", options.vary, binsy, lowy, highy)
      chain.Draw(options.vary+">>"+"temphisty",""+options.cut, "goff")
      c_y = TCanvas()
      c_y.cd()
      temphisty.Draw()
    elif cmd == "gaus":
      newhist.Fit("gaus")
      newhist.Draw("same")
    elif cmd == "options":
      print "save     saves plot in file\n" +\
            "saveas   saves plot in file, prompting for filename" +\
            "gaus     fits to a gaussian\n" +\
            "drawx    draws x axis distribution\n" +\
            "drawy    draws y axis distribution\n"
