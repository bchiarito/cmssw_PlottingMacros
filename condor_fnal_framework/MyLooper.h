#ifndef MyLooper_h
#define MyLooper_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include "vector"

// the base class
#include "MyClassDATA.C"

class MyLooper : public MyClassDATA {
public :
   MyLooper(TTree* tree) : MyClassDATA(tree)
   {
   }

   void CustomLoop(const char *, Long64_t);
};

#endif

#ifdef MyLooper_cxx
#endif
