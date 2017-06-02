from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys
import os
import glob
import fnmatch

parser = OptionParser()
parser.add_option('--out',
                  dest='out', default="output.root",
                  help='output file')
parser.add_option('--file',
                  dest='file',
                  help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--tree',
                  dest='treename', default="diphotonAnalyzer/fTree2",
                  help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False,
                  dest='dir',
                  help='treat file option as a directory instead of a single file')
(options, args) = parser.parse_args()

out_file = TFile(options.out, 'recreate')

chain = TChain(options.treename)
if (not options.dir):
  chain.Add(options.file)
elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

events_with_photon = 0
events_HLT_Photon175 = 0
events_HLT_Photon22_Iso = 0
events_HLT_full = 0
events_photon_plus_HLT_Photon175 = 0
events_photon_plus_HLT_Photon22_Iso = 0
events_photon_plus_HLT = 0

nbins = 20
bins_array = [0,10,20,30,40,50,60,80,100,120,140,160,180,200,220,240,300,400,500,600,1000]
bins = array('d', bins_array)
low = 0
high = 600

hist_photon = TH1F("hist_photon","Has HptID photon",nbins,bins)
hist_trigger = TH1F("hist_trigger","Has HptID photon and Passes trigger",nbins,bins)
hist_eff = TH1F("hist_eff","HLT_Photon175 or HLT_Photon22_R9Id90_HE10_IsoM;leading high-pt-id-photon p_{T};Efficency",nbins,bins)

count = 0
total = chain.GetEntries()
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  if event.HLT_Photon175:
    events_HLT_Photon175 += 1
  if event.HLT_Photon22_Iso:
    events_HLT_Photon22_Iso += 1
  if (event.HLT_Photon175 or event.HLT_Photon22_Iso):
    events_HLT_full += 1
  if event.nTightPhotons > 0:
    events_with_photon += 1
    hist_photon.Fill(event.Photon_pt[0])
  if event.HLT_Photon175 and (event.nTightPhotons > 0):
    events_photon_plus_HLT_Photon175 += 1
  if event.HLT_Photon22_Iso and (event.nTightPhotons > 0):
    events_photon_plus_HLT_Photon22_Iso += 1
  if (event.HLT_Photon175 or event.HLT_Photon22_Iso) and (event.nTightPhotons > 0):
    events_photon_plus_HLT += 1
    hist_trigger.Fill(event.Photon_pt[0])

print "Total Events:", count
print "Events with photon object:", events_with_photon
print "Events that pass HLT_Photon175:", events_HLT_Photon175
print "Events that pass HLT_Photon22_Iso:", events_HLT_Photon22_Iso
print "Events that pass combination trigger:", events_HLT_full
print "Events with photon object and HLT_Photon175:", events_photon_plus_HLT_Photon175
print "Events with photon object and HLT_Photon22_Iso:", events_photon_plus_HLT_Photon22_Iso
print "Events with photon object and pass combination trigger:", events_photon_plus_HLT

hist_photon.Sumw2()
hist_trigger.Sumw2()

hist_eff.Add(hist_trigger)
hist_eff.Divide(hist_photon)

hist_eff.SetStats(0)
hist_eff.Draw()
raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
