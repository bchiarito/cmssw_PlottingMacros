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

count = 0
total = chain.GetEntries()
for event in chain:
  if count % 1000 == 0:
    percentDone = float(count) / float(total) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(count, total, percentDone )
  count += 1

  print "number of twoprongs", event.nTwoProngs
  for i in range(len(event.TwoProng_pt)):
    print " twoprong pt: ", event.TwoProng_pt[i]

  print "number of photons", event.nTightPhotons
  for i in range(len(event.Photon_pt)):
    print " photon pt: ", event.Photon_pt[i]

  # selection
  if (event.nTwoProngs>=1 and event.nTightPhotons>=1):
    Phi_candiate = TLorentzVector()
    
    #Phi_candidate.SetPxPyPzE(event.TwoProng_px[0]+event.Photon_px[0],
    #                         event.TwoProng_py[0]+event.Photon_py[0],
    #                         event.TwoProng_pz[0]+event.Photon_pz[0],
    #                         event.TwoProng_energy[0]+event.Photon_energy[0])

    twoprong = TLorentzVector()
    twoprong.SetPtEtaPhiM(event.TwoProng_pt[0],
                               event.TwoProng_eta[0],
                               event.TwoProng_phi[0],
                               event.TwoProng_mass[0])

    photon = TLorentzVector()
    photon.SetPtEtaPhiM(event.Photon_pt[0],
                               event.Photon_eta[0],
                               event.Photon_phi[0],
                               event.Photon_mass[0])

    Phi_candidate = twoprong + photon
    
    print "Phi candidate mass: ", Phi_candiate.M()

  print ""
  
  if count == 100: break

# Save file with histograms
out_file.cd()
out_file.Write()
out_file.Close()
