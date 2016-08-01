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

bins = 50
low = 0
high = 50
chargedIsoCount_fail = TH1F('chargedIsoCount_fail', 'Count of PF cands in Charged Iso Cone for failing Two-Prong Candidates', bins, low, high)
neutralIsoCount_fail = TH1F('neutralIsoCount_fail', 'Count of PF cands in Neutral Iso Cone for failing Two-Prong Candidates', bins, low, high)
egammaIsoCount_fail = TH1F('egammaIsoCount_fail', 'Count of PF cands in EGamma Iso Cone for failing Two-Prong Candidates', bins, low, high)
chargedIsoCount_pass = TH1F('chargedIsoCount_pass', 'Count of PF cands in Charged Iso Cone for passing Two-Prong Candidates', bins, low, high)
neutralIsoCount_pass = TH1F('neutralIsoCount_pass', 'Count of PF cands in Neutral Iso Cone for passing Two-Prong Candidates', bins, low, high)
egammaIsoCount_pass = TH1F('egammaIsoCount_pass', 'Count of PF cands in EGamma Iso Cone for passing Two-Prong Candidates', bins, low, high)

count = 0
total = chain.GetEntries()
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  numcands = len(event.Cand_pt)
  for i in range(numcands):
    if not event.Cand_passChargedIso[i]:
      chargedIsoCount_fail.Fill(event.Cand_nChargedIsoCone[i])
    if not event.Cand_passNeutralIso[i]:
      neutralIsoCount_fail.Fill(event.Cand_nNeutralIsoCone[i])
    if not event.Cand_passEGammaIso[i]:
      egammaIsoCount_fail.Fill(event.Cand_nEGammaIsoCone[i])
    if event.Cand_passChargedIso[i]:
      chargedIsoCount_pass.Fill(event.Cand_nChargedIsoCone[i])
    if event.Cand_passNeutralIso[i]:
      neutralIsoCount_pass.Fill(event.Cand_nNeutralIsoCone[i])
    if event.Cand_passEGammaIso[i]:
      egammaIsoCount_pass.Fill(event.Cand_nEGammaIsoCone[i])

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
