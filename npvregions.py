from ROOT import *
filelow = TFile("signal125_egamma_npvlow.root")
filehigh = TFile("signal125_egamma_npvhigh.root")
filemed = TFile("signal125_egamma_npvmed.root")
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

leg.AddEntry(histlow, 'npv<5', "l")
leg.AddEntry(histmed, 'npv>=5 && npv<15', "l")
leg.AddEntry(histhigh, 'npv>=15', "l")

histmed.SetTitle("Isolation Variable Pre-Cut")
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
