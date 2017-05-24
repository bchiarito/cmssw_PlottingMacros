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
parser.add_option('--drcut', action='store_true', default=False,
                  dest='drcut',
                  help='')
parser.add_option('--selection',
                  dest='selection', default="",
                  help='photon / jet')
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
"struct recoPhotonInfo_t {\
    Double_t pt;\
    Double_t eta;\
    Double_t phi;\
    Double_t detEta;\
    Double_t detPhi;\
    Double_t r9;\
    Double_t sigmaIetaIeta;\
    Double_t sigmaEtaEta;\
    Double_t sigmaIphiIphi;\
    Double_t sigmaPhiPhi;\
    Double_t maxEnergyXtal;\
    Double_t e1x5;\
    Double_t e2x5;\
    Double_t e3x3;\
    Double_t e5x5;\
    Double_t r1x5;\
    Double_t r2x5;\
    Double_t swisscross;\
    Double_t eMax;\
    Double_t eLeft;\
    Double_t eRight;\
    Double_t eTop;\
    Double_t eBottom;\
    Double_t eSecond;\
    Double_t e2x2;\
    Double_t e4x4;\
    Double_t e2e9;\
    Double_t maxRecHitTime;\
    Double_t sumRecHitsEnergiesNoKGood;\
    Double_t RecHitsNoKGoodEnergyRatio;\
    Double_t hadOverEm;\
    Double_t hadTowerOverEm;\
    Double_t hadDepth1OverEm;\
    Double_t hadDepth2OverEm;\
    Double_t hcalIso04;\
    Double_t hcalIso03;\
    Double_t ecalIso04;\
    Double_t ecalIso03;\
    Double_t trkIsoSumPtHollow04;\
    Double_t trkIsoSumPtSolid04;\
    Double_t trkIsoSumPtHollow03;\
    Double_t trkIsoSumPtSolid03;\
    Double_t PFIsoCharged04;\
    Double_t PFIsoNeutral04;\
    Double_t PFIsoPhoton04;\
    Double_t PFIsoAll04;\
    Double_t PFIsoCharged03;\
    Double_t PFIsoNeutral03;\
    Double_t PFIsoPhoton03;\
    Double_t PFIsoAll03;\
    Double_t PFIsoCharged02;\
    Double_t PFIsoNeutral02;\
    Double_t PFIsoPhoton02;\
    Double_t PFIsoAll02;\
    Double_t rhocorPFIsoCharged04;\
    Double_t rhocorPFIsoNeutral04;\
    Double_t rhocorPFIsoPhoton04;\
    Double_t rhocorPFIsoAll04;\
    Double_t rhocorPFIsoCharged03;\
    Double_t rhocorPFIsoNeutral03;\
    Double_t rhocorPFIsoPhoton03;\
    Double_t rhocorPFIsoAll03;\
    Double_t rhocorPFIsoCharged02;\
    Double_t rhocorPFIsoNeutral02;\
    Double_t rhocorPFIsoPhoton02;\
    Double_t rhocorPFIsoAll02;\
    Double_t EAPhotonHighPtID;\
    Double_t alphaPhotonHighPtID;\
    Double_t kappaPhotonHighPtID;\
    Double_t corPhotonIsoHighPtID;\
    Double_t esRatio;\
    Double_t scEta;\
    Double_t scPhi;\
    Double_t scRawEnergy;\
    Double_t scPreshowerEnergy;\
    Double_t scPhiWidth;\
    Double_t scEtaWidth;\
    Double_t seedEnergy;\
    Double_t satSeedEnergy;\
    Int_t scNumBasicClusters;\
    Int_t trkIsoNtrksHollow03;\
    Int_t trkIsoNtrksSolid03;\
    Int_t trkIsoNtrksHollow04;\
    Int_t trkIsoNtrksSolid04;\
    Int_t severityLevel;\
    Int_t recHitFlag;\
    Int_t detId;\
    Int_t iEtaY;\
    Int_t iPhiX;\
    Int_t numRecHitsNoKGood;\
    Int_t nSatCells;\
    Bool_t isEB;\
    Bool_t isEE;\
    Bool_t isEBEtaGap;\
    Bool_t isEBPhiGap;\
    Bool_t isEERingGap;\
    Bool_t isEEDeeGap;\
    Bool_t isEBEEGap;\
    Bool_t hasPixelSeed;\
    Bool_t hasMatchedPromptElec;\
    Bool_t isFakeable;\
    Bool_t isTightDetPhoton;\
    Bool_t isTightPFPhoton;\
    Bool_t isMediumPFPhoton;\
    Bool_t isLoosePFPhoton;\
    Bool_t isHighPtPFPhoton;\
    Bool_t hasGoodRecHits;\
    Bool_t isSaturated;\
  };")
Photon1 = recoPhotonInfo_t()
chain.SetBranchAddress("Photon1", AddressOf(Photon1, "pt") )

# binning
num_even_mass_bins = 9
even_mass_bins_array = [0,.400,.600,.800,1.000,1.200,1.400,1.600,1.800,2.000]
even_mass_bins = array('d', even_mass_bins_array)
num_odd_mass_bins = 9
odd_mass_bins_array = [0,.300,.500,.700,.900,1.100,1.300,1.500,1.700,1.900]
odd_mass_bins = array('d', odd_mass_bins_array)

num_pt_bins = 26
pt_low = 0
pt_high = 1300
num_eta_bins = 20
eta_low = -5
eta_high = 5
num_phi_bins = 24
phi_low = -3.15
phi_high = 3.15
num_ecal_bins = 26
ecal_low = 0
ecal_high = 1300
num_hcal_bins = 26
hcal_low = 0
hcal_high = 1300

# histograms
FakeNume_even_pt = TH2D("twoprongfakenume_even_pt","Fake Numerator count, pt vs even mass bins",num_pt_bins,pt_low,pt_high,num_even_mass_bins,even_mass_bins)
FakeDeno_even_pt = TH2D("twoprongfakedeno_even_pt","Fake Denominator count, pt vs even mass bins",num_pt_bins,pt_low,pt_high,num_even_mass_bins,even_mass_bins)
FakeRate_even_pt = TH2D("twoprongfakerate_even_pt","Fake Rate, pt vs even mass bins",num_pt_bins,pt_low,pt_high,num_even_mass_bins,even_mass_bins)
FakeNume_odd_pt = TH2D("twoprongfakenume_odd_pt","Fake Numerator count, pt vs odd mass bins",num_pt_bins,pt_low,pt_high,num_odd_mass_bins,odd_mass_bins)
FakeDeno_odd_pt = TH2D("twoprongfakedeno_odd_pt","Fake Denominator count, pt vs odd mass bins",num_pt_bins,pt_low,pt_high,num_odd_mass_bins,odd_mass_bins)
FakeRate_odd_pt = TH2D("twoprongfakerate_odd_pt","Fake Rate, pt vs odd mass bins",num_pt_bins,pt_low,pt_high,num_odd_mass_bins,odd_mass_bins)

FakeNume_even_ecal = TH2D("twoprongfakenume_even_ecal","Fake Numerator count, ecal vs even mass bins",num_ecal_bins,ecal_low,ecal_high,num_even_mass_bins,even_mass_bins)
FakeDeno_even_ecal = TH2D("twoprongfakedeno_even_ecal","Fake Denominator count, ecal vs even mass bins",num_ecal_bins,ecal_low,ecal_high,num_even_mass_bins,even_mass_bins)
FakeRate_even_ecal = TH2D("twoprongfakerate_even_ecal","Fake Rate, ecal vs even mass bins",num_ecal_bins,ecal_low,ecal_high,num_even_mass_bins,even_mass_bins)
FakeNume_odd_ecal = TH2D("twoprongfakenume_odd_ecal","Fake Numerator count, ecal vs odd mass bins",num_ecal_bins,ecal_low,ecal_high,num_odd_mass_bins,odd_mass_bins)
FakeDeno_odd_ecal = TH2D("twoprongfakedeno_odd_ecal","Fake Denominator count, ecal vs odd mass bins",num_ecal_bins,ecal_low,ecal_high,num_odd_mass_bins,odd_mass_bins)
FakeRate_odd_ecal = TH2D("twoprongfakerate_odd_ecal","Fake Rate, ecal vs odd mass bins",num_ecal_bins,ecal_low,ecal_high,num_odd_mass_bins,odd_mass_bins)

FakeNume_even_hcal = TH2D("twoprongfakenume_even_hcal","Fake Numerator count, hcal vs even mass bins",num_hcal_bins,hcal_low,hcal_high,num_even_mass_bins,even_mass_bins)
FakeDeno_even_hcal = TH2D("twoprongfakedeno_even_hcal","Fake Denominator count, hcal vs even mass bins",num_hcal_bins,hcal_low,hcal_high,num_even_mass_bins,even_mass_bins)
FakeRate_even_hcal = TH2D("twoprongfakerate_even_hcal","Fake Rate, hcal vs even mass bins",num_hcal_bins,hcal_low,hcal_high,num_even_mass_bins,even_mass_bins)
FakeNume_odd_hcal = TH2D("twoprongfakenume_odd_hcal","Fake Numerator count, hcal vs odd mass bins",num_hcal_bins,hcal_low,hcal_high,num_odd_mass_bins,odd_mass_bins)
FakeDeno_odd_hcal = TH2D("twoprongfakedeno_odd_hcal","Fake Denominator count, hcal vs odd mass bins",num_hcal_bins,hcal_low,hcal_high,num_odd_mass_bins,odd_mass_bins)
FakeRate_odd_hcal = TH2D("twoprongfakerate_odd_hcal","Fake Rate, hcal vs odd mass bins",num_hcal_bins,hcal_low,hcal_high,num_odd_mass_bins,odd_mass_bins)

FakeNume_even_eta = TH2D("twoprongfakenume_even_eta","Fake Numerator count, eta vs even mass bins",num_eta_bins,eta_low,eta_high,num_even_mass_bins,even_mass_bins)
FakeDeno_even_eta = TH2D("twoprongfakedeno_even_eta","Fake Denominator count, eta vs even mass bins",num_eta_bins,eta_low,eta_high,num_even_mass_bins,even_mass_bins)
FakeRate_even_eta = TH2D("twoprongfakerate_even_eta","Fake Rate, eta vs even mass bins",num_eta_bins,eta_low,eta_high,num_even_mass_bins,even_mass_bins)
FakeNume_odd_eta = TH2D("twoprongfakenume_odd_eta","Fake Numerator count, eta vs odd mass bins",num_eta_bins,eta_low,eta_high,num_odd_mass_bins,odd_mass_bins)
FakeDeno_odd_eta = TH2D("twoprongfakedeno_odd_eta","Fake Denominator count, eta vs odd mass bins",num_eta_bins,eta_low,eta_high,num_odd_mass_bins,odd_mass_bins)
FakeRate_odd_eta = TH2D("twoprongfakerate_odd_eta","Fake Rate, eta vs odd mass bins",num_eta_bins,eta_low,eta_high,num_odd_mass_bins,odd_mass_bins)

FakeNume_even_phi = TH2D("twoprongfakenume_even_phi","Fake Numerator count, phi vs even mass bins",num_phi_bins,phi_low,phi_high,num_even_mass_bins,even_mass_bins)
FakeDeno_even_phi = TH2D("twoprongfakedeno_even_phi","Fake Denominator count, phi vs even mass bins",num_phi_bins,phi_low,phi_high,num_even_mass_bins,even_mass_bins)
FakeRate_even_phi = TH2D("twoprongfakerate_even_phi","Fake Rate, phi vs even mass bins",num_phi_bins,phi_low,phi_high,num_even_mass_bins,even_mass_bins)
FakeNume_odd_phi = TH2D("twoprongfakenume_odd_phi","Fake Numerator count, phi vs odd mass bins",num_phi_bins,phi_low,phi_high,num_odd_mass_bins,odd_mass_bins)
FakeDeno_odd_phi = TH2D("twoprongfakedeno_odd_phi","Fake Denominator count, phi vs odd mass bins",num_phi_bins,phi_low,phi_high,num_odd_mass_bins,odd_mass_bins)
FakeRate_odd_phi = TH2D("twoprongfakerate_odd_phi","Fake Rate, phi vs odd mass bins",num_phi_bins,phi_low,phi_high,num_odd_mass_bins,odd_mass_bins)

FakeNume_pt_vs_eta = TH2D("twoprongfakenume_pt_vs_eta", "Fake Numerator count, pt vs eta", num_pt_bins,pt_low,pt_high,num_eta_bins,eta_low,eta_high)
FakeDeno_pt_vs_eta = TH2D("twoprongfakedeno_pt_vs_eta", "Fake Denominator count, pt vs eta", num_pt_bins,pt_low,pt_high,num_eta_bins,eta_low,eta_high)
FakeRate_pt_vs_eta = TH2D("twoprongfakerate_pt_vs_eta", "Fake Rate, pt vs eta", num_pt_bins,pt_low,pt_high,num_eta_bins,eta_low,eta_high)

dr_tight = TH1D('dr_tight', 'DR twoprong tight to leading object', 60, 0, 6)
dr_loose = TH1D('dr_loose', 'DR twoprong loose to leading object', 60, 0, 6)

# event loop
count = 0
total = chain.GetEntries()
for event in chain:
  if count % 100000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  # Apply event selection
  fail_selection = False
  has_leading_photon = False
  has_leading_jet = False
  if event.nPhotons >= 1:
    photon = TLorentzVector()
    photon.SetPtEtaPhiM(event.photon_pt[0], event.photon_eta[0], event.photon_phi[0], event.photon_mass[0])
    if photon.Pt() > 150:
      has_leading_photon = True
  if event.nJets >= 1:
    jet = TLorentzVector()
    jet.SetPtEtaPhiM(event.jet_pt[0], event.jet_eta[0], event.jet_phi[0], event.jet_mass[0])
    has_leading_jet = True

  if options.selection == 'photon':
    if has_leading_photon:
      for i in range(len(event.TwoProng_pt)):
        vec = TLorentzVector()
        vec.SetPtEtaPhiM(event.TwoProng_pt[i], event.TwoProng_eta[i], event.TwoProng_phi[i], event.TwoProng_mass[i])
        dr_to_lead = photon.DeltaR(vec)
        dr_tight.Fill(dr_to_lead)
        if options.drcut and dr_to_lead < 0.3:
          fail_selection = True
      for i in range(len(event.TwoProngLoose_pt)):
        vec = TLorentzVector()
        vec.SetPtEtaPhiM(event.TwoProngLoose_pt[i], event.TwoProngLoose_eta[i], event.TwoProngLoose_phi[i], event.TwoProngLoose_mass[i])
        dr_to_lead = photon.DeltaR(vec)
        dr_loose.Fill(dr_to_lead)
        if options.drcut and dr_to_lead < 0.3:
          fail_selection = True
    else:
      fail_selection = True # fail if no leading photon
  if options.selection == 'jet':
    if has_leading_jet:
      for i in range(len(event.TwoProng_pt)):
        vec = TLorentzVector()
        vec.SetPtEtaPhiM(event.TwoProng_pt[i], event.TwoProng_eta[i], event.TwoProng_phi[i], event.TwoProng_mass[i])
        dr_to_lead = jet.DeltaR(vec)
        dr_tight.Fill(dr_to_lead)
        if options.drcut and dr_to_lead < 0.3:
          fail_selection = True
      for i in range(len(event.TwoProngLoose_pt)):
        vec = TLorentzVector()
        vec.SetPtEtaPhiM(event.TwoProngLoose_pt[i], event.TwoProngLoose_eta[i], event.TwoProngLoose_phi[i], event.TwoProngLoose_mass[i])
        dr_to_lead = jet.DeltaR(vec)
        dr_loose.Fill(dr_to_lead)
        if options.drcut and dr_to_lead < 0.3:
          fail_selection = True
    else:
      fail_selection = True # fail if no leading jet

  if not fail_selection: 
    # Fill fake count histograms
    for i in range(len(event.TwoProng_pt)):
      FakeNume_even_pt.Fill(event.TwoProng_pt[i], event.TwoProng_Mass[i])
      FakeNume_odd_pt.Fill(event.TwoProng_pt[i], event.TwoProng_Mass[i])
      FakeNume_even_eta.Fill(event.TwoProng_eta[i], event.TwoProng_Mass[i])
      FakeNume_odd_eta.Fill(event.TwoProng_eta[i], event.TwoProng_Mass[i])
      FakeNume_even_phi.Fill(event.TwoProng_phi[i], event.TwoProng_Mass[i])
      FakeNume_odd_phi.Fill(event.TwoProng_phi[i], event.TwoProng_Mass[i])
      FakeNume_even_ecal.Fill(event.TwoProng_photon_pt[i], event.TwoProng_Mass[i])
      FakeNume_odd_ecal.Fill(event.TwoProng_photon_pt[i], event.TwoProng_Mass[i])
      FakeNume_even_hcal.Fill(event.TwoProng_CHpos_pt[i]+event.TwoProng_CHneg_pt[i], event.TwoProng_Mass[i])
      FakeNume_odd_hcal.Fill(event.TwoProng_CHpos_pt[i]+event.TwoProng_CHneg_pt[i], event.TwoProng_Mass[i])

      FakeNume_pt_vs_eta.Fill(event.TwoProng_pt[i], event.TwoProng_eta[i])
      
    for i in range(len(event.TwoProngLoose_pt)):
      FakeDeno_even_pt.Fill(event.TwoProngLoose_pt[i], event.TwoProngLoose_Mass[i])
      FakeDeno_odd_pt.Fill(event.TwoProngLoose_pt[i], event.TwoProngLoose_Mass[i])
      FakeDeno_even_eta.Fill(event.TwoProngLoose_eta[i], event.TwoProngLoose_Mass[i])
      FakeDeno_odd_eta.Fill(event.TwoProngLoose_eta[i], event.TwoProngLoose_Mass[i])
      FakeDeno_even_phi.Fill(event.TwoProngLoose_phi[i], event.TwoProngLoose_Mass[i])
      FakeDeno_odd_phi.Fill(event.TwoProngLoose_phi[i], event.TwoProngLoose_Mass[i])
      FakeDeno_even_ecal.Fill(event.TwoProngLoose_photon_pt[i], event.TwoProngLoose_Mass[i])
      FakeDeno_odd_ecal.Fill(event.TwoProngLoose_photon_pt[i], event.TwoProngLoose_Mass[i])
      FakeDeno_even_hcal.Fill(event.TwoProngLoose_CHpos_pt[i]+event.TwoProngLoose_CHneg_pt[i], event.TwoProngLoose_Mass[i])
      FakeDeno_odd_hcal.Fill(event.TwoProngLoose_CHpos_pt[i]+event.TwoProngLoose_CHneg_pt[i], event.TwoProngLoose_Mass[i])

      FakeDeno_pt_vs_eta.Fill(event.TwoProngLoose_pt[i], event.TwoProngLoose_eta[i])

# Calculate fake rates
FakeNume_even_pt.Sumw2()
FakeNume_even_eta.Sumw2()
FakeNume_even_phi.Sumw2()
FakeNume_even_ecal.Sumw2()
FakeNume_even_hcal.Sumw2()
FakeNume_odd_pt.Sumw2()
FakeNume_odd_eta.Sumw2()
FakeNume_odd_phi.Sumw2()
FakeNume_odd_ecal.Sumw2()
FakeNume_odd_hcal.Sumw2()
FakeDeno_even_pt.Sumw2()
FakeDeno_even_eta.Sumw2()
FakeDeno_even_phi.Sumw2()
FakeDeno_even_ecal.Sumw2()
FakeDeno_even_hcal.Sumw2()
FakeDeno_odd_pt.Sumw2()
FakeDeno_odd_eta.Sumw2()
FakeDeno_odd_phi.Sumw2()
FakeDeno_odd_ecal.Sumw2()
FakeDeno_odd_hcal.Sumw2()
FakeNume_pt_vs_eta.Sumw2()
FakeDeno_pt_vs_eta.Sumw2()

FakeRate_even_pt.Add(FakeNume_even_pt)
FakeRate_even_pt.Divide(FakeDeno_even_pt)
FakeRate_odd_pt.Add(FakeNume_odd_pt)
FakeRate_odd_pt.Divide(FakeDeno_odd_pt)

FakeRate_even_eta.Add(FakeNume_even_eta)
FakeRate_even_eta.Divide(FakeDeno_even_eta)
FakeRate_odd_eta.Add(FakeNume_odd_eta)
FakeRate_odd_eta.Divide(FakeDeno_odd_eta)

FakeRate_even_phi.Add(FakeNume_even_phi)
FakeRate_even_phi.Divide(FakeDeno_even_phi)
FakeRate_odd_phi.Add(FakeNume_odd_phi)
FakeRate_odd_phi.Divide(FakeDeno_odd_phi)

FakeRate_even_ecal.Add(FakeNume_even_ecal)
FakeRate_even_ecal.Divide(FakeDeno_even_ecal)
FakeRate_odd_ecal.Add(FakeNume_odd_ecal)
FakeRate_odd_ecal.Divide(FakeDeno_odd_ecal)

FakeRate_even_hcal.Add(FakeNume_even_hcal)
FakeRate_even_hcal.Divide(FakeDeno_even_hcal)
FakeRate_odd_hcal.Add(FakeNume_odd_hcal)
FakeRate_odd_hcal.Divide(FakeDeno_odd_hcal)

FakeRate_pt_vs_eta.Add(FakeNume_pt_vs_eta)
FakeRate_pt_vs_eta.Divide(FakeDeno_pt_vs_eta)

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
