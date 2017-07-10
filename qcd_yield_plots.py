from ROOT import *
from sys import *

fi = TFile("qcd_compare.root")
hist1 = fi.Get("qcd_compare_sum_1")
hist2 = fi.Get("qcd_compare_sum_2")
hist3 = fi.Get("qcd_compare_sum_3")

hist1.SetLineColor(kBlue)
hist2.SetLineColor(kRed)
hist3.SetLineColor(kGreen)

hist1.Sumw2()
hist2.Sumw2()
hist3.Sumw2()

c = TCanvas()
c.cd()
c.SetLogy()

leg = TLegend(0.55, 0.80, 0.9, 0.9)
leg.AddEntry(hist1, "pt0_con10", "l")
leg.AddEntry(hist2, "pt0_con1", "l")
leg.AddEntry(hist3, "pt20_con1", "l")

hist2.SetTitle("QCD MC 2016")
hist2.GetYaxis().SetTitle("Twoprong Object count")
hist2.GetXaxis().SetTitle("pT")
hist2.SetStats(0)

hist2.Draw("same")
hist1.Draw("same")
hist3.Draw("same")
leg.Draw("Same")

hist1.Print("all")
hist2.Print("all")
hist3.Print("all")

raw_input()
