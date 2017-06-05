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

eff_nume = TH1F("eff_nume","HLT_Photon175 or HLT_Photon22_R9Id90_HE10_IsoM Numerator;leading high-pt-id-photon p_{T};Efficency",nbins,bins)
eff_deno = TH1F("eff_deno","Denominator;leading high-pt-id-photon p_{T};Efficency",nbins,bins)
eff = TH1F("eff","HLT_Photon175 or HLT_Photon22_R9Id90_HE10_IsoM;leading high-pt-id-photon p_{T};Efficency",nbins,bins)

eff_175_nume = TH1F("eff_175_nume","HLT_Photon175 Numerator;leading high-pt-id-photon p_{T};Efficency",nbins,bins)
#eff_175_deno = TH1F("eff_175_deno","HLT_Photon175 Denominator;leading high-pt-id-photon p_{T};Efficency",nbins,bins)
eff_175 = TH1F("eff_175","HLT_Photon175;leading high-pt-id-photon p_{T};Efficency",nbins,bins)

eff_22iso_nume = TH1F("eff_22iso_nume","HLT_Photon22_R9Id90_HE10_IsoM Numerator;leading high-pt-id-photon p_{T};Efficency",nbins,bins)
#eff_22iso_deno = TH1F("eff_22iso_deno","HLT_Photon175 Denominator;leading high-pt-id-photon p_{T};Efficency",nbins,bins)
eff_22iso = TH1F("eff_22iso","HLT_Photon22_R9Id90_HE10_IsoM;leading high-pt-id-photon p_{T};Efficency",nbins,bins)

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
  if event.HLT_Photon175 and (event.nTightPhotons > 0):
    events_photon_plus_HLT_Photon175 += 1
  if event.HLT_Photon22_Iso and (event.nTightPhotons > 0):
    events_photon_plus_HLT_Photon22_Iso += 1

  if event.nTightPhotons > 0:
    events_with_photon += 1
    eff_deno.Fill(event.Photon_pt[0])
  if (event.HLT_Photon175 or event.HLT_Photon22_Iso) and (event.nTightPhotons > 0):
    events_photon_plus_HLT += 1
    eff_nume.Fill(event.Photon_pt[0])
  if (event.HLT_Photon175) and (event.nTightPhotons > 0):
    eff_175_nume.Fill(event.Photon_pt[0])
  if (event.HLT_Photon22_Iso) and (event.nTightPhotons > 0):
    eff_22iso_nume.Fill(event.Photon_pt[0])

print "Total Events:", count
print "Events with photon object:", events_with_photon
print "Events that pass HLT_Photon175:", events_HLT_Photon175
print "Events that pass HLT_Photon22_Iso:", events_HLT_Photon22_Iso
print "Events that pass combination trigger:", events_HLT_full
print "Events with photon object and HLT_Photon175:", events_photon_plus_HLT_Photon175
print "Events with photon object and HLT_Photon22_Iso:", events_photon_plus_HLT_Photon22_Iso
print "Events with photon object and pass combination trigger:", events_photon_plus_HLT

eff_nume.Sumw2()
eff_deno.Sumw2()
eff.Add(eff_nume)
eff.Divide(eff_deno)

eff_175_nume.Sumw2()
eff_175.Add(eff_175_nume)
eff_175.Divide(eff_deno)

eff_22iso_nume.Sumw2()
eff_22iso.Add(eff_22iso_nume)
eff_22iso.Divide(eff_deno)

#eff.SetStats(0)
#eff.Draw()
#raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
