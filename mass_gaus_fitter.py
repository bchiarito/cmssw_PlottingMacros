from ROOT import *
import sys

fi = TFile(sys.argv[1])

hist_zero = fi.Get("hist_sum_1")
hist_pi0 = fi.Get("hist_sum_2")

low = float(sys.argv[2])
high = float(sys.argv[3])

c = TCanvas()
c.cd()
hist_zero.SetStats(0)
hist_zero.SetLineColor(kBlack)
hist_zero.SetTitle(sys.argv[4]+", zero mass")
hist_zero.GetXaxis().SetTitle("mass (GeV)")
hist_zero.GetYaxis().SetTitle("twoprong objects")
hist_zero.Sumw2()
hist_zero.Fit("gaus","","",low,high)

c2 = TCanvas()
c2.cd()
hist_pi0.SetStats(0)
hist_pi0.SetLineColor(kBlack)
hist_pi0.SetTitle(sys.argv[4]+", pi0 mass")
hist_pi0.GetXaxis().SetTitle("mass (GeV)")
hist_pi0.GetYaxis().SetTitle("twoprong objects")
hist_pi0.Sumw2()
hist_pi0.Fit("gaus","","",low,high)
