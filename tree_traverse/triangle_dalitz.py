from ROOT import *
from array import array
from math import *
from optparse import OptionParser
import sys
import os
import glob
import fnmatch
import time

time_begin = time.time()

parser = OptionParser()
parser.add_option('--out', dest='out', default="output.root", help='output file')
parser.add_option('--file', dest='file', help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--tree', dest='treename', default="diphotonAnalyzer/fTree2", help='name of tree inside files')
parser.add_option('--dir', action='store_true', default=False, dest='dir', help='treat file option as a directory instead of a single file')
parser.add_option('--dat', action='store_true', default=False, dest='dat', help='')
parser.add_option('--saveplot', dest='saveplot', help='')
parser.add_option('--reportevery', dest='reportevery', default=1000,help='')
parser.add_option('--plot',dest="plot", action='store_true',default=False)
parser.add_option('--title',dest="title", action='store')
parser.add_option('--smallrun',dest="smallrun", action='store')
parser.add_option('--logz', action='store_true', default=False, dest='logz', help='')

parser.add_option('--lumi', dest='lumi', default=1.0,help='integrated lumi in pb^-1')
parser.add_option('--2016lumi', action='store_true', default=False, dest='lumi_set_to_2016', help='')

parser.add_option('--tight', dest="tight", action='store_true', default=True)
parser.add_option('--cand', dest="tight", action='store_false')

parser.add_option('--leading',dest="use_leading", action='store_true')
parser.add_option('--summed',dest="use_leading", action='store_false',default=False)
parser.add_option('--pi0mass',dest="pi0mass", action='store_true',default=False)
parser.add_option('--photonmass',dest="pi0mass", action='store_false')

parser.add_option('--overlap',dest="overlap", action='store_true',default=False)
parser.add_option('--exclusive',dest="exclusive", action='store_true',default=False)

parser.add_option('--double',dest="double", action='store_true', default=False)
parser.add_option('--triple',dest="triple", action='store_true', default=False)
parser.add_option('--pt',dest="pt", action='store_true', default=False)

parser.add_option('--masslow',dest="masslow", action='store_true',default=False)
parser.add_option('--masshigh',dest="masshigh", action='store_true',default=False)
(options, args) = parser.parse_args()

if options.overlap and options.exclusive:
  print "--overlap and --exclusive not compatible."
  sys.exit()

if options.masslow and options.masshigh:
  print "--masslow and --masshigh not compatible."
  sys.exit()

if options.lumi_set_to_2016:
  lumi = 41070.0
else:
  lumi = options.lumi

doublever = options.double
triplever = options.triple
ptver = options.pt

vers = 0
if doublever:
  vers += 1
if triplever:
  vers += 1
if ptver:
  vers += 1

if vers == 2 or vers == 3:
  print "only use one of --double, --triple, --pt"
  sys.exit()

if vers == 0:
  ptver = True

out_file = TFile(options.out, 'recreate')

entries = []
if (not options.dir) and (not options.dat):
  chain = TChain(options.treename)
  chain.Add(options.file)
  entries.append([chain, 1.0, 1.0])
elif options.dir:
  rootfiles = []
  for root, dirnames, filenames in os.walk(options.file):
    for filename in fnmatch.filter(filenames, '*.root'):
      rootfiles.append(os.path.join(root, filename))
  for rootfile in rootfiles:
    chain.Add(rootfile)
  entries.append([chain, 1.0, 1.0])
elif options.dat:
  path = options.file
  inputfile = open(path, 'r')
  for line in inputfile:
    line_list = line.split()
    # Get name, xs, and num from line
    if len(line_list) == 1:
      path_to_file = line_list[0]
      xs = 1
      N = 1
      treename = options.treename
    if len(line_list) == 3:
      path_to_file = line_list[0]
      xs = float(line_list[1])
      N = float(line_list[2])
      treename = options.treename
    if len(line_list) == 4:
      path_to_file = line_list[0]
      xs = float(line_list[1])
      N = float(line_list[2])
      treename = line_list[3]
    if len(line_list) == 2 or len(line_list) == 0 or len(line_list) > 4:
      print "couldn't parse this line from input file"
      print line
      continue
    # add files to chain
    chain = TChain(treename)
    if fnmatch.fnmatch(path_to_file, "*.root"):
      chain.Add(path_to_file)
    elif fnmatch.fnmatch(path_to_file, "*/"):
      rootfiles = []
      for root, dirnames, filenames in os.walk(path_to_file):
        for filename in fnmatch.filter(filenames, '*.root'):
          rootfiles.append(os.path.join(root, filename))
      for rootfile in rootfiles:
        chain.Add(rootfile)
    else:
      # line doesn't make sense
      print "couldn't parse this line from input file", path
      print line
    entries.append([chain, xs, N])

# book histos
tvl = TH2F('tracks_v_larger' ,'tracks vs larger', 100,0,1, 100,0,1)
tvs = TH2F('tracks_v_smaller' ,'tracks vs smaller', 100,0,1, 100,0,1)
hvm = TH2F('hvm' ,'high vs mid', 100,0,1, 100,0,1)
hvl = TH2F('hvl' ,'high vs low', 100,0,1, 100,0,1)
mvl = TH2F('mvl' ,'mid vs low', 100,0,1, 100,0,1)
full = TH2F('full', 'Dalitz Plot', 100,0,1, 100,0,1)

hist_d1s = TH1F('d1s', 'distance 1 squared', 30,0,0.6)
hist_d2s = TH1F('d2s', 'distance 1 squared', 30,0,0.6)
hist_d3s = TH1F('d3s', 'distance 1 squared', 30,0,0.6)
hist_ds = TH1F('ds', 'sum distance squared', 90,0,1.8)

pvl = TH2F('pvl' ,'photon vs larger', 100,0,1, 100,0,1)
pvs = TH2F('pvs' ,'photon vs smaller', 100,0,1, 100,0,1)

double_pt = TH2F('double_pt' ,'pT asymmetry', 100,0,1, 100,0,1)
triple_pt = TH2F('triple_pt' ,'pT asymmetry', 100,0,1, 100,0,1)

for entry in range(len(entries)):
  chain = entries[entry][0]
  xs = entries[entry][1]
  N = entries[entry][2]
  if not options.smallrun == None:
    N = min(N, int(options.smallrun))

  count = 0
  total = chain.GetEntries()
  if not (len(entries) == 1):
    print 'Processing entry', entry+1, 'of ', len(entries)
  for event in chain:
    if count % int(options.reportevery) == 0:
      percentDone = float(count) / float(total) * 100.0
      if not (len(entries) == 1):
        print ' Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
      else:
        print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
    count += 1

    if options.tight and not ptver:
      for i in range(len(event.TwoProng_pt)):
        norm_leading_photonmass = event.TwoProng_CHpos_mass[i]*event.TwoProng_CHpos_mass[i] + event.TwoProng_CHneg_mass[i]*event.TwoProng_CHneg_mass[i] + \
                                  event.TwoProng_photon_mass_l[i]*event.TwoProng_photon_mass_l[i] + event.TwoProng_mass_l[i]*event.TwoProng_mass_l[i]
        norm_leading_pi0mass = event.TwoProng_CHpos_mass[i]*event.TwoProng_CHpos_mass[i] + event.TwoProng_CHneg_mass[i]*event.TwoProng_CHneg_mass[i] + \
                               event.TwoProng_photon_Mass[i]*event.TwoProng_photon_Mass[i] + event.TwoProng_Mass_l[i]*event.TwoProng_Mass_l[i]
        norm_summed_photonmass = event.TwoProng_CHpos_mass[i]*event.TwoProng_CHpos_mass[i] + event.TwoProng_CHneg_mass[i]*event.TwoProng_CHneg_mass[i] + \
                                 event.TwoProng_photon_mass[i]*event.TwoProng_photon_mass[i] + event.TwoProng_mass[i]*event.TwoProng_mass[i]
        norm_summed_pi0mass = event.TwoProng_CHpos_mass[i]*event.TwoProng_CHpos_mass[i] + event.TwoProng_CHneg_mass[i]*event.TwoProng_CHneg_mass[i] + \
                              event.TwoProng_photon_Mass[i]*event.TwoProng_photon_Mass[i] + event.TwoProng_Mass[i]*event.TwoProng_Mass[i]

        if options.exclusive:
          if event.TwoProng_photon_nElectron[i] > 0:
            continue
          if event.TwoProng_photon_nGamma[i] == 1:
            continue

        if options.overlap:
          if event.TwoProng_photon_nElectron[i] > 0:
            continue
          if event.TwoProng_photon_nGamma[i] > 1:
            continue

        if options.use_leading:
          obj_mass = event.TwoProng_Mass[i]
        else:
          obj_mass = event.TwoProng_mass[i]
        if options.masslow and obj_mass > 0.75:
          continue
        if options.masshigh and obj_mass < 0.75:
          continue

        if not options.pi0mass:
          norm_s = norm_summed_photonmass
          norm_l = norm_leading_photonmass
        else:
          norm_s = norm_summed_pi0mass
          norm_l = norm_leading_pi0mass

        if options.use_leading:
          norm = norm_l
        else:
          norm = norm_s

        if options.use_leading and not options.pi0mass: # leading, photon mass
          msmaller = min(event.TwoProng_mPosPho_l[i], event.TwoProng_mNegPho_l[i]) / norm
          mlarger = max(event.TwoProng_mPosPho_l[i], event.TwoProng_mNegPho_l[i]) / norm
          m12 = event.TwoProng_mPosNeg[i] / norm
          m23 = event.TwoProng_mPosPho_l[i] / norm
          m13 = event.TwoProng_mNegPho_l[i] / norm

        elif options.use_leading and options.pi0mass: # leading, pi0mass
          msmaller = min(event.TwoProng_mPosPho_lpi0[i], event.TwoProng_mNegPho_lpi0[i]) / norm
          mlarger = max(event.TwoProng_mPosPho_lpi0[i], event.TwoProng_mNegPho_lpi0[i]) / norm
          m12 = event.TwoProng_mPosNeg[i] / norm
          m23 = event.TwoProng_mPosPho_lpi0[i] / norm
          m13 = event.TwoProng_mNegPho_lpi0[i] / norm

        elif not options.use_leading and options.pi0mass: # summed, pi0mass
          msmaller = min(event.TwoProng_mPosPho_pi0[i], event.TwoProng_mNegPho_pi0[i]) / norm
          mlarger = max(event.TwoProng_mPosPho_pi0[i], event.TwoProng_mNegPho_pi0[i]) / norm
          m12 = event.TwoProng_mPosNeg[i] / norm
          m23 = event.TwoProng_mPosPho_pi0[i] / norm
          m13 = event.TwoProng_mNegPho_pi0[i] / norm

        elif not options.use_leading and not options.pi0mass: # summed, photon mass
          msmaller = min(event.TwoProng_mPosPho[i], event.TwoProng_mNegPho[i]) / norm
          mlarger = max(event.TwoProng_mPosPho[i], event.TwoProng_mNegPho[i]) / norm
          m12 = event.TwoProng_mPosNeg[i] / norm
          m23 = event.TwoProng_mPosPho[i] / norm
          m13 = event.TwoProng_mNegPho[i] / norm

        mtracks = event.TwoProng_mPosNeg[i] / norm
        high = max(m12, m23, m13)
        low = min(m12, m23, m13)
        if m12 < high and m12 > low:
          mid = m12
        if m23 < high and m23 > low:
          mid = m23
        if m13 < high and m13 > low:
          mid = m13

        hvm.Fill(mid, high, xs*lumi/N)
        hvl.Fill(low, high, xs*lumi/N)
        mvl.Fill(low, mid, xs*lumi/N)
        tvl.Fill(mlarger, mtracks, xs*lumi/N)
        tvs.Fill(msmaller, mtracks, xs*lumi/N)

        d1s = (high - 1.0/3.0)**2 + (mid - 1.0/3.0)**2
        d2s = (high - 1.0/3.0)**2 + (low - 1.0/3.0)**2
        d3s = (mid - 1.0/3.0)**2 + (low - 1.0/3.0)**2

        hist_d1s.Fill(d1s, xs*lumi/N)
        hist_d2s.Fill(d2s, xs*lumi/N)
        hist_d3s.Fill(d3s, xs*lumi/N)
        hist_ds.Fill(d1s+d2s+d3s, xs*lumi/N)

    elif not options.tight and not ptver:
      for i in range(len(event.Cand_pt)):
        norm_leading_photonmass = event.Cand_CHpos_mass[i]*event.Cand_CHpos_mass[i] + event.Cand_CHneg_mass[i]*event.Cand_CHneg_mass[i] + \
                                  event.Cand_photon_mass_l[i]*event.Cand_photon_mass_l[i] + event.Cand_mass_l[i]*event.Cand_mass_l[i]
        norm_leading_pi0mass = event.Cand_CHpos_mass[i]*event.Cand_CHpos_mass[i] + event.Cand_CHneg_mass[i]*event.Cand_CHneg_mass[i] + \
                               event.Cand_photon_Mass[i]*event.Cand_photon_Mass[i] + event.Cand_Mass_l[i]*event.Cand_Mass_l[i]
        norm_summed_photonmass = event.Cand_CHpos_mass[i]*event.Cand_CHpos_mass[i] + event.Cand_CHneg_mass[i]*event.Cand_CHneg_mass[i] + \
                                 event.Cand_photon_mass[i]*event.Cand_photon_mass[i] + event.Cand_mass[i]*event.Cand_mass[i]
        norm_summed_pi0mass = event.Cand_CHpos_mass[i]*event.Cand_CHpos_mass[i] + event.Cand_CHneg_mass[i]*event.Cand_CHneg_mass[i] + \
                              event.Cand_photon_Mass[i]*event.Cand_photon_Mass[i] + event.Cand_Mass[i]*event.Cand_Mass[i]

        if options.exclusive:
          if event.Cand_photon_nElectron[i] > 0:
            continue
          if event.Cand_photon_nGamma[i] == 1:
            continue

        if options.overlap:
          if event.Cand_photon_nElectron[i] > 0:
            continue
          if event.Cand_photon_nGamma[i] > 1:
            continue

        if options.use_leading:
          obj_mass = event.Cand_Mass[i]
        else:
          obj_mass = event.Cand_mass[i]
        if options.masslow and obj_mass > 0.75:
          continue
        if options.masshigh and obj_mass < 0.75:
          continue

        if not options.pi0mass:
          norm_s = norm_summed_photonmass
          norm_l = norm_leading_photonmass
        else:
          norm_s = norm_summed_pi0mass
          norm_l = norm_leading_pi0mass

        if options.use_leading:
          norm = norm_l
        else:
          norm = norm_s

        if options.use_leading and not options.pi0mass: # leading, photon mass
          msmaller = min(event.Cand_mPosPho_l[i], event.Cand_mNegPho_l[i]) / norm
          mlarger = max(event.Cand_mPosPho_l[i], event.Cand_mNegPho_l[i]) / norm
          m12 = event.Cand_mPosNeg[i] / norm
          m23 = event.Cand_mPosPho_l[i] / norm
          m13 = event.Cand_mNegPho_l[i] / norm

        elif options.use_leading and options.pi0mass: # leading, pi0mass
          msmaller = min(event.Cand_mPosPho_lpi0[i], event.Cand_mNegPho_lpi0[i]) / norm
          mlarger = max(event.Cand_mPosPho_lpi0[i], event.Cand_mNegPho_lpi0[i]) / norm
          m12 = event.Cand_mPosNeg[i] / norm
          m23 = event.Cand_mPosPho_lpi0[i] / norm
          m13 = event.Cand_mNegPho_lpi0[i] / norm

        elif not options.use_leading and options.pi0mass: # summed, pi0mass
          msmaller = min(event.Cand_mPosPho_pi0[i], event.Cand_mNegPho_pi0[i]) / norm
          mlarger = max(event.Cand_mPosPho_pi0[i], event.Cand_mNegPho_pi0[i]) / norm
          m12 = event.Cand_mPosNeg[i] / norm
          m23 = event.Cand_mPosPho_pi0[i] / norm
          m13 = event.Cand_mNegPho_pi0[i] / norm

        elif not options.use_leading and not options.pi0mass: # summed, photon mass
          msmaller = min(event.Cand_mPosPho[i], event.Cand_mNegPho[i]) / norm
          mlarger = max(event.Cand_mPosPho[i], event.Cand_mNegPho[i]) / norm
          m12 = event.Cand_mPosNeg[i] / norm
          m23 = event.Cand_mPosPho[i] / norm
          m13 = event.Cand_mNegPho[i] / norm

        mtracks = event.Cand_mPosNeg[i] / norm

        high = max(m12, m23, m13)
        low = min(m12, m23, m13)
        if m12 < high and m12 > low:
          mid = m12
        if m23 < high and m23 > low:
          mid = m23
        if m13 < high and m13 > low:
          mid = m13

        hvm.Fill(mid, high, xs*lumi/N)
        hvl.Fill(low, high, xs*lumi/N)
        mvl.Fill(low, mid, xs*lumi/N)
        tvl.Fill(mlarger, mtracks, xs*lumi/N)
        tvs.Fill(msmaller, mtracks, xs*lumi/N)

        d1s = (high - 1.0/3.0)**2 + (mid - 1.0/3.0)**2
        d2s = (high - 1.0/3.0)**2 + (low - 1.0/3.0)**2
        d3s = (mid - 1.0/3.0)**2 + (low - 1.0/3.0)**2

        hist_d1s.Fill(d1s, xs*lumi/N)
        hist_d2s.Fill(d2s, xs*lumi/N)
        hist_d3s.Fill(d3s, xs*lumi/N)
        hist_ds.Fill(d1s+d2s+d3s, xs*lumi/N)

    if options.tight and ptver:
      for i in range(len(event.TwoProng_pt)):
        pt_photon = event.TwoProng_photon_pt[i]
        pt_track1 = event.TwoProng_CHpos_pt[i]
        pt_track2 = event.TwoProng_CHneg_pt[i]
        norm = pt_photon + pt_track1 + pt_track2
        ptg = pt_photon / norm
        pt1 = pt_track1 / norm
        pt2 = pt_track2 / norm

        high = max(ptg, pt1, pt2)
        low = min(ptg, pt1, pt2)
        if pt1 < high and pt1 > low:
          mid = pt1
        if pt2 < high and pt2 > low:
          mid = pt2
        if ptg < high and ptg > low:
          mid = ptg

        hvm.Fill(mid, high, xs*lumi/N)
        hvl.Fill(low, high, xs*lumi/N)
        mvl.Fill(low, mid, xs*lumi/N)

        pvl.Fill(max(pt1, pt2), ptg, xs*lumi/N)
        pvs.Fill(min(pt1, pt2), ptg, xs*lumi/N)

if doublever:
  full.Add(tvl)
  full.Add(tvs)
elif triplever:
  full.Add(hvm)
  full.Add(hvl)
  full.Add(mvl)
elif ptver:
  double_pt.Add(pvl)
  double_pt.Add(pvs)
  triple_pt.Add(hvm)
  triple_pt.Add(hvl)
  triple_pt.Add(mvl)

time_end = time.time()
print "Elapsed Time: ", (time_end - time_begin)

if options.plot:
  c = TCanvas()
  if options.logz:
    c.SetLogz()
  if doublever:
    full.GetXaxis().SetTitle('\mathrm{smaller}\ m_{\gamma\ \mathrm{track}}\ ,\ \mathrm{larger}\ m_{\gamma\ \mathrm{track}}')
    full.GetYaxis().SetTitle('m_{\mathrm{track1\ track2}}')
    full.SetStats(0)
    if not options.title == None:
      full.SetTitle(options.title)
    full.Draw('Colz')
  elif triplever:
    full.GetXaxis().SetTitle('high, high, med')
    full.GetYaxis().SetTitle('med, low, low')
    full.SetStats(0)
    if not options.title == None:
      full.SetTitle(options.title)
    full.Draw('Colz')
  elif ptver:
    double_pt.GetYaxis().SetTitle('normalized photon pt')
    double_pt.GetXaxis().SetTitle('normalized smaller track pt, larger track pt')
    double_pt.SetStats(0)
    if not options.title == None:
      double_pt.SetTitle(options.title)
    double_pt.Draw('Colz')

  if not options.saveplot == None:
    c.SaveAs(options.saveplot)
  else:
    raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
