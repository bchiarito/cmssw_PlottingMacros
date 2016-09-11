import ROOT
from array import array
from math import *
import sys
import os
import glob
import fnmatch
from optparse import OptionParser

path = "samples/trees/trees/SinglePhoton/crab_SinglePhoton_RunD/"
tree = "diphotonAnalyzer/fTree2"

bins = 71
low = 0
high = 5000
title = "M_GammaEta"

outputfile = ROOT.TFile("m_gamma_eta_wfakeratepred_histograms.root", "recreate")

m_gammaEta = ROOT.TH1F("m_gammaEta", "M_GammaEta", bins, low, high)
m_gammaEta_Endcap = ROOT.TH1F("m_gammaEta_Endcap", "M_GammaEta_Endcap", bins, low, high)
m_gammaEta_Barrel = ROOT.TH1F("m_gammaEta_Barrel", "M_GammaEta_Barrel", bins, low, high)
m_gammaEta_0_2000 = ROOT.TH1F("m_gammaEta_0_2000", "M_GammaEta_massWindow_0to2000", bins, low, high)
m_gammaEta_0_2000_Endcap = ROOT.TH1F("m_gammaEta_0_2000_Endcap", "M_GammaEta_massWindow_0to2000_Endcap", bins, low, high)
m_gammaEta_0_2000_Barrel = ROOT.TH1F("m_gammaEta_0_2000_Barrel", "M_GammaEta_massWindow_0to2000_Barrel", bins, low, high)

m_gammaEta_0_400 = ROOT.TH1F("m_gammaEta_0_400", "M_GammaEta_massWindow_0to400", bins, low, high)
m_gammaEta_400_600 = ROOT.TH1F("m_gammaEta_400_600", "M_GammaEta_massWindow_400to600", bins, low, high)
m_gammaEta_500_700 = ROOT.TH1F("m_gammaEta_500_700", "M_GammaEta_massWindow_500to700", bins, low, high)
m_gammaEta_600_800 = ROOT.TH1F("m_gammaEta_600_800", "M_GammaEta_massWindow_600to800", bins, low, high)
m_gammaEta_700_900 = ROOT.TH1F("m_gammaEta_700_900", "M_GammaEta_massWindow_700to900", bins, low, high)
m_gammaEta_800_1000 = ROOT.TH1F("m_gammaEta_800_1000", "M_GammaEta_massWindow_800to1000", bins, low, high)
m_gammaEta_900_1100 = ROOT.TH1F("m_gammaEta_900_1100", "M_GammaEta_massWindow_900to1100", bins, low, high)
m_gammaEta_1000_1200 = ROOT.TH1F("m_gammaEta_1000_1200", "M_GammaEta_massWindow_1000to1200", bins, low, high)
m_gammaEta_1100_1300 = ROOT.TH1F("m_gammaEta_1100_1300", "M_GammaEta_massWindow_1100to1300", bins, low, high)
m_gammaEta_1200_1400 = ROOT.TH1F("m_gammaEta_1200_1400", "M_GammaEta_massWindow_1200to1400", bins, low, high)
m_gammaEta_1300_1500 = ROOT.TH1F("m_gammaEta_1300_1500", "M_GammaEta_massWindow_1300to1500", bins, low, high)
m_gammaEta_1400_1600 = ROOT.TH1F("m_gammaEta_1400_1600", "M_GammaEta_massWindow_1400to1600", bins, low, high)
m_gammaEta_1500_1700 = ROOT.TH1F("m_gammaEta_1500_1700", "M_GammaEta_massWindow_1500to1700", bins, low, high)
m_gammaEta_1600_1800 = ROOT.TH1F("m_gammaEta_1600_1800", "M_GammaEta_massWindow_1600to1800", bins, low, high)
m_gammaEta_1700_1900 = ROOT.TH1F("m_gammaEta_1700_1900", "M_GammaEta_massWindow_1700to1900", bins, low, high)
m_gammaEta_1800_2000 = ROOT.TH1F("m_gammaEta_1800_2000", "M_GammaEta_massWindow_1800to2000", bins, low, high)

m_gammaEta_0_400_Endcap = ROOT.TH1F("m_gammaEta_0_400_Endcap", "M_GammaEta_massWindow_0to400_Endcap", bins, low, high)
m_gammaEta_400_600_Endcap = ROOT.TH1F("m_gammaEta_400_600_Endcap", "M_GammaEta_massWindow_400to600_Endcap", bins, low, high)
m_gammaEta_500_700_Endcap = ROOT.TH1F("m_gammaEta_500_700_Endcap", "M_GammaEta_massWindow_500to700_Endcap", bins, low, high)
m_gammaEta_600_800_Endcap = ROOT.TH1F("m_gammaEta_600_800_Endcap", "M_GammaEta_massWindow_600to800_Endcap", bins, low, high)
m_gammaEta_700_900_Endcap = ROOT.TH1F("m_gammaEta_700_900_Endcap", "M_GammaEta_massWindow_700to900_Endcap", bins, low, high)
m_gammaEta_800_1000_Endcap = ROOT.TH1F("m_gammaEta_800_1000_Endcap", "M_GammaEta_massWindow_800to1000_Endcap", bins, low, high)
m_gammaEta_900_1100_Endcap = ROOT.TH1F("m_gammaEta_900_1100_Endcap", "M_GammaEta_massWindow_900to1100_Endcap", bins, low, high)
m_gammaEta_1000_1200_Endcap = ROOT.TH1F("m_gammaEta_1000_1200_Endcap", "M_GammaEta_massWindow_1000to1200_Endcap", bins, low, high)
m_gammaEta_1100_1300_Endcap = ROOT.TH1F("m_gammaEta_1100_1300_Endcap", "M_GammaEta_massWindow_1100to1300_Endcap", bins, low, high)
m_gammaEta_1200_1400_Endcap = ROOT.TH1F("m_gammaEta_1200_1400_Endcap", "M_GammaEta_massWindow_1200to1400_Endcap", bins, low, high)
m_gammaEta_1300_1500_Endcap = ROOT.TH1F("m_gammaEta_1300_1500_Endcap", "M_GammaEta_massWindow_1300to1500_Endcap", bins, low, high)
m_gammaEta_1400_1600_Endcap = ROOT.TH1F("m_gammaEta_1400_1600_Endcap", "M_GammaEta_massWindow_1400to1600_Endcap", bins, low, high)
m_gammaEta_1500_1700_Endcap = ROOT.TH1F("m_gammaEta_1500_1700_Endcap", "M_GammaEta_massWindow_1500to1700_Endcap", bins, low, high)
m_gammaEta_1600_1800_Endcap = ROOT.TH1F("m_gammaEta_1600_1800_Endcap", "M_GammaEta_massWindow_1600to1800_Endcap", bins, low, high)
m_gammaEta_1700_1900_Endcap = ROOT.TH1F("m_gammaEta_1700_1900_Endcap", "M_GammaEta_massWindow_1700to1900_Endcap", bins, low, high)
m_gammaEta_1800_2000_Endcap = ROOT.TH1F("m_gammaEta_1800_2000_Endcap", "M_GammaEta_massWindow_1800to2000_Endcap", bins, low, high)

m_gammaEta_0_400_Barrel = ROOT.TH1F("m_gammaEta_0_400_Barrel", "M_GammaEta_massWindow_0to400_Barrel", bins, low, high)
m_gammaEta_400_600_Barrel = ROOT.TH1F("m_gammaEta_400_600_Barrel", "M_GammaEta_massWindow_400to600_Barrel", bins, low, high)
m_gammaEta_500_700_Barrel = ROOT.TH1F("m_gammaEta_500_700_Barrel", "M_GammaEta_massWindow_500to700_Barrel", bins, low, high)
m_gammaEta_600_800_Barrel = ROOT.TH1F("m_gammaEta_600_800_Barrel", "M_GammaEta_massWindow_600to800_Barrel", bins, low, high)
m_gammaEta_700_900_Barrel = ROOT.TH1F("m_gammaEta_700_900_Barrel", "M_GammaEta_massWindow_700to900_Barrel", bins, low, high)
m_gammaEta_800_1000_Barrel = ROOT.TH1F("m_gammaEta_800_1000_Barrel", "M_GammaEta_massWindow_800to1000_Barrel", bins, low, high)
m_gammaEta_900_1100_Barrel = ROOT.TH1F("m_gammaEta_900_1100_Barrel", "M_GammaEta_massWindow_900to1100_Barrel", bins, low, high)
m_gammaEta_1000_1200_Barrel = ROOT.TH1F("m_gammaEta_1000_1200_Barrel", "M_GammaEta_massWindow_1000to1200_Barrel", bins, low, high)
m_gammaEta_1100_1300_Barrel = ROOT.TH1F("m_gammaEta_1100_1300_Barrel", "M_GammaEta_massWindow_1100to1300_Barrel", bins, low, high)
m_gammaEta_1200_1400_Barrel = ROOT.TH1F("m_gammaEta_1200_1400_Barrel", "M_GammaEta_massWindow_1200to1400_Barrel", bins, low, high)
m_gammaEta_1300_1500_Barrel = ROOT.TH1F("m_gammaEta_1300_1500_Barrel", "M_GammaEta_massWindow_1300to1500_Barrel", bins, low, high)
m_gammaEta_1400_1600_Barrel = ROOT.TH1F("m_gammaEta_1400_1600_Barrel", "M_GammaEta_massWindow_1400to1600_Barrel", bins, low, high)
m_gammaEta_1500_1700_Barrel = ROOT.TH1F("m_gammaEta_1500_1700_Barrel", "M_GammaEta_massWindow_1500to1700_Barrel", bins, low, high)
m_gammaEta_1600_1800_Barrel = ROOT.TH1F("m_gammaEta_1600_1800_Barrel", "M_GammaEta_massWindow_1600to1800_Barrel", bins, low, high)
m_gammaEta_1700_1900_Barrel = ROOT.TH1F("m_gammaEta_1700_1900_Barrel", "M_GammaEta_massWindow_1700to1900_Barrel", bins, low, high)
m_gammaEta_1800_2000_Barrel = ROOT.TH1F("m_gammaEta_1800_2000_Barrel", "M_GammaEta_massWindow_1800to2000_Barrel", bins, low, high)

# Make TChain
chain = ROOT.TChain(tree)
rootfiles = []
for root, dirnames, filenames in os.walk(path):
  for filename in fnmatch.filter(filenames, '*.root'):
    rootfiles.append(os.path.join(root, filename))
for rootfile in rootfiles:
  chain.Add(rootfile)
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
Photon1 = ROOT.recoPhotonInfo_t()
outerchain.SetBranchAddress("Photon1", ROOT.AddressOf(Photon1, "pt") )

total = chain.GetEntries()
for event in chain:
  if i % 100000 == 0:
    percentDone = float(i) / float(total) * 100.0
    print 'Processing outer TTree {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(i, total, percentDone )
  chain.GetEntry(i)

  hasPhoton = False
  isBarrel = False
  isEndcap = False
  hasTight = False
  hasLoose = False

  # Get Eta Cand from fTree2 if there is one
  if nPass[0] >= 1:
    hasEta = True
    EtaCand.SetPtEtaPhiM(recoTwoProngInfo.pt, recoTwoProngInfo.eta, recoTwoProngInfo.phi, recoTwoProngInfo.mass)
    EtaMass = recoTwoProngInfo.grommedMass

  # Get Photon from same event in fTree
  entry = EventNumbers.get(eventnum, -1)
  if entry != -1:
    outerchain.GetEntry(EventNumbers[eventnum])
    Photon.SetPtEtaPhiM(recoPhotonInfo.pt, recoPhotonInfo.eta, recoPhotonInfo.phi, 0)
    hasPhoton = True
    sc = recoPhotonInfo.scEta
    if sc < 1.4442:
      isBarrel = True
    elif sc > 1.566 and sc < 2.5:
      isEndcap = True
 
  # If event had a good Eta, combine to make mass distribution
  if hasEta and hasPhoton:
    print "Event ", eventnum, ", run ", run, ", lumi section ", lumi, ", had a passed Eta and Photon. Making Phi and computing mass."
    PhiCand = Photon + EtaCand
    m_gammaEta.Fill(PhiCand.M())
    if isEndcap:
      m_gammaEta_Endcap.Fill(PhiCand.M())
    if isBarrel:
      m_gammaEta_Barrel.Fill(PhiCand.M())
    if EtaMass > 0 and EtaMass < 2:
      m_gammaEta_0_2000.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_0_2000_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_0_2000_Barrel.Fill(PhiCand.M())
    if EtaMass > 0 and EtaMass < 0.4:
      m_gammaEta_0_400.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_0_400_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_0_400_Barrel.Fill(PhiCand.M())
    if EtaMass > 0.4 and EtaMass < 0.6:
      m_gammaEta_400_600.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_400_600_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_400_600_Barrel.Fill(PhiCand.M())
    if EtaMass > 0.5 and EtaMass < 0.7:
      m_gammaEta_500_700.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_500_700_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_500_700_Barrel.Fill(PhiCand.M())
    if EtaMass > 0.6 and EtaMass < 0.8:
      m_gammaEta_600_800.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_600_800_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_600_800_Barrel.Fill(PhiCand.M())
    if EtaMass > 0.7 and EtaMass < 0.9:
      m_gammaEta_700_900.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_700_900_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_700_900_Barrel.Fill(PhiCand.M())
    if EtaMass > 0.8 and EtaMass < 1.0:
      m_gammaEta_800_1000.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_800_1000_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_800_1000_Barrel.Fill(PhiCand.M())
    if EtaMass > 0.900 and EtaMass < 1.100:
      m_gammaEta_900_1100.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_900_1100_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_900_1100_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.000 and EtaMass < 1.200:
      m_gammaEta_1000_1200.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1000_1200_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1000_1200_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.100 and EtaMass < 1.300:
      m_gammaEta_1100_1300.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1100_1300_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1100_1300_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.200 and EtaMass < 1.400:
      m_gammaEta_1200_1400.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1200_1400_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1200_1400_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.300 and EtaMass < 1.500:
      m_gammaEta_1300_1500.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1300_1500_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1300_1500_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.400 and EtaMass < 1.600:
      m_gammaEta_1400_1600.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1400_1600_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1400_1600_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.500 and EtaMass < 1.700:
      m_gammaEta_1500_1700.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1500_1700_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1500_1700_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.600 and EtaMass < 1.800:
      m_gammaEta_1600_1800.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1600_1800_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1600_1800_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.700 and EtaMass < 1.900:
      m_gammaEta_1700_1900.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1700_1900_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1700_1900_Barrel.Fill(PhiCand.M())
    if EtaMass > 1.800 and EtaMass < 2.000:
      m_gammaEta_1800_2000.Fill(PhiCand.M())
      if isEndcap:
        m_gammaEta_1800_2000_Endcap.Fill(PhiCand.M())
      if isBarrel:
        m_gammaEta_1800_2000_Barrel.Fill(PhiCand.M())
        
# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
