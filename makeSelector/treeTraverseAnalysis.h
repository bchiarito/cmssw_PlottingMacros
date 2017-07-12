//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Tue Jul 11 15:47:34 2017 by ROOT version 6.02/12
// from TTree fTree2/ChargedDecayTree
// found on file: TwoProngNtuplizer_signal125_track1_photon1.root
//////////////////////////////////////////////////////////

#ifndef treeTraverseAnalysis_h
#define treeTraverseAnalysis_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>

// Header file for the classes stored in the TTree if any.
#include "vector"

class treeTraverseAnalysis : public TSelector {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   Int_t           HLT_Photon175;
   Int_t           HLT_Photon22_Iso;
   Int_t           eventNum;
   Int_t           runNum;
   Int_t           lumiNum;
   Int_t           nPV;
   Int_t           nPF;
   Int_t           nPrunedPF;
   Double_t        HT;
   Double_t        MET;
   Double_t        MET_phi;
   Int_t           nElectrons;
   Int_t           nMuons;
   Int_t           nJets;
   vector<double>  *jet_pt;
   vector<double>  *jet_eta;
   vector<double>  *jet_phi;
   vector<double>  *jet_mass;
   vector<double>  *jet_px;
   vector<double>  *jet_py;
   vector<double>  *jet_pz;
   vector<double>  *jet_energy;
   Int_t           nPhotons;
   vector<double>  *photon_pt;
   vector<double>  *photon_eta;
   vector<double>  *photon_phi;
   vector<double>  *photon_mass;
   vector<double>  *photon_px;
   vector<double>  *photon_py;
   vector<double>  *photon_pz;
   vector<double>  *photon_energy;
   Int_t           nCands;
   Int_t           nPass;
   Int_t           nMatched;
   Int_t           nPassChargedIso;
   Int_t           nPassNeutralIso;
   Int_t           nPassEGammaIso;
   Int_t           nPassPhotonPtIso;
   Int_t           nFakes;
   Int_t           nOffset;
   vector<double>  *TwoProngLoose_pt;
   vector<double>  *TwoProngLoose_eta;
   vector<double>  *TwoProngLoose_phi;
   vector<double>  *TwoProngLoose_mass;
   vector<double>  *TwoProngLoose_Mass;
   vector<double>  *TwoProngLoose_px;
   vector<double>  *TwoProngLoose_py;
   vector<double>  *TwoProngLoose_pz;
   vector<double>  *TwoProngLoose_energy;
   vector<double>  *TwoProngLoose_CHpos_pt;
   vector<double>  *TwoProngLoose_CHpos_eta;
   vector<double>  *TwoProngLoose_CHpos_phi;
   vector<double>  *TwoProngLoose_CHpos_mass;
   vector<double>  *TwoProngLoose_CHneg_pt;
   vector<double>  *TwoProngLoose_CHneg_eta;
   vector<double>  *TwoProngLoose_CHneg_phi;
   vector<double>  *TwoProngLoose_CHneg_mass;
   vector<double>  *TwoProngLoose_photon_pt;
   vector<double>  *TwoProngLoose_photon_eta;
   vector<double>  *TwoProngLoose_photon_phi;
   vector<double>  *TwoProngLoose_photon_mass;
   vector<double>  *TwoProngLoose_photon_nGamma;
   vector<double>  *TwoProngLoose_photon_nElectron;
   vector<double>  *TwoProngLoose_chargedIso;
   vector<double>  *TwoProngLoose_neutralIso;
   vector<double>  *TwoProngLoose_egammaIso;
   vector<double>  *TwoProngLoose_CHpos_vz;
   vector<double>  *TwoProngLoose_CHpos_vx;
   vector<double>  *TwoProngLoose_CHpos_vy;
   vector<double>  *TwoProngLoose_CHpos_dz;
   vector<double>  *TwoProngLoose_CHpos_dz_PV;
   vector<double>  *TwoProngLoose_CHpos_dz_beamspot;
   vector<double>  *TwoProngLoose_CHpos_dxy;
   vector<double>  *TwoProngLoose_CHpos_dxy_PV;
   vector<double>  *TwoProngLoose_CHpos_dxy_beamspot;
   vector<double>  *TwoProngLoose_CHneg_vz;
   vector<double>  *TwoProngLoose_CHneg_vx;
   vector<double>  *TwoProngLoose_CHneg_vy;
   vector<double>  *TwoProngLoose_CHneg_dz;
   vector<double>  *TwoProngLoose_CHneg_dz_PV;
   vector<double>  *TwoProngLoose_CHneg_dz_beamspot;
   vector<double>  *TwoProngLoose_CHneg_dxy;
   vector<double>  *TwoProngLoose_CHneg_dxy_PV;
   vector<double>  *TwoProngLoose_CHneg_dxy_beamspot;
   vector<double>  *TwoProngLoose_isoPF_vz;
   vector<double>  *TwoProngLoose_isoPF_vx;
   vector<double>  *TwoProngLoose_isoPF_vy;
   vector<double>  *TwoProngLoose_isoPF_dz;
   vector<double>  *TwoProngLoose_isoPF_dz_PV;
   vector<double>  *TwoProngLoose_isoPF_dz_beamspot;
   vector<double>  *TwoProngLoose_isoPF_dxy;
   vector<double>  *TwoProngLoose_isoPF_dxy_PV;
   vector<double>  *TwoProngLoose_isoPF_dxy_beamspot;
   vector<double>  *TwoProngLoose_genDR;
   vector<double>  *TwoProng_pt;
   vector<double>  *TwoProng_eta;
   vector<double>  *TwoProng_phi;
   vector<double>  *TwoProng_mass;
   vector<double>  *TwoProng_Mass;
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
   vector<double>  *TwoProng_genDR;
   Int_t           nTightPhotons;
   vector<double>  *Photon_pt;
   vector<double>  *Photon_eta;
   vector<double>  *Photon_phi;
   vector<double>  *Photon_mass;
   vector<double>  *GenPhi_pt;
   vector<double>  *GenPhi_eta;
   vector<double>  *GenPhi_phi;
   vector<double>  *GenPhi_mass;
   vector<double>  *GenPhi_px;
   vector<double>  *GenPhi_py;
   vector<double>  *GenPhi_pz;
   vector<double>  *GenPhi_energy;
   vector<double>  *GenEta_pt;
   vector<double>  *GenEta_eta;
   vector<double>  *GenEta_phi;
   vector<double>  *GenEta_mass;
   vector<double>  *GenEta_px;
   vector<double>  *GenEta_py;
   vector<double>  *GenEta_pz;
   vector<double>  *GenEta_energy;
   vector<double>  *GenEta_candDR;
   vector<double>  *GenEta_passedCandDR;
   vector<double>  *GenEta_jetDR;
   Int_t           Gen_decayType;
   Double_t        TwoProngTwoProng_pt;
   Double_t        TwoProngTwoProng_phi;
   Double_t        TwoProngTwoProng_eta;
   Double_t        TwoProngTwoProng_mass;
   Double_t        TwoProngTwoProng_px;
   Double_t        TwoProngTwoProng_py;
   Double_t        TwoProngTwoProng_pz;
   Double_t        TwoProngTwoProng_energy;
   Double_t        TwoProngTwoProng_dR;
   Double_t        TwoProngTwoProng_dPt;
   Double_t        TwoProngTwoProng_dPhi;
   Double_t        TwoProngTwoProng_dEta;
   Double_t        TwoProngTwoProng_dMass;

   // List of branches
   TBranch        *b_HLT_Photon175;   //!
   TBranch        *b_HLT_Photon22_Iso;   //!
   TBranch        *b_eventNum;   //!
   TBranch        *b_runNum;   //!
   TBranch        *b_lumiNum;   //!
   TBranch        *b_nPV;   //!
   TBranch        *b_nPF;   //!
   TBranch        *b_numPrunedPF;   //!
   TBranch        *b_HT;   //!
   TBranch        *b_MET;   //!
   TBranch        *b_MET_phi;   //!
   TBranch        *b_nElectrons;   //!
   TBranch        *b_nMuons;   //!
   TBranch        *b_nJets;   //!
   TBranch        *b_jet_pt;   //!
   TBranch        *b_jet_eta;   //!
   TBranch        *b_jet_phi;   //!
   TBranch        *b_jet_mass;   //!
   TBranch        *b_jet_px;   //!
   TBranch        *b_jet_py;   //!
   TBranch        *b_jet_pz;   //!
   TBranch        *b_jet_energy;   //!
   TBranch        *b_nPhotons;   //!
   TBranch        *b_photon_pt;   //!
   TBranch        *b_photon_eta;   //!
   TBranch        *b_photon_phi;   //!
   TBranch        *b_photon_mass;   //!
   TBranch        *b_photon_px;   //!
   TBranch        *b_photon_py;   //!
   TBranch        *b_photon_pz;   //!
   TBranch        *b_photon_energy;   //!
   TBranch        *b_nCands;   //!
   TBranch        *b_nPass;   //!
   TBranch        *b_nMatched;   //!
   TBranch        *b_nPassChargedIso;   //!
   TBranch        *b_nPassNeutralIso;   //!
   TBranch        *b_nPassEGammaIso;   //!
   TBranch        *b_nPassPhotonIso;   //!
   TBranch        *b_nFakes;   //!
   TBranch        *b_nOffset;   //!
   TBranch        *b_TwoProngLoose_pt;   //!
   TBranch        *b_TwoProngLoose_eta;   //!
   TBranch        *b_TwoProngLoose_phi;   //!
   TBranch        *b_TwoProngLoose_mass;   //!
   TBranch        *b_TwoProngLoose_Mass;   //!
   TBranch        *b_TwoProngLoose_px;   //!
   TBranch        *b_TwoProngLoose_py;   //!
   TBranch        *b_TwoProngLoose_pz;   //!
   TBranch        *b_TwoProngLoose_energy;   //!
   TBranch        *b_TwoProngLoose_CHpos_pt;   //!
   TBranch        *b_TwoProngLoose_CHpos_eta;   //!
   TBranch        *b_TwoProngLoose_CHpos_phi;   //!
   TBranch        *b_TwoProngLoose_CHpos_mass;   //!
   TBranch        *b_TwoProngLoose_CHneg_pt;   //!
   TBranch        *b_TwoProngLoose_CHneg_eta;   //!
   TBranch        *b_TwoProngLoose_CHneg_phi;   //!
   TBranch        *b_TwoProngLoose_CHneg_mass;   //!
   TBranch        *b_TwoProngLoose_photon_pt;   //!
   TBranch        *b_TwoProngLoose_photon_eta;   //!
   TBranch        *b_TwoProngLoose_photon_phi;   //!
   TBranch        *b_TwoProngLoose_photon_mass;   //!
   TBranch        *b_TwoProngLoose_photon_nGamma;   //!
   TBranch        *b_TwoProngLoose_photon_nElectron;   //!
   TBranch        *b_TwoProngLoose_chargedIso;   //!
   TBranch        *b_TwoProngLoose_neutralIso;   //!
   TBranch        *b_TwoProngLoose_egammaIso;   //!
   TBranch        *b_TwoProngLoose_CHpos_vz;   //!
   TBranch        *b_TwoProngLoose_CHpos_vx;   //!
   TBranch        *b_TwoProngLoose_CHpos_vy;   //!
   TBranch        *b_TwoProngLoose_CHpos_dz;   //!
   TBranch        *b_TwoProngLoose_CHpos_dz_PV;   //!
   TBranch        *b_TwoProngLoose_CHpos_dz_beamspot;   //!
   TBranch        *b_TwoProngLoose_CHpos_dxy;   //!
   TBranch        *b_TwoProngLoose_CHpos_dxy_PV;   //!
   TBranch        *b_TwoProngLoose_CHpos_dxy_beamspot;   //!
   TBranch        *b_TwoProngLoose_CHneg_vz;   //!
   TBranch        *b_TwoProngLoose_CHneg_vx;   //!
   TBranch        *b_TwoProngLoose_CHneg_vy;   //!
   TBranch        *b_TwoProngLoose_CHneg_dz;   //!
   TBranch        *b_TwoProngLoose_CHneg_dz_PV;   //!
   TBranch        *b_TwoProngLoose_CHneg_dz_beamspot;   //!
   TBranch        *b_TwoProngLoose_CHneg_dxy;   //!
   TBranch        *b_TwoProngLoose_CHneg_dxy_PV;   //!
   TBranch        *b_TwoProngLoose_CHneg_dxy_beamspot;   //!
   TBranch        *b_TwoProngLoose_isoPF_vz;   //!
   TBranch        *b_TwoProngLoose_isoPF_vx;   //!
   TBranch        *b_TwoProngLoose_isoPF_vy;   //!
   TBranch        *b_TwoProngLoose_isoPF_dz;   //!
   TBranch        *b_TwoProngLoose_isoPF_dz_PV;   //!
   TBranch        *b_TwoProngLoose_isoPF_dz_beamspot;   //!
   TBranch        *b_TwoProngLoose_isoPF_dxy;   //!
   TBranch        *b_TwoProngLoose_isoPF_dxy_PV;   //!
   TBranch        *b_TwoProngLoose_isoPF_dxy_beamspot;   //!
   TBranch        *b_TwoProngLoose_genDR;   //!
   TBranch        *b_TwoProng_pt;   //!
   TBranch        *b_TwoProng_eta;   //!
   TBranch        *b_TwoProng_phi;   //!
   TBranch        *b_TwoProng_mass;   //!
   TBranch        *b_TwoProng_Mass;   //!
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
   TBranch        *b_TwoProng_genDR;   //!
   TBranch        *b_nTightPhotons;   //!
   TBranch        *b_Photon_pt;   //!
   TBranch        *b_Photon_eta;   //!
   TBranch        *b_Photon_phi;   //!
   TBranch        *b_Photon_mass;   //!
   TBranch        *b_GenPhi_pt;   //!
   TBranch        *b_GenPhi_eta;   //!
   TBranch        *b_GenPhi_phi;   //!
   TBranch        *b_GenPhi_mass;   //!
   TBranch        *b_GenPhi_px;   //!
   TBranch        *b_GenPhi_py;   //!
   TBranch        *b_GenPhi_pz;   //!
   TBranch        *b_GenPhi_energy;   //!
   TBranch        *b_GenEta_pt;   //!
   TBranch        *b_GenEta_eta;   //!
   TBranch        *b_GenEta_phi;   //!
   TBranch        *b_GenEta_mass;   //!
   TBranch        *b_GenEta_px;   //!
   TBranch        *b_GenEta_py;   //!
   TBranch        *b_GenEta_pz;   //!
   TBranch        *b_GenEta_energy;   //!
   TBranch        *b_GenEta_candDR;   //!
   TBranch        *b_GenEta_passedCandDR;   //!
   TBranch        *b_GenEta_jetDR;   //!
   TBranch        *b_Gen_decayType;   //!
   TBranch        *b_TwoProngTwoProng;   //!

   treeTraverseAnalysis(TTree * /*tree*/ =0) : fChain(0) { }
   virtual ~treeTraverseAnalysis() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();

   ClassDef(treeTraverseAnalysis,0);
};

#endif

#ifdef treeTraverseAnalysis_cxx
void treeTraverseAnalysis::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   jet_pt = 0;
   jet_eta = 0;
   jet_phi = 0;
   jet_mass = 0;
   jet_px = 0;
   jet_py = 0;
   jet_pz = 0;
   jet_energy = 0;
   photon_pt = 0;
   photon_eta = 0;
   photon_phi = 0;
   photon_mass = 0;
   photon_px = 0;
   photon_py = 0;
   photon_pz = 0;
   photon_energy = 0;
   TwoProngLoose_pt = 0;
   TwoProngLoose_eta = 0;
   TwoProngLoose_phi = 0;
   TwoProngLoose_mass = 0;
   TwoProngLoose_Mass = 0;
   TwoProngLoose_px = 0;
   TwoProngLoose_py = 0;
   TwoProngLoose_pz = 0;
   TwoProngLoose_energy = 0;
   TwoProngLoose_CHpos_pt = 0;
   TwoProngLoose_CHpos_eta = 0;
   TwoProngLoose_CHpos_phi = 0;
   TwoProngLoose_CHpos_mass = 0;
   TwoProngLoose_CHneg_pt = 0;
   TwoProngLoose_CHneg_eta = 0;
   TwoProngLoose_CHneg_phi = 0;
   TwoProngLoose_CHneg_mass = 0;
   TwoProngLoose_photon_pt = 0;
   TwoProngLoose_photon_eta = 0;
   TwoProngLoose_photon_phi = 0;
   TwoProngLoose_photon_mass = 0;
   TwoProngLoose_photon_nGamma = 0;
   TwoProngLoose_photon_nElectron = 0;
   TwoProngLoose_chargedIso = 0;
   TwoProngLoose_neutralIso = 0;
   TwoProngLoose_egammaIso = 0;
   TwoProngLoose_CHpos_vz = 0;
   TwoProngLoose_CHpos_vx = 0;
   TwoProngLoose_CHpos_vy = 0;
   TwoProngLoose_CHpos_dz = 0;
   TwoProngLoose_CHpos_dz_PV = 0;
   TwoProngLoose_CHpos_dz_beamspot = 0;
   TwoProngLoose_CHpos_dxy = 0;
   TwoProngLoose_CHpos_dxy_PV = 0;
   TwoProngLoose_CHpos_dxy_beamspot = 0;
   TwoProngLoose_CHneg_vz = 0;
   TwoProngLoose_CHneg_vx = 0;
   TwoProngLoose_CHneg_vy = 0;
   TwoProngLoose_CHneg_dz = 0;
   TwoProngLoose_CHneg_dz_PV = 0;
   TwoProngLoose_CHneg_dz_beamspot = 0;
   TwoProngLoose_CHneg_dxy = 0;
   TwoProngLoose_CHneg_dxy_PV = 0;
   TwoProngLoose_CHneg_dxy_beamspot = 0;
   TwoProngLoose_isoPF_vz = 0;
   TwoProngLoose_isoPF_vx = 0;
   TwoProngLoose_isoPF_vy = 0;
   TwoProngLoose_isoPF_dz = 0;
   TwoProngLoose_isoPF_dz_PV = 0;
   TwoProngLoose_isoPF_dz_beamspot = 0;
   TwoProngLoose_isoPF_dxy = 0;
   TwoProngLoose_isoPF_dxy_PV = 0;
   TwoProngLoose_isoPF_dxy_beamspot = 0;
   TwoProngLoose_genDR = 0;
   TwoProng_pt = 0;
   TwoProng_eta = 0;
   TwoProng_phi = 0;
   TwoProng_mass = 0;
   TwoProng_Mass = 0;
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
   TwoProng_genDR = 0;
   Photon_pt = 0;
   Photon_eta = 0;
   Photon_phi = 0;
   Photon_mass = 0;
   GenPhi_pt = 0;
   GenPhi_eta = 0;
   GenPhi_phi = 0;
   GenPhi_mass = 0;
   GenPhi_px = 0;
   GenPhi_py = 0;
   GenPhi_pz = 0;
   GenPhi_energy = 0;
   GenEta_pt = 0;
   GenEta_eta = 0;
   GenEta_phi = 0;
   GenEta_mass = 0;
   GenEta_px = 0;
   GenEta_py = 0;
   GenEta_pz = 0;
   GenEta_energy = 0;
   GenEta_candDR = 0;
   GenEta_passedCandDR = 0;
   GenEta_jetDR = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("HLT_Photon175", &HLT_Photon175, &b_HLT_Photon175);
   fChain->SetBranchAddress("HLT_Photon22_Iso", &HLT_Photon22_Iso, &b_HLT_Photon22_Iso);
   fChain->SetBranchAddress("eventNum", &eventNum, &b_eventNum);
   fChain->SetBranchAddress("runNum", &runNum, &b_runNum);
   fChain->SetBranchAddress("lumiNum", &lumiNum, &b_lumiNum);
   fChain->SetBranchAddress("nPV", &nPV, &b_nPV);
   fChain->SetBranchAddress("nPF", &nPF, &b_nPF);
   fChain->SetBranchAddress("nPrunedPF", &nPrunedPF, &b_numPrunedPF);
   fChain->SetBranchAddress("HT", &HT, &b_HT);
   fChain->SetBranchAddress("MET", &MET, &b_MET);
   fChain->SetBranchAddress("MET_phi", &MET_phi, &b_MET_phi);
   fChain->SetBranchAddress("nElectrons", &nElectrons, &b_nElectrons);
   fChain->SetBranchAddress("nMuons", &nMuons, &b_nMuons);
   fChain->SetBranchAddress("nJets", &nJets, &b_nJets);
   fChain->SetBranchAddress("jet_pt", &jet_pt, &b_jet_pt);
   fChain->SetBranchAddress("jet_eta", &jet_eta, &b_jet_eta);
   fChain->SetBranchAddress("jet_phi", &jet_phi, &b_jet_phi);
   fChain->SetBranchAddress("jet_mass", &jet_mass, &b_jet_mass);
   fChain->SetBranchAddress("jet_px", &jet_px, &b_jet_px);
   fChain->SetBranchAddress("jet_py", &jet_py, &b_jet_py);
   fChain->SetBranchAddress("jet_pz", &jet_pz, &b_jet_pz);
   fChain->SetBranchAddress("jet_energy", &jet_energy, &b_jet_energy);
   fChain->SetBranchAddress("nPhotons", &nPhotons, &b_nPhotons);
   fChain->SetBranchAddress("photon_pt", &photon_pt, &b_photon_pt);
   fChain->SetBranchAddress("photon_eta", &photon_eta, &b_photon_eta);
   fChain->SetBranchAddress("photon_phi", &photon_phi, &b_photon_phi);
   fChain->SetBranchAddress("photon_mass", &photon_mass, &b_photon_mass);
   fChain->SetBranchAddress("photon_px", &photon_px, &b_photon_px);
   fChain->SetBranchAddress("photon_py", &photon_py, &b_photon_py);
   fChain->SetBranchAddress("photon_pz", &photon_pz, &b_photon_pz);
   fChain->SetBranchAddress("photon_energy", &photon_energy, &b_photon_energy);
   fChain->SetBranchAddress("nCands", &nCands, &b_nCands);
   fChain->SetBranchAddress("nPass", &nPass, &b_nPass);
   fChain->SetBranchAddress("nMatched", &nMatched, &b_nMatched);
   fChain->SetBranchAddress("nPassChargedIso", &nPassChargedIso, &b_nPassChargedIso);
   fChain->SetBranchAddress("nPassNeutralIso", &nPassNeutralIso, &b_nPassNeutralIso);
   fChain->SetBranchAddress("nPassEGammaIso", &nPassEGammaIso, &b_nPassEGammaIso);
   fChain->SetBranchAddress("nPassPhotonPtIso", &nPassPhotonPtIso, &b_nPassPhotonIso);
   fChain->SetBranchAddress("nFakes", &nFakes, &b_nFakes);
   fChain->SetBranchAddress("nOffset", &nOffset, &b_nOffset);
   fChain->SetBranchAddress("TwoProngLoose_pt", &TwoProngLoose_pt, &b_TwoProngLoose_pt);
   fChain->SetBranchAddress("TwoProngLoose_eta", &TwoProngLoose_eta, &b_TwoProngLoose_eta);
   fChain->SetBranchAddress("TwoProngLoose_phi", &TwoProngLoose_phi, &b_TwoProngLoose_phi);
   fChain->SetBranchAddress("TwoProngLoose_mass", &TwoProngLoose_mass, &b_TwoProngLoose_mass);
   fChain->SetBranchAddress("TwoProngLoose_Mass", &TwoProngLoose_Mass, &b_TwoProngLoose_Mass);
   fChain->SetBranchAddress("TwoProngLoose_px", &TwoProngLoose_px, &b_TwoProngLoose_px);
   fChain->SetBranchAddress("TwoProngLoose_py", &TwoProngLoose_py, &b_TwoProngLoose_py);
   fChain->SetBranchAddress("TwoProngLoose_pz", &TwoProngLoose_pz, &b_TwoProngLoose_pz);
   fChain->SetBranchAddress("TwoProngLoose_energy", &TwoProngLoose_energy, &b_TwoProngLoose_energy);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_pt", &TwoProngLoose_CHpos_pt, &b_TwoProngLoose_CHpos_pt);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_eta", &TwoProngLoose_CHpos_eta, &b_TwoProngLoose_CHpos_eta);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_phi", &TwoProngLoose_CHpos_phi, &b_TwoProngLoose_CHpos_phi);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_mass", &TwoProngLoose_CHpos_mass, &b_TwoProngLoose_CHpos_mass);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_pt", &TwoProngLoose_CHneg_pt, &b_TwoProngLoose_CHneg_pt);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_eta", &TwoProngLoose_CHneg_eta, &b_TwoProngLoose_CHneg_eta);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_phi", &TwoProngLoose_CHneg_phi, &b_TwoProngLoose_CHneg_phi);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_mass", &TwoProngLoose_CHneg_mass, &b_TwoProngLoose_CHneg_mass);
   fChain->SetBranchAddress("TwoProngLoose_photon_pt", &TwoProngLoose_photon_pt, &b_TwoProngLoose_photon_pt);
   fChain->SetBranchAddress("TwoProngLoose_photon_eta", &TwoProngLoose_photon_eta, &b_TwoProngLoose_photon_eta);
   fChain->SetBranchAddress("TwoProngLoose_photon_phi", &TwoProngLoose_photon_phi, &b_TwoProngLoose_photon_phi);
   fChain->SetBranchAddress("TwoProngLoose_photon_mass", &TwoProngLoose_photon_mass, &b_TwoProngLoose_photon_mass);
   fChain->SetBranchAddress("TwoProngLoose_photon_nGamma", &TwoProngLoose_photon_nGamma, &b_TwoProngLoose_photon_nGamma);
   fChain->SetBranchAddress("TwoProngLoose_photon_nElectron", &TwoProngLoose_photon_nElectron, &b_TwoProngLoose_photon_nElectron);
   fChain->SetBranchAddress("TwoProngLoose_chargedIso", &TwoProngLoose_chargedIso, &b_TwoProngLoose_chargedIso);
   fChain->SetBranchAddress("TwoProngLoose_neutralIso", &TwoProngLoose_neutralIso, &b_TwoProngLoose_neutralIso);
   fChain->SetBranchAddress("TwoProngLoose_egammaIso", &TwoProngLoose_egammaIso, &b_TwoProngLoose_egammaIso);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_vz", &TwoProngLoose_CHpos_vz, &b_TwoProngLoose_CHpos_vz);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_vx", &TwoProngLoose_CHpos_vx, &b_TwoProngLoose_CHpos_vx);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_vy", &TwoProngLoose_CHpos_vy, &b_TwoProngLoose_CHpos_vy);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_dz", &TwoProngLoose_CHpos_dz, &b_TwoProngLoose_CHpos_dz);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_dz_PV", &TwoProngLoose_CHpos_dz_PV, &b_TwoProngLoose_CHpos_dz_PV);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_dz_beamspot", &TwoProngLoose_CHpos_dz_beamspot, &b_TwoProngLoose_CHpos_dz_beamspot);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_dxy", &TwoProngLoose_CHpos_dxy, &b_TwoProngLoose_CHpos_dxy);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_dxy_PV", &TwoProngLoose_CHpos_dxy_PV, &b_TwoProngLoose_CHpos_dxy_PV);
   fChain->SetBranchAddress("TwoProngLoose_CHpos_dxy_beamspot", &TwoProngLoose_CHpos_dxy_beamspot, &b_TwoProngLoose_CHpos_dxy_beamspot);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_vz", &TwoProngLoose_CHneg_vz, &b_TwoProngLoose_CHneg_vz);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_vx", &TwoProngLoose_CHneg_vx, &b_TwoProngLoose_CHneg_vx);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_vy", &TwoProngLoose_CHneg_vy, &b_TwoProngLoose_CHneg_vy);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_dz", &TwoProngLoose_CHneg_dz, &b_TwoProngLoose_CHneg_dz);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_dz_PV", &TwoProngLoose_CHneg_dz_PV, &b_TwoProngLoose_CHneg_dz_PV);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_dz_beamspot", &TwoProngLoose_CHneg_dz_beamspot, &b_TwoProngLoose_CHneg_dz_beamspot);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_dxy", &TwoProngLoose_CHneg_dxy, &b_TwoProngLoose_CHneg_dxy);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_dxy_PV", &TwoProngLoose_CHneg_dxy_PV, &b_TwoProngLoose_CHneg_dxy_PV);
   fChain->SetBranchAddress("TwoProngLoose_CHneg_dxy_beamspot", &TwoProngLoose_CHneg_dxy_beamspot, &b_TwoProngLoose_CHneg_dxy_beamspot);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_vz", &TwoProngLoose_isoPF_vz, &b_TwoProngLoose_isoPF_vz);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_vx", &TwoProngLoose_isoPF_vx, &b_TwoProngLoose_isoPF_vx);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_vy", &TwoProngLoose_isoPF_vy, &b_TwoProngLoose_isoPF_vy);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_dz", &TwoProngLoose_isoPF_dz, &b_TwoProngLoose_isoPF_dz);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_dz_PV", &TwoProngLoose_isoPF_dz_PV, &b_TwoProngLoose_isoPF_dz_PV);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_dz_beamspot", &TwoProngLoose_isoPF_dz_beamspot, &b_TwoProngLoose_isoPF_dz_beamspot);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_dxy", &TwoProngLoose_isoPF_dxy, &b_TwoProngLoose_isoPF_dxy);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_dxy_PV", &TwoProngLoose_isoPF_dxy_PV, &b_TwoProngLoose_isoPF_dxy_PV);
   fChain->SetBranchAddress("TwoProngLoose_isoPF_dxy_beamspot", &TwoProngLoose_isoPF_dxy_beamspot, &b_TwoProngLoose_isoPF_dxy_beamspot);
   fChain->SetBranchAddress("TwoProngLoose_genDR", &TwoProngLoose_genDR, &b_TwoProngLoose_genDR);
   fChain->SetBranchAddress("TwoProng_pt", &TwoProng_pt, &b_TwoProng_pt);
   fChain->SetBranchAddress("TwoProng_eta", &TwoProng_eta, &b_TwoProng_eta);
   fChain->SetBranchAddress("TwoProng_phi", &TwoProng_phi, &b_TwoProng_phi);
   fChain->SetBranchAddress("TwoProng_mass", &TwoProng_mass, &b_TwoProng_mass);
   fChain->SetBranchAddress("TwoProng_Mass", &TwoProng_Mass, &b_TwoProng_Mass);
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
   fChain->SetBranchAddress("TwoProng_genDR", &TwoProng_genDR, &b_TwoProng_genDR);
   fChain->SetBranchAddress("nTightPhotons", &nTightPhotons, &b_nTightPhotons);
   fChain->SetBranchAddress("Photon_pt", &Photon_pt, &b_Photon_pt);
   fChain->SetBranchAddress("Photon_eta", &Photon_eta, &b_Photon_eta);
   fChain->SetBranchAddress("Photon_phi", &Photon_phi, &b_Photon_phi);
   fChain->SetBranchAddress("Photon_mass", &Photon_mass, &b_Photon_mass);
   fChain->SetBranchAddress("GenPhi_pt", &GenPhi_pt, &b_GenPhi_pt);
   fChain->SetBranchAddress("GenPhi_eta", &GenPhi_eta, &b_GenPhi_eta);
   fChain->SetBranchAddress("GenPhi_phi", &GenPhi_phi, &b_GenPhi_phi);
   fChain->SetBranchAddress("GenPhi_mass", &GenPhi_mass, &b_GenPhi_mass);
   fChain->SetBranchAddress("GenPhi_px", &GenPhi_px, &b_GenPhi_px);
   fChain->SetBranchAddress("GenPhi_py", &GenPhi_py, &b_GenPhi_py);
   fChain->SetBranchAddress("GenPhi_pz", &GenPhi_pz, &b_GenPhi_pz);
   fChain->SetBranchAddress("GenPhi_energy", &GenPhi_energy, &b_GenPhi_energy);
   fChain->SetBranchAddress("GenEta_pt", &GenEta_pt, &b_GenEta_pt);
   fChain->SetBranchAddress("GenEta_eta", &GenEta_eta, &b_GenEta_eta);
   fChain->SetBranchAddress("GenEta_phi", &GenEta_phi, &b_GenEta_phi);
   fChain->SetBranchAddress("GenEta_mass", &GenEta_mass, &b_GenEta_mass);
   fChain->SetBranchAddress("GenEta_px", &GenEta_px, &b_GenEta_px);
   fChain->SetBranchAddress("GenEta_py", &GenEta_py, &b_GenEta_py);
   fChain->SetBranchAddress("GenEta_pz", &GenEta_pz, &b_GenEta_pz);
   fChain->SetBranchAddress("GenEta_energy", &GenEta_energy, &b_GenEta_energy);
   fChain->SetBranchAddress("GenEta_candDR", &GenEta_candDR, &b_GenEta_candDR);
   fChain->SetBranchAddress("GenEta_passedCandDR", &GenEta_passedCandDR, &b_GenEta_passedCandDR);
   fChain->SetBranchAddress("GenEta_jetDR", &GenEta_jetDR, &b_GenEta_jetDR);
   fChain->SetBranchAddress("Gen_decayType", &Gen_decayType, &b_Gen_decayType);
   fChain->SetBranchAddress("TwoProngTwoProng", &TwoProngTwoProng_pt, &b_TwoProngTwoProng);
}

Bool_t treeTraverseAnalysis::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

#endif // #ifdef treeTraverseAnalysis_cxx
