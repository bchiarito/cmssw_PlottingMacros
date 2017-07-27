from ROOT import *
from sys import *

fi1 = TFile('leading_photonmass_largebox.root')
fi2 = TFile('leading_pi0mass_largebox.root')
fi3 = TFile('summed_photonmass_largebox.root')
fi4 = TFile('summed_pi0mass_largebox.root')

obj1 = fi1.Get('hist_sum_1')
obj2 = fi2.Get('hist_sum_1')
obj3 = fi3.Get('hist_sum_1')
obj4 = fi4.Get('hist_sum_1')

obj1.SetStats(0)
obj1.GetXaxis().SetTitle('mass (GeV)')
obj1.GetYaxis().SetTitle('tight twoprong object count')
obj1.SetTitle('Signal 125 MC')

obj1.SetLineColor(kRed)
obj2.SetLineColor(kBlue)
obj3.SetLineColor(kRed+2)
obj4.SetLineColor(kBlue+2)

maximum = max(obj1.GetMaximum(), obj2.GetMaximum(), obj3.GetMaximum(), obj4.GetMaximum())
obj1.SetMaximum(maximum*1.2)

leg = TLegend(0.5, 0.6, 0.9, 0.9)
leg.AddEntry(obj1, 'leading photon, photon mass', 'l')
leg.AddEntry(obj3, 'summed photon, photon mass', 'l')
leg.AddEntry(obj2, 'leading photon, pi0 mass', 'l')
leg.AddEntry(obj4, 'summed photon, pi0 mass', 'l')

c = TCanvas()
obj1.Draw('same hist')
obj2.Draw('same hist')
obj3.Draw('same hist')
obj4.Draw('same hist')
leg.Draw('same')
vert_line = TLine(0.55, 0, 0.55, obj1.GetMaximum())
vert_line.Draw("same")

raw_input()
