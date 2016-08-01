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

pt_bins = 40
pt_low = 0
pt_high = 2000
total_pt = TH1F('total_pt', 'Two-prong total number', pt_bins, pt_low, pt_high)
chargedIso_pass_pt  = TH1F('chargedIso_pass_pt' , 'Two-prong number pass rel charged iso', pt_bins, pt_low, pt_high)
chargedIso_eff_pt   = TH1F('chargedIso_eff_pt'  , 'Two-prong efficiency pass rel charged iso', pt_bins, pt_low, pt_high)
neutralIso_pass_pt  = TH1F('neutralIso_pass_pt' , 'Two-prong number pass rel neutral iso', pt_bins, pt_low, pt_high)
neutralIso_eff_pt   = TH1F('neutralIso_eff_pt'  , 'Two-prong efficiency pass rel neutral iso', pt_bins, pt_low, pt_high)
egammaIso_pass_pt  = TH1F('egammaIso_pass_pt' , 'Two-prong number pass rel egamma iso', pt_bins, pt_low, pt_high)
egammaIso_eff_pt   = TH1F('egammaIso_eff_pt'  , 'Two-prong efficiency pass rel egamma iso', pt_bins, pt_low, pt_high)
photon_req_pass_pt  = TH1F('photon_req_pass_pt' , 'Two-prong number pass photon_req', pt_bins, pt_low, pt_high)
photon_req_eff_pt   = TH1F('photon_req_eff_pt'  , 'Two-prong efficiency pass photon_req', pt_bins, pt_low, pt_high)
overall_pass_pt  = TH1F('overall_pass_pt' , 'Two-prong number pass overall', pt_bins, pt_low, pt_high)
overall_eff_pt   = TH1F('overall_eff_pt'  , 'Two-prong efficiency pass overall', pt_bins, pt_low, pt_high)

eta_bins = 32
eta_low = -4
eta_high = 4
total_eta = TH1F('total_eta', 'Two-prong total number', eta_bins, eta_low, eta_high)
chargedIso_pass_eta  = TH1F('chargedIso_pass_eta' , 'Two-prong number pass rel charged iso', eta_bins, eta_low, eta_high)
chargedIso_eff_eta   = TH1F('chargedIso_eff_eta'  , 'Two-prong efficiency pass rel charged iso', eta_bins, eta_low, eta_high)
neutralIso_pass_eta  = TH1F('neutralIso_pass_eta' , 'Two-prong number pass rel neutral iso', eta_bins, eta_low, eta_high)
neutralIso_eff_eta   = TH1F('neutralIso_eff_eta'  , 'Two-prong efficiency pass rel neutral iso', eta_bins, eta_low, eta_high)
egammaIso_pass_eta  = TH1F('egammaIso_pass_eta' , 'Two-prong number pass rel egamma iso', eta_bins, eta_low, eta_high)
egammaIso_eff_eta   = TH1F('egammaIso_eff_eta'  , 'Two-prong efficiency pass rel egamma iso', eta_bins, eta_low, eta_high)
photon_req_pass_eta  = TH1F('photon_req_pass_eta' , 'Two-prong number pass photon_req', eta_bins, eta_low, eta_high)
photon_req_eff_eta   = TH1F('photon_req_eff_eta'  , 'Two-prong efficiency pass photon_req', eta_bins, eta_low, eta_high)
overall_pass_eta  = TH1F('overall_pass_eta' , 'Two-prong number pass overall', eta_bins, eta_low, eta_high)
overall_eff_eta   = TH1F('overall_eff_eta'  , 'Two-prong efficiency pass overall', eta_bins, eta_low, eta_high)

phi_bins = 32
phi_low = -4
phi_high = 4
total_phi = TH1F('total_phi', 'Two-prong total number', phi_bins, phi_low, phi_high)
chargedIso_pass_phi  = TH1F('chargedIso_pass_phi' , 'Two-prong number pass rel charged iso', phi_bins, phi_low, phi_high)
chargedIso_eff_phi   = TH1F('chargedIso_eff_phi'  , 'Two-prong efficiency pass rel charged iso', phi_bins, phi_low, phi_high)
neutralIso_pass_phi  = TH1F('neutralIso_pass_phi' , 'Two-prong number pass rel neutral iso', phi_bins, phi_low, phi_high)
neutralIso_eff_phi   = TH1F('neutralIso_eff_phi'  , 'Two-prong efficiency pass rel neutral iso', phi_bins, phi_low, phi_high)
egammaIso_pass_phi  = TH1F('egammaIso_pass_phi' , 'Two-prong number pass rel egamma iso', phi_bins, phi_low, phi_high)
egammaIso_eff_phi   = TH1F('egammaIso_eff_phi'  , 'Two-prong efficiency pass rel egamma iso', phi_bins, phi_low, phi_high)
photon_req_pass_phi  = TH1F('photon_req_pass_phi' , 'Two-prong number pass photon_req', phi_bins, phi_low, phi_high)
photon_req_eff_phi   = TH1F('photon_req_eff_phi'  , 'Two-prong efficiency pass photon_req', phi_bins, phi_low, phi_high)
overall_pass_phi  = TH1F('overall_pass_phi' , 'Two-prong number pass overall', phi_bins, phi_low, phi_high)
overall_eff_phi   = TH1F('overall_eff_phi'  , 'Two-prong efficiency pass overall', phi_bins, phi_low, phi_high)

pv_bins = 40
pv_low = 0
pv_high = 40
total_pv = TH1F('total_pv','Two-prong total number', pv_bins, pv_low, pv_high)
chargedIso_pass_pv  = TH1F('chargedIso_pass_pv' , 'Two-prong number pass rel charged iso', pv_bins, pv_low, pv_high)
chargedIso_eff_pv   = TH1F('chargedIso_eff_pv'  , 'Two-prong efficiency pass rel charged iso', pv_bins, pv_low, pv_high)
neutralIso_pass_pv  = TH1F('neutralIso_pass_pv' , 'Two-prong number pass rel neutral iso', pv_bins, pv_low, pv_high)
neutralIso_eff_pv   = TH1F('neutralIso_eff_pv'  , 'Two-prong efficiency pass rel neutral iso', pv_bins, pv_low, pv_high)
egammaIso_pass_pv  = TH1F('egammaIso_pass_pv' , 'Two-prong number pass rel egamma iso', pv_bins, pv_low, pv_high)
egammaIso_eff_pv   = TH1F('egammaIso_eff_pv'  , 'Two-prong efficiency pass rel egamma iso', pv_bins, pv_low, pv_high)
photon_req_pass_pv  = TH1F('photon_req_pass_pv' , 'Two-prong number pass photon_req', pv_bins, pv_low, pv_high)
photon_req_eff_pv   = TH1F('photon_req_eff_pv'  , 'Two-prong efficiency pass photon_req', pv_bins, pv_low, pv_high)
overall_pass_pv  = TH1F('overall_pass_pv' , 'Two-prong number pass overall', pv_bins, pv_low, pv_high)
overall_eff_pv   = TH1F('overall_eff_pv'  , 'Two-prong efficiency pass overall', pv_bins, pv_low, pv_high)

njet_bins = 25
njet_low = 0
njet_high = 25
total_njet = TH1F('total_njet', 'Two-prong total number', njet_bins, njet_low, njet_high)
chargedIso_pass_njet  = TH1F('chargedIso_pass_njet' , 'Two-prong number pass rel charged iso', njet_bins, njet_low, njet_high)
chargedIso_eff_njet   = TH1F('chargedIso_eff_njet'  , 'Two-prong efficiency pass rel charged iso', njet_bins, njet_low, njet_high)
neutralIso_pass_njet  = TH1F('neutralIso_pass_njet' , 'Two-prong number pass rel neutral iso', njet_bins, njet_low, njet_high)
neutralIso_eff_njet   = TH1F('neutralIso_eff_njet'  , 'Two-prong efficiency pass rel neutral iso', njet_bins, njet_low, njet_high)
egammaIso_pass_njet  = TH1F('egammaIso_pass_njet' , 'Two-prong number pass rel egamma iso', njet_bins, njet_low, njet_high)
egammaIso_eff_njet   = TH1F('egammaIso_eff_njet'  , 'Two-prong efficiency pass rel egamma iso', njet_bins, njet_low, njet_high)
photon_req_pass_njet  = TH1F('photon_req_pass_njet' , 'Two-prong number pass photon_req', njet_bins, njet_low, njet_high)
photon_req_eff_njet   = TH1F('photon_req_eff_njet'  , 'Two-prong efficiency pass photon_req', njet_bins, njet_low, njet_high)
overall_pass_njet  = TH1F('overall_pass_njet' , 'Two-prong number pass overall', njet_bins, njet_low, njet_high)
overall_eff_njet   = TH1F('overall_eff_njet'  , 'Two-prong efficiency pass overall', njet_bins, njet_low, njet_high)

ht_bins = 40
ht_low = 0
ht_high = 4000
total_ht = TH1F('total_ht', 'Two-prong total number', ht_bins, ht_low, ht_high)
chargedIso_pass_ht  = TH1F('chargedIso_pass_ht' , 'Two-prong number pass rel charged iso', ht_bins, ht_low, ht_high)
chargedIso_eff_ht   = TH1F('chargedIso_eff_ht'  , 'Two-prong efficiency pass rel charged iso', ht_bins, ht_low, ht_high)
neutralIso_pass_ht  = TH1F('neutralIso_pass_ht' , 'Two-prong number pass rel neutral iso', ht_bins, ht_low, ht_high)
neutralIso_eff_ht   = TH1F('neutralIso_eff_ht'  , 'Two-prong efficiency pass rel neutral iso', ht_bins, ht_low, ht_high)
egammaIso_pass_ht  = TH1F('egammaIso_pass_ht' , 'Two-prong number pass rel egamma iso', ht_bins, ht_low, ht_high)
egammaIso_eff_ht   = TH1F('egammaIso_eff_ht'  , 'Two-prong efficiency pass rel egamma iso', ht_bins, ht_low, ht_high)
photon_req_pass_ht  = TH1F('photon_req_pass_ht' , 'Two-prong number pass photon_req', ht_bins, ht_low, ht_high)
photon_req_eff_ht   = TH1F('photon_req_eff_ht'  , 'Two-prong efficiency pass photon_req', ht_bins, ht_low, ht_high)
overall_pass_ht  = TH1F('overall_pass_ht' , 'Two-prong number pass overall', ht_bins, ht_low, ht_high)
overall_eff_ht   = TH1F('overall_eff_ht'  , 'Two-prong efficiency pass overall', ht_bins, ht_low, ht_high)

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
    total_pt.Fill(vec.Pt())
    total_eta.Fill(vec.Eta())
    total_phi.Fill(vec.Phi())
    total_pv.Fill(event.nPV)
    total_njet.Fill(event.nJets)
    total_ht.Fill(event.HT)
    if event.Cand_passChargedIso[i]:
      chargedIso_pass_pt.Fill(vec.Pt())
      chargedIso_pass_eta.Fill(vec.Eta())
      chargedIso_pass_phi.Fill(vec.Phi())
      chargedIso_pass_pv.Fill(event.nPV)
      chargedIso_pass_njet.Fill(event.nJets)
      chargedIso_pass_ht.Fill(event.HT)
    if event.Cand_passNeutralIso[i]:
      neutralIso_pass_pt.Fill(vec.Pt())
      neutralIso_pass_eta.Fill(vec.Eta())
      neutralIso_pass_phi.Fill(vec.Phi())
      neutralIso_pass_pv.Fill(event.nPV)
      neutralIso_pass_njet.Fill(event.nJets)
      neutralIso_pass_ht.Fill(event.HT)
    if event.Cand_passEGammaIso[i]:
      egammaIso_pass_pt.Fill(vec.Pt())
      egammaIso_pass_eta.Fill(vec.Eta())
      egammaIso_pass_phi.Fill(vec.Phi())
      egammaIso_pass_pv.Fill(event.nPV)
      egammaIso_pass_njet.Fill(event.nJets)
      egammaIso_pass_ht.Fill(event.HT)
    if event.Cand_passPhotonPt[i]:
      photon_req_pass_pt.Fill(vec.Pt())
      photon_req_pass_eta.Fill(vec.Eta())
      photon_req_pass_phi.Fill(vec.Phi())
      photon_req_pass_pv.Fill(event.nPV)
      photon_req_pass_njet.Fill(event.nJets)
      photon_req_pass_ht.Fill(event.HT)
    if event.Cand_pass[i]:
      overall_pass_pt.Fill(vec.Pt())
      overall_pass_eta.Fill(vec.Eta())
      overall_pass_phi.Fill(vec.Phi())
      overall_pass_pv.Fill(event.nPV)
      overall_pass_njet.Fill(event.nJets)
      overall_pass_ht.Fill(event.HT)

total_pt.Sumw2()
total_eta.Sumw2()
total_phi.Sumw2()
total_pv.Sumw2()
total_njet.Sumw2()
total_ht.Sumw2()

chargedIso_pass_pt.Sumw2()
chargedIso_pass_eta.Sumw2()
chargedIso_pass_phi.Sumw2()
chargedIso_pass_pv.Sumw2()
chargedIso_pass_njet.Sumw2()
chargedIso_pass_ht.Sumw2()

neutralIso_pass_pt.Sumw2()
neutralIso_pass_eta.Sumw2()
neutralIso_pass_phi.Sumw2()
neutralIso_pass_pv.Sumw2()
neutralIso_pass_njet.Sumw2()
neutralIso_pass_ht.Sumw2()

egammaIso_pass_pt.Sumw2()
egammaIso_pass_eta.Sumw2()
egammaIso_pass_phi.Sumw2()
egammaIso_pass_pv.Sumw2()
egammaIso_pass_njet.Sumw2()
egammaIso_pass_ht.Sumw2()

photon_req_pass_pt.Sumw2()
photon_req_pass_eta.Sumw2()
photon_req_pass_phi.Sumw2()
photon_req_pass_pv.Sumw2()
photon_req_pass_njet.Sumw2()
photon_req_pass_ht.Sumw2()

overall_pass_pt.Sumw2()
overall_pass_eta.Sumw2()
overall_pass_phi.Sumw2()
overall_pass_pv.Sumw2()
overall_pass_njet.Sumw2()
overall_pass_ht.Sumw2()

# divide to get efficiencies
chargedIso_eff_pt.Add(chargedIso_pass_pt)
chargedIso_eff_pt.Divide(total_pt)
chargedIso_eff_pt.SetMaximum(1.1)
chargedIso_eff_pt.SetMinimum(0.0)
chargedIso_eff_pt.GetXaxis().SetTitle("p_{T}")
neutralIso_eff_pt.Add(neutralIso_pass_pt)
neutralIso_eff_pt.Divide(total_pt)
neutralIso_eff_pt.SetMaximum(1.1)
neutralIso_eff_pt.SetMinimum(0.0)
neutralIso_eff_pt.GetXaxis().SetTitle("p_{T}")
egammaIso_eff_pt.Add(egammaIso_pass_pt)
egammaIso_eff_pt.Divide(total_pt)
egammaIso_eff_pt.SetMaximum(1.1)
egammaIso_eff_pt.SetMinimum(0.0)
egammaIso_eff_pt.GetXaxis().SetTitle("p_{T}")
photon_req_eff_pt.Add(photon_req_pass_pt)
photon_req_eff_pt.Divide(total_pt)
photon_req_eff_pt.SetMaximum(1.1)
photon_req_eff_pt.SetMinimum(0.0)
photon_req_eff_pt.GetXaxis().SetTitle("p_{T}")
overall_eff_pt.Add(overall_pass_pt)
overall_eff_pt.Divide(total_pt)
overall_eff_pt.SetMaximum(1.1)
overall_eff_pt.SetMinimum(0.0)
overall_eff_pt.GetXaxis().SetTitle("p_{T}")

chargedIso_eff_eta.Add(chargedIso_pass_eta)
chargedIso_eff_eta.Divide(total_eta)
chargedIso_eff_eta.SetMaximum(1.1)
chargedIso_eff_eta.SetMinimum(0.0)
chargedIso_eff_eta.GetXaxis().SetTitle("\eta")
neutralIso_eff_eta.Add(neutralIso_pass_eta)
neutralIso_eff_eta.Divide(total_eta)
neutralIso_eff_eta.SetMaximum(1.1)
neutralIso_eff_eta.SetMinimum(0.0)
neutralIso_eff_eta.GetXaxis().SetTitle("\eta")
egammaIso_eff_eta.Add(egammaIso_pass_eta)
egammaIso_eff_eta.Divide(total_eta)
egammaIso_eff_eta.SetMaximum(1.1)
egammaIso_eff_eta.SetMinimum(0.0)
egammaIso_eff_eta.GetXaxis().SetTitle("\eta")
photon_req_eff_eta.Add(photon_req_pass_eta)
photon_req_eff_eta.Divide(total_eta)
photon_req_eff_eta.SetMaximum(1.1)
photon_req_eff_eta.SetMinimum(0.0)
photon_req_eff_eta.GetXaxis().SetTitle("\eta")
overall_eff_eta.Add(overall_pass_eta)
overall_eff_eta.Divide(total_eta)
overall_eff_eta.SetMaximum(1.1)
overall_eff_eta.SetMinimum(0.0)
overall_eff_eta.GetXaxis().SetTitle("\eta")

chargedIso_eff_phi.Add(chargedIso_pass_phi)
chargedIso_eff_phi.Divide(total_phi)
chargedIso_eff_phi.SetMaximum(1.1)
chargedIso_eff_phi.SetMinimum(0.0)
chargedIso_eff_phi.GetXaxis().SetTitle("\phi")
neutralIso_eff_phi.Add(neutralIso_pass_phi)
neutralIso_eff_phi.Divide(total_phi)
neutralIso_eff_phi.SetMaximum(1.1)
neutralIso_eff_phi.SetMinimum(0.0)
neutralIso_eff_phi.GetXaxis().SetTitle("\phi")
egammaIso_eff_phi.Add(egammaIso_pass_phi)
egammaIso_eff_phi.Divide(total_phi)
egammaIso_eff_phi.SetMaximum(1.1)
egammaIso_eff_phi.SetMinimum(0.0)
egammaIso_eff_phi.GetXaxis().SetTitle("\phi")
photon_req_eff_phi.Add(photon_req_pass_phi)
photon_req_eff_phi.Divide(total_phi)
photon_req_eff_phi.SetMaximum(1.1)
photon_req_eff_phi.SetMinimum(0.0)
photon_req_eff_phi.GetXaxis().SetTitle("\phi")
overall_eff_phi.Add(overall_pass_phi)
overall_eff_phi.Divide(total_phi)
overall_eff_phi.SetMaximum(1.1)
overall_eff_phi.SetMinimum(0.0)
overall_eff_phi.GetXaxis().SetTitle("\phi")

chargedIso_eff_pv.Add(chargedIso_pass_pv)
chargedIso_eff_pv.Divide(total_pv)
chargedIso_eff_pv.SetMaximum(1.1)
chargedIso_eff_pv.SetMinimum(0.0)
chargedIso_eff_pv.GetXaxis().SetTitle("num PV")
neutralIso_eff_pv.Add(neutralIso_pass_pv)
neutralIso_eff_pv.Divide(total_pv)
neutralIso_eff_pv.SetMaximum(1.1)
neutralIso_eff_pv.SetMinimum(0.0)
neutralIso_eff_pv.GetXaxis().SetTitle("num PV")
egammaIso_eff_pv.Add(egammaIso_pass_pv)
egammaIso_eff_pv.Divide(total_pv)
egammaIso_eff_pv.SetMaximum(1.1)
egammaIso_eff_pv.SetMinimum(0.0)
egammaIso_eff_pv.GetXaxis().SetTitle("num PV")
photon_req_eff_pv.Add(photon_req_pass_pv)
photon_req_eff_pv.Divide(total_pv)
photon_req_eff_pv.SetMaximum(1.1)
photon_req_eff_pv.SetMinimum(0.0)
photon_req_eff_pv.GetXaxis().SetTitle("num PV")
overall_eff_pv.Add(overall_pass_pv)
overall_eff_pv.Divide(total_pv)
overall_eff_pv.SetMaximum(1.1)
overall_eff_pv.SetMinimum(0.0)
overall_eff_pv.GetXaxis().SetTitle("num PV")

chargedIso_eff_njet.Add(chargedIso_pass_njet)
chargedIso_eff_njet.Divide(total_njet)
chargedIso_eff_njet.SetMaximum(1.1)
chargedIso_eff_njet.SetMinimum(0.0)
chargedIso_eff_njet.GetXaxis().SetTitle("num ak4 jets")
neutralIso_eff_njet.Add(neutralIso_pass_njet)
neutralIso_eff_njet.Divide(total_njet)
neutralIso_eff_njet.SetMaximum(1.1)
neutralIso_eff_njet.SetMinimum(0.0)
neutralIso_eff_njet.GetXaxis().SetTitle("num ak4 jets")
egammaIso_eff_njet.Add(egammaIso_pass_njet)
egammaIso_eff_njet.Divide(total_njet)
egammaIso_eff_njet.SetMaximum(1.1)
egammaIso_eff_njet.SetMinimum(0.0)
egammaIso_eff_njet.GetXaxis().SetTitle("num ak4 jets")
photon_req_eff_njet.Add(photon_req_pass_njet)
photon_req_eff_njet.Divide(total_njet)
photon_req_eff_njet.SetMaximum(1.1)
photon_req_eff_njet.SetMinimum(0.0)
photon_req_eff_njet.GetXaxis().SetTitle("num ak4 jets")
overall_eff_njet.Add(overall_pass_njet)
overall_eff_njet.Divide(total_njet)
overall_eff_njet.SetMaximum(1.1)
overall_eff_njet.SetMinimum(0.0)
overall_eff_njet.GetXaxis().SetTitle("num ak4 jets")

chargedIso_eff_ht.Add(chargedIso_pass_ht)
chargedIso_eff_ht.Divide(total_ht)
chargedIso_eff_ht.SetMaximum(1.1)
chargedIso_eff_ht.SetMinimum(0.0)
chargedIso_eff_ht.GetXaxis().SetTitle("H_{T}")
neutralIso_eff_ht.Add(neutralIso_pass_ht)
neutralIso_eff_ht.Divide(total_ht)
neutralIso_eff_ht.SetMaximum(1.1)
neutralIso_eff_ht.SetMinimum(0.0)
neutralIso_eff_ht.GetXaxis().SetTitle("H_{T}")
egammaIso_eff_ht.Add(egammaIso_pass_ht)
egammaIso_eff_ht.Divide(total_ht)
egammaIso_eff_ht.SetMaximum(1.1)
egammaIso_eff_ht.SetMinimum(0.0)
egammaIso_eff_ht.GetXaxis().SetTitle("H_{T}")
photon_req_eff_ht.Add(photon_req_pass_ht)
photon_req_eff_ht.Divide(total_ht)
photon_req_eff_ht.SetMaximum(1.1)
photon_req_eff_ht.SetMinimum(0.0)
photon_req_eff_ht.GetXaxis().SetTitle("H_{T}")
overall_eff_ht.Add(overall_pass_ht)
overall_eff_ht.Divide(total_ht)
overall_eff_ht.SetMaximum(1.1)
overall_eff_ht.SetMinimum(0.0)
overall_eff_ht.GetXaxis().SetTitle("H_{T}")

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
