from ROOT import *
from array import array
from math import *
import sys
import os
import glob
import fnmatch
from optparse import OptionParser

def delta_phi(phi1, phi2):
  dphi = math.fabs(phi1 - phi2)
  return delta_phi_helper(dphi)

def delta_phi_helper(dphi):
  if dphi > 3.1415926535:
    return delta_phi_helper(dphi - 3.1415926535)
  else:
    return dphi

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

gROOT.ProcessLine(
"struct recoDiObjectInfo_t {\
    Double_t pt;\
    Double_t phi;\
    Double_t eta;\
    Double_t mass;\
    Double_t px;\
    Double_t py;\
    Double_t pz;\
    Double_t energy;\
    Double_t dR;\
    Double_t dPt;\
    Double_t dPhi;\
    Double_t dEta;\
    Double_t dMass;\
  };")
gammatwoprongInfo = recoDiObjectInfo_t()
chain.SetBranchAddress("GammaTwoProng", AddressOf(gammatwoprongInfo, "pt") )

count = 0.0
total = chain.GetEntries()
have_0_matched = 0.0
have_1_matched = 0.0
have_2_matched = 0.0
have_3_matched = 0.0
have_4_matched = 0.0
have_5_matched = 0.0
have_6ormore_matched = 0.0
have_3ormore_matched = 0.0
have_0_passed = 0.0
have_1_passed = 0.0
have_2_passed = 0.0
have_3ormore_passed = 0.0

genetas_total = 0.0
genetas_matchedToCand = 0.0
genetas_matchedToPass = 0.0
genetas_matchedToJet = 0.0

for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  for i in range(len(event.GenEta_candDR)):
    genetas_total += 1
    if event.GenEta_candDR[i] < 0.1:
      genetas_matchedToCand += 1
    if event.GenEta_passedCandDR[i] < 0.1:
      genetas_matchedToPass += 1
    if event.GenEta_jetDR[i] < 0.1:
      genetas_matchedToJet += 1
  
  if event.nPass == 0:
    have_0_passed += 1
  if event.nPass == 1:
    have_1_passed += 1
  if event.nPass == 2:
    have_2_passed += 1
  if event.nPass >= 3:
    have_3ormore_passed += 1
  
  if event.nMatched == 0:
    have_0_matched += 1
  if event.nMatched == 1:
    have_1_matched += 1
  if event.nMatched == 2:
    have_2_matched += 1
  if event.nMatched >= 3:
    have_3ormore_matched += 1
  if event.nMatched == 3:
    have_3_matched += 1
  if event.nMatched == 4:
    have_4_matched += 1
  if event.nMatched == 5:
    have_5_matched += 1
  if event.nMatched >= 6:
    have_6ormore_matched += 1

# print cutflow
print "fraction of Gen Etas matched to Candidate", genetas_matchedToCand / genetas_total
print "fraction of Gen Etas matched to Passed Candidate", genetas_matchedToPass / genetas_total
print "fraction of Gen Etas matched to Jet", genetas_matchedToJet / genetas_total
print ""
print "fraction of event with exactly 0 matched cand" , have_0_matched / total
print "fraction of event with exactly 1 matched cand" , have_1_matched / total
print "fraction of event with exactly 2 matched cand" , have_2_matched / total
print "fraction of event with 3 or more matched cand" , have_3ormore_matched / total
print "fraction of event with exactly 3 matched cand" , have_3_matched / total
print "fraction of event with exactly 4 matched cand" , have_4_matched / total
print "fraction of event with exactly 5 matched cand" , have_5_matched / total
print "fraction of event with 6 or more matched cand" , have_6ormore_matched / total
print ""
print "fraction of event with exactly 0 passed cand" , have_0_passed / total
print "fraction of event with exactly 1 passed cand" , have_1_passed / total
print "fraction of event with exactly 2 passed cand" , have_2_passed / total
print "fraction of event with 3 or more passed cand" , have_3ormore_passed / total
# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
