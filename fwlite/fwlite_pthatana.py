#! /Usr/bin/env python
import ROOT
import sys
import math
from DataFormats.FWLite import Events, Handle

# Input
files = sys.argv[1]

# Make event collection
events = Events(files)

# Make Handles for objects outside event loop
genhandle, genlabel = Handle("vector<reco::GenParticle>"), "prunedGenParticles"

# Book Histograms
outputfilename = "histos.root"
outputfile = ROOT.TFile(outputfilename, "recreate")
statvspt = ROOT.TH2F('statvspt', 'statvspt', 100,0,100, 100,0,5000)
num23 = ROOT.TH1F('num23','num23',20,0,20)
energydiff = ROOT.TH1F('energydiff','energydiff',200,0,2000)
ptdiff = ROOT.TH1F('ptdiff','ptdiff',100,0,0.0000000000000001)
id23 = ROOT.TH1F('id23','id23',10,0,10)

# Loop over events
total = 0
print "Total Events: " + str(events.size())
for event in events:
  total = total + 1
  if (total % 100) == 0 or total == 1:
    print " Processing event " + str(total) + "..."

  # Get Event info
  event.getByLabel(genlabel, genhandle)
  # Get Products
  genparticles = genhandle.product()

  num_stat23 = 0
  energy = []
  pt = []
  for genparticle in genparticles:
   ID = genparticle.pdgId()
   if ID == 1 or ID == 2 or ID == 3 or ID == 4 or ID == 5 or ID == 6 or ID == 21:
     statvspt.Fill(genparticle.status(), genparticle.pt())
     
     if genparticle.status() == 23:
       num_stat23 += 1
       energy.append(genparticle.energy())
       pt.append(genparticle.pt())
       fill_id = 0
       if ID == 1: fill_id = 1
       if ID == 2: fill_id = 2
       if ID == 3: fill_id = 3
       if ID == 4: fill_id = 4
       if ID == 5: fill_id = 5
       if ID == 6: fill_id = 6
       if ID == 21: fill_id = 7
       id23.Fill(fill_id)
     #if genparticle.status() == 23:
     #  print "ID", ID, "status", genparticle.status(), "pt", genparticle.pt(), "eta", genparticle.eta(), "phi", genparticle.phi(), "energy", genparticle.energy()
     #  for daughter_i in range(genparticle.numberOfDaughters()):
     #    daughter = genparticle.daughter(daughter_i)
     #    print "  --> ID", ID, "status", daughter.status(), "pt", daughter.pt(), "eta", daughter.eta(), "phi", daughter.phi(), "energy", daughter.energy()
         
  if num_stat23 == 2:
    energydiff.Fill(math.fabs(energy[0] - energy[1]))
    ptdiff.Fill(math.fabs(pt[0] - pt[1]))
  num23.Fill(num_stat23)

  if num_stat23 == 0 or False:
    print "Event\n"
    for genparticle in genparticles:
      ID = genparticle.pdgId()
      if ID == 1 or ID == 2 or ID == 3 or ID == 4 or ID == 5 or ID == 6 or ID == 21:
        print "ID", ID, "status", genparticle.status(), "pt", genparticle.pt(), "eta", genparticle.eta(), "phi", genparticle.phi(), "energy", genparticle.energy()

  
    

#num23.Draw()
#energydiff.Draw()
#ptdiff.Draw()
#statvspt.Draw("Colz")
id23.Draw()
raw_input()

# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
