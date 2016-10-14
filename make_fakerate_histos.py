from ROOT import *
from math import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--file',
                  dest='file',
                  help='File or group of files using a wildcard (remember to use \\ to input a wildcard)')
parser.add_option('--label',
                  dest='label',
                  default='',
                  help='label for sample')
parser.add_option('--subdir',
                  dest='subdir', default="",
                  help='sub directory location in rootfile')
(options, args) = parser.parse_args()

histo_file = TFile(options.file)
label = options.label
savefile = TFile('fakerate_1D_histos_'+label+'.root', 'RECREATE')

evenmass_pt_nume = histo_file.Get('twoprongfakenume_even_pt')
evenmass_pt_deno = histo_file.Get('twoprongfakedeno_even_pt')
evenmass_eta_nume = histo_file.Get('twoprongfakenume_even_eta')
evenmass_eta_deno = histo_file.Get('twoprongfakedeno_even_eta')
evenmass_phi_nume = histo_file.Get('twoprongfakenume_even_phi')
evenmass_phi_deno = histo_file.Get('twoprongfakedeno_even_phi')
evenmass_ecal_nume = histo_file.Get('twoprongfakenume_even_ecal')
evenmass_ecal_deno = histo_file.Get('twoprongfakedeno_even_ecal')
evenmass_hcal_nume = histo_file.Get('twoprongfakenume_even_hcal')
evenmass_hcal_deno = histo_file.Get('twoprongfakedeno_even_hcal')

oddmass_pt_nume = histo_file.Get('twoprongfakenume_odd_pt')
oddmass_pt_deno = histo_file.Get('twoprongfakedeno_odd_pt')
oddmass_eta_nume = histo_file.Get('twoprongfakenume_odd_eta')
oddmass_eta_deno = histo_file.Get('twoprongfakedeno_odd_eta')
oddmass_phi_nume = histo_file.Get('twoprongfakenume_odd_phi')
oddmass_phi_deno = histo_file.Get('twoprongfakedeno_odd_phi')
oddmass_ecal_nume = histo_file.Get('twoprongfakenume_odd_ecal')
oddmass_ecal_deno = histo_file.Get('twoprongfakedeno_odd_ecal')
oddmass_hcal_nume = histo_file.Get('twoprongfakenume_odd_hcal')
oddmass_hcal_deno = histo_file.Get('twoprongfakedeno_odd_hcal')

fake_numerator_pt = TH1F('fake_nume_pt', 'Number of Numerator Objects, ' + label, evenmass_pt_nume.GetNbinsX(), 0, 1300)
fake_numerator_pt.GetXaxis().SetTitle('p_{T}')
fake_denominator_pt = TH1F('fake_deno_pt', 'Number of Denominator Objects, ' + label, evenmass_pt_deno.GetNbinsX(), 0, 1300)
fake_denominator_pt.GetXaxis().SetTitle('p_{T}')
for pt_bin in range(1, evenmass_pt_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_pt_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_pt_nume.GetBinContent( evenmass_pt_nume.GetBin(pt_bin, mass_bin) )
    total_weight_deno += evenmass_pt_deno.GetBinContent( evenmass_pt_deno.GetBin(pt_bin, mass_bin) )
  total_weight_nume += evenmass_pt_nume.GetBinContent( evenmass_pt_nume.GetBin(pt_bin, evenmass_pt_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_pt_deno.GetBinContent( evenmass_pt_deno.GetBin(pt_bin, evenmass_pt_nume.GetNbinsY()+1) )
  fake_numerator_pt.SetBinContent(pt_bin, total_weight_nume)
  fake_denominator_pt.SetBinContent(pt_bin, total_weight_deno)
fake_numerator_pt.Sumw2()
fake_denominator_pt.Sumw2()

fake_numerator_eta = TH1F('fake_nume_eta', 'Number of Numerator Objects, ' + label, evenmass_eta_nume.GetNbinsX(), -5, 5)
fake_numerator_eta.GetXaxis().SetTitle('\eta')
fake_denominator_eta = TH1F('fake_deno_eta', 'Number of Denominator Objects, ' + label, evenmass_eta_deno.GetNbinsX(), -5, 5)
fake_denominator_eta.GetXaxis().SetTitle('\eta')
for eta_bin in range(1, evenmass_eta_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_eta_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_eta_nume.GetBinContent( evenmass_eta_nume.GetBin(eta_bin, mass_bin) )
    total_weight_deno += evenmass_eta_deno.GetBinContent( evenmass_eta_deno.GetBin(eta_bin, mass_bin) )
  total_weight_nume += evenmass_eta_nume.GetBinContent( evenmass_eta_nume.GetBin(eta_bin, evenmass_eta_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_eta_deno.GetBinContent( evenmass_eta_deno.GetBin(eta_bin, evenmass_eta_nume.GetNbinsY()+1) )
  fake_numerator_eta.SetBinContent(eta_bin, total_weight_nume)
  fake_denominator_eta.SetBinContent(eta_bin, total_weight_deno)
fake_numerator_eta.Sumw2()
fake_denominator_eta.Sumw2()

fake_numerator_phi = TH1F('fake_nume_phi', 'Number of Numerator Objects, ' + label, evenmass_phi_nume.GetNbinsX(), -3.15, 3.15)
fake_numerator_phi.GetXaxis().SetTitle('\phi')
fake_denominator_phi = TH1F('fake_deno_phi', 'Number of Denominator Objects, ' + label, evenmass_phi_deno.GetNbinsX(), -3.15, 31.5)
fake_denominator_phi.GetXaxis().SetTitle('\phi')
for phi_bin in range(1, evenmass_phi_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_phi_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_phi_nume.GetBinContent( evenmass_phi_nume.GetBin(phi_bin, mass_bin) )
    total_weight_deno += evenmass_phi_deno.GetBinContent( evenmass_phi_deno.GetBin(phi_bin, mass_bin) )
  total_weight_nume += evenmass_phi_nume.GetBinContent( evenmass_phi_nume.GetBin(phi_bin, evenmass_phi_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_phi_deno.GetBinContent( evenmass_phi_deno.GetBin(phi_bin, evenmass_phi_nume.GetNbinsY()+1) )
  fake_numerator_phi.SetBinContent(phi_bin, total_weight_nume)
  fake_denominator_phi.SetBinContent(phi_bin, total_weight_deno)
fake_numerator_phi.Sumw2()
fake_denominator_phi.Sumw2()

fake_numerator_ecal = TH1F('fake_nume_ecal', 'Number of Numerator Objects, ' + label, evenmass_ecal_nume.GetNbinsX(), 0, 1300)
fake_numerator_ecal.GetXaxis().SetTitle('Photon Energy')
fake_denominator_ecal = TH1F('fake_deno_ecal', 'Number of Denominator Objects, ' + label, evenmass_ecal_deno.GetNbinsX(), 0, 1300)
fake_denominator_ecal.GetXaxis().SetTitle('Photon Energy')
for ecal_bin in range(1, evenmass_ecal_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_ecal_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_ecal_nume.GetBinContent( evenmass_ecal_nume.GetBin(ecal_bin, mass_bin) )
    total_weight_deno += evenmass_ecal_deno.GetBinContent( evenmass_ecal_deno.GetBin(ecal_bin, mass_bin) )
  total_weight_nume += evenmass_ecal_nume.GetBinContent( evenmass_ecal_nume.GetBin(ecal_bin, evenmass_ecal_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_ecal_deno.GetBinContent( evenmass_ecal_deno.GetBin(ecal_bin, evenmass_ecal_nume.GetNbinsY()+1) )
  fake_numerator_ecal.SetBinContent(ecal_bin, total_weight_nume)
  fake_denominator_ecal.SetBinContent(ecal_bin, total_weight_deno)
fake_numerator_ecal.Sumw2()
fake_denominator_ecal.Sumw2()

fake_numerator_hcal = TH1F('fake_nume_hcal', 'Number of Numerator Objects, ' + label, evenmass_hcal_nume.GetNbinsX(), 0, 1300)
fake_numerator_hcal.GetXaxis().SetTitle('Photon Energy')
fake_denominator_hcal = TH1F('fake_deno_hcal', 'Number of Denominator Objects, ' + label, evenmass_hcal_deno.GetNbinsX(), 0, 1300)
fake_denominator_hcal.GetXaxis().SetTitle('Photon Energy')
for hcal_bin in range(1, evenmass_hcal_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_hcal_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_hcal_nume.GetBinContent( evenmass_hcal_nume.GetBin(hcal_bin, mass_bin) )
    total_weight_deno += evenmass_hcal_deno.GetBinContent( evenmass_hcal_deno.GetBin(hcal_bin, mass_bin) )
  total_weight_nume += evenmass_hcal_nume.GetBinContent( evenmass_hcal_nume.GetBin(hcal_bin, evenmass_hcal_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_hcal_deno.GetBinContent( evenmass_hcal_deno.GetBin(hcal_bin, evenmass_hcal_nume.GetNbinsY()+1) )
  fake_numerator_hcal.SetBinContent(hcal_bin, total_weight_nume)
  fake_denominator_hcal.SetBinContent(hcal_bin, total_weight_deno)
fake_numerator_hcal.Sumw2()
fake_denominator_hcal.Sumw2()


fakerate_m0toInf_pt = TH1F('fakerate_m0toInf_pt', 'Fake Rate, ' + label, evenmass_pt_nume.GetNbinsX(), 0, 1300)
fakerate_m0toInf_pt.GetXaxis().SetTitle('p_{T}')
fakerate_m0toInf_pt.SetMaximum(1.0)
for pt_bin in range(1, evenmass_pt_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_pt_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_pt_nume.GetBinContent( evenmass_pt_nume.GetBin(pt_bin, mass_bin) )
    total_weight_deno += evenmass_pt_deno.GetBinContent( evenmass_pt_deno.GetBin(pt_bin, mass_bin) )
  total_weight_nume += evenmass_pt_nume.GetBinContent( evenmass_pt_nume.GetBin(pt_bin, evenmass_pt_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_pt_deno.GetBinContent( evenmass_pt_deno.GetBin(pt_bin, evenmass_pt_nume.GetNbinsY()+1) )
  if not total_weight_deno == 0:
    fakerate_m0toInf_pt.SetBinContent(pt_bin, total_weight_nume / total_weight_deno)
    fakerate_m0toInf_pt.SetBinError(pt_bin, (total_weight_nume / total_weight_deno)*sqrt(1.0/total_weight_nume + 1.0/total_weight_deno))
  else:
    fakerate_m0toInf_pt.SetBinContent(pt_bin, 0)
    #print "filled pt bin", pt_bin, "with zero to avoid divide by zero"
  
fakerate_m0toInf_eta = TH1F('fakerate_m0toInf_eta', 'Fake Rate, ' + label, evenmass_eta_nume.GetNbinsX(), -5, 5)
fakerate_m0toInf_eta.GetXaxis().SetTitle('\eta')
fakerate_m0toInf_eta.SetMaximum(1.0)
for eta_bin in range(1, evenmass_eta_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_eta_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_eta_nume.GetBinContent( evenmass_eta_nume.GetBin(eta_bin, mass_bin) )
    total_weight_deno += evenmass_eta_deno.GetBinContent( evenmass_eta_deno.GetBin(eta_bin, mass_bin) )
  total_weight_nume += evenmass_eta_nume.GetBinContent( evenmass_eta_nume.GetBin(eta_bin, evenmass_eta_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_eta_deno.GetBinContent( evenmass_eta_deno.GetBin(eta_bin, evenmass_eta_nume.GetNbinsY()+1) )
  if not total_weight_deno == 0:
    fakerate_m0toInf_eta.SetBinContent(eta_bin, total_weight_nume / total_weight_deno)
    fakerate_m0toInf_eta.SetBinError(eta_bin, (total_weight_nume / total_weight_deno)*sqrt(1.0/total_weight_nume + 1.0/total_weight_deno))
  else:
    fakerate_m0toInf_eta.SetBinContent(eta_bin, 0)
    #print "filled eta bin", eta_bin, "with zero to avoid divide by zero"
  
fakerate_m0toInf_phi = TH1F('fakerate_m0toInf_phi', 'Fake Rate, ' + label, evenmass_phi_nume.GetNbinsX(), -3.15, 3.15)
fakerate_m0toInf_phi.GetXaxis().SetTitle('\phi')
fakerate_m0toInf_phi.SetMaximum(1.0)
for phi_bin in range(1, evenmass_phi_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_phi_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_phi_nume.GetBinContent( evenmass_phi_nume.GetBin(phi_bin, mass_bin) )
    total_weight_deno += evenmass_phi_deno.GetBinContent( evenmass_phi_deno.GetBin(phi_bin, mass_bin) )
  total_weight_nume += evenmass_phi_nume.GetBinContent( evenmass_phi_nume.GetBin(phi_bin, evenmass_phi_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_phi_deno.GetBinContent( evenmass_phi_deno.GetBin(phi_bin, evenmass_phi_nume.GetNbinsY()+1) )
  if not total_weight_deno == 0:
    fakerate_m0toInf_phi.SetBinContent(phi_bin, total_weight_nume / total_weight_deno)
    fakerate_m0toInf_phi.SetBinError(phi_bin, (total_weight_nume / total_weight_deno)*sqrt(1.0/total_weight_nume + 1.0/total_weight_deno))
  else:
    fakerate_m0toInf_phi.SetBinContent(phi_bin, 0)
    #print "filled phi bin", phi_bin, "with zero to avoid divide by zero"

fakerate_m0toInf_ecal = TH1F('fakerate_m0toInf_ecal', 'Fake Rate, ' + label, evenmass_ecal_nume.GetNbinsX(), 0, 1300)
fakerate_m0toInf_ecal.GetXaxis().SetTitle('Photon Energy')
fakerate_m0toInf_ecal.SetMaximum(1.0)
for ecal_bin in range(1, evenmass_ecal_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_ecal_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_ecal_nume.GetBinContent( evenmass_ecal_nume.GetBin(ecal_bin, mass_bin) )
    total_weight_deno += evenmass_ecal_deno.GetBinContent( evenmass_ecal_deno.GetBin(ecal_bin, mass_bin) )
  total_weight_nume += evenmass_ecal_nume.GetBinContent( evenmass_ecal_nume.GetBin(ecal_bin, evenmass_ecal_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_ecal_deno.GetBinContent( evenmass_ecal_deno.GetBin(ecal_bin, evenmass_ecal_nume.GetNbinsY()+1) )
  if not total_weight_deno == 0 and not total_weight_nume == 0:
    fakerate_m0toInf_ecal.SetBinContent(ecal_bin, total_weight_nume / total_weight_deno)
    fakerate_m0toInf_ecal.SetBinError(ecal_bin, (total_weight_nume / total_weight_deno)*sqrt(1.0/total_weight_nume + 1.0/total_weight_deno))
  else:
    fakerate_m0toInf_ecal.SetBinContent(ecal_bin, 0)
    #print "filled ecal bin", ecal_bin, "with zero to avoid divide by zero"

fakerate_m0toInf_hcal = TH1F('fakerate_m0toInf_hcal', 'Fake Rate, ' + label, evenmass_hcal_nume.GetNbinsX(), 0, 1300)
fakerate_m0toInf_hcal.GetXaxis().SetTitle('Photon Energy')
fakerate_m0toInf_hcal.SetMaximum(1.0)
for hcal_bin in range(1, evenmass_hcal_nume.GetNbinsX()+1):
  total_weight_nume = 0.0
  total_weight_deno = 0.0
  for mass_bin in range(1, evenmass_hcal_nume.GetNbinsY()+1):
    total_weight_nume += evenmass_hcal_nume.GetBinContent( evenmass_hcal_nume.GetBin(hcal_bin, mass_bin) )
    total_weight_deno += evenmass_hcal_deno.GetBinContent( evenmass_hcal_deno.GetBin(hcal_bin, mass_bin) )
  total_weight_nume += evenmass_hcal_nume.GetBinContent( evenmass_hcal_nume.GetBin(hcal_bin, evenmass_hcal_nume.GetNbinsY()+1) )
  total_weight_deno += evenmass_hcal_deno.GetBinContent( evenmass_hcal_deno.GetBin(hcal_bin, evenmass_hcal_nume.GetNbinsY()+1) )
  if not total_weight_deno == 0 and not total_weight_nume == 0:
    fakerate_m0toInf_hcal.SetBinContent(hcal_bin, total_weight_nume / total_weight_deno)
    fakerate_m0toInf_hcal.SetBinError(hcal_bin, (total_weight_nume / total_weight_deno)*sqrt(1.0/total_weight_nume + 1.0/total_weight_deno))
  else:
    fakerate_m0toInf_hcal.SetBinContent(hcal_bin, 0)
    #print "filled hcal bin", hcal_bin, "with zero to avoid divide by zero"

# profile histograms

mass_even_windows = [(0,400), (400,600), (600,800), (800,1000), (1000,1200), (1200,1400), (1400,1600), (1600,1800), (1800,2000), (2000,'Inf')]
mass_odd_windows = [(0,300), (300,500), (500,700), (700,900), (900,1100), (1100,1300), (1300,1500), (1500,1700), (1700,1900), (1900,'Inf')]

profile_histos_pt = []

count = 1
for window in mass_even_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_pt', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', evenmass_pt_nume.GetNbinsX(), 0, 1300)
  profile_histos_pt.append(new_histo)
  new_histo.GetXaxis().SetTitle('p_{T}')
  new_histo.SetMaximum(1.0)
  for pt_bin in range(1, evenmass_pt_nume.GetNbinsX()+1):
    weight_nume = evenmass_pt_nume.GetBinContent( evenmass_pt_nume.GetBin(pt_bin, count) )
    weight_deno = evenmass_pt_deno.GetBinContent( evenmass_pt_deno.GetBin(pt_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(pt_bin, weight_nume / weight_deno)
      new_histo.SetBinError(pt_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(pt_bin, 0)
      #print "filled pt bin", pt_bin, "with zero to avoid divide by zero"
  count += 1
  
count = 1
for window in mass_odd_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_pt', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', oddmass_pt_nume.GetNbinsX(), 0, 1300)
  profile_histos_pt.append(new_histo)
  new_histo.GetXaxis().SetTitle('p_{T}')
  new_histo.SetMaximum(1.0)
  for pt_bin in range(1, oddmass_pt_nume.GetNbinsX()+1):
    weight_nume = oddmass_pt_nume.GetBinContent( oddmass_pt_nume.GetBin(pt_bin, count) )
    weight_deno = oddmass_pt_deno.GetBinContent( oddmass_pt_deno.GetBin(pt_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(pt_bin, weight_nume / weight_deno)
      new_histo.SetBinError(pt_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(pt_bin, 0)
      #print "filled pt bin", pt_bin, "with zero to avoid divide by zero"
  count += 1

profile_histos_eta = []

count = 1
for window in mass_even_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_eta', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', evenmass_eta_nume.GetNbinsX(), -5, 5)
  profile_histos_eta.append(new_histo)
  new_histo.GetXaxis().SetTitle('\eta')
  new_histo.SetMaximum(1.0)
  for eta_bin in range(1, evenmass_eta_nume.GetNbinsX()+1):
    weight_nume = evenmass_eta_nume.GetBinContent( evenmass_eta_nume.GetBin(eta_bin, count) )
    weight_deno = evenmass_eta_deno.GetBinContent( evenmass_eta_deno.GetBin(eta_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(eta_bin, weight_nume / weight_deno)
      new_histo.SetBinError(eta_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(eta_bin, 0)
      #print "filled eta bin", eta_bin, "with zero to avoid divide by zero"
  count += 1

count = 1
for window in mass_odd_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_eta', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', oddmass_eta_nume.GetNbinsX(), -5, 5)
  profile_histos_eta.append(new_histo)
  new_histo.GetXaxis().SetTitle('\eta')
  new_histo.SetMaximum(1.0)
  for eta_bin in range(1, oddmass_eta_nume.GetNbinsX()+1):
    weight_nume = oddmass_eta_nume.GetBinContent( oddmass_eta_nume.GetBin(eta_bin, count) )
    weight_deno = oddmass_eta_deno.GetBinContent( oddmass_eta_deno.GetBin(eta_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(eta_bin, weight_nume / weight_deno)
      new_histo.SetBinError(eta_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(eta_bin, 0)
      #print "filled eta bin", eta_bin, "with zero to avoid divide by zero"
  count += 1

profile_histos_phi = []

count = 1
for window in mass_even_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_phi', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', evenmass_phi_nume.GetNbinsX(), -3.15, 3.15)
  profile_histos_phi.append(new_histo)
  new_histo.GetXaxis().SetTitle('\phi')
  new_histo.SetMaximum(1.0)
  for phi_bin in range(1, evenmass_phi_nume.GetNbinsX()+1):
    weight_nume = evenmass_phi_nume.GetBinContent( evenmass_phi_nume.GetBin(phi_bin, count) )
    weight_deno = evenmass_phi_deno.GetBinContent( evenmass_phi_deno.GetBin(phi_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(phi_bin, weight_nume / weight_deno)
      new_histo.SetBinError(phi_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(phi_bin, 0)
      #print "filled phi bin", phi_bin, "with zero to avoid divide by zero"
  count += 1

count = 1
for window in mass_odd_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_phi', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', oddmass_phi_nume.GetNbinsX(), -3.15, 3.15)
  profile_histos_phi.append(new_histo)
  new_histo.GetXaxis().SetTitle('\phi')
  new_histo.SetMaximum(1.0)
  for phi_bin in range(1, oddmass_phi_nume.GetNbinsX()+1):
    weight_nume = oddmass_phi_nume.GetBinContent( oddmass_phi_nume.GetBin(phi_bin, count) )
    weight_deno = oddmass_phi_deno.GetBinContent( oddmass_phi_deno.GetBin(phi_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(phi_bin, weight_nume / weight_deno)
      new_histo.SetBinError(phi_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(phi_bin, 0)
      #print "filled phi bin", phi_bin, "with zero to avoid divide by zero"
  count += 1

profile_histos_ecal = []

count = 1
for window in mass_even_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_ecal', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', evenmass_ecal_nume.GetNbinsX(), 0, 1300)
  profile_histos_ecal.append(new_histo)
  new_histo.GetXaxis().SetTitle('Photon Energy')
  new_histo.SetMaximum(1.0)
  for ecal_bin in range(1, evenmass_ecal_nume.GetNbinsX()+1):
    weight_nume = evenmass_ecal_nume.GetBinContent( evenmass_ecal_nume.GetBin(ecal_bin, count) )
    weight_deno = evenmass_ecal_deno.GetBinContent( evenmass_ecal_deno.GetBin(ecal_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(ecal_bin, weight_nume / weight_deno)
      new_histo.SetBinError(ecal_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(ecal_bin, 0)
      #print "filled ecal bin", ecal_bin, "with zero to avoid divide by zero"
  count += 1
  
count = 1
for window in mass_odd_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_ecal', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', oddmass_ecal_nume.GetNbinsX(), 0, 1300)
  profile_histos_ecal.append(new_histo)
  new_histo.GetXaxis().SetTitle('Photon Energy')
  new_histo.SetMaximum(1.0)
  for ecal_bin in range(1, oddmass_ecal_nume.GetNbinsX()+1):
    weight_nume = oddmass_ecal_nume.GetBinContent( oddmass_ecal_nume.GetBin(ecal_bin, count) )
    weight_deno = oddmass_ecal_deno.GetBinContent( oddmass_ecal_deno.GetBin(ecal_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(ecal_bin, weight_nume / weight_deno)
      new_histo.SetBinError(ecal_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(ecal_bin, 0)
      #print "filled ecal bin", ecal_bin, "with zero to avoid divide by zero"
  count += 1

profile_histos_hcal = []

count = 1
for window in mass_even_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_hcal', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', evenmass_hcal_nume.GetNbinsX(), 0, 1300)
  profile_histos_hcal.append(new_histo)
  new_histo.GetXaxis().SetTitle('Photon Energy')
  new_histo.SetMaximum(1.0)
  for hcal_bin in range(1, evenmass_hcal_nume.GetNbinsX()+1):
    weight_nume = evenmass_hcal_nume.GetBinContent( evenmass_hcal_nume.GetBin(hcal_bin, count) )
    weight_deno = evenmass_hcal_deno.GetBinContent( evenmass_hcal_deno.GetBin(hcal_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(hcal_bin, weight_nume / weight_deno)
      new_histo.SetBinError(hcal_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(hcal_bin, 0)
      #print "filled hcal bin", hcal_bin, "with zero to avoid divide by zero"
  count += 1
  
count = 1
for window in mass_odd_windows:
  new_histo = TH1F('fakerate_m'+str(window[0])+'to'+str(window[1])+'_hcal', 'Fake Rate '+str(window[0])+' to '+str(window[1])+'', oddmass_hcal_nume.GetNbinsX(), 0, 1300)
  profile_histos_hcal.append(new_histo)
  new_histo.GetXaxis().SetTitle('Photon Energy')
  new_histo.SetMaximum(1.0)
  for hcal_bin in range(1, oddmass_hcal_nume.GetNbinsX()+1):
    weight_nume = oddmass_hcal_nume.GetBinContent( oddmass_hcal_nume.GetBin(hcal_bin, count) )
    weight_deno = oddmass_hcal_deno.GetBinContent( oddmass_hcal_deno.GetBin(hcal_bin, count) )
    if not weight_deno == 0 and not weight_nume == 0:
      new_histo.SetBinContent(hcal_bin, weight_nume / weight_deno)
      new_histo.SetBinError(hcal_bin, (weight_nume / weight_deno)*sqrt(1.0/weight_nume + 1.0/weight_deno))
    else:
      new_histo.SetBinContent(hcal_bin, 0)
      #print "filled hcal bin", hcal_bin, "with zero to avoid divide by zero"
  count += 1

savefile.Write()
