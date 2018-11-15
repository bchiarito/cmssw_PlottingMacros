#define MyLooper_cxx
#include "MyLooper.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLorentzVector.h>
#include <iostream>

void MyLooper::CustomLoop(const char * outputfilename = "output.root", Long64_t MAX_ENTRIES = -1)
{
   // root output file
   TFile * output = new TFile(outputfilename, "RECREATE");

   // book histograms   
   int pass_selection_count = 0;
   double etalow = -6;
   double etahigh = 6;
   int etabins = 60;
   double philow = -3.5;
   double phihigh = 3.5;
   int phibins = 35;
   TH1F * hist_HT = new TH1F("hist_HT", "hist_HT", 200, 0, 2000);
   TH1F * hist_MET = new TH1F("hist_MET", "hist_MET", 100, 0, 1000);
   TH1F * hist_nJets = new TH1F("hist_nJets", "hist_nJets", 40, 0, 40);
   TH1F * hist_nTagMuons = new TH1F("hist_nTagMuons", "hist_nTagMuons", 20, 0, 20);
   TH1F * hist_nProbeTaus = new TH1F("hist_nProbeTaus", "hist_nProbeTaus", 20, 0, 20);
   TH1F * hist_nProbePatTaus = new TH1F("hist_nProbePatTaus", "hist_nProbePatTaus", 20, 0, 20);
   TH1F * hist_nProbeTwoprongs = new TH1F("hist_nProbeTwoprongs", "hist_nProbeTwoprongs", 20, 0, 20);

   TH1F * hist_Zvis_taujet_mass = new TH1F("hist_Zvis_taujet_mass", "hist_Zvis_taujet_mass", 200, 0, 1000);
   TH1F * hist_Zvis_taujet_pt = new TH1F("hist_Zvis_taujet_pt", "hist_Zvis_taujet_pt", 200, 0, 1000);
   TH1F * hist_Zvis_taujet_phi = new TH1F("hist_Zvis_taujet_phi", "hist_Zvis_taujet_phi", phibins, philow, phihigh);
   TH1F * hist_Zvis_taujet_eta = new TH1F("hist_Zvis_taujet_eta", "hist_Zvis_taujet_eta", etabins, etalow, etahigh);
   TH1F * hist_Zvis_pattau_mass = new TH1F("hist_Zvis_pattau_mass", "hist_Zvis_pattau_mass", 200, 0, 1000);
   TH1F * hist_Zvis_pattau_pt = new TH1F("hist_Zvis_pattau_pt", "hist_Zvis_pattau_pt", 200, 0, 1000);
   TH1F * hist_Zvis_pattau_phi = new TH1F("hist_Zvis_pattau_phi", "hist_Zvis_pattau_phi", phibins, philow, phihigh);
   TH1F * hist_Zvis_pattau_eta = new TH1F("hist_Zvis_pattau_eta", "hist_Zvis_pattau_eta", etabins, etalow, etahigh);
   TH1F * hist_Zvis_twoprong_mass = new TH1F("hist_Zvis_twoprong_mass", "hist_Zvis_twoprong_mass", 200, 0, 1000);
   TH1F * hist_Zvis_twoprong_pt = new TH1F("hist_Zvis_twoprong_pt", "hist_Zvis_twoprong_pt", 200, 0, 1000);
   TH1F * hist_Zvis_twoprong_phi = new TH1F("hist_Zvis_twoprong_phi", "hist_Zvis_twoprong_phi", phibins, philow, phihigh);
   TH1F * hist_Zvis_twoprong_eta = new TH1F("hist_Zvis_twoprong_eta", "hist_Zvis_twoprong_eta", etabins, etalow, etahigh);
 
   TH1F * hist_TagMuon_pt = new TH1F("hist_TagMuon_pt", "hist_TagMuon_pt", 200, 0, 1000);
   TH1F * hist_TagMuon_eta = new TH1F("hist_TagMuon_eta", "hist_TagMuon_eta", etabins, etalow, etahigh);
   TH1F * hist_TagMuon_phi = new TH1F("hist_TagMuon_phi", "hist_TagMuon_phi", phibins, philow, phihigh);
   TH1F * hist_TagMuon_dz = new TH1F("hist_TagMuon_dz", "hist_TagMuon_dz", 200, -100, 100);
   TH1F * hist_TagMuon_z = new TH1F("hist_TagMuon_z", "hist_TagMuon_z", 200, -100, 100);
   TH1F * hist_TagMuon_iso = new TH1F("hist_TagMuon_iso", "hist_TagMuon_iso", 100, 0, 1);

   TH1F * hist_ProbeTau_pt = new TH1F("hist_ProbeTau_pt", "hist_ProbeTau_pt", 200, 0, 1000);
   TH1F * hist_ProbeTau_eta = new TH1F("hist_ProbeTau_eta", "hist_ProbeTau_eta", etabins, etalow, etahigh);
   TH1F * hist_ProbeTau_phi = new TH1F("hist_ProbeTau_phi", "hist_ProbeTau_phi", phibins, philow, phihigh);

   TH1F * hist_LeadingJet_pt = new TH1F("hist_LeadingJet_pt", "hist_LeadingJet_pt", 200, 0, 1000);
   TH1F * hist_LeadingJet_eta = new TH1F("hist_LeadingJet_eta", "hist_LeadingJet_eta", etabins, etalow, etahigh);
   TH1F * hist_LeadingJet_phi = new TH1F("hist_LeadingJet_phi", "hist_LeadingJet_phi", phibins, etalow, etahigh);

   TH1F * hist_ProbePatTau_pt = new TH1F("hist_ProbePatTau_pt", "hist_ProbePatTau_pt", 200, 0, 1000);
   TH1F * hist_ProbePatTau_eta = new TH1F("hist_ProbePatTau_eta", "hist_ProbePatTau_eta", etabins, etalow, etahigh);
   TH1F * hist_ProbePatTau_phi = new TH1F("hist_ProbePatTau_phi", "hist_ProbePatTau_phi", phibins, philow, phihigh);
   TH1F * hist_ProbePatTau_dr = new TH1F("hist_ProbePatTau_dr", "hist_ProbePatTau_dr", 100, 0, 1);

   TH1F * hist_ProbeTwoprong_pt = new TH1F("hist_ProbeTwoprong_pt", "hist_ProbeTwoprong_pt", 200, 0, 1000);
   TH1F * hist_ProbeTwoprong_eta = new TH1F("hist_ProbeTwoprong_eta", "hist_ProbeTwoprong_eta", etabins, etalow, etahigh);
   TH1F * hist_ProbeTwoprong_phi = new TH1F("hist_ProbeTwoprong_phi", "hist_ProbeTwoprong_phi", phibins, philow, phihigh);
   TH1F * hist_ProbeTwoprong_dr = new TH1F("hist_ProbeTwoprong_dr", "hist_ProbeTwoprong_dr", 100, 0, 1);

   TH1F * hist_MT = new TH1F("hist_MT", "hist_MT", 60, 0, 300);
   TH1F * hist_MTn1 = new TH1F("hist_MTn1", "hist_MTn1", 60, 0, 300);

   // the loop
   if (fChain == 0) return;
   Long64_t nentries = fChain->GetEntriesFast();
   Long64_t pro_entries = 0;
   Long64_t real_nentries = fChain->GetEntries();
   std::cout << "About to loop over TChain with " << real_nentries << " entries" << std::endl;
   if (MAX_ENTRIES != -1) std::cout <<  "but will terminate after " << MAX_ENTRIES << " passing entries" << std::endl;
   double percentDone;
   double incrementReport = 0.05;
   double incrementProcess = 0.00;
   for (Long64_t jentry=0; jentry<nentries; jentry++)
   {
      // status update
      percentDone = double(pro_entries) / double(real_nentries);
      if (percentDone > incrementProcess) {
        std::cout << "Processing entry " << pro_entries << "..." << std::endl;
        incrementProcess += incrementReport;
      }

      // load the entry
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      fChain->GetEntry(jentry);
      pro_entries += 1;

      // fill pre-selection histos
      hist_nTagMuons->Fill(nTagMuons);
      hist_nProbeTaus->Fill(nProbeTaus);

      // MT histos
      if (passZTnP) {
        hist_MT->Fill(TauPreMT);
      }
      if (passZTnP && passZMuonTrigger && TauPreDr>0.5 && TauPrePzeta>-25 && passZExtraMuon && passZExtraElectron && passZDiMuon && passZBVeto) {
        hist_MTn1->Fill(TauPreMT);
      }

      // apply preselection
      if (!passZPre) continue;
      pass_selection_count += 1;

      // fill histograms
      hist_HT->Fill(HT);
      hist_MET->Fill(MET);
      hist_nJets->Fill(nJets);
      
      TLorentzVector Zvis_pattau;
      TLorentzVector Zvis_taujet;
      TLorentzVector Zvis_twoprong;
      TLorentzVector muon;
      TLorentzVector taujet;
      TLorentzVector pattau;
      TLorentzVector twoprong;
      
      muon.SetPtEtaPhiM((*TagMuon_pt)[0], (*TagMuon_eta)[0], (*TagMuon_phi)[0], (*TagMuon_mass)[0]);
      taujet.SetPtEtaPhiM((*ProbeTau_pt)[0], (*ProbeTau_eta)[0], (*ProbeTau_phi)[0], (*ProbeTau_mass)[0]);

      int pattau_index = -1;
      double best_DR = 100.0;
      for(unsigned int i = 0; i < (*Tau_pt).size(); i++)
      {
        pattau.SetPtEtaPhiM((*Tau_pt)[i], (*Tau_eta)[i], (*Tau_phi)[i], (*Tau_mass)[i]);
        double DR = taujet.DeltaR(pattau);
        if (DR < 0.4 && DR < best_DR) {
          best_DR = DR;
          pattau_index = i;
        } 
      }
      int twoprong_index = -1;
      best_DR = 100.0;
      for(unsigned int i = 0; i < (*TwoProng_pt).size(); i++)
      {
        twoprong.SetPtEtaPhiM((*TwoProng_pt)[i], (*TwoProng_eta)[i], (*TwoProng_phi)[i], (*TwoProng_mass)[i]);
        double DR = taujet.DeltaR(twoprong);
        if (DR < 0.4 && DR < best_DR) {
          best_DR = DR;
          twoprong_index = i;
        } 
      }

      Zvis_taujet = muon;
      Zvis_taujet += taujet;
      hist_Zvis_taujet_mass->Fill(Zvis_taujet.M());
      hist_Zvis_taujet_pt->Fill(Zvis_taujet.Pt());
      hist_Zvis_taujet_phi->Fill(Zvis_taujet.Phi());
      hist_Zvis_taujet_eta->Fill(Zvis_taujet.Eta());
      if(pattau_index != -1) {
        pattau.SetPtEtaPhiM((*Tau_pt)[pattau_index], (*Tau_eta)[pattau_index], (*Tau_phi)[pattau_index], (*Tau_mass)[pattau_index]);
        Zvis_pattau = muon;
        Zvis_pattau += pattau;
        hist_Zvis_pattau_mass->Fill(Zvis_pattau.M());
        hist_Zvis_pattau_pt->Fill(Zvis_pattau.Pt());
        hist_Zvis_pattau_phi->Fill(Zvis_pattau.Phi());
        hist_Zvis_pattau_eta->Fill(Zvis_pattau.Eta());

        hist_ProbePatTau_pt->Fill(pattau.Pt());
        hist_ProbePatTau_eta->Fill(pattau.Eta());
        hist_ProbePatTau_phi->Fill(pattau.Phi());
        hist_ProbePatTau_dr->Fill(pattau.DeltaR(taujet));

        hist_nProbePatTaus->Fill(1);
      } else {
        hist_nProbePatTaus->Fill(0);
      }
      if(twoprong_index != -1) {
        twoprong.SetPtEtaPhiM((*TwoProng_pt)[twoprong_index], (*TwoProng_eta)[twoprong_index], (*TwoProng_phi)[twoprong_index], (*TwoProng_mass)[twoprong_index]);
        Zvis_twoprong = muon;
        Zvis_twoprong += twoprong;
        hist_Zvis_twoprong_mass->Fill(Zvis_twoprong.M());
        hist_Zvis_twoprong_pt->Fill(Zvis_twoprong.Pt());
        hist_Zvis_twoprong_phi->Fill(Zvis_twoprong.Phi());
        hist_Zvis_twoprong_eta->Fill(Zvis_twoprong.Eta());

        hist_ProbeTwoprong_pt->Fill(twoprong.Pt());
        hist_ProbeTwoprong_eta->Fill(twoprong.Eta());
        hist_ProbeTwoprong_phi->Fill(twoprong.Phi());
        hist_ProbeTwoprong_dr->Fill(twoprong.DeltaR(taujet));

        hist_nProbeTwoprongs->Fill(1);
      } else {
        hist_nProbeTwoprongs->Fill(0);
      }
      
      hist_TagMuon_pt->Fill(muon.Pt());
      hist_TagMuon_eta->Fill(muon.Eta());
      hist_TagMuon_phi->Fill(muon.Phi());
      hist_TagMuon_dz->Fill( (*TagMuon_dz)[0] );
      hist_TagMuon_z->Fill( (*TagMuon_z)[0] );
      hist_TagMuon_iso->Fill( (*TagMuon_iso)[0] );

      hist_ProbeTau_pt->Fill(taujet.Pt());
      hist_ProbeTau_eta->Fill(taujet.Eta());
      hist_ProbeTau_phi->Fill(taujet.Phi());

      if(nJets > 0) {
        hist_LeadingJet_pt->Fill((*Jet_pt)[0]);
        hist_LeadingJet_eta->Fill((*Jet_eta)[0]);
        hist_LeadingJet_phi->Fill((*Jet_phi)[0]);
      }

      // possible early exit, and cleanup
      if (pass_selection_count == MAX_ENTRIES) break;
   }

   // save histograms
   output->Write();
   output->Close();
}
