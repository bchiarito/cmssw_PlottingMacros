from ROOT import *
from math import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--file',
                  dest='file', default='none.root',
                  help='')
parser.add_option('--out',
                  dest='saveas',
                  default='',
                  help='')
(options, args) = parser.parse_args()

nodr_file = TFile(options.file)
title = 'Fake Rate'

fakerate_pt = nodr_file.Get('fakerate_m0toInf_pt')
fakerate_ecal = nodr_file.Get('fakerate_m0toInf_ecal')
fakerate_hcal = nodr_file.Get('fakerate_m0toInf_hcal')

c = TCanvas()

fakerate_pt.SetStats(0)
fakerate_pt.SetLineColor(kBlack)
fakerate_pt.Draw()
fakerate_pt.SetTitle(title)

fakerate_ecal.SetStats(0)
fakerate_ecal.SetLineColor(kRed)
fakerate_ecal.Draw('same')

fakerate_hcal.SetStats(0)
fakerate_hcal.SetLineColor(kBlue)
fakerate_hcal.Draw('same')

leg = TLegend(0.7,0.8,0.9,0.9)
leg.AddEntry(fakerate_pt, 'total pt', 'l')
leg.AddEntry(fakerate_ecal, 'photon pt', 'l')
leg.AddEntry(fakerate_hcal, 'tracks pt', 'l')
leg.Draw('same')

raw_input()

#c.SaveAs('')
