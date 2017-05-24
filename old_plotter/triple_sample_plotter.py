import os
import glob
import math
import ROOT
from ROOT import *
import sys

from optparse import OptionParser

parser = OptionParser()

parser.add_option('--cut', metavar='F', type='string', action='store',
                  dest='cut',
                  help='')

parser.add_option('--var', metavar='F', type='string', action='store',
                  dest='var',
                  help='')

parser.add_option('--Min', metavar='F', type='float', action='store',
                  dest='Min',
                  help='')

parser.add_option('--Max', metavar='F', type='float', action='store',
                  dest='Max',
                  help='')

parser.add_option('--name', metavar='F', type='string', action='store',
	    	  default = "blank",
                  dest='name',
                  help='')

parser.add_option('--log', action='store_true', default=False,
                  dest='log',
                  help='log scale on y axis')

parser.add_option('--scale', action='store_true', default=False,
                  dest='scale',
                  help='scale to integral 1')

parser.add_option('--bin', metavar='F', type='int', action='store',
                  default=100,
                  dest='bin',
                  help='')

parser.add_option('--file1', metavar='F', type='string', action='store',
                  default='no',
                  dest='fi1',
                  help='')

parser.add_option('--file2', metavar='F', type='string', action='store',
                  default='no',
                  dest='fi2',
                  help='')

parser.add_option('--save', action='store_true', default=False,
                  dest='save',
                  help='save plot')

parser.add_option('--title', metavar='F', type='string', action='store',
	    	  default = "blank",
                  dest='title',
                  help='')

parser.add_option('--noplot', action='store_true', default=False,
                  dest='noplot',
                  help='Do not draw anything')


(options, args) = parser.parse_args()

scale = options.scale
cut = options.cut
var = options.var
x = options.Min
y = options.Max
log = options.log
bin = options.bin
fi1 = options.fi1
fi2 = options.fi2
name = options.name
title = options.title
noplot = options.noplot

#f = ROOT.TFile( options.name + ".root", "recreate" )
#f.cd()

chain = ROOT.TChain("tree")
chain.Add(fi1)
newhist = ROOT.TH1F(name, name, bin, x, y)	
chain.Draw(var+">>"+name,""+ cut, "goff")
if scale:
  newhist.Scale(1/newhist.Integral())
newhist.SetLineColor(ROOT.kBlue)
newhist.SetFillColor(0)
newhist.SetLineWidth(2)
newhist.SetLineStyle(2)	
newhist.SetStats(0)

name2 = name + "_two"
chain2 = ROOT.TChain("tree")
chain2.Add(fi2)
newhist2 = ROOT.TH1F(name2, name2, bin, x, y)
chain2.Draw(var+">>"+name2,""+ cut, "goff")
if scale:
  newhist2.Scale(1/newhist2.Integral())
newhist2.SetLineColor(ROOT.kRed)
newhist2.SetFillColor(0)
newhist2.SetLineWidth(2)
newhist2.SetLineStyle(2)
newhist2.SetStats(0)

if not noplot:
  c = TCanvas()
  c.cd()
  newhist.SetTitle(title)
  newhist.GetXaxis().SetTitle(var + "  w/  " + cut)
  if cut == "":
    newhist.GetXaxis().SetTitle(var)
  newhist.GetYaxis().SetTitle("Events")
  if log:
    c.SetLogy()
  newhist.Draw()
  newhist2.Draw("same")
  leg = ROOT.TLegend(0.55, 0.85, 0.9, 0.9)
  leg.AddEntry(newhist,  "T1tttt_1300_300_Ch285_mChi280_23body", "l")
  leg.AddEntry(newhist2, "T1tttt_1300_300_mChi280_4body", "l")
  leg.Draw("same")
  if options.save == True:
    c.SaveAs(name + ".png")

print "file1: " + str(newhist.GetEntries())
print "file1: " + str(newhist2.GetEntries())

if options.save == False and noplot == False:
  raw_input()

