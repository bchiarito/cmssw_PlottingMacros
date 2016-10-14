from ROOT import *
from array import array
from math import *
import sys
import os
import glob
import fnmatch
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--file',
                  dest='file', default='',
                  help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--tree',
                  dest='tree', default='fTree2',
                  help='')
parser.add_option('--out',
                  dest='out', default="",
                  help='output file')
(options, args) = parser.parse_args()

path = options.file
tree = options.tree
fakefile = TFile(options.fakerate)

bins = 71
low = 0
high = 5000

outputfile = TFile(options.out, "recreate")

mass_windows = [[0,300], [0,400], [300,500], [400,600], [500,700], 
                [600,900], [700,900], [800,1000], [900,1100], [1000,1200],
                [1100,1300], [1200,1400], [1300,1500], [1400,1600], [1500,1700],
                [1600,1800], [1700,1900], [1800,2000], [0,2000], [0,'Inf']]

for mass_window in mass_windows:
  histo = TH1D('m_gammaTwoProng_gjetsMC_'+str(mass_window[0])+'_'+str(mass_window[1]), 'M_GammaEta mass window '+str(mass_window[0])+' to '+str(mass_window[1])+' MeV', bins, low, high)
  histo_endcap = TH1D('m_gammaTwoProng_gjetsMC_'+str(mass_window[0])+'_'+str(mass_window[1])+'_Endcap', 'M_GammaEta mass window '+str(mass_window[0])+' to '+str(mass_window[1])+' MeV, Endcap Photon', bins, low, high)
  histo_barrel = TH1D('m_gammaTwoProng_gjetsMC_'+str(mass_window[0])+'_'+str(mass_window[1])+'_Barrel', 'M_GammaEta mass window '+str(mass_window[0])+' to '+str(mass_window[1])+' MeV, Barrel Photon', bins, low, high)
  
  mass_window.append(histo)
  mass_window.append(histo_barrel)
  mass_window.append(histo_endcap)

# Make TChain
chain = TChain(tree)
rootfiles = []
for root, dirnames, filenames in os.walk(path):
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

i = 0
total = chain.GetEntries()
for event in chain:
  if i % 100000 == 0:
    percentDone = float(i) / float(total) * 100.0
    print 'Processing outer TTree {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(i, total, percentDone )
  chain.GetEntry(i)
  i += 1
  if i == 1000000:
    break

  # Event Selection
  hasPhoton = False
  hasTwoProngTight = False
  hasTwoProngLoose = False
  isBarrel = False
  isEndcap = False

  if event.nTightPhotons >= 1:
    hasPhoton = True
  if event.nPass >= 1:
    hasTwoProngTight = True
  if event.nFakes >= 1:
    hasTwoProngLoose = True

  # signal region
  if hasPhoton and hasTwoProngTight:
    # Construct invariant mass
    PhotonCand = TLorentzVector()
    PhotonCand.SetPtEtaPhiM(Photon1.pt, Photon1.eta, Photon1.phi, 0)
    EtaCand = TLorentzVector()
    EtaCand.SetPtEtaPhiM(event.TwoProng_pt[0], event.TwoProng_eta[0], event.TwoProng_phi[0], event.TwoProng_mass[0])
    PhiCand = PhotonCand + EtaCand
    EtaMass = event.TwoProng_Mass[0]
    # Fill histograms
    for window in mass_windows:
      mass_low = window[0]
      mass_high = window[1]
      hist = window[2]
      hist_barrel = window[3]
      hist_endcap = window[4]
      if mass_high == 'Inf':
        hist.Fill(PhiCand.M())
        if abs(Photon1.scEta) < 1.4442:
          hist_barrel.Fill(PhiCand.M())
        if abs(Photon1.scEta) < 2.5 and abs(Photon1.scEta) > 1.566:
          hist_endcap.Fill(PhiCand.M())
      elif EtaMass > mass_low/1000.0 and EtaMass <= mass_high/1000.0:
        hist.Fill(PhiCand.M())
        if abs(Photon1.scEta) < 1.4442:
          hist_barrel.Fill(PhiCand.M())
        if abs(Photon1.scEta) < 2.5 and abs(Photon1.scEta) > 1.566:
          hist_endcap.Fill(PhiCand.M())
        
# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
