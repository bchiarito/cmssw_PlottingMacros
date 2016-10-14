from ROOT import *
from math import *
from optparse import OptionParser

def color(count):
  return {
    0 : kRed,
    1 : kRed+1,
    2 : kRed+2,
    3 : kRed+3,
    4 : kBlack,
    5 : 25,
    6 : 26,
    7 : 27,
    8 : 28,
    9 : 29,
    10 : 30,
    11 : 31,
    12 : 32,
    }.get(count, kBlack)

drcut_file = TFile('fakerate_1D_histos_SinglePhoton_nodr.root')
title = "Fake Rate, SinglePhoton, nodr"
savename = "photon_profile_nodr.png"

hists = []
#hists.append(drcut_file.Get('fakerate_m0to400_pt'))
#hists.append(drcut_file.Get('fakerate_m400to600_pt'))
hists.append(drcut_file.Get('fakerate_m600to800_pt'))
#hists.append(drcut_file.Get('fakerate_m800to1000_pt'))
hists.append(drcut_file.Get('fakerate_m1000to1200_pt'))
#hists.append(drcut_file.Get('fakerate_m1200to1400_pt'))
hists.append(drcut_file.Get('fakerate_m1400to1600_pt'))
#hists.append(drcut_file.Get('fakerate_m1600to1800_pt'))
hists.append(drcut_file.Get('fakerate_m1800to2000_pt'))
hists.append(drcut_file.Get('fakerate_m0toInf_pt'))

c = TCanvas()
leg = TLegend(0.7,0.65,0.9,0.9)

count = 0
for hist in hists:
  hist.SetStats(0)
  hist.SetLineColor(color(count))
  hist.SetLineWidth(2)
  if count == 0:
    hist.Draw('hist')
    hist.SetTitle(title)
  else:
    hist.Draw('histsame')
  leg.AddEntry(hist, hist.GetName(), 'l')
  count += 1

leg.Draw('same')

raw_input()

c.SaveAs(savename)
