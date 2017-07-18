from ROOT import *
from sys import *

fi = TFile("qcd.root")
hist1 = fi.Get("qcd_sum_1")
hist2 = fi.Get("qcd_sum_2")
hist3 = fi.Get("qcd_sum_3")
#hist4 = fi.Get("qcd_sum_4")

hist1.SetLineColor(kBlue)
hist2.SetLineColor(kRed)
hist3.SetLineColor(kGreen)
#hist4.SetLineColor(kBlack)

#hist1.Sumw2()
#hist2.Sumw2()
#hist3.Sumw2()
#hist4.Sumw2()

c = TCanvas()
c.cd()
c.SetLogy()

leg = TLegend(0.55, 0.80, 0.9, 0.9)
leg.AddEntry(hist1, "track only", "l")
leg.AddEntry(hist2, "photon only", "l")
leg.AddEntry(hist3, "both asym", "l")
#leg.AddEntry(hist4, "pt20 con1", "l")

hist2.SetTitle("QCD MC 2016")
hist2.GetYaxis().SetTitle("Twoprong Object count")
hist2.GetXaxis().SetTitle("pT")
hist2.SetStats(0)

hist2.Draw("same")
hist1.Draw("same")
hist3.Draw("same")
#hist4.Draw("same")
leg.Draw("Same")

hist1.Print("all")
hist2.Print("all")
hist3.Print("all")
#hist4.Print("all")

raw_input()
