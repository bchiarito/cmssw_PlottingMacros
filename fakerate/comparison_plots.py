from ROOT import *
from math import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--drcut',
                  dest='drcut_file', default="none.root",
                  help='')
parser.add_option('--nodr',
                  dest='nodr_file', default='none.root',
                  help='')
parser.add_option('--title',
                  dest='title',
                  default='',
                  help='')
parser.add_option('--out',
                  dest='saveas',
                  default='',
                  help='')
(options, args) = parser.parse_args()

drcut_file = TFile(options.drcut_file)
nodr_file = TFile(options.nodr_file)
title = options.title

fakerate_drcut_pt = drcut_file.Get('fakerate_m0toInf_phi')
fakerate_nodr_pt = nodr_file.Get('fakerate_m0toInf_phi')

c = TCanvas()

fakerate_drcut_pt.SetStats(0)
fakerate_drcut_pt.SetLineColor(kBlue)
fakerate_drcut_pt.Draw()
fakerate_drcut_pt.SetTitle(title)

fakerate_nodr_pt.SetStats(0)
fakerate_nodr_pt.SetLineColor(kRed)
fakerate_nodr_pt.Draw('same')

leg = TLegend(0.7,0.8,0.9,0.9)
leg.AddEntry(fakerate_drcut_pt, 'with dr>0.3 cut', 'l')
leg.AddEntry(fakerate_nodr_pt, 'with no dr cut', 'l')
leg.Draw('same')

raw_input()

c.SaveAs(options.saveas)
