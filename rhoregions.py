from ROOT import *
filelow = TFile("signal125_rel_egamma_rholow.root")
filehigh = TFile("signal125_rel_egamma_rhohigh.root")
filemed = TFile("signal125_rel_egamma_rhomed.root")
histlow = filelow.Get("hist_sum_1")
histmed = filemed.Get("hist_sum_1")
histhigh = filehigh.Get("hist_sum_1")

hists = []
hists.append(histlow)
hists.append(histmed)
hists.append(histhigh)

for hist in hists:
  hist.SetStats(0)
  hist.Scale(100.0/hist.Integral())

leg = TLegend(0.55,0.7,0.9,0.9)

c = TCanvas()
c.SetLogy()

leg.AddEntry(histlow, 'rho<5', "l")
leg.AddEntry(histmed, 'rho>=5 && rho<15', "l")
leg.AddEntry(histhigh, 'rho>=15', "l")

histmed.SetTitle("Isolation Variable pre-cut, 125 GeV Scalar")
histmed.GetXaxis().SetTitle("rel egamma iso")
histmed.GetYaxis().SetTitle("two-prong objects, scaled")

histlow.SetLineColor(kRed)
histmed.SetLineColor(kBlue)
histhigh.SetLineColor(kGreen)

histmed.Draw('hist')
histlow.Draw('hist same')
histhigh.Draw('hist same')
leg.Draw('same')

raw_input()
