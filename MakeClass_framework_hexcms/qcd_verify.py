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

# extract histos into memory
qcd1000to1400 = ROOT.TFile("output_QCD_1000to1400.root")
qcd1000to1400_hists = extract_histos(qcd1000to1400)
qcd120to170 = ROOT.TFile("output_QCD_120to170.root")
qcd120to170_hists = extract_histos(qcd120to170)
qcd1400to1800 = ROOT.TFile("output_QCD_1400to1800.root")
qcd1400to1800_hists = extract_histos(qcd1400to1800)
qcd15to30 = ROOT.TFile("output_QCD_15to30.root")
qcd15to30_hists = extract_histos(qcd15to30)
qcd170to300 = ROOT.TFile("output_QCD_170to300.root")
qcd170to300_hists = extract_histos(qcd170to300)
qcd1800to2400 = ROOT.TFile("output_QCD_1800to2400.root")
qcd1800to2400_hists = extract_histos(qcd1800to2400)
qcd2400to3200 = ROOT.TFile("output_QCD_2400to3200.root")
qcd2400to3200_hists = extract_histos(qcd2400to3200)
qcd300to470 = ROOT.TFile("output_QCD_300to470.root")
qcd300to470_hists = extract_histos(qcd300to470)
qcd30to50 = ROOT.TFile("output_QCD_30to50.root")
qcd30to50_hists = extract_histos(qcd30to50)
qcd470to600 = ROOT.TFile("output_QCD_470to600.root")
qcd470to600_hists = extract_histos(qcd470to600)
qcd50to80 = ROOT.TFile("output_QCD_50to80.root")
qcd50to80_hists = extract_histos(qcd50to80)
qcd600to800 = ROOT.TFile("output_QCD_600to800.root")
qcd600to800_hists = extract_histos(qcd600to800)
qcd800to1000 = ROOT.TFile("output_QCD_800to1000.root")
qcd800to1000_hists = extract_histos(qcd800to1000)
qcd80to120 = ROOT.TFile("output_QCD_80to120.root")
qcd80to120_hists = extract_histos(qcd80to120)

# cosmetics
qcd_color = ROOT.kOrange
qcd_label = "QCD"
x1 = 0.7
x2 = 0.9
y1 = 0.7
y2 = 0.9

# draw loop
c1 = ROOT.TCanvas()
c1.SetLogy()
for i in range(len(qcd1000to1400_hists)):
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
  
  # set cosmetics
  rebin = 2
  qcd15to30_hist.Rebin(rebin)
  qcd30to50_hist.Rebin(rebin)
  qcd50to80_hist.Rebin(rebin)
  qcd80to120_hist.Rebin(rebin)
  qcd120to170_hist.Rebin(rebin)
  qcd170to300_hist.Rebin(rebin)
  qcd300to470_hist.Rebin(rebin)
  qcd470to600_hist.Rebin(rebin)
  qcd600to800_hist.Rebin(rebin)
  qcd800to1000_hist.Rebin(rebin)
  qcd1000to1400_hist.Rebin(rebin)
  qcd1400to1800_hist.Rebin(rebin)
  qcd1800to2400_hist.Rebin(rebin)
  qcd2400to3200_hist.Rebin(rebin)

  qcd15to30_hist.SetFillColor(qcd_color)
  qcd30to50_hist.SetFillColor(qcd_color+1)
  qcd50to80_hist.SetFillColor(qcd_color+2)
  qcd80to120_hist.SetFillColor(qcd_color+3)
  qcd120to170_hist.SetFillColor(qcd_color+4)
  qcd170to300_hist.SetFillColor(qcd_color+5)
  qcd300to470_hist.SetFillColor(qcd_color+6)
  qcd470to600_hist.SetFillColor(qcd_color+7)
  qcd600to800_hist.SetFillColor(qcd_color+8)
  qcd800to1000_hist.SetFillColor(qcd_color+9)
  qcd1000to1400_hist.SetFillColor(qcd_color+10)
  qcd1400to1800_hist.SetFillColor(qcd_color-1)
  qcd1800to2400_hist.SetFillColor(qcd_color-2)
  qcd2400to3200_hist.SetFillColor(qcd_color-3)

  qcd15to30_hist.SetLineColor(qcd_color)
  qcd30to50_hist.SetLineColor(qcd_color+1)
  qcd50to80_hist.SetLineColor(qcd_color+2)
  qcd80to120_hist.SetLineColor(qcd_color+3)
  qcd120to170_hist.SetLineColor(qcd_color+4)
  qcd170to300_hist.SetLineColor(qcd_color+5)
  qcd300to470_hist.SetLineColor(qcd_color+6)
  qcd470to600_hist.SetLineColor(qcd_color+7)
  qcd600to800_hist.SetLineColor(qcd_color+8)
  qcd800to1000_hist.SetLineColor(qcd_color+9)
  qcd1000to1400_hist.SetLineColor(qcd_color+10)
  qcd1400to1800_hist.SetLineColor(qcd_color-1)
  qcd1800to2400_hist.SetLineColor(qcd_color-2)
  qcd2400to3200_hist.SetLineColor(qcd_color-3)

  # scale to xs
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

  # setup stack
  mc_stack = ROOT.THStack('hs', 'HT')
  mc_stack.Add(qcd15to30_hist)
  mc_stack.Add(qcd30to50_hist)
  mc_stack.Add(qcd50to80_hist)
  mc_stack.Add(qcd80to120_hist)
  mc_stack.Add(qcd120to170_hist)
  mc_stack.Add(qcd170to300_hist)
  mc_stack.Add(qcd300to470_hist)
  mc_stack.Add(qcd470to600_hist)
  mc_stack.Add(qcd600to800_hist)
  mc_stack.Add(qcd800to1000_hist)
  mc_stack.Add(qcd1000to1400_hist)
  mc_stack.Add(qcd1400to1800_hist)
  mc_stack.Add(qcd1800to2400_hist)
  mc_stack.Add(qcd2400to3200_hist)

  mc_stack.SetMinimum(0.01)
  # setup legenc
  leg = ROOT.TLegend(x1, y1, x2, y2)
  leg.AddEntry(qcd15to30_hist, '15to30', 'f')
  leg.AddEntry(qcd30to50_hist, '30to50', 'f')
  leg.AddEntry(qcd50to80_hist, '50to80', 'f')
  leg.AddEntry(qcd80to120_hist, '80to120', 'f')
  leg.AddEntry(qcd120to170_hist, '120to170', 'f')
  leg.AddEntry(qcd170to300_hist, '170to300', 'f')
  # draw
  mc_stack.Draw()
  leg.Draw()
  break

raw_input()
