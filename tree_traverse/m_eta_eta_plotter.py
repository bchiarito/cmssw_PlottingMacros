import ROOT
from array import array
from math import *
import sys
import os
import glob
import fnmatch
from optparse import OptionParser

path = "samples/trees_v2.0/SinglePhoton_runD"
tree = "diphotonAnalyzer/fTree2"

bins = 100
low = 0
high = 40
title = "dEta"

outputfile = ROOT.TFile("dEta.root", "recreate")

dEta = ROOT.TH1F("dEta", "dEta", bins, low, high)

ROOT.gROOT.ProcessLine(
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
Photon = ROOT.recoPhotonInfo_t()

# Make TChain for inner loop
chain = ROOT.TChain(tree)
rootfiles = []
for root, dirnames, filenames in os.walk(path):
  for filename in fnmatch.filter(filenames, '*.root'):
    rootfiles.append(os.path.join(root, filename))
for rootfile in rootfiles:
  chain.Add(rootfile)
chain.SetBranchAddress("Photon1", ROOT.AddressOf(Photon, "pt") )

total = chain.GetEntries()
count = 0
for event in chain:
  if count % 100000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing outer TTree {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )

  chain.GetEntry(count)

  TwoProng = ROOT.TLorentzVector()
  Gamma = ROOT.TLorentzVector()

  if event.nPass >= 1 and event.nTightPhoton >= 1:
    TwoProng.SetPtEtaPhiM(event.Eta_pt[0], event.Eta_eta[0], event.Eta_phi[0], event.Eta_mass[0]) 
    Gamma.SetPtEtaPhiM(Photon.pt, Photon.eta, Photon.phi, 0)
    Phi = TwoProng + Gamma
    dEta.Fill(abs(TwoProng.Eta() - Gamma.Eta()))

  count += 1

# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
