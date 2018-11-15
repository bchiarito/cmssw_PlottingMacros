#ifndef MyLooper_h
#define MyLooper_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include "vector"

// the base class
#include "MyClass.C"

class MyLooper : public MyClass {
public :
   MyLooper(TTree* tree) : MyClass(tree)
   {
   }

   void CustomLoop(const char *, Long64_t);
};

#endif

#ifdef MyLooper_cxx
#endif
