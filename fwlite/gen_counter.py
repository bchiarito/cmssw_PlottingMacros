#! /Usr/bin/env python
import ROOT
import sys
from DataFormats.FWLite import Events, Handle

# Input
files = sys.argv[1]

# Make event collection
events = Events(files)

# Make Handles for objects outside event loop
genhandle, genlabel = Handle("vector<reco::GenParticle>"), "prunedGenParticles"

# Book Histograms
outputfilename = "histos.root"
outputfile = ROOT.TFile(outputfilename, "recreate")

count = 0
# Loop over events
total = 0
print "Total Events: " + str(events.size())
for event in events:
  total = total + 1
  if (total % 500) == 0 or total == 1:
    print " Processing event " + str(total) + "..."

  # Get Event info
  event.getByLabel(genlabel, genhandle)
  # Get Products
  genparticles = genhandle.product()

  for genparticle in genparticles:
    pdgid = genparticle.pdgId()
    status = genparticle.status()
    if pdgid == 331 and status == 2:
      count += 1

print count

# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
