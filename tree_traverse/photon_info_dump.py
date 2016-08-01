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
Photon2 = recoPhotonInfo_t()
Photon3 = recoPhotonInfo_t()
chain.SetBranchAddress("Photon1", AddressOf(Photon1, "pt") )
chain.SetBranchAddress("Photon2", AddressOf(Photon2, "pt") )
chain.SetBranchAddress("Photon3", AddressOf(Photon3, "pt") )

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

count = 0
total = chain.GetEntries()
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  if event.runNum == 254907 and event.lumiNum == 15 and event.eventNum == 22371731:
    print "found the event"
    print Photon1
    print "pt", Photon1.pt
    print "eta", Photon1.eta
    print "phi", Photon1.phi
    print "sigmaIetaIeta", Photon1.sigmaIetaIeta
    print "hadOverEm", Photon1.hadOverEm
    print "hadTwoerOverEm", Photon1.hadTowerOverEm
    print "hcalIso04", Photon1.hcalIso04
    print "hcalIso03", Photon1.hcalIso03
    print "ecalIso04", Photon1.ecalIso04
    print "ecalIso03", Photon1.ecalIso03
    print "PFIsoCharged03", Photon1.PFIsoCharged03
    print "PFIsoNeutral03", Photon1.PFIsoNeutral03
    print "PFIsoPhoton03", Photon1.PFIsoPhoton03
    print "PFIsoAll03", Photon1.PFIsoAll03
    print "rhocorPFIsoCharged03", Photon1.rhocorPFIsoCharged03
    print "rhocorPFIsoNeutral03", Photon1.rhocorPFIsoNeutral03
    print "rhocorPFIsoPhoton03", Photon1.rhocorPFIsoPhoton03
    print "rhocorPFIsoAll03", Photon1.rhocorPFIsoAll03
    print Photon2
    print "pt", Photon2.pt
    print "eta", Photon2.eta
    print "phi", Photon2.phi
    print "sigmaIetaIeta", Photon2.sigmaIetaIeta
    print "hadOverEm", Photon2.hadOverEm
    print "hadTowerOverEm", Photon2.hadTowerOverEm
    print "hcalIso04", Photon2.hcalIso04
    print "hcalIso03", Photon2.hcalIso03
    print "ecalIso04", Photon2.ecalIso04
    print "ecalIso03", Photon2.ecalIso03
    print "PFIsoCharged03", Photon2.PFIsoCharged03
    print "PFIsoNeutral03", Photon2.PFIsoNeutral03
    print "PFIsoPhoton03", Photon2.PFIsoPhoton03
    print "PFIsoAll03", Photon2.PFIsoAll03
    print "rhocorPFIsoCharged03", Photon2.rhocorPFIsoCharged03
    print "rhocorPFIsoNeutral03", Photon2.rhocorPFIsoNeutral03
    print "rhocorPFIsoPhoton03", Photon2.rhocorPFIsoPhoton03
    print "rhocorPFIsoAll03", Photon2.rhocorPFIsoAll03
    print Photon3
    print "pt", Photon3.pt
    print "eta", Photon3.eta
    print "phi", Photon3.phi
    print "sigmaIetaIeta", Photon3.sigmaIetaIeta
    print "hadOverEm", Photon3.hadOverEm
    print "hadTwoerOverEm", Photon3.hadTowerOverEm
    print "hcalIso04", Photon3.hcalIso04
    print "hcalIso03", Photon3.hcalIso03
    print "ecalIso04", Photon3.ecalIso04
    print "ecalIso03", Photon3.ecalIso03
    print "PFIsoCharged03", Photon3.PFIsoCharged03
    print "PFIsoNeutral03", Photon3.PFIsoNeutral03
    print "PFIsoPhoton03", Photon3.PFIsoPhoton03
    print "PFIsoAll03", Photon3.PFIsoAll03
    print "rhocorPFIsoCharged03", Photon3.rhocorPFIsoCharged03
    print "rhocorPFIsoNeutral03", Photon3.rhocorPFIsoNeutral03
    print "rhocorPFIsoPhoton03", Photon3.rhocorPFIsoPhoton03
    print "rhocorPFIsoAll03", Photon3.rhocorPFIsoAll03
    break


# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
