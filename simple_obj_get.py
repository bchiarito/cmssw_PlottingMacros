from ROOT import *
from sys import *
print argv[1]
print argv[2]
fi = TFile(argv[1])
obj = fi.Get('diphotonAnalyzer/'+argv[2])
