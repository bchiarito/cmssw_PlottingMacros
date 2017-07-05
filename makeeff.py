from ROOT import *
from sys import *
if len(argv) == 2:
  print argv[1]
  fi = TFile(argv[1])
  fi.cd("diphotonAnalyzer")
  fi.ls()
if len(argv) == 4:
  print argv[1]
  print argv[2]
  fi = TFile(argv[1])
  nume = fi.Get('diphotonAnalyzer/'+argv[2])
  deno = fi.Get('diphotonAnalyzer/'+argv[3])
  nume.Divide(deno)
  nume.GetYaxis().SetTitle("Efficiency")
  nume.Draw()
  raw_input()
