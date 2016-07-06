import ROOT
from DataFormats.FWLite import Events, Handle
from array import array
from math import *
import sys
from optparse import OptionParser
sys.path.insert(0, '/uscms/home/bchiari1/work/SUSY/Analysis/CMSSW_5_3_8_patch1/test/ttree')
from JetTools import *
from lepWmaker import *

def show(vec):
  string = "("
  string += str(vec.Pt()) + ", " + str(vec.Eta()) + ", " + str(vec.Phi()) + ", " + str(vec.M()) + ")"
  return string

def delta_phi(phi1, phi2):
  dphi = math.fabs(phi1 - phi2)
  return delta_phi_helper(dphi)

def delta_phi_helper(dphi):
  if dphi > 3.1415926535:
    return delta_phi_helper(dphi - 3.1415926535)
  else:
    return dphi

parser = OptionParser()

parser.add_option('-f', '--file',
                  dest='file',
                  help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('-M', '--max', type='int', default=-1,
                  dest='max',
                  help='Maximum number of events to process')
parser.add_option('-w', '--weight', default=1.0,
                  dest='weight',
                  help='Weight of each event as it is added to the TTree')

(options, args) = parser.parse_args()

# Get the old tree
oldfile = ROOT.TFile(options.file, "update")
oldtree = oldfile.Get("tree")
filename = options.file[0:options.file.find(".root")] + "_toptag.root"
newfile = ROOT.TFile(filename, "recreate")

# Make a new tree with desired content
oldtree.SetBranchStatus("*", 1)
newtree = oldtree.CloneTree()

# Get any information from branches we need to compute new variables
metphi = array('f',  [0.0])
oldtree.SetBranchAddress('metphi', metphi)

numjets = array('f',  [0.0])
oldtree.SetBranchAddress('numjets', numjets)
numak4jets = array('f',  [0.0])
oldtree.SetBranchAddress('numak4jets', numak4jets)
numtoptagjets = array('f',  [0.0])
oldtree.SetBranchAddress('numtoptagjets', numtoptagjets)
numgoodleptons = array('f',  [0.0])
oldtree.SetBranchAddress('numgoodleptons', numgoodleptons)

jet1pt = array('f', [0.0])
oldtree.SetBranchAddress('jet1pt', jet1pt)
jet1eta = array('f', [0.0])
oldtree.SetBranchAddress('jet1eta', jet1eta)
jet1phi = array('f', [0.0])
oldtree.SetBranchAddress('jet1phi', jet1phi)
jet1mass = array('f', [0.0])
oldtree.SetBranchAddress('jet1mass', jet1mass)
jet1csv = array('f', [0.0])
oldtree.SetBranchAddress('jet1csv', jet1csv)
jet1tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet1tau1', jet1tau1)
jet1tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet1tau2', jet1tau2)
jet1tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet1tau3', jet1tau3)
jet2pt = array('f', [0.0])
oldtree.SetBranchAddress('jet2pt', jet2pt)
jet2eta = array('f', [0.0])
oldtree.SetBranchAddress('jet2eta', jet2eta)
jet2phi = array('f', [0.0])
oldtree.SetBranchAddress('jet2phi', jet2phi)
jet2mass = array('f', [0.0])
oldtree.SetBranchAddress('jet2mass', jet2mass)
jet2csv = array('f', [0.0])
oldtree.SetBranchAddress('jet2csv', jet2csv)
jet2tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet2tau1', jet2tau1)
jet2tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet2tau2', jet2tau2)
jet2tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet2tau3', jet2tau3)
jet3pt = array('f', [0.0])
oldtree.SetBranchAddress('jet3pt', jet3pt)
jet3eta = array('f', [0.0])
oldtree.SetBranchAddress('jet3eta', jet3eta)
jet3phi = array('f', [0.0])
oldtree.SetBranchAddress('jet3phi', jet3phi)
jet3mass = array('f', [0.0])
oldtree.SetBranchAddress('jet3mass', jet3mass)
jet3csv = array('f', [0.0])
oldtree.SetBranchAddress('jet3csv', jet3csv)
jet3tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet3tau1', jet3tau1)
jet3tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet3tau2', jet3tau2)
jet3tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet3tau3', jet3tau3)
jet4pt = array('f', [0.0])
oldtree.SetBranchAddress('jet4pt', jet4pt)
jet4eta = array('f', [0.0])
oldtree.SetBranchAddress('jet4eta', jet4eta)
jet4phi = array('f', [0.0])
oldtree.SetBranchAddress('jet4phi', jet4phi)
jet4mass = array('f', [0.0])
oldtree.SetBranchAddress('jet4mass', jet4mass)
jet4csv = array('f', [0.0])
oldtree.SetBranchAddress('jet4csv', jet4csv)
jet4tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet4tau1', jet4tau1)
jet4tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet4tau2', jet4tau2)
jet4tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet4tau3', jet4tau3)
jet5pt = array('f', [0.0])
oldtree.SetBranchAddress('jet5pt', jet5pt)
jet5eta = array('f', [0.0])
oldtree.SetBranchAddress('jet5eta', jet5eta)
jet5phi = array('f', [0.0])
oldtree.SetBranchAddress('jet5phi', jet5phi)
jet5mass = array('f', [0.0])
oldtree.SetBranchAddress('jet5mass', jet5mass)
jet5csv = array('f', [0.0])
oldtree.SetBranchAddress('jet5csv', jet5csv)
jet5tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet5tau1', jet5tau1)
jet5tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet5tau2', jet5tau2)
jet5tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet5tau3', jet5tau3)
jet6pt = array('f', [0.0])
oldtree.SetBranchAddress('jet6pt', jet6pt)
jet6eta = array('f', [0.0])
oldtree.SetBranchAddress('jet6eta', jet6eta)
jet6phi = array('f', [0.0])
oldtree.SetBranchAddress('jet6phi', jet6phi)
jet6mass = array('f', [0.0])
oldtree.SetBranchAddress('jet6mass', jet6mass)
jet6csv = array('f', [0.0])
oldtree.SetBranchAddress('jet6csv', jet6csv)
jet6tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet6tau1', jet6tau1)
jet6tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet6tau2', jet6tau2)
jet6tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet6tau3', jet6tau3)
jet7pt = array('f', [0.0])
oldtree.SetBranchAddress('jet7pt', jet7pt)
jet7eta = array('f', [0.0])
oldtree.SetBranchAddress('jet7eta', jet7eta)
jet7phi = array('f', [0.0])
oldtree.SetBranchAddress('jet7phi', jet7phi)
jet7mass = array('f', [0.0])
oldtree.SetBranchAddress('jet7mass', jet7mass)
jet7csv = array('f', [0.0])
oldtree.SetBranchAddress('jet7csv', jet7csv)
jet7tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet7tau1', jet7tau1)
jet7tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet7tau2', jet7tau2)
jet7tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet7tau3', jet7tau3)
jet8pt = array('f', [0.0])
oldtree.SetBranchAddress('jet8pt', jet8pt)
jet8eta = array('f', [0.0])
oldtree.SetBranchAddress('jet8eta', jet8eta)
jet8phi = array('f', [0.0])
oldtree.SetBranchAddress('jet8phi', jet8phi)
jet8mass = array('f', [0.0])
oldtree.SetBranchAddress('jet8mass', jet8mass)
jet8csv = array('f', [0.0])
oldtree.SetBranchAddress('jet8csv', jet8csv)
jet8tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet8tau1', jet8tau1)
jet8tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet8tau2', jet8tau2)
jet8tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet8tau3', jet8tau3)
jet9pt = array('f', [0.0])
oldtree.SetBranchAddress('jet9pt', jet9pt)
jet9eta = array('f', [0.0])
oldtree.SetBranchAddress('jet9eta', jet9eta)
jet9phi = array('f', [0.0])
oldtree.SetBranchAddress('jet9phi', jet9phi)
jet9mass = array('f', [0.0])
oldtree.SetBranchAddress('jet9mass', jet9mass)
jet9csv = array('f', [0.0])
oldtree.SetBranchAddress('jet9csv', jet9csv)
jet9tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet9tau1', jet9tau1)
jet9tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet9tau2', jet9tau2)
jet9tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet9tau3', jet9tau3)
jet10pt = array('f', [0.0])
oldtree.SetBranchAddress('jet10pt', jet10pt)
jet10eta = array('f', [0.0])
oldtree.SetBranchAddress('jet10eta', jet10eta)
jet10phi = array('f', [0.0])
oldtree.SetBranchAddress('jet10phi', jet10phi)
jet10mass = array('f', [0.0])
oldtree.SetBranchAddress('jet10mass', jet10mass)
jet10csv = array('f', [0.0])
oldtree.SetBranchAddress('jet10csv', jet10csv)
jet10tau1 = array('f', [0.0])
oldtree.SetBranchAddress('jet10tau1', jet10tau1)
jet10tau2 = array('f', [0.0])
oldtree.SetBranchAddress('jet10tau2', jet10tau2)
jet10tau3 = array('f', [0.0])
oldtree.SetBranchAddress('jet10tau3', jet10tau3)

toptagjet1pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet1pt', toptagjet1pt)
toptagjet1eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet1eta', toptagjet1eta)
toptagjet1phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet1phi', toptagjet1phi)
toptagjet1mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet1mass', toptagjet1mass)
toptagjet1minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet1minmass', toptagjet1minmass)
toptagjet1Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet1Wmass', toptagjet1Wmass)
toptagjet1topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet1topmass', toptagjet1topmass)
toptagjet1nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet1nsub', toptagjet1nsub)
toptagjet2pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet2pt', toptagjet2pt)
toptagjet2eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet2eta', toptagjet2eta)
toptagjet2phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet2phi', toptagjet2phi)
toptagjet2mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet2mass', toptagjet2mass)
toptagjet2minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet2minmass', toptagjet2minmass)
toptagjet2Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet2Wmass', toptagjet2Wmass)
toptagjet2topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet2topmass', toptagjet2topmass)
toptagjet2nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet2nsub', toptagjet2nsub)
toptagjet3pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet3pt', toptagjet3pt)
toptagjet3eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet3eta', toptagjet3eta)
toptagjet3phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet3phi', toptagjet3phi)
toptagjet3mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet3mass', toptagjet3mass)
toptagjet3minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet3minmass', toptagjet3minmass)
toptagjet3Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet3Wmass', toptagjet3Wmass)
toptagjet3topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet3topmass', toptagjet3topmass)
toptagjet3nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet3nsub', toptagjet3nsub)
toptagjet4pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet4pt', toptagjet4pt)
toptagjet4eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet4eta', toptagjet4eta)
toptagjet4phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet4phi', toptagjet4phi)
toptagjet4mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet4mass', toptagjet4mass)
toptagjet4minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet4minmass', toptagjet4minmass)
toptagjet4Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet4Wmass', toptagjet4Wmass)
toptagjet4topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet4topmass', toptagjet4topmass)
toptagjet4nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet4nsub', toptagjet4nsub)
toptagjet5pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet5pt', toptagjet5pt)
toptagjet5eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet5eta', toptagjet5eta)
toptagjet5phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet5phi', toptagjet5phi)
toptagjet5mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet5mass', toptagjet5mass)
toptagjet5minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet5minmass', toptagjet5minmass)
toptagjet5Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet5Wmass', toptagjet5Wmass)
toptagjet5topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet5topmass', toptagjet5topmass)
toptagjet5nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet5nsub', toptagjet5nsub)
toptagjet6pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet6pt', toptagjet6pt)
toptagjet6eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet6eta', toptagjet6eta)
toptagjet6phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet6phi', toptagjet6phi)
toptagjet6mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet6mass', toptagjet6mass)
toptagjet6minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet6minmass', toptagjet6minmass)
toptagjet6Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet6Wmass', toptagjet6Wmass)
toptagjet6topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet6topmass', toptagjet6topmass)
toptagjet6nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet6nsub', toptagjet6nsub)
toptagjet7pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet7pt', toptagjet7pt)
toptagjet7eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet7eta', toptagjet7eta)
toptagjet7phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet7phi', toptagjet7phi)
toptagjet7mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet7mass', toptagjet7mass)
toptagjet7minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet7minmass', toptagjet7minmass)
toptagjet7Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet7Wmass', toptagjet7Wmass)
toptagjet7topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet7topmass', toptagjet7topmass)
toptagjet7nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet7nsub', toptagjet7nsub)
toptagjet8pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet8pt', toptagjet8pt)
toptagjet8eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet8eta', toptagjet8eta)
toptagjet8phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet8phi', toptagjet8phi)
toptagjet8mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet8mass', toptagjet8mass)
toptagjet8minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet8minmass', toptagjet8minmass)
toptagjet8Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet8Wmass', toptagjet8Wmass)
toptagjet8topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet8topmass', toptagjet8topmass)
toptagjet8nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet8nsub', toptagjet8nsub)
toptagjet9pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet9pt', toptagjet9pt)
toptagjet9eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet9eta', toptagjet9eta)
toptagjet9phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet9phi', toptagjet9phi)
toptagjet9mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet9mass', toptagjet9mass)
toptagjet9minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet9minmass', toptagjet9minmass)
toptagjet9Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet9Wmass', toptagjet9Wmass)
toptagjet9topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet9topmass', toptagjet9topmass)
toptagjet9nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet9nsub', toptagjet9nsub)
toptagjet10pt = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet10pt', toptagjet10pt)
toptagjet10eta = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet10eta', toptagjet10eta)
toptagjet10phi = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet10phi', toptagjet10phi)
toptagjet10mass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet10mass', toptagjet10mass)
toptagjet10minmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet10minmass', toptagjet10minmass)
toptagjet10Wmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet10Wmass', toptagjet10Wmass)
toptagjet10topmass = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet10topmass', toptagjet10topmass)
toptagjet10nsub = array('f', [0.0])
oldtree.SetBranchAddress('toptagjet10nsub', toptagjet10nsub)

lep1id = array('f', [0.0])
oldtree.SetBranchAddress('lep1id', lep1id)
lep1pt = array('f', [0.0])
oldtree.SetBranchAddress('lep1pt', lep1pt)
lep1eta = array('f', [0.0])
oldtree.SetBranchAddress('lep1eta', lep1eta)
lep1phi = array('f', [0.0])
oldtree.SetBranchAddress('lep1phi', lep1phi)
lep1mass = array('f', [0.0])
oldtree.SetBranchAddress('lep1mass', lep1mass)
lep2id = array('f', [0.0])
oldtree.SetBranchAddress('lep2id', lep2id)
lep2pt = array('f', [0.0])
oldtree.SetBranchAddress('lep2pt', lep2pt)
lep2eta = array('f', [0.0])
oldtree.SetBranchAddress('lep2eta', lep2eta)
lep2phi = array('f', [0.0])
oldtree.SetBranchAddress('lep2phi', lep2phi)
lep2mass = array('f', [0.0])
oldtree.SetBranchAddress('lep2mass', lep2mass)
lep3id = array('f', [0.0])
oldtree.SetBranchAddress('lep3id', lep3id)
lep3pt = array('f', [0.0])
oldtree.SetBranchAddress('lep3pt', lep3pt)
lep3eta = array('f', [0.0])
oldtree.SetBranchAddress('lep3eta', lep3eta)
lep3phi = array('f', [0.0])
oldtree.SetBranchAddress('lep3phi', lep3phi)
lep3mass = array('f', [0.0])
oldtree.SetBranchAddress('lep3mass', lep3mass)
lep4id = array('f', [0.0])
oldtree.SetBranchAddress('lep4id', lep4id)
lep4pt = array('f', [0.0])
oldtree.SetBranchAddress('lep4pt', lep4pt)
lep4eta = array('f', [0.0])
oldtree.SetBranchAddress('lep4eta', lep4eta)
lep4phi = array('f', [0.0])
oldtree.SetBranchAddress('lep4phi', lep4phi)
lep4mass = array('f', [0.0])
oldtree.SetBranchAddress('lep4mass', lep4mass)

WcandPpt = array('f', [0.0])
oldtree.SetBranchAddress('WcandPpt', WcandPpt)
WcandPeta = array('f', [0.0])
oldtree.SetBranchAddress('WcandPeta', WcandPeta)
WcandPphi = array('f', [0.0])
oldtree.SetBranchAddress('WcandPphi', WcandPphi)
WcandPm = array('f', [0.0])
oldtree.SetBranchAddress('WcandPm', WcandPm)
WcandNpt = array('f', [0.0])
oldtree.SetBranchAddress('WcandNpt', WcandNpt)
WcandNeta = array('f', [0.0])
oldtree.SetBranchAddress('WcandNeta', WcandNeta)
WcandNphi = array('f', [0.0])
oldtree.SetBranchAddress('WcandNphi', WcandNphi)
WcandNm = array('f', [0.0])
oldtree.SetBranchAddress('WcandNm', WcandNm)

lep2D_rel = array('f', [0.0])
oldtree.SetBranchAddress('lep2D_rel', lep2D_rel)
lep2D_dr = array('f', [0.0])
oldtree.SetBranchAddress('lep2D_dr', lep2D_dr)
eventType = array('f', [0.0])
oldtree.SetBranchAddress('eventType', eventType)


# Define any new variables
branches = []
numleptops = array('f', [0.0])
branches.append(newtree.Branch('numleptops', numleptops, "numleptops/F"))
numhadtops = array('f', [0.0])
branches.append(newtree.Branch('numhadtops', numhadtops, "numhadtops/F"))
numtoptags = array('f', [0.0])
branches.append(newtree.Branch('numtoptags', numtoptags, "numtoptags/F"))
numtops = array('f', [0.0])
branches.append(newtree.Branch('numtops', numtops, "numtops/F"))
Htextra = array('f', [0.0])
branches.append(newtree.Branch('Htextra', Htextra, "Htextra/F"))
Httops = array('f', [0.0])
branches.append(newtree.Branch('Httops', Httops, "Httops/F"))
tt_dR = array('f', [0.0])
branches.append(newtree.Branch('tt_dR', tt_dR, "tt_dR/F"))
tt_dPhi = array('f', [0.0])
branches.append(newtree.Branch('tt_dPhi', tt_dPhi, "tt_dPhi/F"))
tt_dEta = array('f', [0.0])
branches.append(newtree.Branch('tt_dEta', tt_dEta, "tt_dEta/F"))
tt_mtt = array('f', [0.0])
branches.append(newtree.Branch('tt_mtt', tt_mtt, "tt_mtt/F"))
pz_tt_extra = array('f', [0.0])
branches.append(newtree.Branch('pz_tt_extra', pz_tt_extra, "pz_tt_extra/F"))
dHt = array('f', [0.0])
branches.append(newtree.Branch('dHt', dHt, "dHt/F"))
dPhi_met_t1 = array('f', [0.0])
branches.append(newtree.Branch('dPhi_met_t1', dPhi_met_t1, "dPhi_met_t1/F"))
dPhi_met_t2 = array('f', [0.0])
branches.append(newtree.Branch('dPhi_met_t2', dPhi_met_t2, "dPhi_met_t2/F"))

# Event loop to calculate the new variables
n = oldtree.GetEntries()
for e in range(n):
  if e % 10000 == 0:
    percentDone = float(e) / float(n) * 100.0
    print 'Processing {0:10.0f}/{1:10.0f} : {2:5.2f} %'.format(e, n, percentDone )
  oldtree.GetEntry(e)

  # Make lepton collection
  leptons = []
  if numgoodleptons[0] > 0:
    lep1 = ROOT.TLorentzVector()
    lep1.SetPtEtaPhiM(lep1pt[0], lep1eta[0], lep1phi[0], lep1mass[0])
    leptons.append(lep1)
  if numgoodleptons[0] > 1:
    lep2 = ROOT.TLorentzVector()
    lep2.SetPtEtaPhiM(lep2pt[0], lep2eta[0], lep2phi[0], lep2mass[0])
    leptons.append(lep2)
  if numgoodleptons[0] > 2:
    lep3 = ROOT.TLorentzVector()
    lep3.SetPtEtaPhiM(lep3pt[0], lep3eta[0], lep3phi[0], lep3mass[0])
    leptons.append(lep3)
  if numgoodleptons[0] > 3:
    lep4 = ROOT.TLorentzVector()
    lep4.SetPtEtaPhiM(lep4pt[0], lep4eta[0], lep4phi[0], lep4mass[0])
    leptons.append(lep4)

  # Remake jet collection
  cajets = []
  jettaus = []
  if numjets[0] > 0:
    jet1 = ROOT.TLorentzVector()
    jet1.SetPtEtaPhiM(jet1pt[0], jet1eta[0], jet1phi[0], jet1mass[0])
    cajets.append(jet1)
    jettaus.append( (jet1tau1[0], jet1tau2[0], jet1tau3[0]) )
  if numjets[0] > 1:
    jet2 = ROOT.TLorentzVector()
    jet2.SetPtEtaPhiM(jet2pt[0], jet2eta[0], jet2phi[0], jet2mass[0])
    cajets.append(jet2)
    jettaus.append( (jet2tau1[0], jet2tau2[0], jet2tau3[0]) )
  if numjets[0] > 2:
    jet3 = ROOT.TLorentzVector()
    jet3.SetPtEtaPhiM(jet3pt[0], jet3eta[0], jet3phi[0], jet3mass[0])
    cajets.append(jet3)
    jettaus.append( (jet3tau1[0], jet3tau2[0], jet3tau3[0]) )
  if numjets[0] > 3:
    jet4 = ROOT.TLorentzVector()
    jet4.SetPtEtaPhiM(jet4pt[0], jet4eta[0], jet4phi[0], jet4mass[0])
    cajets.append(jet4)
    jettaus.append( (jet4tau1[0], jet4tau2[0], jet4tau3[0]) )
  if numjets[0] > 4:
    jet5 = ROOT.TLorentzVector()
    jet5.SetPtEtaPhiM(jet5pt[0], jet5eta[0], jet5phi[0], jet5mass[0])
    cajets.append(jet5)
    jettaus.append( (jet5tau1[0], jet5tau2[0], jet5tau3[0]) )
  if numjets[0] > 5:
    jet6 = ROOT.TLorentzVector()
    jet6.SetPtEtaPhiM(jet6pt[0], jet6eta[0], jet6phi[0], jet6mass[0])
    cajets.append(jet6)
    jettaus.append( (jet6tau1[0], jet6tau2[0], jet6tau3[0]) )
  if numjets[0] > 6:
    jet7 = ROOT.TLorentzVector()
    jet7.SetPtEtaPhiM(jet7pt[0], jet7eta[0], jet7phi[0], jet7mass[0])
    cajets.append(jet7)
    jettaus.append( (jet7tau1[0], jet7tau2[0], jet7tau3[0]) )
  if numjets[0] > 7:
    jet8 = ROOT.TLorentzVector()
    jet8.SetPtEtaPhiM(jet8pt[0], jet8eta[0], jet8phi[0], jet8mass[0])
    cajets.append(jet8)
    jettaus.append( (jet8tau1[0], jet8tau2[0], jet8tau3[0]) )
  if numjets[0] > 8:
    jet9 = ROOT.TLorentzVector()
    jet9.SetPtEtaPhiM(jet9pt[0], jet9eta[0], jet9phi[0], jet9mass[0])
    cajets.append(jet9)
    jettaus.append( (jet9tau1[0], jet9tau2[0], jet9tau3[0]) )
  if numjets[0] > 9:
    jet10 = ROOT.TLorentzVector()
    jet10.SetPtEtaPhiM(jet10pt[0], jet10eta[0], jet10phi[0], jet10mass[0])
    cajets.append(jet10)
    jettaus.append( (jet10tau1[0], jet10tau2[0], jet10tau3[0]) )

  toptagjets = []
  toptagminmasses = []
  toptagWmasses = []
  toptagtopmasses = []
  toptagnsubs = []
  if numtoptagjets[0] > 0:
    jet1 = ROOT.TLorentzVector()
    jet1.SetPtEtaPhiM(toptagjet1pt[0], toptagjet1eta[0], toptagjet1phi[0], toptagjet1mass[0])
    toptagjets.append(jet1)
    toptagminmasses.append(toptagjet1minmass[0])
    toptagtopmasses.append(toptagjet1topmass[0])
    toptagWmasses.append(toptagjet1Wmass[0])
    toptagnsubs.append(toptagjet1nsub[0])
  if numtoptagjets[0] > 1:
    jet2 = ROOT.TLorentzVector()
    jet2.SetPtEtaPhiM(toptagjet2pt[0], toptagjet2eta[0], toptagjet2phi[0], toptagjet2mass[0])
    toptagjets.append(jet2)
    toptagminmasses.append(toptagjet2minmass[0])
    toptagtopmasses.append(toptagjet2topmass[0])
    toptagWmasses.append(toptagjet2Wmass[0])
    toptagnsubs.append(toptagjet2nsub[0])
  if numtoptagjets[0] > 2:
    jet3 = ROOT.TLorentzVector()
    jet3.SetPtEtaPhiM(toptagjet3pt[0], toptagjet3eta[0], toptagjet3phi[0], toptagjet3mass[0])
    toptagjets.append(jet3)
    toptagminmasses.append(toptagjet3minmass[0])
    toptagtopmasses.append(toptagjet3topmass[0])
    toptagWmasses.append(toptagjet3Wmass[0])
    toptagnsubs.append(toptagjet3nsub[0])
  if numtoptagjets[0] > 3:
    jet4 = ROOT.TLorentzVector()
    jet4.SetPtEtaPhiM(toptagjet4pt[0], toptagjet4eta[0], toptagjet4phi[0], toptagjet4mass[0])
    toptagjets.append(jet4)
    toptagminmasses.append(toptagjet4minmass[0])
    toptagtopmasses.append(toptagjet4topmass[0])
    toptagWmasses.append(toptagjet4Wmass[0])
    toptagnsubs.append(toptagjet4nsub[0])
  if numtoptagjets[0] > 4:
    jet5 = ROOT.TLorentzVector()
    jet5.SetPtEtaPhiM(toptagjet5pt[0], toptagjet5eta[0], toptagjet5phi[0], toptagjet5mass[0])
    toptagjets.append(jet5)
    toptagminmasses.append(toptagjet5minmass[0])
    toptagtopmasses.append(toptagjet5topmass[0])
    toptagWmasses.append(toptagjet5Wmass[0])
    toptagnsubs.append(toptagjet5nsub[0])
  if numtoptagjets[0] > 5:
    jet6 = ROOT.TLorentzVector()
    jet6.SetPtEtaPhiM(toptagjet6pt[0], toptagjet6eta[0], toptagjet6phi[0], toptagjet6mass[0])
    toptagjets.append(jet6)
    toptagminmasses.append(toptagjet6minmass[0])
    toptagtopmasses.append(toptagjet6topmass[0])
    toptagWmasses.append(toptagjet6Wmass[0])
    toptagnsubs.append(toptagjet6nsub[0])
  if numtoptagjets[0] > 6:
    jet7 = ROOT.TLorentzVector()
    jet7.SetPtEtaPhiM(toptagjet7pt[0], toptagjet7eta[0], toptagjet7phi[0], toptagjet7mass[0])
    toptagjets.append(jet7)
    toptagminmasses.append(toptagjet7minmass[0])
    toptagtopmasses.append(toptagjet7topmass[0])
    toptagWmasses.append(toptagjet7Wmass[0])
    toptagnsubs.append(toptagjet7nsub[0])
  if numtoptagjets[0] > 7:
    jet8 = ROOT.TLorentzVector()
    jet8.SetPtEtaPhiM(toptagjet8pt[0], toptagjet8eta[0], toptagjet8phi[0], toptagjet8mass[0])
    toptagjets.append(jet8)
    toptagminmasses.append(toptagjet8minmass[0])
    toptagtopmasses.append(toptagjet8topmass[0])
    toptagWmasses.append(toptagjet8Wmass[0])
    toptagnsubs.append(toptagjet8nsub[0])
  if numtoptagjets[0] > 8:
    jet9 = ROOT.TLorentzVector()
    jet9.SetPtEtaPhiM(toptagjet9pt[0], toptagjet9eta[0], toptagjet9phi[0], toptagjet9mass[0])
    toptagjets.append(jet9)
    toptagminmasses.append(toptagjet9minmass[0])
    toptagtopmasses.append(toptagjet9topmass[0])
    toptagWmasses.append(toptagjet9Wmass[0])
    toptagnsubs.append(toptagjet9nsub[0])
  if numtoptagjets[0] > 9:
    jet10 = ROOT.TLorentzVector()
    jet10.SetPtEtaPhiM(toptagjet10pt[0], toptagjet10eta[0], toptagjet10phi[0], toptagjet10mass[0])
    toptagjets.append(jet10)
    toptagminmasses.append(toptagjet10minmass[0])
    toptagtopmasses.append(toptagjet10topmass[0])
    toptagWmasses.append(toptagjet10Wmass[0])
    toptagnsubs.append(toptagjet10nsub[0])
  
  nleptops = 0
  leptops = []
  nhadtops = 0
  hadtops = []
  ntoptags = 0
  toptags = []
  ntops = 0
  jets = list(cajets)
  # count hadronic tops
  temp = list(jets)
  for i in range(len(temp)):
    if jettaus[i][2] != 0 and jettaus[i][1] != 0:
      if temp[i].Pt() > 400 and jettaus[i][2]/jettaus[i][1] < 0.75 and temp[i].M() > 140:
        nhadtops += 1
        hadtops.append(temp[i])
        jets.remove(temp[i])
  # count leptonic tops
  for lep in leptons:
    if len(jets) > 0:
      nearest_jet = jets[0]
      for jet in jets[:]:
        if lep.DeltaR(jet) < lep.DeltaR(nearest_jet):
          nearest_jet = jet
      if lep.DeltaR(nearest_jet) < 1.0:
        top_cand = lep + nearest_jet
        nleptops += 1
        leptops.append(top_cand)
        jets.remove(nearest_jet)
        
  # count top tags
  for i in range(len(toptagjets)):
    if toptagnsubs[i] == 3 and toptagminmasses[i] >= 65 and toptagtopmasses[i] > 140 and toptagtopmasses[i] < 250:
      ntoptags += 1
      toptags.append(toptagjets[i])

  # Calculate Ht of remaining stuff
  Ht_extra = 0
  for jet in jets:
    Ht_extra += jet.Pt()
  
  Ht_tops = 0
  for jet in hadtops:
    Ht_tops += jet.Pt()
  for jet in leptops:
    Ht_tops += jet.Pt()

  numleptops[0] = nleptops
  numhadtops[0] = nhadtops
  numtoptags[0] = ntoptags
  numtops[0] = nleptops + nhadtops
  Htextra[0] = Ht_extra
  Httops[0] = Ht_tops

  # tt variables
  if len(hadtops) == 2:
    tt_dR[0] = hadtops[0].DeltaR(hadtops[1])
    tt_dPhi[0] = hadtops[0].DeltaPhi(hadtops[1])
    tt_dEta[0] = fabs(hadtops[0].Eta() - hadtops[1].Eta())
    tt_mtt[0] = (hadtops[0] + hadtops[1]).M()

    tt_extra = hadtops[0] + hadtops[1]
    for jet in jets:
      tt_extra += jet
    pz_tt_extra[0] = tt_extra.Pz()
    dHt[0] = math.fabs(hadtops[0].Pt() - hadtops[1].Pt())
    dphi1 = delta_phi(metphi[0], hadtops[0].Phi())
    dphi2 = delta_phi(metphi[0], hadtops[1].Phi())
    dPhi_met_t1[0] = max(dphi1, dphi2)
    dPhi_met_t2[0] = min(dphi1, dphi2)

  # Fill branches
  for branch in branches:
    branch.Fill()

  # Reset new tree
  numleptops[0] = -1.0
  numhadtops[0] = -1.0
  numtoptags[0] = -1.0
  numtops[0] = -1.0
  Htextra[0] = -1.0
  Httops[0] = -1.0
  tt_dR[0] = 100
  tt_dPhi[0] = 100
  tt_dEta[0] = 100
  tt_mtt[0] = 0
  pz_tt_extra[0] = 0
  dHt[0] = -1.0
  dPhi_met_t1[0] = 100
  dPhi_met_t2[0] = 100

# Save and close
newfile.Write()
newfile.Close()
