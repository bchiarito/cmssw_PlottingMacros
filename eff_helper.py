from ROOT import *
import math
import sys
from optparse import *

# helper function
def compute_eff_error_bars(eff, numer, denom):
    eff.Add(numer)
    eff.Divide(denom)
    for b in range(1, eff.GetNbinsX()+1):
      e = eff.GetBinContent(b)
      d = denom.GetBinContent(b)
      if not d==0:
        error = math.sqrt( (e * (1-e)) / (d) )
      else:
        error = 0
      eff.SetBinError(b, error)

# command line options
parser = OptionParser()
parser.add_option('--out', type='string', action='store', default='', dest='out', help='rootfile output')
parser.add_option('--bins', type='string', action='store', default='', dest='bins', help='binning')
parser.add_option('--cut', type='string', action='store', default='', dest='cut', help='extra cut')
parser.add_option('--cand', action='store_true', default=False, dest='cand', help='candidates vs tight')
(options, args) = parser.parse_args()

# need varaible to plot
if len(sys.argv) <= 2:
  sys.exit()

# shell commands
from subprocess import call
cut_numer = ""
if sys.argv[1]=='eta':
  label="\eta"
  var = "GenTau_eta"
  bins = "30,-6,6"
  cut_denom = "GenTau_objDR<0.2 && nTwoProngs>0" if not options.cand else "GenTau_candobjDR<0.2 && nTwoProngCands>0"
elif sys.argv[1]=='pt':
  label="p_{T}"
  var = "GenTau_pt"
  bins = "80,0,400"
  cut_denom = "GenTau_objDR<0.2 && nTwoProngs>0" if not options.cand else "GenTau_candobjDR<0.2 && nTwoProngCands>0"
elif sys.argv[1]=='phi':
  label="\phi"
  var = "GenTau_phi"
  bins = "30,-6,6"
  cut_denom = "GenTau_objDR<0.2 && nTwoProngs>0" if not options.cand else "GenTau_candobjDR<0.2 && nTwoProngCands>0"
elif sys.argv[1]=='npv':
  label="nPV"
  var = "nPV"
  bins = "40,0,100"
  cut_denom = "nTwoProngs>0" if not options.cand else "nTwoProngCands>0"
elif sys.argv[1]=='rho':
  label="rho"
  var = "rho"
  bins = "40,0,100"
  cut_denom = "nTwoProngs>0" if not options.cand else "nTwoProngCands>0"
else:
  sys.exit()
if not options.cut=="":
  cut_numer = options.cut
  cut_denom = cut_denom + " && " + options.cut
directory = sys.argv[2]
command_numer = 'python plotting/plotter.py -q --var="%s" --bins=%s --cut="%s" --savehist=denom ' % (var,bins,cut_numer) + directory
command_denom = 'python plotting/plotter.py -q --var="%s" --bins=%s --cut="%s" --savehist=numer ' % (var,bins,cut_denom) + directory
print command_numer
call(command_numer, shell=True)
print command_denom
call(command_denom, shell=True)

# eff histo
file1 = TFile('numer.root')
file2 = TFile('denom.root')
numer = file1.Get("hist_sum_1")
denom = file2.Get("hist_sum_1")
nbins = numer.GetNbinsX()
w = numer.GetBinWidth(1)
low = numer.GetBinLowEdge(1)
high = numer.GetBinLowEdge(nbins) + w
eff = TH1F("eff","eff",nbins,low,high)
compute_eff_error_bars(eff,numer,denom)
eff.SetMaximum(1.0)
eff.SetStats(0)
eff.GetYaxis().SetTitle("efficiency")
eff.GetXaxis().SetTitle("%s \mathrm{\,of\,gen\,obj}" % label)
eff.SetTitle("Efficiency to reconstruct tau as 2-prong obj")

# end
if options.out == "":
  eff.Draw()
  raw_input()
else:
  outfile = TFile(options.out, 'recreate')
  outfile.cd()
  eff.Write()
  outfile.Close()

# cleanup
import os
os.remove('numer.root')
os.remove('denom.root')
