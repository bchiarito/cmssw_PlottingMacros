//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Nov 13 19:40:38 2018 by ROOT version 6.06/01
// from TTree fTree2/ChargedDecayTree
// found on file: /cms/chiarito/eos/twoprong/ztagandprobe/Nov12_trees/DATA/SingleMuon/RunH/181113_163123/0000/TwoProngNtuplizer_1.root
//////////////////////////////////////////////////////////

#ifndef MyClassDATA_h
#define MyClassDATA_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "vector"
#include "vector"

class MyClassDATA {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Int_t           HLT_Photon175;
   Int_t           HLT_Photon22_Iso;
   Int_t           eventNum;
   Int_t           runNum;
   Int_t           lumiNum;
   Double_t        mcXS;
   Double_t        mcN;
   Int_t           nPV;
   Double_t        rho;
   Int_t           nPF;
   Int_t           nPrunedPF;
   Double_t        HT;
   Double_t        HT_pf;
   Double_t        MET;
   Double_t        MET_phi;
   Int_t           nElectrons;
   vector<double>  *Electron_pt;
   vector<double>  *Electron_eta;
   vector<double>  *Electron_phi;
   vector<double>  *Electron_mass;
   Int_t           nMuons;
   vector<double>  *Muon_pt;
   vector<double>  *Muon_eta;
   vector<double>  *Muon_phi;
   vector<double>  *Muon_mass;
   Int_t           nTaus;
   vector<double>  *Tau_pt;
   vector<double>  *Tau_eta;
   vector<double>  *Tau_phi;
   vector<double>  *Tau_mass;
   Int_t           nJets;
   vector<double>  *Jet_pt;
   vector<double>  *Jet_eta;
   vector<double>  *Jet_phi;
   vector<double>  *Jet_mass;
   Int_t           nPhotons;
   vector<double>  *Photon_pt;
   vector<double>  *Photon_eta;
   vector<double>  *Photon_phi;
   vector<double>  *Photon_mass;
   vector<double>  *BaseIDPhoton_pt;
   vector<double>  *BaseIDPhoton_eta;
   vector<double>  *BaseIDPhoton_phi;
   vector<double>  *BaseIDPhoton_mass;
   vector<double>  *BaseIDPhoton_iso_gamma;
   vector<double>  *BaseIDPhoton_iso_ch;
   vector<double>  *BaseIDPhoton_HE;
   vector<double>  *BaseIDPhoton_sigmaieie;
   vector<double>  *LooseIDPhoton_pt;
   vector<double>  *LooseIDPhoton_eta;
   vector<double>  *LooseIDPhoton_phi;
   vector<double>  *LooseIDPhoton_mass;
   vector<double>  *LooseIDPhoton_iso_gamma;
   Int_t           nIDPhotons;
   vector<double>  *IDPhoton_pt;
   vector<double>  *IDPhoton_eta;
   vector<double>  *IDPhoton_phi;
   vector<double>  *IDPhoton_mass;
   Double_t        Photon1_pt;
   Double_t        Photon1_eta;
   Double_t        Photon1_phi;
   Double_t        Photon1_detEta;
   Double_t        Photon1_detPhi;
   Double_t        Photon1_r9;
   Double_t        Photon1_sigmaIetaIeta;
   Double_t        Photon1_sigmaEtaEta;
   Double_t        Photon1_sigmaIphiIphi;
   Double_t        Photon1_sigmaPhiPhi;
   Double_t        Photon1_maxEnergyXtal;
   Double_t        Photon1_e1x5;
   Double_t        Photon1_e2x5;
   Double_t        Photon1_e3x3;
   Double_t        Photon1_e5x5;
   Double_t        Photon1_r1x5;
   Double_t        Photon1_r2x5;
   Double_t        Photon1_swisscross;
   Double_t        Photon1_eMax;
   Double_t        Photon1_eLeft;
   Double_t        Photon1_eRight;
   Double_t        Photon1_eTop;
   Double_t        Photon1_eBottom;
   Double_t        Photon1_eSecond;
   Double_t        Photon1_e2x2;
   Double_t        Photon1_e4x4;
   Double_t        Photon1_e2e9;
   Double_t        Photon1_maxRecHitTime;
   Double_t        Photon1_sumRecHitsEnergiesNoKGood;
   Double_t        Photon1_RecHitsNoKGoodEnergyRatio;
   Double_t        Photon1_hadOverEm;
   Double_t        Photon1_hadTowerOverEm;
   Double_t        Photon1_hadDepth1OverEm;
   Double_t        Photon1_hadDepth2OverEm;
   Double_t        Photon1_hcalIso04;
   Double_t        Photon1_hcalIso03;
   Double_t        Photon1_ecalIso04;
   Double_t        Photon1_ecalIso03;
   Double_t        Photon1_trkIsoSumPtHollow04;
   Double_t        Photon1_trkIsoSumPtSolid04;
   Double_t        Photon1_trkIsoSumPtHollow03;
   Double_t        Photon1_trkIsoSumPtSolid03;
   Double_t        Photon1_PFIsoCharged04;
   Double_t        Photon1_PFIsoNeutral04;
   Double_t        Photon1_PFIsoPhoton04;
   Double_t        Photon1_PFIsoAll04;
   Double_t        Photon1_PFIsoCharged03;
   Double_t        Photon1_PFIsoNeutral03;
   Double_t        Photon1_PFIsoPhoton03;
   Double_t        Photon1_PFIsoAll03;
   Double_t        Photon1_PFIsoCharged02;
   Double_t        Photon1_PFIsoNeutral02;
   Double_t        Photon1_PFIsoPhoton02;
   Double_t        Photon1_PFIsoAll02;
   Double_t        Photon1_rhocorPFIsoCharged04;
   Double_t        Photon1_rhocorPFIsoNeutral04;
   Double_t        Photon1_rhocorPFIsoPhoton04;
   Double_t        Photon1_rhocorPFIsoAll04;
   Double_t        Photon1_rhocorPFIsoCharged03;
   Double_t        Photon1_rhocorPFIsoNeutral03;
   Double_t        Photon1_rhocorPFIsoPhoton03;
   Double_t        Photon1_rhocorPFIsoAll03;
   Double_t        Photon1_rhocorPFIsoCharged02;
   Double_t        Photon1_rhocorPFIsoNeutral02;
   Double_t        Photon1_rhocorPFIsoPhoton02;
   Double_t        Photon1_rhocorPFIsoAll02;
   Double_t        Photon1_EAPhotonHighPtID;
   Double_t        Photon1_alphaPhotonHighPtID;
   Double_t        Photon1_kappaPhotonHighPtID;
   Double_t        Photon1_corPhotonIsoHighPtID;
   Double_t        Photon1_esRatio;
   Double_t        Photon1_scEta;
   Double_t        Photon1_scPhi;
   Double_t        Photon1_scRawEnergy;
   Double_t        Photon1_scPreshowerEnergy;
   Double_t        Photon1_scPhiWidth;
   Double_t        Photon1_scEtaWidth;
   Double_t        Photon1_seedEnergy;
   Double_t        Photon1_satSeedEnergy;
   Int_t           Photon1_scNumBasicClusters;
   Int_t           Photon1_trkIsoNtrksHollow04;
   Int_t           Photon1_trkIsoNtrksSolid04;
   Int_t           Photon1_trkIsoNtrksHollow03;
   Int_t           Photon1_trkIsoNtrksSolid03;
   Int_t           Photon1_severityLevel;
   Int_t           Photon1_recHitFlag;
   Int_t           Photon1_detId;
   Int_t           Photon1_iEtaY;
   Int_t           Photon1_iPhiX;
   Int_t           Photon1_numRecHitsNoKGood;
   Int_t           Photon1_nSatCells;
   Bool_t          Photon1_isEB;
   Bool_t          Photon1_isEE;
   Bool_t          Photon1_isEBEtaGap;
   Bool_t          Photon1_isEBPhiGap;
   Bool_t          Photon1_isEERingGap;
   Bool_t          Photon1_isEEDeeGap;
   Bool_t          Photon1_isEBEEGap;
   Bool_t          Photon1_hasPixelSeed;
   Bool_t          Photon1_hasMatchedPromptElec;
   Bool_t          Photon1_isFakeable;
   Bool_t          Photon1_isTightDetPhoton;
   Bool_t          Photon1_isTightPFPhoton;
   Bool_t          Photon1_isMediumPFPhoton;
   Bool_t          Photon1_isLoosePFPhoton;
   Bool_t          Photon1_isHighPtPFPhoton;
   Bool_t          Photon1_hasGoodRecHits;
   Bool_t          Photon1_isSaturated;
   Double_t        Photon2_pt;
   Double_t        Photon2_eta;
   Double_t        Photon2_phi;
   Double_t        Photon2_detEta;
   Double_t        Photon2_detPhi;
   Double_t        Photon2_r9;
   Double_t        Photon2_sigmaIetaIeta;
   Double_t        Photon2_sigmaEtaEta;
   Double_t        Photon2_sigmaIphiIphi;
   Double_t        Photon2_sigmaPhiPhi;
   Double_t        Photon2_maxEnergyXtal;
   Double_t        Photon2_e1x5;
   Double_t        Photon2_e2x5;
   Double_t        Photon2_e3x3;
   Double_t        Photon2_e5x5;
   Double_t        Photon2_r1x5;
   Double_t        Photon2_r2x5;
   Double_t        Photon2_swisscross;
   Double_t        Photon2_eMax;
   Double_t        Photon2_eLeft;
   Double_t        Photon2_eRight;
   Double_t        Photon2_eTop;
   Double_t        Photon2_eBottom;
   Double_t        Photon2_eSecond;
   Double_t        Photon2_e2x2;
   Double_t        Photon2_e4x4;
   Double_t        Photon2_e2e9;
   Double_t        Photon2_maxRecHitTime;
   Double_t        Photon2_sumRecHitsEnergiesNoKGood;
   Double_t        Photon2_RecHitsNoKGoodEnergyRatio;
   Double_t        Photon2_hadOverEm;
   Double_t        Photon2_hadTowerOverEm;
   Double_t        Photon2_hadDepth1OverEm;
   Double_t        Photon2_hadDepth2OverEm;
   Double_t        Photon2_hcalIso04;
   Double_t        Photon2_hcalIso03;
   Double_t        Photon2_ecalIso04;
   Double_t        Photon2_ecalIso03;
   Double_t        Photon2_trkIsoSumPtHollow04;
   Double_t        Photon2_trkIsoSumPtSolid04;
   Double_t        Photon2_trkIsoSumPtHollow03;
   Double_t        Photon2_trkIsoSumPtSolid03;
   Double_t        Photon2_PFIsoCharged04;
   Double_t        Photon2_PFIsoNeutral04;
   Double_t        Photon2_PFIsoPhoton04;
   Double_t        Photon2_PFIsoAll04;
   Double_t        Photon2_PFIsoCharged03;
   Double_t        Photon2_PFIsoNeutral03;
   Double_t        Photon2_PFIsoPhoton03;
   Double_t        Photon2_PFIsoAll03;
   Double_t        Photon2_PFIsoCharged02;
   Double_t        Photon2_PFIsoNeutral02;
   Double_t        Photon2_PFIsoPhoton02;
   Double_t        Photon2_PFIsoAll02;
   Double_t        Photon2_rhocorPFIsoCharged04;
   Double_t        Photon2_rhocorPFIsoNeutral04;
   Double_t        Photon2_rhocorPFIsoPhoton04;
   Double_t        Photon2_rhocorPFIsoAll04;
   Double_t        Photon2_rhocorPFIsoCharged03;
   Double_t        Photon2_rhocorPFIsoNeutral03;
   Double_t        Photon2_rhocorPFIsoPhoton03;
   Double_t        Photon2_rhocorPFIsoAll03;
   Double_t        Photon2_rhocorPFIsoCharged02;
   Double_t        Photon2_rhocorPFIsoNeutral02;
   Double_t        Photon2_rhocorPFIsoPhoton02;
   Double_t        Photon2_rhocorPFIsoAll02;
   Double_t        Photon2_EAPhotonHighPtID;
   Double_t        Photon2_alphaPhotonHighPtID;
   Double_t        Photon2_kappaPhotonHighPtID;
   Double_t        Photon2_corPhotonIsoHighPtID;
   Double_t        Photon2_esRatio;
   Double_t        Photon2_scEta;
   Double_t        Photon2_scPhi;
   Double_t        Photon2_scRawEnergy;
   Double_t        Photon2_scPreshowerEnergy;
   Double_t        Photon2_scPhiWidth;
   Double_t        Photon2_scEtaWidth;
   Double_t        Photon2_seedEnergy;
   Double_t        Photon2_satSeedEnergy;
   Int_t           Photon2_scNumBasicClusters;
   Int_t           Photon2_trkIsoNtrksHollow04;
   Int_t           Photon2_trkIsoNtrksSolid04;
   Int_t           Photon2_trkIsoNtrksHollow03;
   Int_t           Photon2_trkIsoNtrksSolid03;
   Int_t           Photon2_severityLevel;
   Int_t           Photon2_recHitFlag;
   Int_t           Photon2_detId;
   Int_t           Photon2_iEtaY;
   Int_t           Photon2_iPhiX;
   Int_t           Photon2_numRecHitsNoKGood;
   Int_t           Photon2_nSatCells;
   Bool_t          Photon2_isEB;
   Bool_t          Photon2_isEE;
   Bool_t          Photon2_isEBEtaGap;
   Bool_t          Photon2_isEBPhiGap;
   Bool_t          Photon2_isEERingGap;
   Bool_t          Photon2_isEEDeeGap;
   Bool_t          Photon2_isEBEEGap;
   Bool_t          Photon2_hasPixelSeed;
   Bool_t          Photon2_hasMatchedPromptElec;
   Bool_t          Photon2_isFakeable;
   Bool_t          Photon2_isTightDetPhoton;
   Bool_t          Photon2_isTightPFPhoton;
   Bool_t          Photon2_isMediumPFPhoton;
   Bool_t          Photon2_isLoosePFPhoton;
   Bool_t          Photon2_isHighPtPFPhoton;
   Bool_t          Photon2_hasGoodRecHits;
   Bool_t          Photon2_isSaturated;
   Double_t        Photon3_pt;
   Double_t        Photon3_eta;
   Double_t        Photon3_phi;
   Double_t        Photon3_detEta;
   Double_t        Photon3_detPhi;
   Double_t        Photon3_r9;
   Double_t        Photon3_sigmaIetaIeta;
   Double_t        Photon3_sigmaEtaEta;
   Double_t        Photon3_sigmaIphiIphi;
   Double_t        Photon3_sigmaPhiPhi;
   Double_t        Photon3_maxEnergyXtal;
   Double_t        Photon3_e1x5;
   Double_t        Photon3_e2x5;
   Double_t        Photon3_e3x3;
   Double_t        Photon3_e5x5;
   Double_t        Photon3_r1x5;
   Double_t        Photon3_r2x5;
   Double_t        Photon3_swisscross;
   Double_t        Photon3_eMax;
   Double_t        Photon3_eLeft;
   Double_t        Photon3_eRight;
   Double_t        Photon3_eTop;
   Double_t        Photon3_eBottom;
   Double_t        Photon3_eSecond;
   Double_t        Photon3_e2x2;
   Double_t        Photon3_e4x4;
   Double_t        Photon3_e2e9;
   Double_t        Photon3_maxRecHitTime;
   Double_t        Photon3_sumRecHitsEnergiesNoKGood;
   Double_t        Photon3_RecHitsNoKGoodEnergyRatio;
   Double_t        Photon3_hadOverEm;
   Double_t        Photon3_hadTowerOverEm;
   Double_t        Photon3_hadDepth1OverEm;
   Double_t        Photon3_hadDepth2OverEm;
   Double_t        Photon3_hcalIso04;
   Double_t        Photon3_hcalIso03;
   Double_t        Photon3_ecalIso04;
   Double_t        Photon3_ecalIso03;
   Double_t        Photon3_trkIsoSumPtHollow04;
   Double_t        Photon3_trkIsoSumPtSolid04;
   Double_t        Photon3_trkIsoSumPtHollow03;
   Double_t        Photon3_trkIsoSumPtSolid03;
   Double_t        Photon3_PFIsoCharged04;
   Double_t        Photon3_PFIsoNeutral04;
   Double_t        Photon3_PFIsoPhoton04;
   Double_t        Photon3_PFIsoAll04;
   Double_t        Photon3_PFIsoCharged03;
   Double_t        Photon3_PFIsoNeutral03;
   Double_t        Photon3_PFIsoPhoton03;
   Double_t        Photon3_PFIsoAll03;
   Double_t        Photon3_PFIsoCharged02;
   Double_t        Photon3_PFIsoNeutral02;
   Double_t        Photon3_PFIsoPhoton02;
   Double_t        Photon3_PFIsoAll02;
   Double_t        Photon3_rhocorPFIsoCharged04;
   Double_t        Photon3_rhocorPFIsoNeutral04;
   Double_t        Photon3_rhocorPFIsoPhoton04;
   Double_t        Photon3_rhocorPFIsoAll04;
   Double_t        Photon3_rhocorPFIsoCharged03;
   Double_t        Photon3_rhocorPFIsoNeutral03;
   Double_t        Photon3_rhocorPFIsoPhoton03;
   Double_t        Photon3_rhocorPFIsoAll03;
   Double_t        Photon3_rhocorPFIsoCharged02;
   Double_t        Photon3_rhocorPFIsoNeutral02;
   Double_t        Photon3_rhocorPFIsoPhoton02;
   Double_t        Photon3_rhocorPFIsoAll02;
   Double_t        Photon3_EAPhotonHighPtID;
   Double_t        Photon3_alphaPhotonHighPtID;
   Double_t        Photon3_kappaPhotonHighPtID;
   Double_t        Photon3_corPhotonIsoHighPtID;
   Double_t        Photon3_esRatio;
   Double_t        Photon3_scEta;
   Double_t        Photon3_scPhi;
   Double_t        Photon3_scRawEnergy;
   Double_t        Photon3_scPreshowerEnergy;
   Double_t        Photon3_scPhiWidth;
   Double_t        Photon3_scEtaWidth;
   Double_t        Photon3_seedEnergy;
   Double_t        Photon3_satSeedEnergy;
   Int_t           Photon3_scNumBasicClusters;
   Int_t           Photon3_trkIsoNtrksHollow04;
   Int_t           Photon3_trkIsoNtrksSolid04;
   Int_t           Photon3_trkIsoNtrksHollow03;
   Int_t           Photon3_trkIsoNtrksSolid03;
   Int_t           Photon3_severityLevel;
   Int_t           Photon3_recHitFlag;
   Int_t           Photon3_detId;
   Int_t           Photon3_iEtaY;
   Int_t           Photon3_iPhiX;
   Int_t           Photon3_numRecHitsNoKGood;
   Int_t           Photon3_nSatCells;
   Bool_t          Photon3_isEB;
   Bool_t          Photon3_isEE;
   Bool_t          Photon3_isEBEtaGap;
   Bool_t          Photon3_isEBPhiGap;
   Bool_t          Photon3_isEERingGap;
   Bool_t          Photon3_isEEDeeGap;
   Bool_t          Photon3_isEBEEGap;
   Bool_t          Photon3_hasPixelSeed;
   Bool_t          Photon3_hasMatchedPromptElec;
   Bool_t          Photon3_isFakeable;
   Bool_t          Photon3_isTightDetPhoton;
   Bool_t          Photon3_isTightPFPhoton;
   Bool_t          Photon3_isMediumPFPhoton;
   Bool_t          Photon3_isLoosePFPhoton;
   Bool_t          Photon3_isHighPtPFPhoton;
   Bool_t          Photon3_hasGoodRecHits;
   Bool_t          Photon3_isSaturated;
   Int_t           nTwoProngCands;
   Int_t           nTwoProngs;
   Int_t           nTwoProngsLoose;
   vector<double>  *TwoProng_pt;
   vector<double>  *TwoProng_eta;
   vector<double>  *TwoProng_phi;
   vector<double>  *TwoProng_mass;
   vector<double>  *TwoProng_mass_l;
   vector<double>  *TwoProng_Mass;
   vector<double>  *TwoProng_Mass_l;
   vector<double>  *TwoProng_MassEta;
   vector<double>  *TwoProng_MassEta_l;
   vector<double>  *TwoProng_Mass300;
   vector<bool>    *TwoProng_FoundExtraTrack;
   vector<bool>    *TwoProng_nExtraTracks;
   vector<double>  *TwoProng_px;
   vector<double>  *TwoProng_py;
   vector<double>  *TwoProng_pz;
   vector<double>  *TwoProng_energy;
   vector<double>  *TwoProng_CHpos_pt;
   vector<double>  *TwoProng_CHpos_eta;
   vector<double>  *TwoProng_CHpos_phi;
   vector<double>  *TwoProng_CHpos_mass;
   vector<double>  *TwoProng_CHneg_pt;
   vector<double>  *TwoProng_CHneg_eta;
   vector<double>  *TwoProng_CHneg_phi;
   vector<double>  *TwoProng_CHneg_mass;
   vector<double>  *TwoProng_photon_pt;
   vector<double>  *TwoProng_photon_eta;
   vector<double>  *TwoProng_photon_phi;
   vector<double>  *TwoProng_photon_mass;
   vector<double>  *TwoProng_photon_pt_l;
   vector<double>  *TwoProng_photon_eta_l;
   vector<double>  *TwoProng_photon_phi_l;
   vector<double>  *TwoProng_photon_mass_l;
   vector<double>  *TwoProng_photon_Mass;
   vector<double>  *TwoProng_photon_nGamma;
   vector<double>  *TwoProng_photon_nElectron;
   vector<double>  *TwoProng_chargedIso;
   vector<double>  *TwoProng_neutralIso;
   vector<double>  *TwoProng_egammaIso;
   vector<double>  *TwoProng_CHpos_vz;
   vector<double>  *TwoProng_CHpos_vx;
   vector<double>  *TwoProng_CHpos_vy;
   vector<double>  *TwoProng_CHpos_dz;
   vector<double>  *TwoProng_CHpos_dz_PV;
   vector<double>  *TwoProng_CHpos_dz_beamspot;
   vector<double>  *TwoProng_CHpos_dxy;
   vector<double>  *TwoProng_CHpos_dxy_PV;
   vector<double>  *TwoProng_CHpos_dxy_beamspot;
   vector<double>  *TwoProng_CHneg_vz;
   vector<double>  *TwoProng_CHneg_vx;
   vector<double>  *TwoProng_CHneg_vy;
   vector<double>  *TwoProng_CHneg_dz;
   vector<double>  *TwoProng_CHneg_dz_PV;
   vector<double>  *TwoProng_CHneg_dz_beamspot;
   vector<double>  *TwoProng_CHneg_dxy;
   vector<double>  *TwoProng_CHneg_dxy_PV;
   vector<double>  *TwoProng_CHneg_dxy_beamspot;
   vector<double>  *TwoProng_isoPF_vz;
   vector<double>  *TwoProng_isoPF_vx;
   vector<double>  *TwoProng_isoPF_vy;
   vector<double>  *TwoProng_isoPF_dz;
   vector<double>  *TwoProng_isoPF_dz_PV;
   vector<double>  *TwoProng_isoPF_dz_beamspot;
   vector<double>  *TwoProng_isoPF_dxy;
   vector<double>  *TwoProng_isoPF_dxy_PV;
   vector<double>  *TwoProng_isoPF_dxy_beamspot;
   vector<double>  *TwoProng_trackAsym;
   vector<double>  *TwoProng_photonAsym;
   vector<double>  *TwoProng_genOmega_dR;
   vector<double>  *TwoProng_genTau_dR;
   vector<double>  *TwoProng_mPosPho;
   vector<double>  *TwoProng_mPosPho_l;
   vector<double>  *TwoProng_mPosPho_pi0;
   vector<double>  *TwoProng_mPosPho_lpi0;
   vector<double>  *TwoProng_mNegPho;
   vector<double>  *TwoProng_mNegPho_l;
   vector<double>  *TwoProng_mNegPho_pi0;
   vector<double>  *TwoProng_mNegPho_lpi0;
   vector<double>  *TwoProng_mPosNeg;
   vector<double>  *TwoProng_CHpos_p3;
   vector<double>  *TwoProng_CHneg_p3;
   vector<double>  *TwoProng_photon_p3;
   Double_t        RecoPhiDiTwoProng_pt;
   Double_t        RecoPhiDiTwoProng_phi;
   Double_t        RecoPhiDiTwoProng_eta;
   Double_t        RecoPhiDiTwoProng_mass;
   Double_t        RecoPhiDiTwoProng_energy;
   Double_t        RecoPhiDiTwoProng_part1_pt;
   Double_t        RecoPhiDiTwoProng_part1_eta;
   Double_t        RecoPhiDiTwoProng_part1_phi;
   Double_t        RecoPhiDiTwoProng_part1_mass;
   Double_t        RecoPhiDiTwoProng_part1_energy;
   Double_t        RecoPhiDiTwoProng_part2_pt;
   Double_t        RecoPhiDiTwoProng_part2_eta;
   Double_t        RecoPhiDiTwoProng_part2_phi;
   Double_t        RecoPhiDiTwoProng_part2_mass;
   Double_t        RecoPhiDiTwoProng_part2_energy;
   Double_t        RecoPhiDiTwoProng_dR;
   Double_t        RecoPhiPhotonTwoProng_pt;
   Double_t        RecoPhiPhotonTwoProng_phi;
   Double_t        RecoPhiPhotonTwoProng_eta;
   Double_t        RecoPhiPhotonTwoProng_mass;
   Double_t        RecoPhiPhotonTwoProng_energy;
   Double_t        RecoPhiPhotonTwoProng_part1_pt;
   Double_t        RecoPhiPhotonTwoProng_part1_eta;
   Double_t        RecoPhiPhotonTwoProng_part1_phi;
   Double_t        RecoPhiPhotonTwoProng_part1_mass;
   Double_t        RecoPhiPhotonTwoProng_part1_energy;
   Double_t        RecoPhiPhotonTwoProng_part2_pt;
   Double_t        RecoPhiPhotonTwoProng_part2_eta;
   Double_t        RecoPhiPhotonTwoProng_part2_phi;
   Double_t        RecoPhiPhotonTwoProng_part2_mass;
   Double_t        RecoPhiPhotonTwoProng_part2_energy;
   Double_t        RecoPhiPhotonTwoProng_dR;
   Double_t        RecoPhiInclusive_pt;
   Double_t        RecoPhiInclusive_phi;
   Double_t        RecoPhiInclusive_eta;
   Double_t        RecoPhiInclusive_mass;
   Double_t        RecoPhiInclusive_energy;
   Double_t        RecoPhiInclusive_part1_pt;
   Double_t        RecoPhiInclusive_part1_eta;
   Double_t        RecoPhiInclusive_part1_phi;
   Double_t        RecoPhiInclusive_part1_mass;
   Double_t        RecoPhiInclusive_part1_energy;
   Double_t        RecoPhiInclusive_part2_pt;
   Double_t        RecoPhiInclusive_part2_eta;
   Double_t        RecoPhiInclusive_part2_phi;
   Double_t        RecoPhiInclusive_part2_mass;
   Double_t        RecoPhiInclusive_part2_energy;
   Double_t        RecoPhiInclusive_dR;
   Bool_t          passZMuonTrigger;
   Bool_t          passZTnP;
   Bool_t          passZPre;
   Bool_t          passZExtraMuon;
   Bool_t          passZExtraElectron;
   Bool_t          passZDiMuon;
   Bool_t          passZBVeto;
   Double_t        ZBVetoVal;
   Int_t           nTagMuons;
   Int_t           nProbeTaus;
   Double_t        TauPreDr;
   Double_t        TauPreMT;
   Double_t        TauPrePzeta;
   vector<double>  *TagMuon_pt;
   vector<double>  *TagMuon_eta;
   vector<double>  *TagMuon_phi;
   vector<double>  *TagMuon_mass;
   vector<double>  *TagMuon_z;
   vector<double>  *TagMuon_dz;
   vector<double>  *TagMuon_iso;
   vector<double>  *ProbeTau_pt;
   vector<double>  *ProbeTau_eta;
   vector<double>  *ProbeTau_phi;
   vector<double>  *ProbeTau_mass;
   vector<double>  *ProbeTau_genDR;
   Double_t        ZvisibleMuonProbeTau_pt;
   Double_t        ZvisibleMuonProbeTau_phi;
   Double_t        ZvisibleMuonProbeTau_eta;
   Double_t        ZvisibleMuonProbeTau_mass;
   Double_t        ZvisibleMuonProbeTau_energy;
   Double_t        ZvisibleMuonProbeTau_part1_pt;
   Double_t        ZvisibleMuonProbeTau_part1_eta;
   Double_t        ZvisibleMuonProbeTau_part1_phi;
   Double_t        ZvisibleMuonProbeTau_part1_mass;
   Double_t        ZvisibleMuonProbeTau_part1_energy;
   Double_t        ZvisibleMuonProbeTau_part2_pt;
   Double_t        ZvisibleMuonProbeTau_part2_eta;
   Double_t        ZvisibleMuonProbeTau_part2_phi;
   Double_t        ZvisibleMuonProbeTau_part2_mass;
   Double_t        ZvisibleMuonProbeTau_part2_energy;
   Double_t        ZvisibleMuonProbeTau_dR;
   Double_t        ZvisibleMuonPatTau_pt;
   Double_t        ZvisibleMuonPatTau_phi;
   Double_t        ZvisibleMuonPatTau_eta;
   Double_t        ZvisibleMuonPatTau_mass;
   Double_t        ZvisibleMuonPatTau_energy;
   Double_t        ZvisibleMuonPatTau_part1_pt;
   Double_t        ZvisibleMuonPatTau_part1_eta;
   Double_t        ZvisibleMuonPatTau_part1_phi;
   Double_t        ZvisibleMuonPatTau_part1_mass;
   Double_t        ZvisibleMuonPatTau_part1_energy;
   Double_t        ZvisibleMuonPatTau_part2_pt;
   Double_t        ZvisibleMuonPatTau_part2_eta;
   Double_t        ZvisibleMuonPatTau_part2_phi;
   Double_t        ZvisibleMuonPatTau_part2_mass;
   Double_t        ZvisibleMuonPatTau_part2_energy;
   Double_t        ZvisibleMuonPatTau_dR;
   Double_t        ZvisibleMuonTwoProng_pt;
   Double_t        ZvisibleMuonTwoProng_phi;
   Double_t        ZvisibleMuonTwoProng_eta;
   Double_t        ZvisibleMuonTwoProng_mass;
   Double_t        ZvisibleMuonTwoProng_energy;
   Double_t        ZvisibleMuonTwoProng_part1_pt;
   Double_t        ZvisibleMuonTwoProng_part1_eta;
   Double_t        ZvisibleMuonTwoProng_part1_phi;
   Double_t        ZvisibleMuonTwoProng_part1_mass;
   Double_t        ZvisibleMuonTwoProng_part1_energy;
   Double_t        ZvisibleMuonTwoProng_part2_pt;
   Double_t        ZvisibleMuonTwoProng_part2_eta;
   Double_t        ZvisibleMuonTwoProng_part2_phi;
   Double_t        ZvisibleMuonTwoProng_part2_mass;
   Double_t        ZvisibleMuonTwoProng_part2_energy;
   Double_t        ZvisibleMuonTwoProng_dR;

   // List of branches
   TBranch        *b_HLT_Photon175;   //!
   TBranch        *b_HLT_Photon22_Iso;   //!
   TBranch        *b_eventNum;   //!
   TBranch        *b_runNum;   //!
   TBranch        *b_lumiNum;   //!
   TBranch        *b_mcXS;   //!
   TBranch        *b_mcN;   //!
   TBranch        *b_nPV;   //!
   TBranch        *b_rho;   //!
   TBranch        *b_nPF;   //!
   TBranch        *b_numPrunedPF;   //!
   TBranch        *b_HT;   //!
   TBranch        *b_HT_pf;   //!
   TBranch        *b_MET;   //!
   TBranch        *b_MET_phi;   //!
   TBranch        *b_nElectrons;   //!
   TBranch        *b_Electron_pt;   //!
   TBranch        *b_Electron_eta;   //!
   TBranch        *b_Electron_phi;   //!
   TBranch        *b_Electron_mass;   //!
   TBranch        *b_nMuons;   //!
   TBranch        *b_Muon_pt;   //!
   TBranch        *b_Muon_eta;   //!
   TBranch        *b_Muon_phi;   //!
   TBranch        *b_Muon_mass;   //!
   TBranch        *b_nTaus;   //!
   TBranch        *b_Tau_pt;   //!
   TBranch        *b_Tau_eta;   //!
   TBranch        *b_Tau_phi;   //!
   TBranch        *b_Tau_mass;   //!
   TBranch        *b_nJets;   //!
   TBranch        *b_Jet_pt;   //!
   TBranch        *b_Jet_eta;   //!
   TBranch        *b_Jet_phi;   //!
   TBranch        *b_Jet_mass;   //!
   TBranch        *b_nPhotons;   //!
   TBranch        *b_Photon_pt;   //!
   TBranch        *b_Photon_eta;   //!
   TBranch        *b_Photon_phi;   //!
   TBranch        *b_Photon_mass;   //!
   TBranch        *b_BaseIDPhoton_pt;   //!
   TBranch        *b_BaseIDPhoton_eta;   //!
   TBranch        *b_BaseIDPhoton_phi;   //!
   TBranch        *b_BaseIDPhoton_mass;   //!
   TBranch        *b_BaseIDPhoton_iso_gamma;   //!
   TBranch        *b_BaseIDPhoton_iso_ch;   //!
   TBranch        *b_BaseIDPhoton_HE;   //!
   TBranch        *b_BaseIDPhoton_sigmaieie;   //!
   TBranch        *b_LooseIDPhoton_pt;   //!
   TBranch        *b_LooseIDPhoton_eta;   //!
   TBranch        *b_LooseIDPhoton_phi;   //!
   TBranch        *b_LooseIDPhoton_mass;   //!
   TBranch        *b_LooseIDPhoton_iso_gamma;   //!
   TBranch        *b_nTightPhotons;   //!
   TBranch        *b_IDPhoton_pt;   //!
   TBranch        *b_IDPhoton_eta;   //!
   TBranch        *b_IDPhoton_phi;   //!
   TBranch        *b_IDPhoton_mass;   //!
   TBranch        *b_Photon1;   //!
   TBranch        *b_Photon2;   //!
   TBranch        *b_Photon3;   //!
   TBranch        *b_nTwoProngCands;   //!
   TBranch        *b_nTwoProngs;   //!
   TBranch        *b_nTwoProngsLoose;   //!
   TBranch        *b_TwoProng_pt;   //!
   TBranch        *b_TwoProng_eta;   //!
   TBranch        *b_TwoProng_phi;   //!
   TBranch        *b_TwoProng_mass;   //!
   TBranch        *b_TwoProng_mass_l;   //!
   TBranch        *b_TwoProng_Mass;   //!
   TBranch        *b_TwoProng_Mass_l;   //!
   TBranch        *b_TwoProng_MassEta;   //!
   TBranch        *b_TwoProng_MassEta_l;   //!
   TBranch        *b_TwoProng_Mass300;   //!
   TBranch        *b_TwoProng_FoundExtraTrack;   //!
   TBranch        *b_TwoProng_nExtraTracks;   //!
   TBranch        *b_TwoProng_px;   //!
   TBranch        *b_TwoProng_py;   //!
   TBranch        *b_TwoProng_pz;   //!
   TBranch        *b_TwoProng_energy;   //!
   TBranch        *b_TwoProng_CHpos_pt;   //!
   TBranch        *b_TwoProng_CHpos_eta;   //!
   TBranch        *b_TwoProng_CHpos_phi;   //!
   TBranch        *b_TwoProng_CHpos_mass;   //!
   TBranch        *b_TwoProng_CHneg_pt;   //!
   TBranch        *b_TwoProng_CHneg_eta;   //!
   TBranch        *b_TwoProng_CHneg_phi;   //!
   TBranch        *b_TwoProng_CHneg_mass;   //!
   TBranch        *b_TwoProng_photon_pt;   //!
   TBranch        *b_TwoProng_photon_eta;   //!
   TBranch        *b_TwoProng_photon_phi;   //!
   TBranch        *b_TwoProng_photon_mass;   //!
   TBranch        *b_TwoProng_photon_pt_l;   //!
   TBranch        *b_TwoProng_photon_eta_l;   //!
   TBranch        *b_TwoProng_photon_phi_l;   //!
   TBranch        *b_TwoProng_photon_mass_l;   //!
   TBranch        *b_TwoProng_photon_Mass;   //!
   TBranch        *b_TwoProng_photon_nGamma;   //!
   TBranch        *b_TwoProng_photon_nElectron;   //!
   TBranch        *b_TwoProng_chargedIso;   //!
   TBranch        *b_TwoProng_neutralIso;   //!
   TBranch        *b_TwoProng_egammaIso;   //!
   TBranch        *b_TwoProng_CHpos_vz;   //!
   TBranch        *b_TwoProng_CHpos_vx;   //!
   TBranch        *b_TwoProng_CHpos_vy;   //!
   TBranch        *b_TwoProng_CHpos_dz;   //!
   TBranch        *b_TwoProng_CHpos_dz_PV;   //!
   TBranch        *b_TwoProng_CHpos_dz_beamspot;   //!
   TBranch        *b_TwoProng_CHpos_dxy;   //!
   TBranch        *b_TwoProng_CHpos_dxy_PV;   //!
   TBranch        *b_TwoProng_CHpos_dxy_beamspot;   //!
   TBranch        *b_TwoProng_CHneg_vz;   //!
   TBranch        *b_TwoProng_CHneg_vx;   //!
   TBranch        *b_TwoProng_CHneg_vy;   //!
   TBranch        *b_TwoProng_CHneg_dz;   //!
   TBranch        *b_TwoProng_CHneg_dz_PV;   //!
   TBranch        *b_TwoProng_CHneg_dz_beamspot;   //!
   TBranch        *b_TwoProng_CHneg_dxy;   //!
   TBranch        *b_TwoProng_CHneg_dxy_PV;   //!
   TBranch        *b_TwoProng_CHneg_dxy_beamspot;   //!
   TBranch        *b_TwoProng_isoPF_vz;   //!
   TBranch        *b_TwoProng_isoPF_vx;   //!
   TBranch        *b_TwoProng_isoPF_vy;   //!
   TBranch        *b_TwoProng_isoPF_dz;   //!
   TBranch        *b_TwoProng_isoPF_dz_PV;   //!
   TBranch        *b_TwoProng_isoPF_dz_beamspot;   //!
   TBranch        *b_TwoProng_isoPF_dxy;   //!
   TBranch        *b_TwoProng_isoPF_dxy_PV;   //!
   TBranch        *b_TwoProng_isoPF_dxy_beamspot;   //!
   TBranch        *b_TwoProng_trackAsym;   //!
   TBranch        *b_TwoProng_photonAsym;   //!
   TBranch        *b_TwoProng_genOmega_dR;   //!
   TBranch        *b_TwoProng_genTau_dR;   //!
   TBranch        *b_TwoProng_mPosPho;   //!
   TBranch        *b_TwoProng_mPosPho_l;   //!
   TBranch        *b_TwoProng_mPosPho_pi0;   //!
   TBranch        *b_TwoProng_mPosPho_lpi0;   //!
   TBranch        *b_TwoProng_mNegPho;   //!
   TBranch        *b_TwoProng_mNegPho_l;   //!
   TBranch        *b_TwoProng_mNegPho_pi0;   //!
   TBranch        *b_TwoProng_mNegPho_lpi0;   //!
   TBranch        *b_TwoProng_mPosNeg;   //!
   TBranch        *b_TwoProng_CHpos_p3;   //!
   TBranch        *b_TwoProng_CHneg_p3;   //!
   TBranch        *b_TwoProng_photon_p3;   //!
   TBranch        *b_RecoPhiDiTwoProng;   //!
   TBranch        *b_RecoPhiPhotonTwoProng;   //!
   TBranch        *b_RecoPhiInclusive;   //!
   TBranch        *b_passZMuonTrigger;   //!
   TBranch        *b_passZTnP;   //!
   TBranch        *b_passZPre;   //!
   TBranch        *b_passZExtraMuon;   //!
   TBranch        *b_passZExtraElectron;   //!
   TBranch        *b_passZDiMuon;   //!
   TBranch        *b_passZBVeto;   //!
   TBranch        *b_ZBVetoVal;   //!
   TBranch        *b_nTagMuons;   //!
   TBranch        *b_nProbeTaus;   //!
   TBranch        *b_TauPreDr;   //!
   TBranch        *b_TauPreMt;   //!
   TBranch        *b_TauPrePzeta;   //!
   TBranch        *b_TagMuon_pt;   //!
   TBranch        *b_TagMuon_eta;   //!
   TBranch        *b_TagMuon_phi;   //!
   TBranch        *b_TagMuon_mass;   //!
   TBranch        *b_TagMuon_z;   //!
   TBranch        *b_TagMuon_dz;   //!
   TBranch        *b_TagMuon_iso;   //!
   TBranch        *b_ProbeTau_pt;   //!
   TBranch        *b_ProbeTau_eta;   //!
   TBranch        *b_ProbeTau_phi;   //!
   TBranch        *b_ProbeTau_mass;   //!
   TBranch        *b_ProbeTau_genDR;   //!
   TBranch        *b_ZvisibleMuonProbeTau;   //!
   TBranch        *b_ZvisibleMuonPatTau;   //!
   TBranch        *b_ZvisibleMuonTwoProng;   //!

   MyClassDATA(TTree *tree=0);
   virtual ~MyClassDATA();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef MyClassDATA_cxx
MyClassDATA::MyClassDATA(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/cms/chiarito/eos/twoprong/ztagandprobe/Nov12_trees/DATA/SingleMuon/RunH/181113_163123/0000/TwoProngNtuplizer_1.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/cms/chiarito/eos/twoprong/ztagandprobe/Nov12_trees/DATA/SingleMuon/RunH/181113_163123/0000/TwoProngNtuplizer_1.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("/cms/chiarito/eos/twoprong/ztagandprobe/Nov12_trees/DATA/SingleMuon/RunH/181113_163123/0000/TwoProngNtuplizer_1.root:/twoprongNtuplizer");
      dir->GetObject("fTree2",tree);

   }
   Init(tree);
}

MyClassDATA::~MyClassDATA()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t MyClassDATA::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t MyClassDATA::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void MyClassDATA::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   Electron_pt = 0;
   Electron_eta = 0;
   Electron_phi = 0;
   Electron_mass = 0;
   Muon_pt = 0;
   Muon_eta = 0;
   Muon_phi = 0;
   Muon_mass = 0;
   Tau_pt = 0;
   Tau_eta = 0;
   Tau_phi = 0;
   Tau_mass = 0;
   Jet_pt = 0;
   Jet_eta = 0;
   Jet_phi = 0;
   Jet_mass = 0;
   Photon_pt = 0;
   Photon_eta = 0;
   Photon_phi = 0;
   Photon_mass = 0;
   BaseIDPhoton_pt = 0;
   BaseIDPhoton_eta = 0;
   BaseIDPhoton_phi = 0;
   BaseIDPhoton_mass = 0;
   BaseIDPhoton_iso_gamma = 0;
   BaseIDPhoton_iso_ch = 0;
   BaseIDPhoton_HE = 0;
   BaseIDPhoton_sigmaieie = 0;
   LooseIDPhoton_pt = 0;
   LooseIDPhoton_eta = 0;
   LooseIDPhoton_phi = 0;
   LooseIDPhoton_mass = 0;
   LooseIDPhoton_iso_gamma = 0;
   IDPhoton_pt = 0;
   IDPhoton_eta = 0;
   IDPhoton_phi = 0;
   IDPhoton_mass = 0;
   TwoProng_pt = 0;
   TwoProng_eta = 0;
   TwoProng_phi = 0;
   TwoProng_mass = 0;
   TwoProng_mass_l = 0;
   TwoProng_Mass = 0;
   TwoProng_Mass_l = 0;
   TwoProng_MassEta = 0;
   TwoProng_MassEta_l = 0;
   TwoProng_Mass300 = 0;
   TwoProng_FoundExtraTrack = 0;
   TwoProng_nExtraTracks = 0;
   TwoProng_px = 0;
   TwoProng_py = 0;
   TwoProng_pz = 0;
   TwoProng_energy = 0;
   TwoProng_CHpos_pt = 0;
   TwoProng_CHpos_eta = 0;
   TwoProng_CHpos_phi = 0;
   TwoProng_CHpos_mass = 0;
   TwoProng_CHneg_pt = 0;
   TwoProng_CHneg_eta = 0;
   TwoProng_CHneg_phi = 0;
   TwoProng_CHneg_mass = 0;
   TwoProng_photon_pt = 0;
   TwoProng_photon_eta = 0;
   TwoProng_photon_phi = 0;
   TwoProng_photon_mass = 0;
   TwoProng_photon_pt_l = 0;
   TwoProng_photon_eta_l = 0;
   TwoProng_photon_phi_l = 0;
   TwoProng_photon_mass_l = 0;
   TwoProng_photon_Mass = 0;
   TwoProng_photon_nGamma = 0;
   TwoProng_photon_nElectron = 0;
   TwoProng_chargedIso = 0;
   TwoProng_neutralIso = 0;
   TwoProng_egammaIso = 0;
   TwoProng_CHpos_vz = 0;
   TwoProng_CHpos_vx = 0;
   TwoProng_CHpos_vy = 0;
   TwoProng_CHpos_dz = 0;
   TwoProng_CHpos_dz_PV = 0;
   TwoProng_CHpos_dz_beamspot = 0;
   TwoProng_CHpos_dxy = 0;
   TwoProng_CHpos_dxy_PV = 0;
   TwoProng_CHpos_dxy_beamspot = 0;
   TwoProng_CHneg_vz = 0;
   TwoProng_CHneg_vx = 0;
   TwoProng_CHneg_vy = 0;
   TwoProng_CHneg_dz = 0;
   TwoProng_CHneg_dz_PV = 0;
   TwoProng_CHneg_dz_beamspot = 0;
   TwoProng_CHneg_dxy = 0;
   TwoProng_CHneg_dxy_PV = 0;
   TwoProng_CHneg_dxy_beamspot = 0;
   TwoProng_isoPF_vz = 0;
   TwoProng_isoPF_vx = 0;
   TwoProng_isoPF_vy = 0;
   TwoProng_isoPF_dz = 0;
   TwoProng_isoPF_dz_PV = 0;
   TwoProng_isoPF_dz_beamspot = 0;
   TwoProng_isoPF_dxy = 0;
   TwoProng_isoPF_dxy_PV = 0;
   TwoProng_isoPF_dxy_beamspot = 0;
   TwoProng_trackAsym = 0;
   TwoProng_photonAsym = 0;
   TwoProng_genOmega_dR = 0;
   TwoProng_genTau_dR = 0;
   TwoProng_mPosPho = 0;
   TwoProng_mPosPho_l = 0;
   TwoProng_mPosPho_pi0 = 0;
   TwoProng_mPosPho_lpi0 = 0;
   TwoProng_mNegPho = 0;
   TwoProng_mNegPho_l = 0;
   TwoProng_mNegPho_pi0 = 0;
   TwoProng_mNegPho_lpi0 = 0;
   TwoProng_mPosNeg = 0;
   TwoProng_CHpos_p3 = 0;
   TwoProng_CHneg_p3 = 0;
   TwoProng_photon_p3 = 0;
   TagMuon_pt = 0;
   TagMuon_eta = 0;
   TagMuon_phi = 0;
   TagMuon_mass = 0;
   TagMuon_z = 0;
   TagMuon_dz = 0;
   TagMuon_iso = 0;
   ProbeTau_pt = 0;
   ProbeTau_eta = 0;
   ProbeTau_phi = 0;
   ProbeTau_mass = 0;
   ProbeTau_genDR = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("HLT_Photon175", &HLT_Photon175, &b_HLT_Photon175);
   fChain->SetBranchAddress("HLT_Photon22_Iso", &HLT_Photon22_Iso, &b_HLT_Photon22_Iso);
   fChain->SetBranchAddress("eventNum", &eventNum, &b_eventNum);
   fChain->SetBranchAddress("runNum", &runNum, &b_runNum);
   fChain->SetBranchAddress("lumiNum", &lumiNum, &b_lumiNum);
   fChain->SetBranchAddress("mcXS", &mcXS, &b_mcXS);
   fChain->SetBranchAddress("mcN", &mcN, &b_mcN);
   fChain->SetBranchAddress("nPV", &nPV, &b_nPV);
   fChain->SetBranchAddress("rho", &rho, &b_rho);
   fChain->SetBranchAddress("nPF", &nPF, &b_nPF);
   fChain->SetBranchAddress("nPrunedPF", &nPrunedPF, &b_numPrunedPF);
   fChain->SetBranchAddress("HT", &HT, &b_HT);
   fChain->SetBranchAddress("HT_pf", &HT_pf, &b_HT_pf);
   fChain->SetBranchAddress("MET", &MET, &b_MET);
   fChain->SetBranchAddress("MET_phi", &MET_phi, &b_MET_phi);
   fChain->SetBranchAddress("nElectrons", &nElectrons, &b_nElectrons);
   fChain->SetBranchAddress("Electron_pt", &Electron_pt, &b_Electron_pt);
   fChain->SetBranchAddress("Electron_eta", &Electron_eta, &b_Electron_eta);
   fChain->SetBranchAddress("Electron_phi", &Electron_phi, &b_Electron_phi);
   fChain->SetBranchAddress("Electron_mass", &Electron_mass, &b_Electron_mass);
   fChain->SetBranchAddress("nMuons", &nMuons, &b_nMuons);
   fChain->SetBranchAddress("Muon_pt", &Muon_pt, &b_Muon_pt);
   fChain->SetBranchAddress("Muon_eta", &Muon_eta, &b_Muon_eta);
   fChain->SetBranchAddress("Muon_phi", &Muon_phi, &b_Muon_phi);
   fChain->SetBranchAddress("Muon_mass", &Muon_mass, &b_Muon_mass);
   fChain->SetBranchAddress("nTaus", &nTaus, &b_nTaus);
   fChain->SetBranchAddress("Tau_pt", &Tau_pt, &b_Tau_pt);
   fChain->SetBranchAddress("Tau_eta", &Tau_eta, &b_Tau_eta);
   fChain->SetBranchAddress("Tau_phi", &Tau_phi, &b_Tau_phi);
   fChain->SetBranchAddress("Tau_mass", &Tau_mass, &b_Tau_mass);
   fChain->SetBranchAddress("nJets", &nJets, &b_nJets);
   fChain->SetBranchAddress("Jet_pt", &Jet_pt, &b_Jet_pt);
   fChain->SetBranchAddress("Jet_eta", &Jet_eta, &b_Jet_eta);
   fChain->SetBranchAddress("Jet_phi", &Jet_phi, &b_Jet_phi);
   fChain->SetBranchAddress("Jet_mass", &Jet_mass, &b_Jet_mass);
   fChain->SetBranchAddress("nPhotons", &nPhotons, &b_nPhotons);
   fChain->SetBranchAddress("Photon_pt", &Photon_pt, &b_Photon_pt);
   fChain->SetBranchAddress("Photon_eta", &Photon_eta, &b_Photon_eta);
   fChain->SetBranchAddress("Photon_phi", &Photon_phi, &b_Photon_phi);
   fChain->SetBranchAddress("Photon_mass", &Photon_mass, &b_Photon_mass);
   fChain->SetBranchAddress("BaseIDPhoton_pt", &BaseIDPhoton_pt, &b_BaseIDPhoton_pt);
   fChain->SetBranchAddress("BaseIDPhoton_eta", &BaseIDPhoton_eta, &b_BaseIDPhoton_eta);
   fChain->SetBranchAddress("BaseIDPhoton_phi", &BaseIDPhoton_phi, &b_BaseIDPhoton_phi);
   fChain->SetBranchAddress("BaseIDPhoton_mass", &BaseIDPhoton_mass, &b_BaseIDPhoton_mass);
   fChain->SetBranchAddress("BaseIDPhoton_iso_gamma", &BaseIDPhoton_iso_gamma, &b_BaseIDPhoton_iso_gamma);
   fChain->SetBranchAddress("BaseIDPhoton_iso_ch", &BaseIDPhoton_iso_ch, &b_BaseIDPhoton_iso_ch);
   fChain->SetBranchAddress("BaseIDPhoton_HE", &BaseIDPhoton_HE, &b_BaseIDPhoton_HE);
   fChain->SetBranchAddress("BaseIDPhoton_sigmaieie", &BaseIDPhoton_sigmaieie, &b_BaseIDPhoton_sigmaieie);
   fChain->SetBranchAddress("LooseIDPhoton_pt", &LooseIDPhoton_pt, &b_LooseIDPhoton_pt);
   fChain->SetBranchAddress("LooseIDPhoton_eta", &LooseIDPhoton_eta, &b_LooseIDPhoton_eta);
   fChain->SetBranchAddress("LooseIDPhoton_phi", &LooseIDPhoton_phi, &b_LooseIDPhoton_phi);
   fChain->SetBranchAddress("LooseIDPhoton_mass", &LooseIDPhoton_mass, &b_LooseIDPhoton_mass);
   fChain->SetBranchAddress("LooseIDPhoton_iso_gamma", &LooseIDPhoton_iso_gamma, &b_LooseIDPhoton_iso_gamma);
   fChain->SetBranchAddress("nIDPhotons", &nIDPhotons, &b_nTightPhotons);
   fChain->SetBranchAddress("IDPhoton_pt", &IDPhoton_pt, &b_IDPhoton_pt);
   fChain->SetBranchAddress("IDPhoton_eta", &IDPhoton_eta, &b_IDPhoton_eta);
   fChain->SetBranchAddress("IDPhoton_phi", &IDPhoton_phi, &b_IDPhoton_phi);
   fChain->SetBranchAddress("IDPhoton_mass", &IDPhoton_mass, &b_IDPhoton_mass);
   fChain->SetBranchAddress("Photon1", &Photon1_pt, &b_Photon1);
   fChain->SetBranchAddress("Photon2", &Photon2_pt, &b_Photon2);
   fChain->SetBranchAddress("Photon3", &Photon3_pt, &b_Photon3);
   fChain->SetBranchAddress("nTwoProngCands", &nTwoProngCands, &b_nTwoProngCands);
   fChain->SetBranchAddress("nTwoProngs", &nTwoProngs, &b_nTwoProngs);
   fChain->SetBranchAddress("nTwoProngsLoose", &nTwoProngsLoose, &b_nTwoProngsLoose);
   fChain->SetBranchAddress("TwoProng_pt", &TwoProng_pt, &b_TwoProng_pt);
   fChain->SetBranchAddress("TwoProng_eta", &TwoProng_eta, &b_TwoProng_eta);
   fChain->SetBranchAddress("TwoProng_phi", &TwoProng_phi, &b_TwoProng_phi);
   fChain->SetBranchAddress("TwoProng_mass", &TwoProng_mass, &b_TwoProng_mass);
   fChain->SetBranchAddress("TwoProng_mass_l", &TwoProng_mass_l, &b_TwoProng_mass_l);
   fChain->SetBranchAddress("TwoProng_Mass", &TwoProng_Mass, &b_TwoProng_Mass);
   fChain->SetBranchAddress("TwoProng_Mass_l", &TwoProng_Mass_l, &b_TwoProng_Mass_l);
   fChain->SetBranchAddress("TwoProng_MassEta", &TwoProng_MassEta, &b_TwoProng_MassEta);
   fChain->SetBranchAddress("TwoProng_MassEta_l", &TwoProng_MassEta_l, &b_TwoProng_MassEta_l);
   fChain->SetBranchAddress("TwoProng_Mass300", &TwoProng_Mass300, &b_TwoProng_Mass300);
   fChain->SetBranchAddress("TwoProng_FoundExtraTrack", &TwoProng_FoundExtraTrack, &b_TwoProng_FoundExtraTrack);
   fChain->SetBranchAddress("TwoProng_nExtraTracks", &TwoProng_nExtraTracks, &b_TwoProng_nExtraTracks);
   fChain->SetBranchAddress("TwoProng_px", &TwoProng_px, &b_TwoProng_px);
   fChain->SetBranchAddress("TwoProng_py", &TwoProng_py, &b_TwoProng_py);
   fChain->SetBranchAddress("TwoProng_pz", &TwoProng_pz, &b_TwoProng_pz);
   fChain->SetBranchAddress("TwoProng_energy", &TwoProng_energy, &b_TwoProng_energy);
   fChain->SetBranchAddress("TwoProng_CHpos_pt", &TwoProng_CHpos_pt, &b_TwoProng_CHpos_pt);
   fChain->SetBranchAddress("TwoProng_CHpos_eta", &TwoProng_CHpos_eta, &b_TwoProng_CHpos_eta);
   fChain->SetBranchAddress("TwoProng_CHpos_phi", &TwoProng_CHpos_phi, &b_TwoProng_CHpos_phi);
   fChain->SetBranchAddress("TwoProng_CHpos_mass", &TwoProng_CHpos_mass, &b_TwoProng_CHpos_mass);
   fChain->SetBranchAddress("TwoProng_CHneg_pt", &TwoProng_CHneg_pt, &b_TwoProng_CHneg_pt);
   fChain->SetBranchAddress("TwoProng_CHneg_eta", &TwoProng_CHneg_eta, &b_TwoProng_CHneg_eta);
   fChain->SetBranchAddress("TwoProng_CHneg_phi", &TwoProng_CHneg_phi, &b_TwoProng_CHneg_phi);
   fChain->SetBranchAddress("TwoProng_CHneg_mass", &TwoProng_CHneg_mass, &b_TwoProng_CHneg_mass);
   fChain->SetBranchAddress("TwoProng_photon_pt", &TwoProng_photon_pt, &b_TwoProng_photon_pt);
   fChain->SetBranchAddress("TwoProng_photon_eta", &TwoProng_photon_eta, &b_TwoProng_photon_eta);
   fChain->SetBranchAddress("TwoProng_photon_phi", &TwoProng_photon_phi, &b_TwoProng_photon_phi);
   fChain->SetBranchAddress("TwoProng_photon_mass", &TwoProng_photon_mass, &b_TwoProng_photon_mass);
   fChain->SetBranchAddress("TwoProng_photon_pt_l", &TwoProng_photon_pt_l, &b_TwoProng_photon_pt_l);
   fChain->SetBranchAddress("TwoProng_photon_eta_l", &TwoProng_photon_eta_l, &b_TwoProng_photon_eta_l);
   fChain->SetBranchAddress("TwoProng_photon_phi_l", &TwoProng_photon_phi_l, &b_TwoProng_photon_phi_l);
   fChain->SetBranchAddress("TwoProng_photon_mass_l", &TwoProng_photon_mass_l, &b_TwoProng_photon_mass_l);
   fChain->SetBranchAddress("TwoProng_photon_Mass", &TwoProng_photon_Mass, &b_TwoProng_photon_Mass);
   fChain->SetBranchAddress("TwoProng_photon_nGamma", &TwoProng_photon_nGamma, &b_TwoProng_photon_nGamma);
   fChain->SetBranchAddress("TwoProng_photon_nElectron", &TwoProng_photon_nElectron, &b_TwoProng_photon_nElectron);
   fChain->SetBranchAddress("TwoProng_chargedIso", &TwoProng_chargedIso, &b_TwoProng_chargedIso);
   fChain->SetBranchAddress("TwoProng_neutralIso", &TwoProng_neutralIso, &b_TwoProng_neutralIso);
   fChain->SetBranchAddress("TwoProng_egammaIso", &TwoProng_egammaIso, &b_TwoProng_egammaIso);
   fChain->SetBranchAddress("TwoProng_CHpos_vz", &TwoProng_CHpos_vz, &b_TwoProng_CHpos_vz);
   fChain->SetBranchAddress("TwoProng_CHpos_vx", &TwoProng_CHpos_vx, &b_TwoProng_CHpos_vx);
   fChain->SetBranchAddress("TwoProng_CHpos_vy", &TwoProng_CHpos_vy, &b_TwoProng_CHpos_vy);
   fChain->SetBranchAddress("TwoProng_CHpos_dz", &TwoProng_CHpos_dz, &b_TwoProng_CHpos_dz);
   fChain->SetBranchAddress("TwoProng_CHpos_dz_PV", &TwoProng_CHpos_dz_PV, &b_TwoProng_CHpos_dz_PV);
   fChain->SetBranchAddress("TwoProng_CHpos_dz_beamspot", &TwoProng_CHpos_dz_beamspot, &b_TwoProng_CHpos_dz_beamspot);
   fChain->SetBranchAddress("TwoProng_CHpos_dxy", &TwoProng_CHpos_dxy, &b_TwoProng_CHpos_dxy);
   fChain->SetBranchAddress("TwoProng_CHpos_dxy_PV", &TwoProng_CHpos_dxy_PV, &b_TwoProng_CHpos_dxy_PV);
   fChain->SetBranchAddress("TwoProng_CHpos_dxy_beamspot", &TwoProng_CHpos_dxy_beamspot, &b_TwoProng_CHpos_dxy_beamspot);
   fChain->SetBranchAddress("TwoProng_CHneg_vz", &TwoProng_CHneg_vz, &b_TwoProng_CHneg_vz);
   fChain->SetBranchAddress("TwoProng_CHneg_vx", &TwoProng_CHneg_vx, &b_TwoProng_CHneg_vx);
   fChain->SetBranchAddress("TwoProng_CHneg_vy", &TwoProng_CHneg_vy, &b_TwoProng_CHneg_vy);
   fChain->SetBranchAddress("TwoProng_CHneg_dz", &TwoProng_CHneg_dz, &b_TwoProng_CHneg_dz);
   fChain->SetBranchAddress("TwoProng_CHneg_dz_PV", &TwoProng_CHneg_dz_PV, &b_TwoProng_CHneg_dz_PV);
   fChain->SetBranchAddress("TwoProng_CHneg_dz_beamspot", &TwoProng_CHneg_dz_beamspot, &b_TwoProng_CHneg_dz_beamspot);
   fChain->SetBranchAddress("TwoProng_CHneg_dxy", &TwoProng_CHneg_dxy, &b_TwoProng_CHneg_dxy);
   fChain->SetBranchAddress("TwoProng_CHneg_dxy_PV", &TwoProng_CHneg_dxy_PV, &b_TwoProng_CHneg_dxy_PV);
   fChain->SetBranchAddress("TwoProng_CHneg_dxy_beamspot", &TwoProng_CHneg_dxy_beamspot, &b_TwoProng_CHneg_dxy_beamspot);
   fChain->SetBranchAddress("TwoProng_isoPF_vz", &TwoProng_isoPF_vz, &b_TwoProng_isoPF_vz);
   fChain->SetBranchAddress("TwoProng_isoPF_vx", &TwoProng_isoPF_vx, &b_TwoProng_isoPF_vx);
   fChain->SetBranchAddress("TwoProng_isoPF_vy", &TwoProng_isoPF_vy, &b_TwoProng_isoPF_vy);
   fChain->SetBranchAddress("TwoProng_isoPF_dz", &TwoProng_isoPF_dz, &b_TwoProng_isoPF_dz);
   fChain->SetBranchAddress("TwoProng_isoPF_dz_PV", &TwoProng_isoPF_dz_PV, &b_TwoProng_isoPF_dz_PV);
   fChain->SetBranchAddress("TwoProng_isoPF_dz_beamspot", &TwoProng_isoPF_dz_beamspot, &b_TwoProng_isoPF_dz_beamspot);
   fChain->SetBranchAddress("TwoProng_isoPF_dxy", &TwoProng_isoPF_dxy, &b_TwoProng_isoPF_dxy);
   fChain->SetBranchAddress("TwoProng_isoPF_dxy_PV", &TwoProng_isoPF_dxy_PV, &b_TwoProng_isoPF_dxy_PV);
   fChain->SetBranchAddress("TwoProng_isoPF_dxy_beamspot", &TwoProng_isoPF_dxy_beamspot, &b_TwoProng_isoPF_dxy_beamspot);
   fChain->SetBranchAddress("TwoProng_trackAsym", &TwoProng_trackAsym, &b_TwoProng_trackAsym);
   fChain->SetBranchAddress("TwoProng_photonAsym", &TwoProng_photonAsym, &b_TwoProng_photonAsym);
   fChain->SetBranchAddress("TwoProng_genOmega_dR", &TwoProng_genOmega_dR, &b_TwoProng_genOmega_dR);
   fChain->SetBranchAddress("TwoProng_genTau_dR", &TwoProng_genTau_dR, &b_TwoProng_genTau_dR);
   fChain->SetBranchAddress("TwoProng_mPosPho", &TwoProng_mPosPho, &b_TwoProng_mPosPho);
   fChain->SetBranchAddress("TwoProng_mPosPho_l", &TwoProng_mPosPho_l, &b_TwoProng_mPosPho_l);
   fChain->SetBranchAddress("TwoProng_mPosPho_pi0", &TwoProng_mPosPho_pi0, &b_TwoProng_mPosPho_pi0);
   fChain->SetBranchAddress("TwoProng_mPosPho_lpi0", &TwoProng_mPosPho_lpi0, &b_TwoProng_mPosPho_lpi0);
   fChain->SetBranchAddress("TwoProng_mNegPho", &TwoProng_mNegPho, &b_TwoProng_mNegPho);
   fChain->SetBranchAddress("TwoProng_mNegPho_l", &TwoProng_mNegPho_l, &b_TwoProng_mNegPho_l);
   fChain->SetBranchAddress("TwoProng_mNegPho_pi0", &TwoProng_mNegPho_pi0, &b_TwoProng_mNegPho_pi0);
   fChain->SetBranchAddress("TwoProng_mNegPho_lpi0", &TwoProng_mNegPho_lpi0, &b_TwoProng_mNegPho_lpi0);
   fChain->SetBranchAddress("TwoProng_mPosNeg", &TwoProng_mPosNeg, &b_TwoProng_mPosNeg);
   fChain->SetBranchAddress("TwoProng_CHpos_p3", &TwoProng_CHpos_p3, &b_TwoProng_CHpos_p3);
   fChain->SetBranchAddress("TwoProng_CHneg_p3", &TwoProng_CHneg_p3, &b_TwoProng_CHneg_p3);
   fChain->SetBranchAddress("TwoProng_photon_p3", &TwoProng_photon_p3, &b_TwoProng_photon_p3);
   fChain->SetBranchAddress("RecoPhiDiTwoProng", &RecoPhiDiTwoProng_pt, &b_RecoPhiDiTwoProng);
   fChain->SetBranchAddress("RecoPhiPhotonTwoProng", &RecoPhiPhotonTwoProng_pt, &b_RecoPhiPhotonTwoProng);
   fChain->SetBranchAddress("RecoPhiInclusive", &RecoPhiInclusive_pt, &b_RecoPhiInclusive);
   fChain->SetBranchAddress("passZMuonTrigger", &passZMuonTrigger, &b_passZMuonTrigger);
   fChain->SetBranchAddress("passZTnP", &passZTnP, &b_passZTnP);
   fChain->SetBranchAddress("passZPre", &passZPre, &b_passZPre);
   fChain->SetBranchAddress("passZExtraMuon", &passZExtraMuon, &b_passZExtraMuon);
   fChain->SetBranchAddress("passZExtraElectron", &passZExtraElectron, &b_passZExtraElectron);
   fChain->SetBranchAddress("passZDiMuon", &passZDiMuon, &b_passZDiMuon);
   fChain->SetBranchAddress("passZBVeto", &passZBVeto, &b_passZBVeto);
   fChain->SetBranchAddress("ZBVetoVal", &ZBVetoVal, &b_ZBVetoVal);
   fChain->SetBranchAddress("nTagMuons", &nTagMuons, &b_nTagMuons);
   fChain->SetBranchAddress("nProbeTaus", &nProbeTaus, &b_nProbeTaus);
   fChain->SetBranchAddress("TauPreDr", &TauPreDr, &b_TauPreDr);
   fChain->SetBranchAddress("TauPreMT", &TauPreMT, &b_TauPreMt);
   fChain->SetBranchAddress("TauPrePzeta", &TauPrePzeta, &b_TauPrePzeta);
   fChain->SetBranchAddress("TagMuon_pt", &TagMuon_pt, &b_TagMuon_pt);
   fChain->SetBranchAddress("TagMuon_eta", &TagMuon_eta, &b_TagMuon_eta);
   fChain->SetBranchAddress("TagMuon_phi", &TagMuon_phi, &b_TagMuon_phi);
   fChain->SetBranchAddress("TagMuon_mass", &TagMuon_mass, &b_TagMuon_mass);
   fChain->SetBranchAddress("TagMuon_z", &TagMuon_z, &b_TagMuon_z);
   fChain->SetBranchAddress("TagMuon_dz", &TagMuon_dz, &b_TagMuon_dz);
   fChain->SetBranchAddress("TagMuon_iso", &TagMuon_iso, &b_TagMuon_iso);
   fChain->SetBranchAddress("ProbeTau_pt", &ProbeTau_pt, &b_ProbeTau_pt);
   fChain->SetBranchAddress("ProbeTau_eta", &ProbeTau_eta, &b_ProbeTau_eta);
   fChain->SetBranchAddress("ProbeTau_phi", &ProbeTau_phi, &b_ProbeTau_phi);
   fChain->SetBranchAddress("ProbeTau_mass", &ProbeTau_mass, &b_ProbeTau_mass);
   fChain->SetBranchAddress("ProbeTau_genDR", &ProbeTau_genDR, &b_ProbeTau_genDR);
   fChain->SetBranchAddress("ZvisibleMuonProbeTau", &ZvisibleMuonProbeTau_pt, &b_ZvisibleMuonProbeTau);
   fChain->SetBranchAddress("ZvisibleMuonPatTau", &ZvisibleMuonPatTau_pt, &b_ZvisibleMuonPatTau);
   fChain->SetBranchAddress("ZvisibleMuonTwoProng", &ZvisibleMuonTwoProng_pt, &b_ZvisibleMuonTwoProng);
   Notify();
}

Bool_t MyClassDATA::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void MyClassDATA::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t MyClassDATA::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef MyClassDATA_cxx
