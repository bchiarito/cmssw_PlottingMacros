from ROOT import *
from array import array
from math import *
import sys
import os
import glob
import fnmatch
from optparse import OptionParser

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

count = 0.0
total = chain.GetEntries()

genetas_total = 0.0
genetas_matchedToCand = 0.0
genetas_matchedToPass = 0.0
genetas_matchedToJet = 0.0

tightcands_total = 0.0
tightcands_matched = 0.0

loosecands_total = 0.0
loosecands_matched = 0.0

event_has0tightmatched = 0.0
event_has1tightmatched = 0.0
event_has2tightmatched = 0.0
event_has3ormoretightmatched = 0.0

event_has0loosematched = 0.0
event_has1loosematched = 0.0
event_has2loosematched = 0.0
event_has3ormoreloosematched = 0.0

event_has0tight = 0.0
event_has1tight = 0.0
event_has2tight = 0.0
event_has3ormoretight = 0.0

pt_bins_array = [0,20,40,60,80,100,150,200,250,300,500,1000]
num_pt_bins = len(pt_bins_array)-1
pt_bins = array('d', pt_bins_array)

eff_genobj_pt_numer = TH1F("eff_genobj_pt_numer","", num_pt_bins, pt_bins)
eff_genobj_pt_denom = TH1F("eff_genobj_pt_denom","", num_pt_bins, pt_bins)
eff_genobj_pt       = TH1F("eff_genobj_pt"      ,"", num_pt_bins, pt_bins)

eff_genobj_phi_numer = TH1F("eff_genobj_phi_numer","",15,-3.15,3.15)
eff_genobj_phi_denom = TH1F("eff_genobj_phi_denom","",15,-3.15,3.15)
eff_genobj_phi       = TH1F("eff_genobj_phi"      ,"",15,-3.15,3.15)

eff_genobj_eta_numer = TH1F("eff_genobj_eta_numer","",15,-3,3)
eff_genobj_eta_denom = TH1F("eff_genobj_eta_denom","",15,-3,3)
eff_genobj_eta       = TH1F("eff_genobj_eta"      ,"",15,-3,3)


for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  # gen object basis
  for i in range(len(event.GenEta_candDR)):
    genetas_total += 1
    if event.GenEta_candDR[i] < 0.1:
      genetas_matchedToCand += 1
    if event.GenEta_passedCandDR[i] < 0.1:
      genetas_matchedToPass += 1
    if event.GenEta_jetDR[i] < 0.1:
      genetas_matchedToJet += 1
    eff_genobj_pt_denom.Fill(event.GenEta_pt[i])
    eff_genobj_phi_denom.Fill(event.GenEta_phi[i])
    eff_genobj_eta_denom.Fill(event.GenEta_eta[i])
    if event.GenEta_candDR[i] < 0.1:
      eff_genobj_pt_numer.Fill(event.GenEta_pt[i]) 
      eff_genobj_phi_numer.Fill(event.GenEta_phi[i]) 
      eff_genobj_eta_numer.Fill(event.GenEta_eta[i]) 
   
  # reco object basis
  event_tightmatched = 0.0
  for i in range(len(event.TwoProng_genDR)):
    tightcands_total += 1
    if event.TwoProng_genDR[i] < 0.1:
      tightcands_matched += 1
      event_tightmatched += 1
  if event_tightmatched == 0:
    event_has0tightmatched += 1
  if event_tightmatched == 1:
    event_has1tightmatched += 1
  if event_tightmatched == 2:
    event_has2tightmatched += 1
  if event_tightmatched >= 3:
    event_has3ormoretightmatched += 1

  event_loosematched = 0.0
  for i in range(len(event.TwoProngLoose_genDR)):
    loosecands_total += 1
    if event.TwoProngLoose_genDR[i] < 0.1:
      loosecands_matched += 1
      event_loosematched += 1
  if event_loosematched == 0:
    event_has0loosematched += 1
  if event_loosematched == 1:
    event_has1loosematched += 1
  if event_loosematched == 2:
    event_has2loosematched += 1
  if event_loosematched >= 3:
    event_has3ormoreloosematched += 1

  if event.nTwoProngs == 0:
    event_has0tight += 1
  if event.nTwoProngs == 1:
    event_has1tight += 1
  if event.nTwoProngs == 2:
    event_has2tight += 1
  if event.nTwoProngs >= 3:
    event_has3ormoretight += 1


# print cutflow
print ""
print "-Per Generator Object basis-"
print "fraction of Gen a0s matched to loose twoprong:", genetas_matchedToCand / genetas_total
print "fraction of Gen a0s matched to tight twoprong:", genetas_matchedToPass / genetas_total
print "fraction of Gen a0s matched to ak4 jet       :", genetas_matchedToJet / genetas_total
print ""
print "-Per RECO Object basis-"
print "fraction of tight TwoProngs matched to Gen a0:", tightcands_matched / tightcands_total
print "fraction of loose TwoProngs matched to Gen a0:", loosecands_matched / loosecands_total
print ""
print "-Per Event basis-"
print "fraction of events with exactly 0 matched tight twoprongs:" , event_has0tightmatched / total
print "fraction of events with exactly 1 matched tight twoprongs:" , event_has1tightmatched / total
print "fraction of events with exactly 2 matched tight twoprongs:" , event_has2tightmatched / total
print "fraction of events with 3 or more matched tight twoprongs:" , event_has3ormoretightmatched / total
print ""
print "fraction of events with exactly 0 matched loose twoprongs:" , event_has0loosematched / total
print "fraction of events with exactly 1 matched loose twoprongs:" , event_has1loosematched / total
print "fraction of events with exactly 2 matched loose twoprongs:" , event_has2loosematched / total
print "fraction of events with 3 or more matched loose twoprongs:" , event_has3ormoreloosematched / total
print ""
print "-Efficiency without matching-"
N0 = event_has0tight
N1 = event_has1tight
N2 = event_has2tight + event_has3ormoretight
Nt = total
Naux = sqrt( 1.0 - (2.0*N1)/(Nt) )
print "efficiency using events with 2 or more tight objects:", sqrt(N2/Nt)
print "efficiency using events with 0 tight objects        :", 1.0 - sqrt(N0/Nt)
print "efficiency using events with 1 tight object         :", (1.0 - Naux)/2.0, (1.0 + Naux)/2.0

# efficiency histograms
eff_genobj_pt_numer.Sumw2()
eff_genobj_pt_denom.Sumw2()
eff_genobj_pt.Add(eff_genobj_pt_numer)
eff_genobj_pt.Divide(eff_genobj_pt_denom)

eff_genobj_phi_numer.Sumw2()
eff_genobj_phi_denom.Sumw2()
eff_genobj_phi.Add(eff_genobj_phi_numer)
eff_genobj_phi.Divide(eff_genobj_phi_denom)

eff_genobj_eta_numer.Sumw2()
eff_genobj_eta_denom.Sumw2()
eff_genobj_eta.Add(eff_genobj_eta_numer)
eff_genobj_eta.Divide(eff_genobj_eta_denom)

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
