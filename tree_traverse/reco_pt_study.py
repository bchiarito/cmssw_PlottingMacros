from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys
import os
import glob
import fnmatch

parser = OptionParser()
parser.add_option('--out',
                  dest='out', default="output.root",
                  help='output file')
parser.add_option('--file',
                  dest='file',
                  help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--tree',
                  dest='treename', default="diphotonAnalyzer/fTree2",
                  help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False,
                  dest='dir',
                  help='treat file option as a directory instead of a single file')
(options, args) = parser.parse_args()

out_file = TFile(options.out, 'recreate')

chain = TChain(options.treename)
if (not options.dir):
  chain.Add(options.file)
elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)


bins_array = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
num_bins = len(bins_array)-1
bins = array('d', bins_array)

num_bins = 40
low = 0
high = 2

reco_leading_over_gen = TH1F('reco_leading_over_gen','',num_bins,low,high)
reco_summed_over_gen = TH1F('reco_summed_over_gen','',num_bins,low,high)

reco_leading_over_gen_single = TH1F('reco_leading_over_gen_single','',num_bins,low,high)
reco_leading_over_gen_multi = TH1F('reco_leading_over_gen_multi','',num_bins,low,high)

reco_summed_over_gen_single = TH1F('reco_summed_over_gen_single','',num_bins,low,high)
reco_summed_over_gen_multi = TH1F('reco_summed_over_gen_multi','',num_bins,low,high)

reco_over_gen_photon = TH1F('reco_over_gen_photon','',num_bins,low,high)
reco_over_gen_electron = TH1F('reco_over_gen_electron','',num_bins,low,high)

count = 0
total = chain.GetEntries()
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  for i in range(len(event.GenEta_pt)):
    gen_vec = TLorentzVector()
    gen_vec.SetPtEtaPhiM(event.GenEta_pt[i], event.GenEta_eta[i], event.GenEta_phi[i], event.GenEta_mass[i])
    closest_reco = -1
    min_dr = 999.0
    for j in range(len(event.TwoProng_pt)):
      twoprong_vec = TLorentzVector()
      twoprong_vec.SetPtEtaPhiM(event.TwoProng_pt[j], event.TwoProng_eta[j], event.TwoProng_phi[j], event.TwoProng_mass[j])
      dr = twoprong_vec.DeltaR(gen_vec)
      if dr < min_dr:
        min_dr = dr
        closest_reco = j
    if min_dr < 0.1:
      if event.TwoProng_photon_nElectron[closest_reco] > 0:
        if event.TwoProng_photon_nGamma[closest_reco] == 1.0:
          reco_over_gen_photon.Fill(reco_pt_leading / gen_pt)
          reco_over_gen_electron.Fill(reco_pt_summed / gen_pt)
      else:
        gen_pt = event.GenEta_pt[i]
        reco_pt_summed = event.TwoProng_pt[closest_reco]
        reco_pt_leading = event.TwoProng_pt_l[closest_reco]
        reco_leading_over_gen.Fill(reco_pt_leading / gen_pt)
        reco_summed_over_gen.Fill(reco_pt_summed / gen_pt) 
        if event.TwoProng_photon_nGamma[closest_reco] == 1.0:
          reco_summed_over_gen_single.Fill(reco_pt_summed / gen_pt) 
          reco_leading_over_gen_single.Fill(reco_pt_leading / gen_pt)
          diff = reco_pt_summed - reco_pt_leading
        else:
          reco_summed_over_gen_multi.Fill(reco_pt_summed / gen_pt) 
          reco_leading_over_gen_multi.Fill(reco_pt_leading / gen_pt)
        if reco_pt_leading / gen_pt > 1.2:
          print "event", event.eventNum, "run", event.runNum, "lumi", event.lumiNum
          print "reco pt", reco_pt_leading, "gen pt", gen_pt
          print "gen phi", event.GenEta_phi[i], "gen eta", event.GenEta_eta[i]
          print "dr", min_dr
          #raw_input()


reco_summed_over_gen_multi.SetStats(0)
reco_summed_over_gen_multi.SetTitle("Signal 125 MC, nPF photon in box > 1")
reco_summed_over_gen_multi.GetXaxis().SetTitle("Reco pT / Generator pT")
reco_summed_over_gen_multi.GetYaxis().SetTitle("tight object count")
reco_summed_over_gen_multi.SetLineColor(kBlack)
reco_summed_over_gen_multi.Draw()
reco_leading_over_gen_multi.SetLineColor(kRed)
reco_leading_over_gen_multi.Draw('same')

leg = TLegend(0.1,0.8,0.3,0.9)
leg.AddEntry(reco_summed_over_gen_multi, 'summed', 'l')
leg.AddEntry(reco_leading_over_gen_multi, 'leading', 'l')
leg.Draw('same')

raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
