from ROOT import *
from sys import *
from optparse import OptionParser
parser = OptionParser()
parser.add_option('--logy',action='store_true',default=False,dest='logy')
(options,args) = parser.parse_args()

files = []
names = []
for i in range(len(args)):
  #if i == 0:
  #  continue
  files.append(TFile(args[i]))
  names.append(args[i])

var = "pt"

objs = []
count = 0
for fi in files:
  obj = fi.Get('eff_genobj_'+var)
  obj.SetLineColor(kPink+count)
  count += 1
  objs.append(obj)

c = TCanvas()
c.cd()
if options.logy:
  c.SetLogy()

leg = TLegend(0.55, 0.80, 0.9, 0.9)
for i in range(len(objs)):
  obj = objs[i]
  if options.logy:
    obj.SetMaximum(2)
    obj.SetMinimum(0.01)
  else:
    obj.SetMaximum(1.1)
    obj.SetMinimum(0.0)
  leg.AddEntry(obj, names[i], "l")
  obj.SetTitle("Gen obj within R=0.1 to RECO obj")
  obj.GetYaxis().SetTitle("Efficiency")
  obj.GetXaxis().SetTitle(var)
  obj.SetStats(0)
  #obj.Draw()
  obj.Draw("Same")
leg.Draw("Same")


raw_input()

