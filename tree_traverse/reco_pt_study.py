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
reco_leading_pi0_over_gen = TH1F('reco_leading_pi0_over_gen','',num_bins,low,high)

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
    for j in range(len(event.Cand_pt)):
      twoprong_vec = TLorentzVector()
      twoprong_vec.SetPtEtaPhiM(event.Cand_pt[j], event.Cand_eta[j], event.Cand_phi[j], event.Cand_mass[j])
      dr = twoprong_vec.DeltaR(gen_vec)
      if dr < min_dr:
        min_dr = dr
        closest_reco = j

    if min_dr < 0.1:
      if event.Cand_photon_nElectron[closest_reco] > 0:
        if event.Cand_photon_nGamma[closest_reco] == 1.0:
          reco_over_gen_photon.Fill(reco_pt_leading / gen_pt)
          reco_over_gen_electron.Fill(reco_pt_summed / gen_pt)
      else:
        # build twoprong vecs
        chpos = TLorentzVector()
        chpos.SetPtEtaPhiM(event.Cand_CHpos_pt[closest_reco], event.Cand_CHpos_eta[closest_reco], event.Cand_CHpos_phi[closest_reco], event.Cand_CHpos_mass[closest_reco])
        chneg = TLorentzVector()
        chneg.SetPtEtaPhiM(event.Cand_CHneg_pt[closest_reco], event.Cand_CHneg_eta[closest_reco], event.Cand_CHneg_phi[closest_reco], event.Cand_CHneg_mass[closest_reco])
        pho = TLorentzVector()
        pho.SetPtEtaPhiM(event.Cand_photon_pt_l[closest_reco], event.Cand_photon_eta_l[closest_reco], event.Cand_photon_phi_l[closest_reco], event.Cand_photon_mass_l[closest_reco])
        pho_wpi0mass = TLorentzVector()
        pho_wpi0mass.SetPtEtaPhiM(event.Cand_photon_pt_l[closest_reco], event.Cand_photon_eta_l[closest_reco], event.Cand_photon_phi_l[closest_reco], event.Cand_photon_Mass[closest_reco])
        pho_summed = TLorentzVector()
        pho_summed.SetPtEtaPhiM(event.Cand_photon_pt[closest_reco], event.Cand_photon_eta[closest_reco], event.Cand_photon_phi[closest_reco], event.Cand_photon_mass[closest_reco])

        twoprong_vec_summed = chpos + chneg + pho_summed
        twoprong_vec_leading = chpos + chneg + pho
        twoprong_vec_leading_pi0 = chpos + chneg + pho_wpi0mass

        # get pt
        gen_pt = event.GenEta_pt[i]
        reco_pt_summed = twoprong_vec_summed.Pt()
        reco_pt_leading = twoprong_vec_leading.Pt()
        reco_pt_leading_pi0 = twoprong_vec_leading_pi0.Pt()

        # fill
        reco_leading_over_gen.Fill(reco_pt_leading / gen_pt)
        reco_leading_pi0_over_gen.Fill(reco_pt_leading_pi0 / gen_pt)
        reco_summed_over_gen.Fill(reco_pt_summed / gen_pt) 

        # fill different regions
        if event.Cand_photon_nGamma[closest_reco] == 1.0:
          reco_summed_over_gen_single.Fill(reco_pt_summed / gen_pt) 
          reco_leading_over_gen_single.Fill(reco_pt_leading / gen_pt)
        else:
          reco_summed_over_gen_multi.Fill(reco_pt_summed / gen_pt) 
          reco_leading_over_gen_multi.Fill(reco_pt_leading / gen_pt)
        if reco_pt_leading / gen_pt > 2:
          print "event", event.eventNum, "run", event.runNum, "lumi", event.lumiNum
          print "reco pt", reco_pt_leading, "gen pt", gen_pt
          print "gen phi", event.GenEta_phi[i], "gen eta", event.GenEta_eta[i]
          print "dr", min_dr
          #raw_input()
        #diff = reco_pt_summed - reco_pt_leading_pi0
        #if not diff == 0:
        #  print diff


# Save file with histograms
out_file.cd()
out_file.Write()

# Plot
hist1 = reco_leading_pi0_over_gen
hist2 = reco_leading_over_gen

maximum = max(hist1.GetMaximum(), hist2.GetMaximum())
hist1.SetMaximum(maximum*1.2)
hist1.SetStats(0)
hist1.SetTitle("Signal 125 MC, nPF photon in box > 1")
hist1.GetXaxis().SetTitle("Reco pT / Generator pT")
hist1.GetYaxis().SetTitle("cand object count")
hist1.SetLineColor(kBlack)
hist1.Draw()
hist2.SetLineColor(kRed)
hist2.Draw('same')

leg = TLegend(0.1,0.8,0.3,0.9)
leg.AddEntry(hist1, 'leading and pi0', 'l')
leg.AddEntry(hist2, 'summed', 'l')
leg.Draw('same')

raw_input()
out_file.Close()
