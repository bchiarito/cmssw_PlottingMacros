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

vz_bins = 200
vz_low = -50
vz_high = 50
vz_tracks_fail = TH1F('vz_tracks_fail', 'vz of CH+ and CH- tracks', vz_bins, vz_low, vz_high)
vz_iso_fail = TH1F('vz_iso_fail', 'vz of charged iso pf cands', vz_bins, vz_low, vz_high)
vz_tracks_pass = TH1F('vz_tracks_pass', 'vz of CH+ and CH- tracks', vz_bins, vz_low, vz_high)
vz_iso_pass = TH1F('vz_iso_pass', 'vz of charged iso pf cands', vz_bins, vz_low, vz_high)
vz_tracks_lowpf = TH1F('vz_tracks_lowpf', 'vz of CH+ and CH- tracks', vz_bins, vz_low, vz_high)
vz_iso_lowpf = TH1F('vz_iso_lowpf', 'vz of charged iso pf cands', vz_bins, vz_low, vz_high)
vz_tracks_highpf = TH1F('vz_tracks_highpf', 'vz of CH+ and CH- tracks', vz_bins, vz_low, vz_high)
vz_iso_highpf = TH1F('vz_iso_highpf', 'vz of charged iso pf cands', vz_bins, vz_low, vz_high)

bins = array('f', [0, 0.0001, 0.001, 0.01, 0.1, 0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1028])

dz_bins = 400
dz_low = -2
dz_high = 2
dz_tracks_fail = TH1F('dz_tracks_fail', 'dz of CH+ and CH- tracks', 16, bins)
dz_iso_fail = TH1F('dz_iso_fail', 'dz of charged iso pf cands', 16, bins)
dz_tracks_pass = TH1F('dz_tracks_pass', 'dz of CH+ and CH- tracks', 16, bins)
dz_iso_pass = TH1F('dz_iso_pass', 'dz of charged iso pf cands', 16, bins)
dz_tracks_lowpf = TH1F('dz_tracks_lowpf', 'dz of CH+ and CH- tracks', 16, bins)
dz_iso_lowpf = TH1F('dz_iso_lowpf', 'dz of charged iso pf cands', 16, bins)
dz_tracks_highpf = TH1F('dz_tracks_highpf', 'dz of CH+ and CH- tracks', 16, bins)
dz_iso_highpf = TH1F('dz_iso_highpf', 'dz of charged iso pf cands', 16, bins)

dz_PV_bins = 400
dz_PV_low = -2
dz_PV_high = 2
dz_PV_tracks_fail = TH1F('dz_PV_tracks_fail', 'dz_PV of CH+ and CH- tracks', 16, bins)
dz_PV_iso_fail = TH1F('dz_PV_iso_fail', 'dz_PV of charged iso pf cands', 16, bins)
dz_PV_tracks_pass = TH1F('dz_PV_tracks_pass', 'dz_PV of CH+ and CH- tracks', 16, bins)
dz_PV_iso_pass = TH1F('dz_PV_iso_pass', 'dz_PV of charged iso pf cands', 16, bins)
dz_PV_tracks_lowpf = TH1F('dz_PV_tracks_lowpf', 'dz_PV of CH+ and CH- tracks', 16, bins)
dz_PV_iso_lowpf = TH1F('dz_PV_iso_lowpf', 'dz_PV of charged iso pf cands', 16, bins)
dz_PV_tracks_highpf = TH1F('dz_PV_tracks_highpf', 'dz_PV of CH+ and CH- tracks', 16, bins)
dz_PV_iso_highpf = TH1F('dz_PV_iso_highpf', 'dz_PV of charged iso pf cands', 16, bins)

dxy_bins = 400
dxy_low = -2
dxy_high = 2
dxy_tracks_fail = TH1F('dxy_tracks_fail', 'dxy of CH+ and CH- tracks', 16, bins)
dxy_iso_fail = TH1F('dxy_iso_fail', 'dxy of charged iso pf cands', 16, bins)
dxy_tracks_pass = TH1F('dxy_tracks_pass', 'dxy of CH+ and CH- tracks', 16, bins)
dxy_iso_pass = TH1F('dxy_iso_pass', 'dxy of charged iso pf cands', 16, bins)
dxy_tracks_lowpf = TH1F('dxy_tracks_lowpf', 'dxy of CH+ and CH- tracks', 16, bins)
dxy_iso_lowpf = TH1F('dxy_iso_lowpf', 'dxy of charged iso pf cands', 16, bins)
dxy_tracks_highpf = TH1F('dxy_tracks_highpf', 'dxy of CH+ and CH- tracks', 16, bins)
dxy_iso_highpf = TH1F('dxy_iso_highpf', 'dxy of charged iso pf cands', 16, bins)

dxy_PV_bins = 400
dxy_PV_low = -2
dxy_PV_high = 2
dxy_PV_tracks_fail = TH1F('dxy_PV_tracks_fail', 'dxy_PV of CH+ and CH- tracks', 16, bins)
dxy_PV_iso_fail = TH1F('dxy_PV_iso_fail', 'dxy_PV of charged iso pf cands', 16, bins)
dxy_PV_tracks_pass = TH1F('dxy_PV_tracks_pass', 'dxy_PV of CH+ and CH- tracks', 16, bins)
dxy_PV_iso_pass = TH1F('dxy_PV_iso_pass', 'dxy_PV of charged iso pf cands', 16, bins)
dxy_PV_tracks_lowpf = TH1F('dxy_PV_tracks_lowpf', 'dxy_PV of CH+ and CH- tracks', 16, bins)
dxy_PV_iso_lowpf = TH1F('dxy_PV_iso_lowpf', 'dxy_PV of charged iso pf cands', 16, bins)
dxy_PV_tracks_highpf = TH1F('dxy_PV_tracks_highpf', 'dxy_PV of CH+ and CH- tracks', 16, bins)
dxy_PV_iso_highpf = TH1F('dxy_PV_iso_highpf', 'dxy_PV of charged iso pf cands', 16, bins)

count = 0
total = chain.GetEntries()
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  numcands = len(event.Cand_pt)
  for i in range(numcands):
    vec = TLorentzVector()
    vec.SetPtEtaPhiM(event.Cand_pt[i], event.Cand_eta[i], event.Cand_phi[i], event.Cand_mass[i])

    if event.Cand_passChargedIso[i]:
      vz_tracks_pass.Fill(event.Cand_CHpos_vz[i])
      vz_tracks_pass.Fill(event.Cand_CHneg_vz[i])
      dz_tracks_pass.Fill(fabs(event.Cand_CHpos_dz[i]))
      dz_tracks_pass.Fill(fabs(event.Cand_CHneg_dz[i]))
      dz_PV_tracks_pass.Fill(fabs(event.Cand_CHpos_dz_PV[i]))
      dz_PV_tracks_pass.Fill(fabs(event.Cand_CHneg_dz_PV[i]))
      dxy_tracks_pass.Fill(fabs(event.Cand_CHpos_dxy[i]))
      dxy_tracks_pass.Fill(fabs(event.Cand_CHneg_dxy[i]))
      dxy_PV_tracks_pass.Fill(fabs(event.Cand_CHpos_dxy_PV[i]))
      dxy_PV_tracks_pass.Fill(fabs(event.Cand_CHneg_dxy_PV[i]))
      for j in range(len(event.Cand_isoPF_vz)):
        vz_iso_pass.Fill(event.Cand_isoPF_vz[j])
        dz_iso_pass.Fill(fabs(event.Cand_isoPF_dz[j]))
        dz_PV_iso_pass.Fill(fabs(event.Cand_isoPF_dz_PV[j]))
        dxy_iso_pass.Fill(fabs(event.Cand_isoPF_dxy[j]))
        dxy_PV_iso_pass.Fill(fabs(event.Cand_isoPF_dxy_PV[j]))
    else:
      vz_tracks_fail.Fill(event.Cand_CHpos_vz[i])
      vz_tracks_fail.Fill(event.Cand_CHneg_vz[i])
      dz_tracks_fail.Fill(fabs(event.Cand_CHpos_dz[i]))
      dz_tracks_fail.Fill(fabs(event.Cand_CHneg_dz[i]))
      dz_PV_tracks_fail.Fill(fabs(event.Cand_CHpos_dz_PV[i]))
      dz_PV_tracks_fail.Fill(fabs(event.Cand_CHneg_dz_PV[i]))
      dxy_tracks_fail.Fill(fabs(event.Cand_CHpos_dxy[i]))
      dxy_tracks_fail.Fill(fabs(event.Cand_CHneg_dxy[i]))
      dxy_PV_tracks_fail.Fill(fabs(event.Cand_CHpos_dxy_PV[i]))
      dxy_PV_tracks_fail.Fill(fabs(event.Cand_CHneg_dxy_PV[i]))
      for j in range(len(event.Cand_isoPF_vz)):
        vz_iso_fail.Fill(event.Cand_isoPF_vz[j])
        dz_iso_fail.Fill(fabs(event.Cand_isoPF_dz[j]))
        dz_PV_iso_fail.Fill(fabs(event.Cand_isoPF_dz_PV[j]))
        dxy_iso_fail.Fill(fabs(event.Cand_isoPF_dxy[j]))
        dxy_PV_iso_fail.Fill(fabs(event.Cand_isoPF_dxy_PV[j]))

    if not event.Cand_passChargedIso[i] and event.Cand_nChargedIsoCone[i] <= 3:
      vz_tracks_lowpf.Fill(event.Cand_CHpos_vz[i])
      vz_tracks_lowpf.Fill(event.Cand_CHneg_vz[i])
      dz_tracks_lowpf.Fill(fabs(event.Cand_CHpos_dz[i]))
      dz_tracks_lowpf.Fill(fabs(event.Cand_CHneg_dz[i]))
      dz_PV_tracks_lowpf.Fill(fabs(event.Cand_CHpos_dz_PV[i]))
      dz_PV_tracks_lowpf.Fill(fabs(event.Cand_CHneg_dz_PV[i]))
      dxy_tracks_lowpf.Fill(fabs(event.Cand_CHpos_dxy[i]))
      dxy_tracks_lowpf.Fill(fabs(event.Cand_CHneg_dxy[i]))
      dxy_PV_tracks_lowpf.Fill(fabs(event.Cand_CHpos_dxy_PV[i]))
      dxy_PV_tracks_lowpf.Fill(fabs(event.Cand_CHneg_dxy_PV[i]))
      for j in range(len(event.Cand_isoPF_vz)):
        vz_iso_lowpf.Fill(event.Cand_isoPF_vz[j])
        dz_iso_lowpf.Fill(fabs(event.Cand_isoPF_dz[j]))
        dz_PV_iso_lowpf.Fill(fabs(event.Cand_isoPF_dz_PV[j]))
        dxy_iso_lowpf.Fill(fabs(event.Cand_isoPF_dxy[j]))
        dxy_PV_iso_lowpf.Fill(fabs(event.Cand_isoPF_dxy_PV[j]))
    if not event.Cand_passChargedIso[i] and event.Cand_nChargedIsoCone[i] > 3:
      vz_tracks_highpf.Fill(event.Cand_CHpos_vz[i])
      vz_tracks_highpf.Fill(event.Cand_CHneg_vz[i])
      dz_tracks_highpf.Fill(fabs(event.Cand_CHpos_dz[i]))
      dz_tracks_highpf.Fill(fabs(event.Cand_CHneg_dz[i]))
      dz_PV_tracks_highpf.Fill(fabs(event.Cand_CHpos_dz_PV[i]))
      dz_PV_tracks_highpf.Fill(fabs(event.Cand_CHneg_dz_PV[i]))
      dxy_tracks_highpf.Fill(fabs(event.Cand_CHpos_dxy[i]))
      dxy_tracks_highpf.Fill(fabs(event.Cand_CHneg_dxy[i]))
      dxy_PV_tracks_highpf.Fill(fabs(event.Cand_CHpos_dxy_PV[i]))
      dxy_PV_tracks_highpf.Fill(fabs(event.Cand_CHneg_dxy_PV[i]))
      for j in range(len(event.Cand_isoPF_vz)):
        vz_iso_highpf.Fill(event.Cand_isoPF_vz[j])
        dz_iso_highpf.Fill(fabs(event.Cand_isoPF_dz[j]))
        dz_PV_iso_highpf.Fill(fabs(event.Cand_isoPF_dz_PV[j]))
        dxy_iso_highpf.Fill(fabs(event.Cand_isoPF_dxy[j]))
        dxy_PV_iso_highpf.Fill(fabs(event.Cand_isoPF_dxy_PV[j]))

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
