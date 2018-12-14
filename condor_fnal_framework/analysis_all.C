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
void make_histos(string);
void ProcessDirectory(std::string directory);
void ProcessFile(std::string file);
void ProcessEntity(struct dirent* entity);

// globals
string treename = "twoprongNtuplizer/fTree2";
//string treename = "twoprongModNtuplizer/fTree2";
TChain * chain = new TChain(treename.c_str());
string path = "./";
vector<string> paths;
Long64_t MAX_ENTRIES = -1;
string output = "";
string pre = "output_test_"; // end in '_'
string post = ".root";

void analysis_all()
{
  chrono::high_resolution_clock::time_point time_start = chrono::high_resolution_clock::now();

  output = "all";
  make_histos(output);

  chrono::high_resolution_clock::time_point time_end = chrono::high_resolution_clock::now();
  auto run_time = chrono::duration_cast<chrono::seconds>( time_end - time_start ).count();
  cout << "\nFinished producing " << pre+"X"+post << " files, overall processing took " << run_time << " seconds" << endl;
}

void make_histos(string output)
{
  ProcessDirectory("");

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
