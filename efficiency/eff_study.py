from array import array
from math import *
import sys
import os
import glob
import fnmatch
from optparse import OptionParser

# run on ttree of twoprong ntuplizer
# makes file with eff computed as f'n of eta,phi,pt,npv,rho
# can then combine with secondary script to plots multiple effs together on same plot

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
usage = "Usage: %prog TwoProngNtuplizer.root --signal/tau --tight/cand\n\nRun on ttree of twoprong ntuplizer, makes rootfile with eff as f'n of pt/eta/phi/npv/rho"
parser = OptionParser(usage=usage)
parser.add_option('--out', dest='out', default="output_eff.root", help='output file')
parser.add_option('--tree', dest='treename', default="twoprongNtuplizer/fTree2", help='name of tree inside files')
parser.add_option('--signal', action='store_true', default=False, dest='signal', help='file is signal or bkg to signal')
parser.add_option('--tau', action='store_true', default=False, dest='tau', help='file is tau or bkg to tau')
parser.add_option('--tight', action='store_true', default=True, dest='tight', help='')
parser.add_option('--cand', action='store_false', dest='tight', help='')
(options, args) = parser.parse_args()
# prevents ROOT from also reading options
sys.argv = []
from ROOT import *

out_file = TFile('eff_' + options.out + '.root', 'recreate')
if options.signal and options.tau:
  print "cannot choose both --signal and --tight"
  sys.exit()

num_phi_bin = 15
phi_low = -3.15
phi_high = 3.15

num_eta_bins = 30
eta_low = -6
eta_high = 6

pt_bins_array = [0,20,40,60,80,100,150,200,250,300,500,1000]
num_pt_bins = len(pt_bins_array)-1
pt_bins = array('d', pt_bins_array)

npv_bins_array = [0,5,7,9,11,13,15,17,19,21,40]
num_npv_bins = len(npv_bins_array)-1
npv_bins = array('d', npv_bins_array)

rho_bins_array = [0,5,7,9,11,13,15,17,19,21,40]
num_rho_bins = len(rho_bins_array)-1
rho_bins = array('d', rho_bins_array)

# get ttrees in tchain
chain = TChain(options.treename)
direc = args[0][-1:len(args[0])] == '/'
if (not direc):
  chain.Add(args[0])
elif direc:
  rootfiles = []
  for root, dirnames, filenames in os.walk(args[0]):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)

# book histograms
TH1.SetDefaultSumw2()

eff_genobj_pt_numer = TH1F("eff_genobj_pt_numer","", num_pt_bins, pt_bins)
eff_genobj_pt_denom = TH1F("eff_genobj_pt_denom","", num_pt_bins, pt_bins)
eff_genobj_pt       = TH1F("eff_genobj_pt"      ,"", num_pt_bins, pt_bins)

eff_genobj_phi_numer = TH1F("eff_genobj_phi_numer","",num_phi_bin,phi_low,phi_high)
eff_genobj_phi_denom = TH1F("eff_genobj_phi_denom","",num_phi_bin,phi_low,phi_high)
eff_genobj_phi       = TH1F("eff_genobj_phi"      ,"",num_phi_bin,phi_low,phi_high)

eff_genobj_eta_numer = TH1F("eff_genobj_eta_numer","",num_eta_bins,eta_low,eta_high)
eff_genobj_eta_denom = TH1F("eff_genobj_eta_denom","",num_eta_bins,eta_low,eta_high)
eff_genobj_eta       = TH1F("eff_genobj_eta"      ,"",num_eta_bins,eta_low,eta_high)

eff_genobj_npv_numer = TH1F("eff_genobj_npv_numer","", num_npv_bins, npv_bins)
eff_genobj_npv_denom = TH1F("eff_genobj_npv_denom","", num_npv_bins, npv_bins)
eff_genobj_npv       = TH1F("eff_genobj_npv"      ,"", num_npv_bins, npv_bins)

eff_genobj_rho_numer = TH1F("eff_genobj_rho_numer","", num_rho_bins, rho_bins)
eff_genobj_rho_denom = TH1F("eff_genobj_rho_denom","", num_rho_bins, rho_bins)
eff_genobj_rho       = TH1F("eff_genobj_rho"      ,"", num_rho_bins, rho_bins)

eff_recoobj_pt_numer = TH1F("eff_recoobj_pt_numer","", num_pt_bins, pt_bins)
eff_recoobj_pt_denom = TH1F("eff_recoobj_pt_denom","", num_pt_bins, pt_bins)
eff_recoobj_pt       = TH1F("eff_recoobj_pt"      ,"", num_pt_bins, pt_bins)

eff_recoobj_phi_numer = TH1F("eff_recoobj_phi_numer","",num_phi_bin,phi_low,phi_high)
eff_recoobj_phi_denom = TH1F("eff_recoobj_phi_denom","",num_phi_bin,phi_low,phi_high)
eff_recoobj_phi       = TH1F("eff_recoobj_phi"      ,"",num_phi_bin,phi_low,phi_high)

eff_recoobj_eta_numer = TH1F("eff_recoobj_eta_numer","",num_eta_bins,eta_low,eta_high)
eff_recoobj_eta_denom = TH1F("eff_recoobj_eta_denom","",num_eta_bins,eta_low,eta_high)
eff_recoobj_eta       = TH1F("eff_recoobj_eta"      ,"",num_eta_bins,eta_low,eta_high)

eff_recoobj_npv_numer = TH1F("eff_recoobj_npv_numer","",num_npv_bins, npv_bins)
eff_recoobj_npv_denom = TH1F("eff_recoobj_npv_denom","",num_npv_bins, npv_bins)
eff_recoobj_npv       = TH1F("eff_recoobj_npv"      ,"",num_npv_bins, npv_bins)

eff_recoobj_rho_numer = TH1F("eff_recoobj_rho_numer","",num_rho_bins, rho_bins)
eff_recoobj_rho_denom = TH1F("eff_recoobj_rho_denom","",num_rho_bins, rho_bins)
eff_recoobj_rho       = TH1F("eff_recoobj_rho"      ,"",num_rho_bins, rho_bins)

# overall
genobj_total = 0
genobj_matched = 0

# event loop
total = chain.GetEntries()
count = 0.0
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  # gen signal eff
  if options.signal:
    for i in range(len(event.GenOmega_objDR)):
      genobj_total+=1
      eff_genobj_pt_denom.Fill(event.GenOmega_pt[i])
      eff_genobj_phi_denom.Fill(event.GenOmega_phi[i])
      eff_genobj_eta_denom.Fill(event.GenOmega_eta[i])
      eff_genobj_npv_denom.Fill(event.nPV)
      eff_genobj_rho_denom.Fill(event.rho)
      if options.tight:
        matchDR = event.GenOmega_objDR[i]
      else:
        matchDR = event.GenOmega_candobjDR[i]
      if matchDR < 0.1:
        genobj_matched+=1
        eff_genobj_pt_numer.Fill(event.GenOmega_pt[i]) 
        eff_genobj_phi_numer.Fill(event.GenOmega_phi[i]) 
        eff_genobj_eta_numer.Fill(event.GenOmega_eta[i]) 
        eff_genobj_npv_numer.Fill(event.nPV) 
        eff_genobj_rho_numer.Fill(event.rho) 

  # hadronic tau eff
  if options.tau:
    index_of_leading = -1
    pt_of_leading = -1.0
    for i in range(len(event.GenTau_objDR)):
      if event.GenTau_pt[i] > pt_of_leading:
        pt_of_leading = event.GenTau_pt[i]
        index_of_leading = i
    genobj_total+=1
    eff_genobj_pt_denom.Fill(event.GenTau_pt[index_of_leading])
    eff_genobj_phi_denom.Fill(event.GenTau_phi[index_of_leading])
    eff_genobj_eta_denom.Fill(event.GenTau_eta[index_of_leading])
    eff_genobj_npv_denom.Fill(event.nPV)
    eff_genobj_rho_denom.Fill(event.rho)
    if options.tight:
      matchDR = event.GenTau_objDR[index_of_leading]
    else:
      matchDR = event.GenTau_candobjDR[index_of_leading]
    if matchDR < 0.2:
      genobj_matched+=1
      eff_genobj_pt_numer.Fill(event.GenTau_pt[index_of_leading])
      eff_genobj_phi_numer.Fill(event.GenTau_phi[index_of_leading])
      eff_genobj_eta_numer.Fill(event.GenTau_eta[index_of_leading])
      eff_genobj_npv_numer.Fill(event.nPV)
      eff_genobj_rho_numer.Fill(event.rho)
   
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
if not genobj_total == 0:
  print "fraction of gen objs matched :", float(genobj_matched) / genobj_total
