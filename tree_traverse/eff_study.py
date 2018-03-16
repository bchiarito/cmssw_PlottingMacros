from ROOT import *
from array import array
from math import *
import sys
import os
import glob
import fnmatch
from optparse import OptionParser

def compute_eff_error_bars(eff, numer, denom):
    eff.Add(numer)
    eff.Divide(denom)
    for b in range(1, eff.GetNbinsX()+1):
      e = eff.GetBinContent(b)
      d = denom.GetBinContent(b)
      if not d==0:
        error = sqrt( (e * (1-e)) / (d) )
      else:
        error = 0
      eff.SetBinError(b, error)

parser = OptionParser()
parser.add_option('--out', dest='out', default="output.root",
                  help='output file')
parser.add_option('--file', dest='file',
                  help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--tree', dest='treename', default="diphotonAnalyzer/fTree2",
                  help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False, dest='dir',
                  help='treat file option as a directory instead of a single file')
(options, args) = parser.parse_args()
out_file = TFile(options.out, 'recreate')

TH1.SetDefaultSumw2()

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

npv_bins_array = [0,5,7,9,11,13,15,17,19,21,40]
num_npv_bins = len(npv_bins_array)-1
npv_bins = array('d', npv_bins_array)

rho_bins_array = [0,5,7,9,11,13,15,17,19,21,40]
num_rho_bins = len(rho_bins_array)-1
rho_bins = array('d', rho_bins_array)

eff_genobj_pt_numer = TH1F("eff_genobj_pt_numer","", num_pt_bins, pt_bins)
eff_genobj_pt_denom = TH1F("eff_genobj_pt_denom","", num_pt_bins, pt_bins)
eff_genobj_pt       = TH1F("eff_genobj_pt"      ,"", num_pt_bins, pt_bins)

eff_genobj_phi_numer = TH1F("eff_genobj_phi_numer","",15,-3.15,3.15)
eff_genobj_phi_denom = TH1F("eff_genobj_phi_denom","",15,-3.15,3.15)
eff_genobj_phi       = TH1F("eff_genobj_phi"      ,"",15,-3.15,3.15)

eff_genobj_eta_numer = TH1F("eff_genobj_eta_numer","",15,-3,3)
eff_genobj_eta_denom = TH1F("eff_genobj_eta_denom","",15,-3,3)
eff_genobj_eta       = TH1F("eff_genobj_eta"      ,"",15,-3,3)

eff_genobj_npv_numer = TH1F("eff_genobj_npv_numer","", num_npv_bins, npv_bins)
eff_genobj_npv_denom = TH1F("eff_genobj_npv_denom","", num_npv_bins, npv_bins)
eff_genobj_npv       = TH1F("eff_genobj_npv"      ,"", num_npv_bins, npv_bins)

eff_genobj_rho_numer = TH1F("eff_genobj_rho_numer","", num_rho_bins, rho_bins)
eff_genobj_rho_denom = TH1F("eff_genobj_rho_denom","", num_rho_bins, rho_bins)
eff_genobj_rho       = TH1F("eff_genobj_rho"      ,"", num_rho_bins, rho_bins)

eff_recoobj_pt_numer = TH1F("eff_recoobj_pt_numer","", num_pt_bins, pt_bins)
eff_recoobj_pt_denom = TH1F("eff_recoobj_pt_denom","", num_pt_bins, pt_bins)
eff_recoobj_pt       = TH1F("eff_recoobj_pt"      ,"", num_pt_bins, pt_bins)

eff_recoobj_phi_numer = TH1F("eff_recoobj_phi_numer","",15,-3.15,3.15)
eff_recoobj_phi_denom = TH1F("eff_recoobj_phi_denom","",15,-3.15,3.15)
eff_recoobj_phi       = TH1F("eff_recoobj_phi"      ,"",15,-3.15,3.15)

eff_recoobj_eta_numer = TH1F("eff_recoobj_eta_numer","",15,-3,3)
eff_recoobj_eta_denom = TH1F("eff_recoobj_eta_denom","",15,-3,3)
eff_recoobj_eta       = TH1F("eff_recoobj_eta"      ,"",15,-3,3)

eff_recoobj_npv_numer = TH1F("eff_recoobj_npv_numer","",num_npv_bins, npv_bins)
eff_recoobj_npv_denom = TH1F("eff_recoobj_npv_denom","",num_npv_bins, npv_bins)
eff_recoobj_npv       = TH1F("eff_recoobj_npv"      ,"",num_npv_bins, npv_bins)

eff_recoobj_rho_numer = TH1F("eff_recoobj_rho_numer","",num_rho_bins, rho_bins)
eff_recoobj_rho_denom = TH1F("eff_recoobj_rho_denom","",num_rho_bins, rho_bins)
eff_recoobj_rho       = TH1F("eff_recoobj_rho"      ,"",num_rho_bins, rho_bins)

print total, "Total Events."

for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  # gen object basis
  for i in range(len(event.GenOmega_objDR)):
    genetas_total += 1
    if event.GenOmega_candobjDR[i] < 0.1:
      genetas_matchedToCand += 1
    if event.GenOmega_objDR[i] < 0.1:
      genetas_matchedToPass += 1
    if event.GenOmega_jetDR[i] < 0.1:
      genetas_matchedToJet += 1
    eff_genobj_pt_denom.Fill(event.GenOmega_pt[i])
    eff_genobj_phi_denom.Fill(event.GenOmega_phi[i])
    eff_genobj_eta_denom.Fill(event.GenOmega_eta[i])
    eff_genobj_npv_denom.Fill(event.nPV)
    eff_genobj_rho_denom.Fill(event.rho)
    if event.GenOmega_objDR[i] < 0.1:
      eff_genobj_pt_numer.Fill(event.GenOmega_pt[i]) 
      eff_genobj_phi_numer.Fill(event.GenOmega_phi[i]) 
      eff_genobj_eta_numer.Fill(event.GenOmega_eta[i]) 
      eff_genobj_npv_numer.Fill(event.nPV) 
      eff_genobj_rho_numer.Fill(event.rho) 
   
  # reco object basis
  event_tightmatched = 0.0
  for i in range(len(event.TwoProng_genOmega_dR)):
    tightcands_total += 1
    eff_recoobj_pt_denom.Fill(event.TwoProng_pt[i])
    eff_recoobj_phi_denom.Fill(event.TwoProng_phi[i])
    eff_recoobj_eta_denom.Fill(event.TwoProng_eta[i])
    eff_recoobj_npv_denom.Fill(event.nPV)
    eff_recoobj_rho_denom.Fill(event.rho)
    if event.TwoProng_genOmega_dR[i] < 0.1:
      tightcands_matched += 1
      event_tightmatched += 1
      eff_recoobj_pt_numer.Fill(event.TwoProng_pt[i]) 
      eff_recoobj_phi_numer.Fill(event.TwoProng_phi[i]) 
      eff_recoobj_eta_numer.Fill(event.TwoProng_eta[i]) 
      eff_recoobj_npv_numer.Fill(event.nPV)  
      eff_recoobj_rho_numer.Fill(event.rho)  
  if event_tightmatched == 0:
    event_has0tightmatched += 1
  if event_tightmatched == 1:
    event_has1tightmatched += 1
  if event_tightmatched == 2:
    event_has2tightmatched += 1
  if event_tightmatched >= 3:
    event_has3ormoretightmatched += 1

  # event wide
  if event.nTwoProngs == 0:
    event_has0tight += 1
  if event.nTwoProngs == 1:
    event_has1tight += 1
  if event.nTwoProngs == 2:
    event_has2tight += 1
  if event.nTwoProngs >= 3:
    event_has3ormoretight += 1

# efficiency histograms
compute_eff_error_bars(eff_genobj_pt, eff_genobj_pt_numer, eff_genobj_pt_denom)
compute_eff_error_bars(eff_genobj_phi, eff_genobj_phi_numer, eff_genobj_phi_denom)
compute_eff_error_bars(eff_genobj_eta, eff_genobj_eta_numer, eff_genobj_eta_denom)
compute_eff_error_bars(eff_genobj_npv, eff_genobj_npv_numer, eff_genobj_npv_denom)
compute_eff_error_bars(eff_genobj_rho, eff_genobj_rho_numer, eff_genobj_rho_denom)

compute_eff_error_bars(eff_recoobj_pt, eff_recoobj_pt_numer, eff_recoobj_pt_denom)
compute_eff_error_bars(eff_recoobj_phi, eff_recoobj_phi_numer, eff_recoobj_phi_denom)
compute_eff_error_bars(eff_recoobj_eta, eff_recoobj_eta_numer, eff_recoobj_eta_denom)
compute_eff_error_bars(eff_recoobj_npv, eff_recoobj_npv_numer, eff_recoobj_npv_denom)
compute_eff_error_bars(eff_recoobj_rho, eff_recoobj_rho_numer, eff_recoobj_rho_denom)

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()

# print cutflow
print "-Per Generator Object basis-"
print "fraction of Gen objs matched to cand  twoprong:", genetas_matchedToCand / genetas_total
print "fraction of Gen objs matched to tight twoprong:", genetas_matchedToPass / genetas_total
print "fraction of Gen objs matched to ak4 jet       :", genetas_matchedToJet / genetas_total
print ""
print "-Per RECO Object basis-"
print "fraction of tight TwoProngs matched to Gen a0:", tightcands_matched / tightcands_total
print ""
print "-Per Event basis-"
print "fraction of events with exactly 0 matched tight twoprongs:" , event_has0tightmatched / total
print "fraction of events with exactly 1 matched tight twoprongs:" , event_has1tightmatched / total
print "fraction of events with exactly 2 matched tight twoprongs:" , event_has2tightmatched / total
print "fraction of events with 3 or more matched tight twoprongs:" , event_has3ormoretightmatched / total
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
sys.exit()
