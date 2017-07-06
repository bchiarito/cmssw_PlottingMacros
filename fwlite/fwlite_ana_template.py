#! /Usr/bin/env python
import ROOT
import sys
from DataFormats.FWLite import Events, Handle

# Input
files = sys.argv[1]

# Make event collection
events = Events(files)

# Make Handles for objects outside event loop
ak4handle, ak4label = Handle("std::vector<pat::Jet>"), "slimmedJets"

# Book Histograms
pvqual = ROOT.TH1F('histo', 'histo', 10, 0, 10)
outputfilename = "histos.root"
outputfile = ROOT.TFile(outputfilename, "recreate")

# Loop over events
total = 0
print "Total Events: " + str(events.size())
for event in events:
  total = total + 1
  if (total % 500) == 0 or total == 1:
    print " Processing event " + str(total) + "..."

  # Get Event info
  event.getByLabel(ak4label, ak4handle)
  # Get Products
  ak4jets = ak4handle.product()

# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
