import sys
import os
import fnmatch
import subprocess

# usage:
# python <script.py> /eos/uscms/store/user/bchiari1/twoprong/ztagandprobe/Nov29_trees/regpre/

def get_commands(dataset_paths):
  commands = []
  for i,dataset_path in enumerate(dataset_paths):
    print "getting listing for", store_user_base + dataset_path
    listing = subprocess.check_output(["eos", "root://cmseos.fnal.gov", "find", store_user_base + dataset_path])
    listing = listing.split('\n')
    for entry in listing:
      parsed_path = (entry[11:len(entry)]).split('/')
      if 'failed' in parsed_path: continue
      rootfilename = fnmatch.filter(parsed_path, '*.root')
      if not rootfilename == []:
        master = (store_user_base + dataset_path).split('/')
        list_path_to_file = [chunk for chunk in parsed_path if chunk not in master]
        path_to_file = ""
        for chunk in list_path_to_file:
          path_to_file += '/' + chunk
        destination = "./location" + str(i) + "_" + rootfilename[0]
        command = 'xrdcp --nopbar ' + prefix + store_user_base + dataset_path + path_to_file + " " + destination
        commands.append(command)
  return commands

def add_to_dict(fi, tag, paths):
  commands = get_commands(paths)
  for command in commands:
    fi.write(tag + ":::" + command + "\n")

# setup  
prefix = "root://cmsxrootd.fnal.gov//"
base_path = sys.argv[1]
store_user_base = base_path[11:len(base_path)]

# generate dictionary file
dict_file = open('xrdcp_dict.txt', 'w')
tag = "TT"
end_paths = ["BKG/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"]
add_to_dict(dict_file, tag, end_paths)
tag = "STtop"
end_paths = ["BKG/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1"]
add_to_dict(dict_file, tag, end_paths)
tag = "STantitop"
end_paths = ["BKG/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1"]
add_to_dict(dict_file, tag, end_paths)
tag = "tWtop"
end_paths = ["BKG/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
             "BKG/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1"]
add_to_dict(dict_file, tag, end_paths)
tag = "WJets"
end_paths = ["BKG/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer",
             "BKG/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer_ext2"]
add_to_dict(dict_file, tag, end_paths)
tag = "W1Jets"
end_paths = ["BKG/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"]
add_to_dict(dict_file, tag, end_paths)
tag = "W2Jets"
end_paths = ["BKG/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer"]#,
#             "BKG/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "W3Jets"
end_paths = ["BKG/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer",
             "BKG/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "W4Jets"
end_paths = ["BKG/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer",
             "BKG/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer_ext1",
             "BKG/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/twoprongntuplizer_ext2"]
add_to_dict(dict_file, tag, end_paths)
tag = "WW"
end_paths = ["BKG/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8"]
add_to_dict(dict_file, tag, end_paths)
tag = "WZ1L"
end_paths = ["BKG/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8"]
add_to_dict(dict_file, tag, end_paths)
tag = "WZ3Nu"
end_paths = ["BKG/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/twoprongntuplizer",
             "BKG/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/twoprongntuplizer_ext1"]
add_to_dict(dict_file, tag, end_paths)

tag = "DYsig"
dataset_paths = ["DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext1_signal",
                 "DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext2_signal"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY10sig"
dataset_paths = ["DY/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_10to50_bkg"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY10bkg"
dataset_paths= ["DY/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_10to50_signal"]
add_to_dict(dict_file, tag, end_paths)
tag = "DYbkg"
end_paths = ["DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext1_bkg",
             "DY/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY_50_ext2_bkg"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY1sig"
end_paths = ["DY/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY1_50_signal"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY2sig"
end_paths = ["DY/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY2_50_signal"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY3sig"
end_paths = ["DY/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY3_50_signal"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY4sig"
end_paths = ["DY/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY4_50_signal"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY1bkg"
end_paths = ["DY/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY1_50_bkg"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY2bkg"
end_paths = ["DY/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY2_50_bkg"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY3bkg"
end_paths = ["DY/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY3_50_bkg"]
add_to_dict(dict_file, tag, end_paths)
tag = "DY4bkg"
end_paths = ["DY/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/DY4_50_bkg"]
add_to_dict(dict_file, tag, end_paths)

tag = "DATA"
end_paths = ["DATA/SingleMuon/RunB_ver2", "DATA/SingleMuon/RunC", "DATA/SingleMuon/RunD", "DATA/SingleMuon/RunE", "DATA/SingleMuon/RunF", "DATA/SingleMuon/RunG", "DATA/SingleMuon/RunH"]
add_to_dict(dict_file, tag, end_paths)

tag = "QCD_1000to1400"
end_paths = ["QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_120to170"
end_paths = ["QCD/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_1400to1800"
end_paths = ["QCD/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_15to30"
end_paths = ["QCD/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_170to300"
end_paths = ["QCD/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_1800to2400"
end_paths = ["QCD/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_2400to3200"
end_paths = ["QCD/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_300to470"
end_paths = ["QCD/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_30to50"
end_paths = ["QCD/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_470to600"
end_paths = ["QCD/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_50to80"
end_paths = ["QCD/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_600to800"
end_paths = ["QCD/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_800to1000"
end_paths = ["QCD/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/twoprongntuplizer",
             "QCD/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/TauPreSelection_ext1"]
add_to_dict(dict_file, tag, end_paths)
tag = "QCD_80to120"
end_paths = ["QCD/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8"]
add_to_dict(dict_file, tag, end_paths)
