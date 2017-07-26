from ROOT import *
from sys import *
from optparse import OptionParser
parser = OptionParser()
parser.add_option('--logy',action='store_true',default=False,dest='logy')
parser.add_option('--leg1',action='store',default='',dest='leg1')
parser.add_option('--leg2',action='store',default='',dest='leg2')
parser.add_option('--leg3',action='store',default='',dest='leg3')
parser.add_option('--leg4',action='store',default='',dest='leg4')
parser.add_option('--title',action='store',default='',dest='title')
parser.add_option('--save',action='store',default='',dest='save')
(options,args) = parser.parse_args()

files = []
names = []
for i in range(len(args)):
  files.append(TFile(args[i]))
  if (i == 0) and options.leg1 != '':
    names.append(options.leg1)
  elif (i == 1) and options.leg2 != '':
    names.append(options.leg2)
  elif (i == 2) and options.leg3 != '':
    names.append(options.leg3)
  elif (i == 3) and options.leg4 != '':
    names.append(options.leg4)
  else:
    names.append(args[i])

var = "pt"

objs = []
count = 0
for fi in files:
  obj = fi.Get('eff_genobj_'+var)
  'obj.SetLineColor(kPink+count)'
  '''if count == 0:
    obj.SetLineColor(kBlue+4)
    obj.SetMarkerStyle(5)
  if count == 1:
    obj.SetLineColor(kBlue+2)
  if count == 2:
    obj.SetLineColor(kPink+2)
  if count == 3:
    obj.SetLineColor(kPink)''' 
  if count == 0:
    obj.SetLineColor(kBlue)
  elif count == 4:
    obj.SetLineColor(kRed)
  #elif count == 0:
  #  obj.SetLineColor(kGray+2)
  #else:
  #  obj.SetLineColor(kGray)
  else:
    obj.SetLineColor(kBlack)
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
  if options.title == "":
    obj.SetTitle("Gen obj within R=0.1 to RECO obj")
  else:
    obj.SetTitle(options.title)
  obj.GetYaxis().SetTitle("Efficiency")
  obj.GetXaxis().SetTitle(var)
  obj.SetStats(0)
  obj.Draw("Same")
leg.Draw("Same")

if not options.save == "":
  c.SaveAs(options.save)
else:
  raw_input()
