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
parser.add_option('--summed',dest="use_leading", action='store_false',default=True)
parser.add_option('--pi0',dest="pi0mass", action='store_true',default=False)
parser.add_option('--plot',dest="plot", action='store_true',default=False)
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

hvm = TH2F('hvm' ,'high vs mid', 100,0,1, 100,0,1)
hvl = TH2F('hvl' ,'high vs low', 100,0,1, 100,0,1)
mvl = TH2F('mvl' ,'mid vs low', 100,0,1, 100,0,1)
full = TH2F('full', 'Dalitz Plot', 100,0,1, 100,0,1)

count = 0
total = chain.GetEntries()
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  for i in range(len(event.TwoProng_pt)):
    norm_leading_photonmass = event.TwoProng_CHpos_mass[i]*event.TwoProng_CHpos_mass[i] + event.TwoProng_CHneg_mass[i]*event.TwoProng_CHneg_mass[i] + \
                              event.TwoProng_photon_Mass[i]*event.TwoProng_photon_Mass[i] + event.TwoProng_Mass[i]*event.TwoProng_Mass[i]

    norm_leading_pi0mass = event.TwoProng_CHpos_mass[i]*event.TwoProng_CHpos_mass[i] + event.TwoProng_CHneg_mass[i]*event.TwoProng_CHneg_mass[i] + \
                           0.135*0.135 + event.TwoProng_Mass[i]*event.TwoProng_Mass[i]

    norm_summed_photonmass = event.TwoProng_CHpos_mass[i]*event.TwoProng_CHpos_mass[i] + event.TwoProng_CHneg_mass[i]*event.TwoProng_CHneg_mass[i] + \
                             event.TwoProng_photon_mass[i]*event.TwoProng_photon_mass[i] + event.TwoProng_mass[i]*event.TwoProng_mass[i]

    norm_summed_pi0mass = event.TwoProng_CHpos_mass[i]*event.TwoProng_CHpos_mass[i] + event.TwoProng_CHneg_mass[i]*event.TwoProng_CHneg_mass[i] + \
                          0.135*0.135 + event.TwoProng_mass[i]*event.TwoProng_mass[i]

    usephotonmass = not options.pi0mass
    if usephotonmass:
      norm = norm_summed_photonmass
      norm_l = norm_leading_photonmass
    else:
      norm = norm_summed_pi0mass
      norm_l = norm_leading_pi0mass

    m12_l = event.TwoProng_mPosNeg[i]  / norm_l
    m23_l = event.TwoProng_mPosPho_l[i] / norm_l
    m13_l = event.TwoProng_mNegPho_l[i] / norm_l

    m12 = event.TwoProng_mPosNeg[i] / norm
    m23 = event.TwoProng_mPosPho[i] / norm
    m13 = event.TwoProng_mNegPho[i] / norm

    use_leading = options.use_leading
    if use_leading:
      m1 = m12_l
      m2 = m23_l
      m3 = m13_l
    else:
      m1 = m12
      m2 = m23
      m3 = m13

    high = max(m1, m2, m3)
    low = min(m1, m2, m3)
    temp = max(m1, m2)
    mid = min(temp, m3)

    hvm.Fill(mid, high)
    hvl.Fill(low, high)
    mvl.Fill(low, mid)

full.Add(hvm)
full.Add(hvl)
full.Add(mvl)

if options.plot:
  full.Draw('Colz')
  raw_input()

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
