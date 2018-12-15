#! /Usr/bin/env python
import ROOT
import glob
import sys
import math
import datetime
from array import array
from DataFormats.FWLite import Events, Handle
import warnings
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )

# Constants
MATCH_DR = 0.1 # DR to match candidates with gen Etas
CAND_PT_CUT = 10 # min pt for candidates used for charged hadron pair
CAND_DR = 0.05 # DR between charged hadrons to consider a pair
BOX_PHI = 0.8 # phi dimension of photon box
BOX_ETA = 0.087 # eta dimension of photon box
ISO_DR = 0.3 # Cone size for defining isolation
ISO_INNER_DR = 0.05 # Smaller cone within which to include hadrons
CHARGED_ISO_CUT = 0.1 # relative charged isolation cut point
NEUTRAL_ISO_CUT = 0.1 # relative neutral isolation cut point
EM_ISO_CUT = 0.1 # relative egamma isolation cut point
PHOTON_PT_CUT = 10.0 # cut on pt of combined photon constituent of candidate
USE_ATVTX = True # use phiAtVtx() instead of phi()
ALLOW_EXTRA_TRACKS = 0
EXTRA_TRACK_DR = CAND_DR

DUMP_EVENT_BY_NUM = () # dump a particular event's contents, -1 to run over all events
RUNNING_ON_SIGNAL = True # if we are running over signal with generator information or not
TXT_FILE_INPUT = True # if the first argument is a local path to files or a txt file of PFN filenames
MAX_EVENTS = -1
MAX_FILES = -1

def DeltaR(vec1, vec2, op=""):
  if op == "":
    vec1p4 = ROOT.TLorentzVector()
    vec1p4.SetPtEtaPhiM(vec1.pt(), vec1.eta(), vec1.phi(), vec1.mass())
    vec2p4 = ROOT.TLorentzVector()
    vec2p4.SetPtEtaPhiM(vec2.pt(), vec2.eta(), vec2.phi(), vec2.mass())
    return vec1p4.DeltaR(vec2p4)
  elif op == "AtVtx":
    vec1p4 = ROOT.TLorentzVector()
    vec1p4.SetPtEtaPhiM(vec1.pt(), vec1.eta(), vec1.phiAtVtx(), vec1.mass())
    vec2p4 = ROOT.TLorentzVector()
    vec2p4.SetPtEtaPhiM(vec2.pt(), vec2.eta(), vec2.phiAtVtx(), vec2.mass())
    return vec1p4.DeltaR(vec2p4)
  else:
    return None

def TDeltaR(Tvec, vec, op=""):
  if op == "":
    vecp4 = ROOT.TLorentzVector()
    vecp4.SetPtEtaPhiE(vec.pt(), vec.eta(), vec.phi(), vec.energy())
    return Tvec.DeltaR(vecp4)
  elif op == "AtVtx":
    vecp4 = ROOT.TLorentzVector()
    vecp4.SetPtEtaPhiE(vec.pt(), vec.eta(), vec.phiAtVtx(), vec.energy())
    return Tvec.DeltaR(vecp4)
  else:
    return None

def WithinPhiEtaBox(vec, center, dphi, deta, op=""):
  if op == "":
    if (vec.phi() < center.Phi() + dphi and vec.phi() > center.Phi() - dphi and
        vec.eta() < center.Eta() + deta and vec.eta() > center.Eta() - deta):
      return True
    return False
  elif op == "AtVtx":
    if (vec.phiAtVtx() < center.Phi() + dphi and vec.phiAtVtx() > center.Phi() - dphi and
        vec.eta() < center.Eta() + deta and vec.eta() > center.Eta() - deta):
      return True
    return False
  else:
    return None

def MakeTVector(cand):
  vector = ROOT.TLorentzVector()
  vector.SetPtEtaPhiM(cand.pt(), cand.eta(), cand.phi(), cand.mass())
  return vector

def dump(cand):
  print "  CH+:              pt ", cand['CH+'].pt(), ", eta ", cand['CH+'].eta(), ", phi ", cand['CH+'].phi(), ", mass ", cand['CH+'].mass()
  print "  CH-:              pt ", cand['CH-'].pt(), ", eta ", cand['CH-'].eta(), ", phi ", cand['CH-'].phi(), ", mass ", cand['CH-'].mass()
  for gamma in cand['photon_gamma_pfs']:
    print "  gamma pf:         pt ", gamma.pt(), ", eta ", gamma.eta(), ", phi ", gamma.phi(), ", mass ", gamma.mass()
  for elec in cand['photon_electron_pfs']:
    print "  electron pf:      pt ", elec.pt(), ", eta ", elec.eta(), ", phi ", elec.phi(), ", mass ", elec.mass()
  print "  combined photon:  pt ", cand['photon'].Pt(), ", eta ", cand['photon'].Eta(), ", phi ", cand['photon'].Phi(), ", mass ", cand['photon'].M()
  print "  Reco Eta:         pt ", cand['eta'].Pt(), ", eta ", cand['eta'].Eta(), ", phi ", cand['eta'].Phi(), ", mass ", cand['eta'].M()
  print "  Reco Grommed Eta: pt ", cand['eta_leadingonly'].Pt(), ", eta_leadingonly ", cand['eta_leadingonly'].Eta(), ", phi ", cand['eta_leadingonly'].Phi(), ", mass ", cand['eta_leadingonly'].M()
  etaPt = candidate['eta'].Pt()
  print "  charged rel iso:  ", cand['chargedIso']/etaPt
  print "  neutral rel iso:  ", cand['neutralIso']/etaPt
  print "  egamma rel iso:   ", cand['emIso']/etaPt
  print "  dR to Nearest Gen Eta:  ", "%.3f" % cand['nearest_gen_dr']

# Define list of files
print datetime.datetime.now(), " Begin."
print sys.argv[1]
if TXT_FILE_INPUT:
    print "Treating this as a path to file of input filenames"
    count = 0
    inputfile = open(sys.argv[1], 'r')
    filelist = []
    for line in inputfile:
      filelist.append(line.rstrip('\n'))
      count += 1
      if count == MAX_FILES:
        break
    files = filelist
    print len(files), " total filenames"
    
if not TXT_FILE_INPUT:
    print "getting all files at this local path"
    files = glob.glob(sys.argv[1])

# Make TFile to hold histograms
if len(sys.argv) >= 4:
  outputfilename = sys.argv[3]
else:
  outputfilename = "histos.root"
outputfile = ROOT.TFile(outputfilename, "recreate")

# Make event collection
events = Events(files)

# Make Handles for objects outside event loop
print datetime.datetime.now(), " Creating handles..."
ak4handle, ak4label = Handle("std::vector<pat::Jet>"), "slimmedJets"
pfcandhandle, pfcandlabel = Handle("std::vector<pat::PackedCandidate>"), "packedPFCandidates"
genhandle, genlabel = Handle("vector<reco::GenParticle>"), "prunedGenParticles"
pvhandle, pvlabel = Handle("vector<reco::Vertex>"), "offlineSlimmedPrimaryVertices"

# Book Histograms
num_pfcands = ROOT.TH1F('num_pfcands', 'Number of PF cands', 100, 0, 5000)
pvqual = ROOT.TH1F('pvqual', 'PV Quality of PF cands part of CH pair', 10, 0, 10)
impact = ROOT.TH1F('impact', 'impact param dxy()', 200, -0.1, 0.1)
impact_sig = ROOT.TH1F('impact_sig', 'impact param significance dxyError()', 100, 0, 0.1)

num_pairs = ROOT.TH1F('num_pairs', 'Number of pairs of CH+/CH- within DR', 80, 0, 80)
num_emiso = ROOT.TH1F('num_emiso', 'Number of candidates that pass E/M isolation', 15, 0, 15)
num_neutraliso = ROOT.TH1F('num_neutraliso', 'Number of candidates that pass neutral hadron isolation', 15, 0, 15)
num_chargediso = ROOT.TH1F('num_chargediso', 'Number of candidates that pass charged hadron isolation', 15, 0, 15)
num_full = ROOT.TH1F('num_full', 'Number of candidates that pass full isolation', 15, 0, 15)
num_matched = ROOT.TH1F('num_matched', 'Number of passed candidates matched to within DR of a generator Eta', 15, 0, 15)
num_matchedonly = ROOT.TH1F('num_matchedonly', 'Number of candidates matched to within DR of a generator Eta', 15, 0, 15)

gen_num_etas = ROOT.TH1F('gen_num_etas', 'Number of status = 2 generator Etas', 5, 0, 5)
gen_canddr = ROOT.TH1F('gen_canddr', 'DR from candidate to nearest generator Eta', 600, 0, 6)
gen_candindex = ROOT.TH1F('gen_candindex', 'Index of neareast generator Eta to candidate', 10, 0, 10)
gen_passedcanddr = ROOT.TH1F('gen_passedcanddr', 'DR from passed candidate to nearest generator Eta', 600, 0, 6)
gen_passedcandindex = ROOT.TH1F('gen_passedcandindex', 'Index of neareast generator Eta to passed candidate', 10, 0, 10)
gen_etarelDR = ROOT.TH1F('gen_etarelRD', 'DR between first two generator Etas', 200, 0, 8)
gen_etapt = ROOT.TH1F('gen_etapt', 'generator Eta pt', 100, 0, 1000)
gen_etapt_first2 = ROOT.TH1F('gen_etapt_first2', 'generator Eta pt', 100, 0, 1000)
gen_etaphi = ROOT.TH1F('gen_etaphi', 'generator Eta phi', 20, -4, 4)
gen_etaphi_first2 = ROOT.TH1F('gen_etaphi_first2', 'generator Eta phi', 20, -4, 4)
gen_etaeta = ROOT.TH1F('gen_etaeta', 'generator Eta eta', 50, -7, 7)
gen_etaeta_first2 = ROOT.TH1F('gen_etaeta_first2', 'generator Eta eta', 50, -7, 7)
gen_etam = ROOT.TH1F('gen_etam', 'generator Eta mass', 200, 0, 5)
gen_etam_first2 = ROOT.TH1F('gen_etam_first2', 'generator Eta mass', 200, 0, 5)

reliso_charged = ROOT.TH1F('reliso_charged', 'Relative charged isolation', 200, 0, 2)
reliso_neutral = ROOT.TH1F('reliso_neutral', 'Relative neutral isolation', 200, 0, 2)
reliso_em = ROOT.TH1F('reliso_em', 'Relative em isolation', 200, 0, 2)

photon_num_e = ROOT.TH1F('photon_num_e', 'Number of electron pf cands in photon for passed candidates', 10, 0, 10)
photon_num_gamma = ROOT.TH1F('photon_num_gamma', 'Number of gamma pf cands in photon for passed candidates', 50, 0, 50)

hadronmass = ROOT.TH1F('hadronmass', 'mass of associated CH+/CH- pair', 1000, 0, 10)
hadronpt = ROOT.TH1F('hadronpt', 'pt of associated CH+/CH- pair', 100, 0, 1000)
hadronphi = ROOT.TH1F('hadronphi', 'phi of associated CH+/CH- pair', 20, -4, 4)
hadroneta = ROOT.TH1F('hadroneta', 'eta of associated CH+/CH- pair', 50, -7, 7)
etamass = ROOT.TH1F('etamass', 'mass of passed candidate', 1000, 0, 10)
etagrommedmass = ROOT.TH1F('etagrommedmass', '"grommed" mass of passed candidate', 1000, 0, 10)
etapt = ROOT.TH1F('etapt', 'pt of passed candidate', 100, 0, 1000)
etaphi = ROOT.TH1F('etaphi', 'phi of passed candidate', 20, -4, 4)
etaeta = ROOT.TH1F('etaeta', 'eta of passed candidate', 50, -7, 7)
photonmass = ROOT.TH1F('photonmass', 'mass of associated photon', 1000, 0, 10)
photonpt = ROOT.TH1F('photonpt', 'pt of associated photon', 100, 0, 1000)
photonphi = ROOT.TH1F('photonphi', 'phi of associated photon', 20, -4, 4)
photoneta = ROOT.TH1F('photoneta', 'eta of associated photon', 50, -7, 7)
m_etaeta = ROOT.TH1F('m_etaeta', 'M_EtaEta', 25, 0, 5)
dr_etaeta = ROOT.TH1F('dr_etaeta', 'dR_EtaEta', 25, 0, 6)

# Book TTree
tree = ROOT.TTree("tree", "fwlite Analysis Tree")
cand_pt = ROOT.std.vector(float)()
cand_eta = ROOT.std.vector(float)()
cand_phi = ROOT.std.vector(float)()
cand_mass = ROOT.std.vector(float)()
tree.Branch("Cand_pt", cand_pt)
tree.Branch("Cand_eta", cand_eta)
tree.Branch("Cand_phi", cand_phi)
tree.Branch("Cand_mass", cand_mass)

geneta_pt = ROOT.std.vector(float)()
geneta_eta = ROOT.std.vector(float)()
geneta_phi = ROOT.std.vector(float)()
geneta_mass = ROOT.std.vector(float)()
geneta_candDR = ROOT.std.vector(float)()
geneta_passedCandDR = ROOT.std.vector(float)()
tree.Branch("GenEta_pt", geneta_pt)
tree.Branch("GenEta_eta", geneta_eta)
tree.Branch("GenEta_phi", geneta_phi)
tree.Branch("GenEta_mass", geneta_mass)
tree.Branch("GenEta_candDR", geneta_candDR)
tree.Branch("GenEta_passedCandDR", geneta_passedCandDR)

nCands = array('f', [-99.9])
nPass = array('f', [-99.9])
tree.Branch('nCands', nCands, "nCands/F")
tree.Branch('nPass', nPass, "nPass/F")

# Loop over events
total = 0
has_pair = 0
has_pairx2 = 0
pass_emiso = 0
pass_neutraliso = 0
pass_chargediso = 0
pass_photonpt = 0
pass_full = 0
pass_fullx2 = 0
pass_matched = 0
pass_matchedx2 = 0
pass_matchedonly = 0
pass_matchedonlyx2 = 0
print datetime.datetime.now(), " Calculating total number of events..."
print datetime.datetime.now(), " Total Events: " + str(events.size())
for event in events:
  total = total + 1
  if (total % 500) == 0 or total == 1:
    print datetime.datetime.now(), " Processing event " + str(total) + "..."
  if total == MAX_EVENTS:
    break
  if not DUMP_EVENT_BY_NUM == ():
    if not event.object().id().event() in DUMP_EVENT_BY_NUM:
      continue

  # Get Event info
  event.getByLabel(ak4label, ak4handle)
  event.getByLabel(pfcandlabel, pfcandhandle)
  event.getByLabel(pvlabel, pvhandle)
  if RUNNING_ON_SIGNAL:
    event.getByLabel(genlabel, genhandle)
  # Get Products
  ak4jets = ak4handle.product()
  pfcands = pfcandhandle.product()
  vertecies = pvhandle.product()
  if RUNNING_ON_SIGNAL:
    genparticles = genhandle.product()

  # Clear Tree variables
  cand_pt.clear()
  cand_eta.clear()
  cand_phi.clear()
  cand_mass.clear()
  geneta_pt.clear()
  geneta_eta.clear()
  geneta_phi.clear()
  geneta_mass.clear()
  geneta_candDR.clear()
  geneta_passedCandDR.clear()
  
  # Generator Particles
  if RUNNING_ON_SIGNAL:
      gen_etas = []
      for genparticle in genparticles:
        id = genparticle.pdgId()
        status = genparticle.status()
        if (id == 221 or id == -221) and (status == 2):
          gen_etas.append(genparticle)

  dr_option = ""
  if USE_ATVTX:
    dr_option = "AtVtx"

  # find CH pair
  pfcands_pruned = []
  for pfcand in pfcands:
    if pfcand.pt() < CAND_PT_CUT:
      continue
    if pfcand.fromPV() <= 1:
      continue
    pfcands_pruned.append(pfcand)

  pfcands_iso = []
  for pfcand in pfcands:
    if pfcand.fromPV() <= 1:
      continue
    pfcands_iso.append(pfcand)

  candidates = []
  for pf1 in pfcands_pruned:
    if pf1.pdgId() != 211:
      continue
    for pf2 in pfcands_pruned:
      if pf2.pdgId() != -211:
        continue
      pf1p4 = ROOT.TLorentzVector()
      pf2p4 = ROOT.TLorentzVector()
      if USE_ATVTX:
        pf1p4.SetPtEtaPhiE(pf1.pt(), pf1.eta(), pf1.phiAtVtx(), pf1.energy())
        pf2p4.SetPtEtaPhiE(pf2.pt(), pf2.eta(), pf2.phiAtVtx(), pf2.energy())
      else:
        pf2p4.SetPtEtaPhiE(pf2.pt(), pf2.eta(), pf2.phi(), pf2.energy())
        pf1p4.SetPtEtaPhiE(pf1.pt(), pf1.eta(), pf1.phi(), pf1.energy())
      if pf1p4.DeltaR(pf2p4) < CAND_DR:
        # found CH pair
        center = pf1p4 + pf2p4
        candidate = {}
        candidate['center'] = center
        candidate['CH+'] = pf1
        candidate['CH-'] = pf2
        # allow extra tracks
        candidate['extra_tracks'] = []
        if ALLOW_EXTRA_TRACKS > 0:
          extra_tracks = []
          for pfcand in pfcands_iso:
            if math.fabs(pfcand.pdgId()) == 211 and TDeltaR(center, pfcand, dr_option) < EXTRA_TRACK_DR:
              extra_tracks.append(pfcand)
          extra_tracks.sort(key=lambda pfcand : pfcand.pt(), reverse=True)
          if len(extra_tracks) <= ALLOW_EXTRA_TRACKS:
            candidate['extra_tracks'] = extra_tracks
        # define photon
        photon = ROOT.TLorentzVector()
        candidate['photon_gamma_pfs'] = []
        candidate['photon_electron_pfs'] = []
        candidate['found_leading_gamma'] = False
        leading_gamma_pt = -1
        for pf3 in pfcands_iso:
          if ((abs(pf3.pdgId()) == 11 or pf3.pdgId() == 22) and
              WithinPhiEtaBox(pf3, center, BOX_PHI/2.0, BOX_ETA/2.0, dr_option)):
            pf3p4 = ROOT.TLorentzVector()
            if USE_ATVTX:
              pf3p4.SetPtEtaPhiE(pf3.pt(), pf3.eta(), pf3.phiAtVtx(), pf3.energy())
            else:
              pf3p4.SetPtEtaPhiE(pf3.pt(), pf3.eta(), pf3.phi(), pf3.energy())
            if pf3.pdgId() == 22:
              candidate['photon_gamma_pfs'].append(pf3)
              if pf3.pt() > leading_gamma_pt:
                leading_gamma_pt = pf3.pt()
                candidate['leading_gamma'] = pf3p4
                candidate['found_leading_gamma'] = True
            if abs(pf3.pdgId()) == 11:
              candidate['photon_electron_pfs'].append(pf3)
            photon = photon + pf3p4
        if candidate['found_leading_gamma'] == True:
          # found a candidate
          candidate['photon'] = photon
          candidate['eta'] = candidate['center'] + candidate['photon']
          candidate['eta_leadingonly'] = candidate['center'] + candidate['leading_gamma']
          candidates.append(candidate)
          pvqual.Fill(pf1.pvAssociationQuality())
          pvqual.Fill(pf2.pvAssociationQuality())
          # Define reconstructed Eta
          candidate['eta'] = candidate['center'] + candidate['photon']
          for extra_track in candidate['extra_tracks']:
            extra_track_vec = MakeTVector(extra_track)
            candidate['eta'] = candidate['eta'] + extra_track_vec
          if ISO_INNER_DR > 0:
            for pfcand in pfcands_iso:
              if TDeltaR(candidate['center'], pfcand, dr_option) < ISO_INNER_DR:
                if not (pfcand.pdgId()==130 or abs(pfcand.pdgId())==211):
                  continue
                candidate['eta'] = candidate['eta'] + MakeTVector(pfcand)
          candidate['eta_leadingonly'] = candidate['center'] + candidate['leading_gamma']
   
  # Define isolations
  for candidate in candidates:
    neutralIso = 0
    chargedIso = 0
    emIso = 0
    for pfcand in pfcands_iso:
      if TDeltaR(candidate['center'], pfcand, dr_option) > ISO_DR:
        continue # must be within iso cone
      if TDeltaR(candidate['center'], pfcand, dr_option) < ISO_INNER_DR:
        if (pfcand.pdgId()==130 or abs(pfcand.pdgId())==211):
          continue # if a hadron within inner cone, included in candidate instead
      # Neutral isolation
      if pfcand.pdgId() == 130:
        neutralIso += pfcand.pt()
      # Charged Isolation, muons
      if abs(pfcand.pdgId()) == 13:
        chargedIso += pfcand.pt()
      # Charged Isolation, hadrons
      if abs(pfcand.pdgId()) == 211:
        if pfcand.fromPV() <= 1:
          continue
        if pfcand == candidate['CH+']:
          continue
        if pfcand == candidate['CH-']:
          continue
        if pfcand in candidate['extra_tracks']:
          continue
        chargedIso += pfcand.pt()
      # EGamma Isolation
      if not WithinPhiEtaBox(pfcand, candidate['center'], BOX_PHI/2.0, BOX_ETA/2.0, dr_option):
        if abs(pfcand.pdgId()) == 11 or pfcand.pdgId() == 22:
          emIso += pfcand.pt()
    candidate['neutralIso'] = neutralIso 
    candidate['chargedIso'] = chargedIso 
    candidate['emIso'] = emIso 

  # Do selection on candidates
  numneutraliso = 0
  numchargediso = 0
  numemiso = 0
  numphotonpt = 0
  numfull = 0
  passed_candidates = []
  for candidate in candidates:
    etaPt = candidate['eta'].Pt()
    reliso_neutral.Fill(candidate['neutralIso']/etaPt)
    reliso_charged.Fill(candidate['chargedIso']/etaPt)
    reliso_em.Fill(candidate['emIso']/etaPt)
    if candidate['chargedIso']/etaPt < CHARGED_ISO_CUT:
      numchargediso += 1
    if candidate['neutralIso']/etaPt < NEUTRAL_ISO_CUT:
      numneutraliso += 1
    if candidate['emIso']/etaPt < EM_ISO_CUT:
      numemiso += 1
    if candidate['photon'].Pt() > PHOTON_PT_CUT:
      numphotonpt += 1
    if (candidate['chargedIso']/etaPt < CHARGED_ISO_CUT and
        candidate['neutralIso']/etaPt < NEUTRAL_ISO_CUT and
        candidate['emIso']/etaPt < EM_ISO_CUT and
        candidate['photon'].Pt() > PHOTON_PT_CUT):
      numfull += 1
      passed_candidates.append(candidate)

  # Finding nearest gen Eta and Matching
  nummatched = 0
  nummatchedonly = 0
  if RUNNING_ON_SIGNAL:
    for geneta in gen_etas:
      geneta_pt.push_back(geneta.pt())
      geneta_eta.push_back(geneta.eta())
      geneta_phi.push_back(geneta.phi())
      geneta_mass.push_back(geneta.mass())
      # match to candidate
      mindr = 99.9
      for candidate in candidates:
        dr = TDeltaR(candidate['eta'], geneta)
        if dr < mindr:
          mindr = dr
      geneta_candDR.push_back(mindr)
      # match to passed candidate
      mindr = 99.9
      for candidate in passed_candidates:
        dr = TDeltaR(candidate['eta'], geneta)
        if dr < mindr:
          mindr = dr
      geneta_passedCandDR.push_back(mindr)
        
  # store PV info
  for candidate in candidates:
    CHpos = candidate['CH+'] 
    CHneg = candidate['CH-']
    impact.Fill(CHpos.dxy())
    impact.Fill(CHneg.dxy())
    impact_sig.Fill(CHpos.dxyError())
    impact_sig.Fill(CHneg.dxyError())

  # Dump particular events by event number
  if not DUMP_EVENT_BY_NUM == ():
    if event.object().id().event() in DUMP_EVENT_NUM:
      print "Event ", event.object().id().event(), " has ", len(candidates), " candidate(s)"
      for candidate in candidates:
        dump(candidate)
      print "And ", len(passed_candidates), " passing candidate(s):"
      for candidate in passed_candidates:
        dump(candidate)
      if len(passed_candidates) >= 2:
        print "dREtaEta: ", passed_candidates[0]['eta'].DeltaR(passed_candidates[1]['eta'])
        print "mEtaEta: ", (passed_candidates[0]['eta'] + passed_candidates[1]['eta']).M()
      print "  [Enter] for next event."
      raw_input()

  # Fill Tree
  nCands[0] = len(candidates)
  nPass[0] = len(passed_candidates)
  tree.Fill()

  # Fill Histograms
  num_pfcands.Fill(len(pfcands))

  num_pairs.Fill(len(candidates))
  num_chargediso.Fill(numchargediso)
  num_neutraliso.Fill(numneutraliso)
  num_emiso.Fill(numemiso)
  num_full.Fill(numfull)
  num_matched.Fill(nummatched)
  num_matchedonly.Fill(nummatchedonly)

  if RUNNING_ON_SIGNAL:
      gen_num_etas.Fill(len(gen_etas))
      gen_etarelDR.Fill(DeltaR(gen_etas[0], gen_etas[1])) 
      for gen_eta in gen_etas:
        gen_etapt.Fill(gen_eta.pt())
        gen_etaphi.Fill(gen_eta.phi())
        gen_etaeta.Fill(gen_eta.eta())
        gen_etam.Fill(gen_eta.mass())
      gen_etapt_first2.Fill(gen_etas[0].pt())
      gen_etapt_first2.Fill(gen_etas[1].pt())
      gen_etaphi_first2.Fill(gen_etas[0].phi())
      gen_etaphi_first2.Fill(gen_etas[1].phi())
      gen_etaeta_first2.Fill(gen_etas[0].eta())
      gen_etaeta_first2.Fill(gen_etas[1].eta())
      gen_etam_first2.Fill(gen_etas[0].mass())
      gen_etam_first2.Fill(gen_etas[1].mass())

  for candidate in passed_candidates:
    hadronmass.Fill(candidate['center'].M())
    hadronpt.Fill(candidate['center'].Pt())
    hadronphi.Fill(candidate['center'].Phi())
    hadroneta.Fill(candidate['center'].Eta())
    etamass.Fill(candidate['eta'].M())
    if candidate['found_leading_gamma']:
      etagrommedmass.Fill(candidate['eta_leadingonly'].M())
    etapt.Fill(candidate['eta'].Pt())
    etaphi.Fill(candidate['eta'].Phi())
    etaeta.Fill(candidate['eta'].Eta())
    photon_num_e.Fill(len(candidate['photon_electron_pfs']))
    photon_num_gamma.Fill(len(candidate['photon_gamma_pfs']))
    photonmass.Fill(candidate['photon'].M())
    photonpt.Fill(candidate['photon'].Pt())
    photonphi.Fill(candidate['photon'].Phi())
    photoneta.Fill(candidate['photon'].Eta())

  if len(passed_candidates) >= 2:
    m_etaeta.Fill((passed_candidates[0]['eta']+passed_candidates[1]['eta']).M())
    dr_etaeta.Fill(passed_candidates[0]['eta'].DeltaR(passed_candidates[1]['eta']))
 
  # Cutflow information
  if len(candidates) >= 1:
    has_pair += 1
  if len(candidates) >= 2:
    has_pairx2 += 1
  if numemiso >= 1:
    pass_emiso += 1
  if numneutraliso >= 1:
    pass_neutraliso += 1
  if numchargediso >= 1:
    pass_chargediso += 1
  if numphotonpt >=1:
    pass_photonpt += 1
  if numfull >= 1:
    pass_full += 1
  if numfull >= 2:
    pass_fullx2 += 1
  if nummatched >= 1:
    pass_matched += 1
  if nummatched >= 2:
    pass_matchedx2 += 1
  if nummatchedonly >= 1:
    pass_matchedonly += 1
  if nummatchedonly >= 2:
    pass_matchedonlyx2 += 1

# Print cutflow
if DUMP_EVENT_BY_NUM == ():
  print "Efficiencies"
  print "Events with one +CH/-CH pair                                  : " + str(has_pair) + " events, " + str(has_pair*100.0/total) + "%"
  print "Events with two +CH/-CH pairs                                 : " + str(has_pairx2) + " events, " + str(has_pairx2*100.0/total) + "%"
  print "Events with one candidate passing full selection              : " + str(pass_full) + " events, " + str(pass_full*100.0/total) + "%"
  print "Events with two candidates passing full selection             : " + str(pass_fullx2) + " events, " + str(pass_fullx2*100.0/total) + "%"
  print "Events with one candidate matched                             : " + str(pass_matchedonly) + " events, " + str(pass_matchedonly*100.0/total) + "%"
  print "Events with two candidates matched                            : " + str(pass_matchedonlyx2) + " events, " + str(pass_matchedonlyx2*100.0/total) + "%"
  print "Events with one candidate passing full selection and matched  : " + str(pass_matched) + " events, " + str(pass_matched*100.0/total) + "%"
  print "Events with two candidates passing full selection and matched : " + str(pass_matchedx2) + " events, " + str(pass_matchedx2*100.0/total) + "%"

  print "Selection Cutflow:"
  print "Events with one candidate passing charged isolation          : " + str(pass_chargediso) + " events, " + str(pass_chargediso*100.0/has_pair) + "%"
  print "Events with one candidate passing neutral isolation          : " + str(pass_neutraliso) + " events, " + str(pass_neutraliso*100.0/has_pair) + "%"
  print "Events with one candidate passing E/M isolation              : " + str(pass_emiso) + " events, " + str(pass_emiso*100.0/has_pair) + "%"
  print "Events with one candidate passing Photon Pt requirement      : " + str(pass_photonpt) + " events, " + str(pass_photonpt*100.0/has_pair) + "%"
# Save file with histograms
outputfile.cd()
outputfile.Write()
outputfile.Close()
