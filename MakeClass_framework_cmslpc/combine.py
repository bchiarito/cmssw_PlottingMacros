from __future__ import division
import ROOT
import cross_sections as xs

# help message
from optparse import OptionParser
usage = "python %prog <path_with_histos> [options]\n\n<path_with_histos> should be the relative path to a folder whose contents are rootfiles output_DYsig.root etc."
parser = OptionParser(usage=usage)
parser.add_option('--out', type='string', action='store', default='summary_hists.pdf', dest='out', help='the output filename')
parser.add_option('--test', action='store_true', default=False, dest='test', help='instead of saving the output, draw one histogram and display it')
(options, args) = parser.parse_args()

# configuration
filename_prefix = args[0] + "/output_"
pdf_filename = options.out

# cosmetics
data_color = ROOT.kBlack
dysig_color = ROOT.kMagenta
dybkg_color = ROOT.kRed
wjets_color = ROOT.kOrange-9
wwwz_color = ROOT.kOrange+1
ttbar_color = ROOT.kGreen
top_color = ROOT.kGreen+1
qcd_color = ROOT.kGray
data_label = "SingleMuon"
dysig_label = "DY signal"
dybkg_label = "DY bkg"
wjets_label = "Wjets"
wwwz_label = "WW+WZ"
ttbar_label = "ttbar"
top_label = "t+tW"
qcd_label = "QCD"
x1 = 0.7
x2 = 0.89
y1 = 0.7
y2 = 0.89
reversed_histos = []
reversed_histos.append('Zvis_taujet_mass')
reversed_histos.append('Zvis_pattau_mass')
reversed_histos.append('Zvis_twoprong_mass')
reversed_histos.append('Zvis_pattau_mass_fail')
reversed_histos.append('Zvis_twoprong_mass_fail')

# helper functions
def extract_histos(rootfile):
  histos = []
  keyList = rootfile.GetListOfKeys()
  for key in keyList:
    cl = ROOT.gROOT.GetClass(key.GetClassName())
    if not cl.InheritsFrom("TH1"): continue
    hist = key.ReadObj()
    histos.append(hist)
  return histos

def total_weight(hist):
  return hist.Integral() + hist.GetBinContent(hist.GetNbinsX()+1) + hist.GetBinContent(0)

def entries(hist):
  return hist.GetEntries()

# extract histos into memory
data = ROOT.TFile(filename_prefix+"DATA.root")
data_hists = extract_histos(data)
dy10sig = ROOT.TFile(filename_prefix+"DY10sig.root")
dy10sig_hists = extract_histos(dy10sig)
dysig = ROOT.TFile(filename_prefix+"DYsig.root")
dysig_hists = extract_histos(dysig)

dy1sig = ROOT.TFile(filename_prefix+"DY1sig.root")
dy1sig_hists = extract_histos(dy1sig)
dy2sig = ROOT.TFile(filename_prefix+"DY2sig.root")
dy2sig_hists = extract_histos(dy2sig)
dy3sig = ROOT.TFile(filename_prefix+"DY3sig.root")
dy3sig_hists = extract_histos(dy3sig)
dy4sig = ROOT.TFile(filename_prefix+"DY3sig.root")
dy4sig_hists = extract_histos(dy3sig)
dy1bkg = ROOT.TFile(filename_prefix+"DY1bkg.root")
dy1bkg_hists = extract_histos(dy1bkg)
dy2bkg = ROOT.TFile(filename_prefix+"DY2bkg.root")
dy2bkg_hists = extract_histos(dy2bkg)
dy3bkg = ROOT.TFile(filename_prefix+"DY3bkg.root")
dy3bkg_hists = extract_histos(dy3bkg)
dy4bkg = ROOT.TFile(filename_prefix+"DY3bkg.root")
dy4bkg_hists = extract_histos(dy3bkg)

dy10bkg = ROOT.TFile(filename_prefix+"DY10bkg.root")
dy10bkg_hists = extract_histos(dy10bkg)
dybkg = ROOT.TFile(filename_prefix+"DYbkg.root")
dybkg_hists = extract_histos(dybkg)
wjets = ROOT.TFile(filename_prefix+"WJets.root")
wjets_hists = extract_histos(wjets)

w1jets = ROOT.TFile(filename_prefix+"W1Jets.root")
w1jets_hists = extract_histos(w1jets)
w2jets = ROOT.TFile(filename_prefix+"W2Jets.root")
w2jets_hists = extract_histos(w2jets)
w3jets = ROOT.TFile(filename_prefix+"W3Jets.root")
w3jets_hists = extract_histos(w3jets)
w4jets = ROOT.TFile(filename_prefix+"W4Jets.root")
w4jets_hists = extract_histos(w4jets)

ww = ROOT.TFile(filename_prefix+"WW.root")
ww_hists = extract_histos(ww)
wz3nu = ROOT.TFile(filename_prefix+"WZ3Nu.root")
wz3nu_hists = extract_histos(wz3nu)
wz2q = ROOT.TFile(filename_prefix+"WZ1L.root")
wz2q_hists = extract_histos(wz2q)
ttbar = ROOT.TFile(filename_prefix+"TT.root")
ttbar_hists = extract_histos(ttbar)
top = ROOT.TFile(filename_prefix+"STtop.root")
top_hists = extract_histos(top)
antitop = ROOT.TFile(filename_prefix+"STantitop.root")
antitop_hists = extract_histos(antitop)
tW = ROOT.TFile(filename_prefix+"tW.root")
tW_hists = extract_histos(tW)
qcd1000to1400 = ROOT.TFile(filename_prefix+"QCD_1000to1400.root")
qcd1000to1400_hists = extract_histos(qcd1000to1400)
qcd120to170 = ROOT.TFile(filename_prefix+"QCD_120to170.root")
qcd120to170_hists = extract_histos(qcd120to170)
qcd1400to1800 = ROOT.TFile(filename_prefix+"QCD_1400to1800.root")
qcd1400to1800_hists = extract_histos(qcd1400to1800)
qcd15to30 = ROOT.TFile(filename_prefix+"QCD_15to30.root")
qcd15to30_hists = extract_histos(qcd15to30)
qcd170to300 = ROOT.TFile(filename_prefix+"QCD_170to300.root")
qcd170to300_hists = extract_histos(qcd170to300)
qcd1800to2400 = ROOT.TFile(filename_prefix+"QCD_1800to2400.root")
qcd1800to2400_hists = extract_histos(qcd1800to2400)
qcd2400to3200 = ROOT.TFile(filename_prefix+"QCD_2400to3200.root")
qcd2400to3200_hists = extract_histos(qcd2400to3200)
qcd300to470 = ROOT.TFile(filename_prefix+"QCD_300to470.root")
qcd300to470_hists = extract_histos(qcd300to470)
qcd30to50 = ROOT.TFile(filename_prefix+"QCD_30to50.root")
qcd30to50_hists = extract_histos(qcd30to50)
qcd470to600 = ROOT.TFile(filename_prefix+"QCD_470to600.root")
qcd470to600_hists = extract_histos(qcd470to600)
qcd50to80 = ROOT.TFile(filename_prefix+"QCD_50to80.root")
qcd50to80_hists = extract_histos(qcd50to80)
qcd600to800 = ROOT.TFile(filename_prefix+"QCD_600to800.root")
qcd600to800_hists = extract_histos(qcd600to800)
qcd800to1000 = ROOT.TFile(filename_prefix+"QCD_800to1000.root")
qcd800to1000_hists = extract_histos(qcd800to1000)
qcd80to120 = ROOT.TFile(filename_prefix+"QCD_80to120.root")
qcd80to120_hists = extract_histos(qcd80to120)

# draw loop
logy = True
c1 = ROOT.TCanvas()
c1.SetLogy()
if not options.test: c1.Print(pdf_filename+"[")
for i in range(len(dysig_hists)):
  data_hist = data_hists[i]
  dy10sig_hist = dy10sig_hists[i]
  dysig_hist = dysig_hists[i]

  dy1sig_hist = dy1sig_hists[i]
  dy2sig_hist = dy2sig_hists[i]
  dy3sig_hist = dy3sig_hists[i]
  dy4sig_hist = dy4sig_hists[i]
  dy1bkg_hist = dy1bkg_hists[i]
  dy2bkg_hist = dy2bkg_hists[i]
  dy3bkg_hist = dy3bkg_hists[i]
  dy4bkg_hist = dy4bkg_hists[i]

  dy10bkg_hist = dy10bkg_hists[i]
  dybkg_hist = dybkg_hists[i]
  wjets_hist = wjets_hists[i]

  w1jets_hist = w1jets_hists[i]
  w2jets_hist = w2jets_hists[i]
  w3jets_hist = w3jets_hists[i]
  w4jets_hist = w4jets_hists[i]

  ww_hist = ww_hists[i]
  wz3nu_hist = wz3nu_hists[i]
  wz2q_hist = wz2q_hists[i]
  ttbar_hist = ttbar_hists[i]
  top_hist = top_hists[i]
  antitop_hist = antitop_hists[i]
  tW_hist = tW_hists[i]
  qcd1000to1400_hist = qcd1000to1400_hists[i]
  qcd120to170_hist = qcd120to170_hists[i]
  qcd1400to1800_hist = qcd1400to1800_hists[i]
  qcd15to30_hist = qcd15to30_hists[i]
  qcd170to300_hist = qcd170to300_hists[i]
  qcd1800to2400_hist = qcd1800to2400_hists[i]
  qcd2400to3200_hist = qcd2400to3200_hists[i]
  qcd300to470_hist = qcd300to470_hists[i]
  qcd30to50_hist = qcd30to50_hists[i]
  qcd470to600_hist = qcd470to600_hists[i]
  qcd50to80_hist = qcd50to80_hists[i]
  qcd600to800_hist = qcd600to800_hists[i]
  qcd800to1000_hist = qcd800to1000_hists[i]
  qcd80to120_hist = qcd80to120_hists[i]
  # scale to xs
  dy10sig_hist.Scale(xs.dy10 * xs.lumi2016 / xs.dy10_ngen)
  dysig_hist.Scale(xs.dy * xs.lumi2016 / xs.dy_ngen)

  dy1sig_hist.Scale(xs.dy1 * xs.lumi2016 / xs.dy1_ngen)
  dy2sig_hist.Scale(xs.dy2 * xs.lumi2016 / xs.dy2_ngen)
  dy3sig_hist.Scale(xs.dy2 * xs.lumi2016 / xs.dy2_ngen)
  dy4sig_hist.Scale(xs.dy2 * xs.lumi2016 / xs.dy2_ngen)
  dy1bkg_hist.Scale(xs.dy1 * xs.lumi2016 / xs.dy1_ngen)
  dy2bkg_hist.Scale(xs.dy2 * xs.lumi2016 / xs.dy2_ngen)
  dy3bkg_hist.Scale(xs.dy2 * xs.lumi2016 / xs.dy2_ngen)
  dy4bkg_hist.Scale(xs.dy2 * xs.lumi2016 / xs.dy2_ngen)

  dy10bkg_hist.Scale(xs.dy10 * xs.lumi2016 / xs.dy10_ngen)
  dybkg_hist.Scale(xs.dy * xs.lumi2016 / xs.dy_ngen)
  wjets_hist.Scale(xs.wjets * xs.lumi2016 / xs.wjets_ngen)

  w1jets_hist.Scale(xs.w1jets * xs.lumi2016 / xs.w1jets_ngen)
  w2jets_hist.Scale(xs.w2jets * xs.lumi2016 / xs.w2jets_ngen)
  w3jets_hist.Scale(xs.w3jets * xs.lumi2016 / xs.w3jets_ngen)
  w4jets_hist.Scale(xs.w4jets * xs.lumi2016 / xs.w4jets_ngen)

  ww_hist.Scale(xs.ww * xs.lumi2016 / xs.ww_ngen)
  wz3nu_hist.Scale(xs.wz1l3nu * xs.lumi2016 / xs.wz1l3nu_ngen)
  wz2q_hist.Scale(xs.wz1l2q * xs.lumi2016 / xs.wz1l2q_ngen)
  ttbar_hist.Scale(xs.ttbar * xs.lumi2016 / xs.ttbar_ngen)
  top_hist.Scale(xs.top * xs.lumi2016 / xs.top_ngen)
  antitop_hist.Scale(xs.antitop * xs.lumi2016 / xs.antitop_ngen)
  tW_hist.Scale(xs.tW * xs.lumi2016 / xs.tW_ngen)
  qcd1000to1400_hist.Scale(xs.qcd1000to1400 * xs.lumi2016 / xs.qcd1000to1400_ngen)
  qcd120to170_hist.Scale(xs.qcd120to170 * xs.lumi2016 / xs.qcd120to170_ngen)
  qcd1400to1800_hist.Scale(xs.qcd1400to1800 * xs.lumi2016 / xs.qcd1400to1800_ngen)
  qcd15to30_hist.Scale(xs.qcd15to30 * xs.lumi2016 / xs.qcd15to30_ngen)
  qcd170to300_hist.Scale(xs.qcd170to300 * xs.lumi2016 / xs.qcd170to300_ngen)
  qcd1800to2400_hist.Scale(xs.qcd1800to2400 * xs.lumi2016 / xs.qcd1800to2400_ngen)
  qcd2400to3200_hist.Scale(xs.qcd2400to3200 * xs.lumi2016 / xs.qcd2400to3200_ngen)
  qcd300to470_hist.Scale(xs.qcd300to470 * xs.lumi2016 / xs.qcd300to470_ngen)
  qcd30to50_hist.Scale(xs.qcd30to50 * xs.lumi2016 / xs.qcd30to50_ngen)
  qcd470to600_hist.Scale(xs.qcd470to600 * xs.lumi2016 / xs.qcd470to600_ngen)
  qcd50to80_hist.Scale(xs.qcd50to80 * xs.lumi2016 / xs.qcd50to80_ngen)
  qcd600to800_hist.Scale(xs.qcd600to800 * xs.lumi2016 / xs.qcd600to800_ngen)
  qcd800to1000_hist.Scale(xs.qcd800to1000 * xs.lumi2016 / xs.qcd800to1000_ngen)
  qcd80to120_hist.Scale(xs.qcd80to120 * xs.lumi2016 / xs.qcd80to120_ngen)
  # add up qcd
  qcd_hist = qcd1000to1400_hist.Clone()
  qcd_hist.Add(qcd120to170_hist)
  qcd_hist.Add(qcd1400to1800_hist)
  qcd_hist.Add(qcd15to30_hist)
  qcd_hist.Add(qcd170to300_hist)
  qcd_hist.Add(qcd1800to2400_hist)
  qcd_hist.Add(qcd2400to3200_hist)
  qcd_hist.Add(qcd300to470_hist)
  qcd_hist.Add(qcd30to50_hist)
  qcd_hist.Add(qcd470to600_hist)
  qcd_hist.Add(qcd50to80_hist)
  qcd_hist.Add(qcd600to800_hist)
  qcd_hist.Add(qcd800to1000_hist)
  qcd_hist.Add(qcd80to120_hist)
  # add up dy
  dysig_hist.Add(dy10sig_hist)
  dysig_hist.Add(dy1sig_hist)
  dysig_hist.Add(dy2sig_hist)
  dysig_hist.Add(dy3sig_hist)
  dysig_hist.Add(dy4sig_hist)
  dybkg_hist.Add(dy10bkg_hist)
  dybkg_hist.Add(dy1bkg_hist)
  dybkg_hist.Add(dy2bkg_hist)
  dybkg_hist.Add(dy3bkg_hist)
  dybkg_hist.Add(dy4bkg_hist)
  # add up wjets
  wjets.Add(w1jets)
  wjets.Add(w2jets)
  wjets.Add(w3jets)
  wjets.Add(w4jets)
  # add up top
  top_hist.Add(antitop_hist)
  top_hist.Add(tW_hist)
  # add up wwwz
  wwwz_hist = ww_hist.Clone()
  wwwz_hist.Add(wz3nu_hist)
  wwwz_hist.Add(wz2q_hist)
  # set cosmetics
  data_hist.SetLineColor(data_color)
  data_hist.Sumw2()
  data_hist.SetLineWidth(2)
  dysig_hist.SetLineColor(dysig_color)
  dysig_hist.SetFillColor(dysig_color)
  dybkg_hist.SetLineColor(dybkg_color)
  dybkg_hist.SetFillColor(dybkg_color)
  wjets_hist.SetLineColor(wjets_color)
  wjets_hist.SetFillColor(wjets_color)
  wwwz_hist.SetLineColor(wwwz_color)
  wwwz_hist.SetFillColor(wwwz_color)
  ttbar_hist.SetLineColor(ttbar_color)
  ttbar_hist.SetFillColor(ttbar_color)
  top_hist.SetLineColor(top_color)
  top_hist.SetFillColor(top_color)
  qcd_hist.SetFillColor(qcd_color)
  qcd_hist.SetLineColor(qcd_color)
  # setup stack
  title = (dysig_hist.GetName())[5:len(dysig_hist.GetName())]
  mc_stack = ROOT.THStack('hs', title)
  if title in reversed_histos:
    logy = False
    mc_stack.Add(wwwz_hist)
    mc_stack.Add(wjets_hist)
    mc_stack.Add(ttbar_hist)
    mc_stack.Add(top_hist)
    mc_stack.Add(dybkg_hist)
    mc_stack.Add(dysig_hist)
    mc_stack.Add(qcd_hist)
  else:
    logy = True
    mc_stack.Add(dysig_hist)
    mc_stack.Add(dybkg_hist)
    mc_stack.Add(top_hist)
    mc_stack.Add(ttbar_hist)
    mc_stack.Add(wjets_hist)
    mc_stack.Add(wwwz_hist)
    mc_stack.Add(qcd_hist)
  # calc max
  ymax = max(data_hist.GetMaximum(), mc_stack.GetMaximum())
  ymin = mc_stack.GetMinimum('nostack')
  if logy:
    mc_stack.SetMaximum(ymax)
    mc_stack.SetMinimum(max(ymin, 10**-1))
  else:
    mc_stack.SetMaximum(ymax * 1.15)
    mc_stack.SetMinimum(0)
  # stats
  underflow_mc = 0
  underflow_mc += dysig_hist.GetBinContent(0)
  underflow_mc += dybkg_hist.GetBinContent(0)
  underflow_mc += ttbar_hist.GetBinContent(0)
  underflow_mc += top_hist.GetBinContent(0)
  underflow_mc += wjets_hist.GetBinContent(0)
  underflow_mc += wwwz_hist.GetBinContent(0)
  underflow_mc +=  qcd_hist.GetBinContent(0)
  underflow_data = data_hist.GetBinContent(0)
  overflow_mc = 0
  overflow_mc += dysig_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += dybkg_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += ttbar_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += top_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += wjets_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += wwwz_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc +=  qcd_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_data = data_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  total_mc = 0
  total_mc += dysig_hist.Integral()
  total_mc += dybkg_hist.Integral()
  total_mc += ttbar_hist.Integral()
  total_mc += top_hist.Integral()
  total_mc += wjets_hist.Integral()
  total_mc += wwwz_hist.Integral()
  total_mc +=  qcd_hist.Integral()
  total_data = data_hist.Integral()
  # setup legend
  leg = ROOT.TLegend(x1, y1, x2, y2)
  leg.SetLineColor(ROOT.kWhite)
  whole_count =    ' : {0:,.0f}'
  count = ' : {0:,.1f} ({1:,.0f} entries)'
  leg.AddEntry(data_hist, data_label+whole_count.format(total_weight(data_hist)), 'l')
  leg.AddEntry('', "Total MC : {0:,.1f}".format(total_mc+underflow_mc+overflow_mc), '')
  leg.AddEntry(dysig_hist, dysig_label+count.format(total_weight(dysig_hist), entries(dysig_hist)), 'f')
  leg.AddEntry(dybkg_hist, dybkg_label+count.format(total_weight(dybkg_hist), entries(dybkg_hist)), 'f')
  leg.AddEntry(ttbar_hist, ttbar_label+count.format(total_weight(ttbar_hist), entries(ttbar_hist)), 'f')
  leg.AddEntry(top_hist, top_label+count.format(total_weight(top_hist), entries(top_hist)), 'f')
  leg.AddEntry(wjets_hist, wjets_label+count.format(total_weight(wjets_hist), entries(wjets_hist)), 'f')
  leg.AddEntry(wwwz_hist, wwwz_label+count.format(total_weight(wwwz_hist), entries(wwwz_hist)), 'f')
  leg.AddEntry(qcd_hist, qcd_label+count.format(total_weight(qcd_hist), entries(qcd_hist)), 'f')
  if overflow_data>0 or overflow_mc>0:
    leg.AddEntry('', "Overflow(data|MC) : {0:,.0f}|{1:,.1f}".format(overflow_data, overflow_mc), '')
  if underflow_data>0 or underflow_mc>0:
    leg.AddEntry('', "Underflow(data|MC) : {0:,.0f}|{1:,.1f}".format(underflow_data, underflow_mc), '')
  # draw
  mc_stack.Draw()
  data_hist.Draw('e same')
  leg.Draw('same')
  c1.SetLogy(logy)
  if not options.test:
    print mc_stack.GetTitle()
    c1.Print(pdf_filename);
  if options.test: break

if options.test: raw_input()
if not options.test: c1.Print(pdf_filename+"]")
