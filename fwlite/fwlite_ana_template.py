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
time_begin = time.time()
time_checkpoint = time.time()
count = 0
total = chain.GetEntries()
print_threshold = 0
print_increment = 10
print "Total Events: " + str(events.size())
for event in events:
  # feedback to stdout
  percentDone = float(count+1) / float(total) * 100.0
  if percentDone > print_threshold:
    print('{0:10.1f} sec :'.format(time.time() - time_checkpoint), 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count+1, total, percentDone))
    time_checkpoint = time.time()
    print_threshold += print_increment

  # Get Event info
  event.getByLabel(ak4label, ak4handle)
  # Get Products
  ak4jets = ak4handle.product()

# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
