#include <string>
#include <vector>
#include <iostream>
#include <dirent.h> // for traversing a directory
#include <chrono> // for timing
#include "TChain.h"
#include "MyLooper.C+O" // the name of the MakeClass() .C file
using std::vector;
using std::string;
using std::cout;
using std::endl;

// forward declare helper functions
void make_histos(vector<string>, string);
void ProcessDirectory(std::string directory);
void ProcessFile(std::string file);
void ProcessEntity(struct dirent* entity);

// globals
string treename = "twoprongNtuplizer/fTree2";
//string treename = "twoprongModNtuplizer/fTree2";
string base_path = "/cms/chiarito/eos/twoprong/ztagandprobe/Nov17_trees/"; // end in '/'
TChain * chain = new TChain(treename.c_str());
string path = "";
vector<string> paths;
Long64_t MAX_ENTRIES = 100;
string output = "";
string pre = "output_test_"; // end in '_'
string post = ".root";

void analysis_all()
{
  chrono::high_resolution_clock::time_point time_start = chrono::high_resolution_clock::now();

  paths.push_back("DY/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_10to50_signal_MuonHadronicFilter/");
  output = "DY10sig";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext1_signal_MuonHadronicFilter/");
  paths.push_back("DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext2_signal_MuonHadronicFilter/");
  output = "DYsig";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("DY/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_10to50_bkg_MuonHadronicExcludedFilter/");
  output = "DY10bkg";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext1_bkg_MuonHadronicExcludedFilter/");
  paths.push_back("DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext2_bkg_MuonHadronicExcludedFilter/");
  output = "DYbkg";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_1000to1400";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_120to170";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_1400to1800";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_15to30";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_170to300";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_1800to2400";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_2400to3200";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_300to470";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_30to50";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_470to600";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_50to80";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_600to800";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_800to1000";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("QCD/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/");
  output = "QCD_80to120";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("BKG/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/");
  output = "WJets";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("BKG/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/");
  output = "WW";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("BKG/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/");
  output = "WZ1L3Nu";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("BKG/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/");
  output = "WZ1L2Q";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("BKG/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/");
  output = "STbar";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("BKG/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/");
  output = "ST";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("BKG/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/");
  paths.push_back("BKG/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/");
  output = "tW";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("BKG/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/");
  output = "TT";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("DATA/SingleMuon/RunC/");
  paths.push_back("DATA/SingleMuon/RunD/");
  paths.push_back("DATA/SingleMuon/RunE/");
  paths.push_back("DATA/SingleMuon/RunF/");
  paths.push_back("DATA/SingleMuon/RunG/");
  paths.push_back("DATA/SingleMuon/RunH/");
  output = "DATA";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

/*
  paths.push_back("");
  output = "";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  paths.push_back("");
  output = "";
  make_histos(paths, output);
  paths.clear();
  chain->Reset();

  */
  chrono::high_resolution_clock::time_point time_end = chrono::high_resolution_clock::now();
  auto run_time = chrono::duration_cast<chrono::seconds>( time_end - time_start ).count();
  cout << "\nFinished producing " << pre+"X"+post << " files, overall processing took " << run_time << " seconds" << endl;
}

void make_histos(vector<string> paths, string output)
{
  // make a chain with all rootfiles in a directory
  for(int i = 0; i < paths.size(); i++) {
    path = base_path + paths[i];
    cout << "Running on " << path << endl;
    ProcessDirectory("");
  }

  // make a MakeClass object using the above chain
  MyLooper * looper = new MyLooper(chain);

  // define output file name
  string outputfilename = pre + output + post;

  // tell the object to loop, and time it
  chrono::high_resolution_clock::time_point time_1 = chrono::high_resolution_clock::now();
  looper->CustomLoop(outputfilename.c_str(), MAX_ENTRIES);
  chrono::high_resolution_clock::time_point time_2 = chrono::high_resolution_clock::now();

  // report
  auto run_time = chrono::duration_cast<chrono::seconds>( time_2 - time_1 ).count();
  cout << "Loop() took " << run_time << " seconds" << endl;  
}

// helper function definitions
void ProcessDirectory(std::string directory)
{
    std::string dirToOpen = path + directory;
    auto dir = opendir(dirToOpen.c_str());
    path = dirToOpen + "/";
    if(NULL == dir) {
        std::cout << "could not open directory: " << dirToOpen.c_str() << std::endl;
        return;
    }
    auto entity = readdir(dir);
    while(entity != NULL) {
        ProcessEntity(entity);
        entity = readdir(dir);
    }
    path.resize(path.length() - 1 - directory.length());
    closedir(dir);
}

void ProcessEntity(struct dirent* entity)
{
    if(entity->d_type == DT_DIR) {
        if(entity->d_name[0] == '.') return;
        ProcessDirectory(std::string(entity->d_name));
        return;
    }
    if(entity->d_type == DT_REG) {
        ProcessFile(std::string(entity->d_name));
        return;
    }
}

void ProcessFile(std::string file)
{
    if (file.find(".root") != std::string::npos) {
      //std::cout << "Found rootfile     : " << (file) << std::endl;
      chain->Add((path + file).c_str());
    }
}
