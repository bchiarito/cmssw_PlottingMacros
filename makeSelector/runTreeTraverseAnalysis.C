{
  TChain chain("diphotonAnalyzer/fTree2");

  chain.Add("TwoProngNtuplizer_signal125_track10_photon10.root");
  chain.Add("TwoProngNtuplizer_signal125_track10_photon1.root");

  chain.Process("treeTraverseAnalysis.C")
}
