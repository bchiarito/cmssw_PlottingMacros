import os
import glob
import fnmatch
import sys
import time
import subprocess
import cross_sections as xs

# help message
from optparse import OptionParser
usage = "python %prog <path_to_run> -n [N] -f [string]\n\n<path_to_run> should be the /store/user/ path (ending in '/') to the highest level of the run, whose contents will be directories: BKG, DY, DATA, and QCD.\nThe program will find the .tar.gz log files, extract them, and search the output for a printed cutflow, and it will aggregate the results accorss a whole dataset. The results are dumped to stdout."
parser = OptionParser(usage=usage)
parser.add_option('-n', '--num', type='int', action='store', default=18, dest='num', help='the number of lines in the cutflow')
parser.add_option('--lumi', type='float', action='store', default=37196.0, dest='lumi', help='integrated luminosity of data in pb^-1')
parser.add_option('-f', '--flag', type='string', action='store', default='ran filter', dest='flag', help='the string in the output signifying that the cutflow is being printed next')
parser.add_option('--check', action='store_true', default=False, dest='check', help='instead of a full run, just print one example cutflow found in the logs')
parser.add_option('--debug', action='store_true', default=False, dest='debug', help='print messages while traversing the directory')
(options, args) = parser.parse_args()

# globals
prefix = "root://cmsxrootd.fnal.gov//"

# classes
class Dataset:
  pass

class CutflowCollection:

  def __init__(self, initial_path, num, flag, lumi): # external
    self.datasets = []
    self.lumi = lumi
    self.num = num;
    self.flag = flag
    self.store_user_base = initial_path
    self.names = {}
    self.extracted_names = False
  
  def add_dataset(self, name, locations, group="", xs=1.0, ngen=1.0): # external
    new_dataset = Dataset()
    new_dataset.name = name
    new_dataset.locations = locations
    new_dataset.logs = []
    new_dataset.xs = float(xs)
    new_dataset.ngen = float(ngen)
    new_dataset.group = group
    self.datasets.append(new_dataset)

  def traverse_for_log_commands(self, debug=False): # external
    for dataset in self.datasets:
      logs = []
      for i,location in enumerate(dataset.locations):
        print "getting listing for", self.store_user_base + location
        listing = subprocess.check_output(["eos", "root://cmseos.fnal.gov", "find", self.store_user_base + location])
        listing = listing.split('\n')
        for entry in listing:
          parsed_path = (entry[11:len(entry)]).split('/')
          if 'failed' in parsed_path: continue
          rootfilename = fnmatch.filter(parsed_path, '*.tar.gz')
          if not rootfilename == []:
            master = (self.store_user_base + location).split('/')
            list_path_to_file = [chunk for chunk in parsed_path if chunk not in master]
            path_to_file = ""
            for chunk in list_path_to_file:
              path_to_file += '/' + chunk
            destination = "./location" + str(i) + "_" + rootfilename[0]
            command = 'xrdcp --nopbar ' + prefix + self.store_user_base + location + path_to_file + " " + destination
            #command = 'xrdcp ' + prefix + self.store_user_base + location + path_to_file + " " + destination
            filename = destination[2:len(destination)]
            basefilename = rootfilename[0]
            num = basefilename[basefilename.find('_')+1:basefilename.find('.')]
            entry = (command, num, filename)
            logs.append(entry)
            if options.check: break
      dataset.logs = logs

  def compute_cutflows(self, debug=False): # external
   for dataset in self.datasets:
      print "computing cutflow for", dataset.name
      dataset.cutflow = {}
      for i in range(self.num):
        dataset.cutflow[i] = 0
      for copy_command, num, tarball_filename in dataset.logs:
        #print "*** doing next"
        #print "*** copy_command", copy_command
        #print "*** num", num
        #print "*** tarball_filename", tarball_filename
        os.system(copy_command)
        #print "*** done copying, now untar"
        extract_command = "tar -xzf " + tarball_filename
        #print "*** extract_command", extract_command
        os.system(extract_command)
        #print "*** done extracting"
        stdout_filename = "cmsRun-stdout-" + num + ".log"
        stderr_filename = "cmsRun-stderr-" + num + ".log"
        framwk_filename = "FrameworkJobReport-" + num + ".xml"
        if debug: print stdout_filename
        stdout = open(stdout_filename,'r')
        record = False
        count = 0
        if not self.extracted_names:
          will_extract_names_this_file = True
        for line in stdout:
          if record:
            #print line
            l = line.split()
            if not self.extracted_names:
              # then we should take the chance to get names from this file
              self.names[count] = l[0]
            dataset.cutflow[count] = dataset.cutflow[count] + int(l[1])
            count = count + 1
          if count == self.num:
            record = False
          if line.strip()[0:len(self.flag)] == self.flag:
            record = True
        if will_extract_names_this_file: self.extracted_names = True
        os.system("rm " + stdout_filename)
        os.system("rm " + stderr_filename)
        os.system("rm " + framwk_filename)
        os.system("rm " + tarball_filename)
        #raw_input()
        #print ""

  def print_datasets(self): # external
    for dataset in self.datasets:
      print dataset.name, len(dataset.logs), 'logs |', "group = ", dataset.group, "| xs, ngen = ", dataset.xs, dataset.ngen
      if options.debug:
        for command in dataset.logs:
          print command

  def print_cutflows(self): # external
    print "--- printing cutflows ---"
    for dataset in self.datasets:
      print dataset.name
      # this block specific to my cutflows #
      total = dataset.cutflow[0]
      total_pass = dataset.cutflow[9]
      total_reco_trigger = dataset.cutflow[3]
      ###
      for index in dataset.cutflow:
        eff = 0
        if index == 0: eff = 0
        if index >= 1 and index <= 9 and not total == 0: eff = dataset.cutflow[index]/float(total)
        if index >= 10 and index <= 16 and not dataset.cutflow[index] == 0: eff = float(total_pass)/dataset.cutflow[index]
        if index == 17 and not total_reco_trigger == 0: eff = dataset.cutflow[index]/float(total_reco_trigger)
        print "{0:<30} {1:<20,.0f} {2:<10.2%}".format(self.names[index], dataset.cutflow[index], eff)
      print ""

  def print_summary(self): # external
    print "--- printing summary ---"
    groups = {}
    for dataset in self.datasets:
      if not groups.has_key(dataset.group):
        groups[dataset.group] = 0
      scaled_passing_preselection = dataset.cutflow[9] * self.lumi * dataset.xs / dataset.ngen
      groups[dataset.group] += scaled_passing_preselection
    for group in groups:
      print "Group", group, "total yield {:,.1f}".format(groups[group])
    print ""

# main
time_start = time.time()
mycutflows = CutflowCollection(args[0], options.num, options.flag, options.lumi)
mycutflows.add_dataset('ttbar', ['BKG/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'], 'BKG', xs.ttbar, xs.ttbar_ngen)
if options.check:
  mycutflows.traverse_for_log_commands(options.debug)
  mycutflows.compute_cutflows(options.debug)
  mycutflows.print_cutflows()
  sys.exit()
mycutflows.add_dataset('antitop', ['BKG/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1'], 'BKG', xs.top, xs.top_ngen)
mycutflows.add_dataset('top', ['BKG/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1'], 'BKG', xs.top, xs.top_ngen)
mycutflows.add_dataset('tWtop', ['BKG/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1'], 'BKG', xs.tW, xs.tW_ngen)
mycutflows.add_dataset('tWantitop', ['BKG/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1'], 'BKG', xs.tW, xs.tW_ngen)
mycutflows.add_dataset('wjets', ['BKG/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'], 'BKG', xs.wjets, xs.wjets_ngen)
mycutflows.add_dataset('w1jets', ['BKG/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'], 'BKG', xs.w1jets, xs.w1jets_ngen)
mycutflows.add_dataset('w2jets', ['BKG/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'], 'BKG', xs.w2jets, xs.w2jets_ngen)
mycutflows.add_dataset('w3jets', ['BKG/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'], 'BKG', xs.w3jets, xs.w3jets_ngen)
mycutflows.add_dataset('w4jets', ['BKG/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'], 'BKG', xs.w4jets, xs.w4jets_ngen)
mycutflows.add_dataset('ww', ['BKG/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8'], 'BKG', xs.ww, xs.ww_ngen)
mycutflows.add_dataset('wz1l2q', ['BKG/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8'], 'BKG', xs.wz1l2q, xs.wz1l2q_ngen)
mycutflows.add_dataset('wz1l3nu', ['BKG/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8'], 'BKG', xs.wz1l3nu, xs.wz1l3nu_ngen)
mycutflows.add_dataset('dysig', ['DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext1_signal',
                                 'DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext2_signal'], 'DY' , xs.dy, xs.dy_ngen)
mycutflows.add_dataset('dybkg', ['DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext1_bkg',
                                 'DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext2_bkg'], 'BKG', xs.dy, xs.dy_ngen)
mycutflows.add_dataset('dy10sig', ['DY/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_10to50_signal'], 'DY', xs.dy10, xs.dy10_ngen)
mycutflows.add_dataset('dy10bkg', ['DY/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_10to50_bkg'], 'BKG', xs.dy10, xs.dy10_ngen)
mycutflows.add_dataset('qcd15to30', ['QCD/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd15to30, xs.qcd15to30_ngen)
mycutflows.add_dataset('qcd30to50', ['QCD/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd30to50, xs.qcd30to50_ngen)
mycutflows.add_dataset('qcd50to80', ['QCD/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd50to80, xs.qcd50to80_ngen)
mycutflows.add_dataset('qcd80to120', ['QCD/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd80to120, xs.qcd80to120_ngen)
mycutflows.add_dataset('qcd120to170', ['QCD/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd120to170, xs.qcd120to170_ngen)
mycutflows.add_dataset('qcd170to300', ['QCD/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd170to300, xs.qcd170to300_ngen)
mycutflows.add_dataset('qcd300to470', ['QCD/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd300to470, xs.qcd300to470_ngen)
mycutflows.add_dataset('qcd470to600', ['QCD/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd470to600, xs.qcd470to600_ngen)
mycutflows.add_dataset('qcd600to800', ['QCD/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd600to800, xs.qcd600to800_ngen)
mycutflows.add_dataset('qcd800to1000', ['QCD/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd800to1000, xs.qcd800to1000_ngen)
mycutflows.add_dataset('qcd1000to1400', ['QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd1000to1400, xs.qcd1000to1400_ngen)
mycutflows.add_dataset('qcd1400to1800', ['QCD/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd1400to1800, xs.qcd1400to1800_ngen)
mycutflows.add_dataset('qcd1800to2400', ['QCD/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd1800to2400, xs.qcd1800to2400_ngen)
mycutflows.add_dataset('qcd2400to3200', ['QCD/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8'], 'QCD', xs.qcd2400to3200, xs.qcd2400to3200_ngen)
mycutflows.add_dataset('data', ['DATA/SingleMuon/RunB_ver2', 'DATA/SingleMuon/RunC', 'DATA/SingleMuon/RunD', 'DATA/SingleMuon/RunE',
                                'DATA/SingleMuon/RunF', 'DATA/SingleMuon/RunG', 'DATA/SingleMuon/RunH'], 'DATA', 1.0, options.lumi)

mycutflows.traverse_for_log_commands(options.debug)
time_middle = time.time()
print "getting logs took {:.2f} minutes".format((time_middle - time_start)/60.0)
mycutflows.print_datasets()
mycutflows.compute_cutflows(options.debug)
mycutflows.print_cutflows()
mycutflows.print_summary()
time_end = time.time()
print "computing cutflows took {:.2f} minutes".format((time_end - time_middle)/60.0)
print "overall took {:.2f} minutes".format((time_end - time_start)/60.0)
