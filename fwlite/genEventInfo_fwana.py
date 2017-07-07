#! /Usr/bin/env python
import ROOT
import sys
from DataFormats.FWLite import Events, Handle

# Input
files = sys.argv[1]

# Make event collection
events = Events(files)

# Make Handles for objects outside event loop
geninfohandle, geninfolabel = Handle("GenEventInfoProduct"), "generator"

# Book Histograms
outputfilename = "histos.root"
outputfile = ROOT.TFile(outputfilename, "recreate")

weight = ROOT.TH1F('w', 'w', 100, 0, 100)
weights = ROOT.TH1F('ws', 'ws', 100, 0, 100)
qscale = ROOT.TH1F('qscale', 'qscale', 100, 120, 130)
qed = ROOT.TH1F('qed', 'qed', 100, 0.007, .008)
qcd = ROOT.TH1F('qcd', 'qcd', 100, 0.1, .2)

# Loop over events
total = 0
print "Total Events: " + str(events.size())
for event in events:
  total = total + 1
  if (total % 500) == 0 or total == 1:
    print " Processing event " + str(total) + "..."
  #if total >= 10:
  #  break

  # Get Event info
  event.getByLabel(geninfolabel, geninfohandle)
  # Get Products
  geninfo = geninfohandle.product()

  '''print "weight", geninfo.weight()
  print "weightProduct", geninfo.weightProduct()
  print "qScale", geninfo.qScale()
  print "QCD", geninfo.alphaQCD()
  print "QED", geninfo.alphaQED()

  print "weights:"
  weights = geninfo.weights()
  for w in weights:
    print w'''

  weight.Fill(geninfo.weight())
  qscale.Fill(geninfo.qScale())
  qed.Fill(geninfo.alphaQED())
  qcd.Fill(geninfo.alphaQCD())
  ws = geninfo.weights()
  for w in ws:
    weights.Fill(w)

# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
