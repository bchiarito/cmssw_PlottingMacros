from __future__ import division
import ROOT
import cross_sections as xs

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

filename_prefix = "output_reg_nov17_" # ends with '_'
pdf_filename = "summary_"+filename_prefix+"hists.pdf"

# cosmetics
save = True
only_one = False
data_color = ROOT.kBlack
dysig_color = ROOT.kMagenta
dybkg_color = ROOT.kRed
wjets_color = ROOT.kOrange-9
ttbar_color = ROOT.kGreen
top_color = ROOT.kGreen+1
qcd_color = ROOT.kGray
data_label = "SingleMuon"
dysig_label = "DY signal"
dybkg_label = "DY bkg"
wjets_label = "Wjets"
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

# extract histos into memory
data = ROOT.TFile(filename_prefix+"DATA.root")
data_hists = extract_histos(data)
dy10sig = ROOT.TFile(filename_prefix+"DY10sig.root")
dy10sig_hists = extract_histos(dy10sig)
dysig = ROOT.TFile(filename_prefix+"DYsig.root")
dysig_hists = extract_histos(dysig)
dy10bkg = ROOT.TFile(filename_prefix+"DY10bkg.root")
dy10bkg_hists = extract_histos(dy10bkg)
dybkg = ROOT.TFile(filename_prefix+"DYbkg.root")
dybkg_hists = extract_histos(dybkg)
wjets = ROOT.TFile(filename_prefix+"WJets.root")
wjets_hists = extract_histos(wjets)
ttbar = ROOT.TFile(filename_prefix+"TT.root")
ttbar_hists = extract_histos(ttbar)
top = ROOT.TFile(filename_prefix+"ST.root")
top_hists = extract_histos(top)
antitop = ROOT.TFile(filename_prefix+"STbar.root")
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
if save: c1.Print(pdf_filename+"[")
for i in range(len(dysig_hists)):
  data_hist = data_hists[i]
  dy10sig_hist = dy10sig_hists[i]
  dysig_hist = dysig_hists[i]
  dy10bkg_hist = dy10bkg_hists[i]
  dybkg_hist = dybkg_hists[i]
  wjets_hist = wjets_hists[i]
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
  dy10bkg_hist.Scale(xs.dy10 * xs.lumi2016 / xs.dy10_ngen)
  dybkg_hist.Scale(xs.dy * xs.lumi2016 / xs.dy_ngen)
  wjets_hist.Scale(xs.wjets * xs.lumi2016 / xs.wjets_ngen)
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
  dybkg_hist.Add(dy10bkg_hist)
  # add up top
  top_hist.Add(antitop_hist)
  top_hist.Add(tW_hist)
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
    mc_stack.Add(qcd_hist)
    mc_stack.Add(wjets_hist)
    mc_stack.Add(ttbar_hist)
    mc_stack.Add(top_hist)
    mc_stack.Add(dybkg_hist)
    mc_stack.Add(dysig_hist)
  else:
    logy = True
    mc_stack.Add(dysig_hist)
    mc_stack.Add(dybkg_hist)
    mc_stack.Add(top_hist)
    mc_stack.Add(ttbar_hist)
    mc_stack.Add(wjets_hist)
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
  underflow_mc +=  qcd_hist.GetBinContent(0)
  underflow_data = data_hist.GetBinContent(0)
  overflow_mc = 0
  overflow_mc += dysig_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += dybkg_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += ttbar_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += top_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc += wjets_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_mc +=  qcd_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  overflow_data = data_hist.GetBinContent(dysig_hist.GetNbinsX()+1)
  total_mc = 0
  total_mc += dysig_hist.Integral()
  total_mc += dybkg_hist.Integral()
  total_mc += ttbar_hist.Integral()
  total_mc += top_hist.Integral()
  total_mc += wjets_hist.Integral()
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
  if save:
    print mc_stack.GetTitle()
    c1.Print(pdf_filename);
  if only_one: break

if only_one: raw_input()
if save: c1.Print(pdf_filename+"]")
