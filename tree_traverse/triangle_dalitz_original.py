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
parser.add_option('--dat', action='store_true', default=False,
                  dest='dat',
                  help='')


parser.add_option('--saveplot', dest='saveplot', help='')

parser.add_option('--leading',dest="use_leading", action='store_true')
parser.add_option('--summed',dest="use_leading", action='store_false',default=False)
parser.add_option('--pi0mass',dest="pi0mass", action='store_true',default=False)
parser.add_option('--photonmass',dest="pi0mass", action='store_false')
parser.add_option('--plot',dest="plot", action='store_true',default=False)
parser.add_option('--title',dest="title", action='store')
parser.add_option('--overlap',dest="overlap", action='store_true',default=False)
parser.add_option('--exclusive',dest="exclusive", action='store_true',default=False)
parser.add_option('--double',dest="double", action='store_true',default=False)
parser.add_option('--triple',dest="double", action='store_false')
parser.add_option('--masslow',dest="masslow", action='store_true',default=False)
parser.add_option('--masshigh',dest="masshigh", action='store_true',default=False)
(options, args) = parser.parse_args()

if options.overlap and options.exclusive:
  print "--overlap and --exclusive not compatible."
  sys.exit()

if options.masslow and options.masshigh:
  print "--masslow and --masshigh not compatible."
  sys.exit()

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
elif options.dat:
  dirs = []
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
    chain = ROOT.TChain(treename)
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
    N = chain.GetEntries()
    dirs.append([chain, xs, N])

tvl = TH2F('tracks_v_larger' ,'tracks vs larger', 100,0,1, 100,0,1)
tvs = TH2F('tracks_v_smaller' ,'tracks vs smaller', 100,0,1, 100,0,1)
hvm = TH2F('hvm' ,'high vs mid', 100,0,1, 100,0,1)
hvl = TH2F('hvl' ,'high vs low', 100,0,1, 100,0,1)
mvl = TH2F('mvl' ,'mid vs low', 100,0,1, 100,0,1)

full = TH2F('full', 'Dalitz Plot', 100,0,1, 100,0,1)

count = 0
total = chain.GetEntries()
for event in chain:
  if count % 100000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

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

    hvm.Fill(mid, high)
    hvl.Fill(low, high)
    mvl.Fill(low, mid)
    tvl.Fill(mlarger, mtracks)
    tvs.Fill(msmaller, mtracks)

if options.double:
  full.Add(tvl)
  full.Add(tvs)
else:
  full.Add(hvm)
  full.Add(hvl)
  full.Add(mvl)

if options.plot:
  c = TCanvas()
  if options.double:
    full.GetXaxis().SetTitle('\mathrm{smaller}\ m_{\gamma\ \mathrm{track}}\ ,\ \mathrm{larger}\ m_{\gamma\ \mathrm{track}}')
    full.GetYaxis().SetTitle('m_{\mathrm{track1\ track2}}')
  else:
    full.GetXaxis().SetTitle('high, high, med')
    full.GetYaxis().SetTitle('med, low, low')
  full.SetStats(0)
  if not options.title == None:
    full.SetTitle(options.title)
  full.Draw('Colz')

  if not options.saveplot == None:
    c.SaveAs(options.saveplot)
  else:
    raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
