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

dr_bins = 100
dr_low = 0
dr_high = 10

npf_bins = 50
npf_low = 0
npf_high = 50

dr_vs_npf = TH2F('dr_vs_npf', 'TwoProng candidates failing charged isolation', npf_bins, npf_low, npf_high, dr_bins, dr_low, dr_high)
dr_vs_npf.GetXaxis().SetTitle('number of extra tracks')
dr_vs_npf.GetYaxis().SetTitle('\Delta \\text{R to the nearest generator Eta}')

ngamma_bins = 20
ngamma_low = 0
ngamma_high = 20

ngamma_vs_npf = TH2F('ngamma_vs_npf', 'TwoProng candidates failing charged isolation', npf_bins, npf_low, npf_high, ngamma_bins, ngamma_low, ngamma_high)
ngamma_vs_npf.GetXaxis().SetTitle('number of extra tracks')
ngamma_vs_npf.GetYaxis().SetTitle('number of pf photons included in definition of Photon')

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
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  numcands = len(event.Cand_pt)
  for i in range(numcands):
    vec = TLorentzVector()
    vec.SetPtEtaPhiM(event.Cand_pt[i], event.Cand_eta[i], event.Cand_phi[i], event.Cand_mass[i])

    if not event.Cand_passChargedIso[i]:
      dr_vs_npf.Fill(event.Cand_nChargedIsoCone[i], event.Cand_genDR[i])
      ngamma_vs_npf.Fill(event.Cand_nChargedIsoCone[i], event.Cand_photon_nGamma[i])

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
