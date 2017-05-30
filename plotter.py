import os
import glob
import fnmatch
import math
import ROOT
import string
from ROOT import *
import sys
import time

from optparse import OptionParser

time_begin = time.time()

parser = OptionParser()

# Variable options
parser.add_option('--var', metavar='F', type='string', action='store',
                  dest='var',
                  help='')
parser.add_option('--varx', metavar='F', type='string', action='store',
                  dest='varx',
                  help='')
parser.add_option('--vary', metavar='F', type='string', action='store',
                  dest='vary',
                  help='')
parser.add_option('--bins', metavar='F', type='string', action='store',
                  default='100,0,100',
                  dest='binning',
                  help='')
parser.add_option('--binx', metavar='F', type='string', action='store',
                  default='100,0,100',
                  dest='binningx',
                  help='')
parser.add_option('--biny', metavar='F', type='string', action='store',
                  default='100,0,100',
                  dest='binningy',
                  help='')
parser.add_option('--cut', metavar='F', type='string', action='store',
                  default='',
                  dest='cut',
                  help='')

# Input files options
parser.add_option('--sample', metavar='F', type='string', action='store',
                  dest='sample1',
                  help='')
parser.add_option('--sample1', metavar='F', type='string', action='store',
                  default='',
                  dest='sample1',
                  help='')
parser.add_option('--sample2', metavar='F', type='string', action='store',
                  default='',
                  dest='sample2',
                  help='')
parser.add_option('--sample3', metavar='F', type='string', action='store',
                  default='',
                  dest='sample3',
                  help='')
parser.add_option('--sample4', metavar='F', type='string', action='store',
                  default='',
                  dest='sample4',
                  help='')
parser.add_option('--sample5', metavar='F', type='string', action='store',
                  default='',
                  dest='sample5',
                  help='')
parser.add_option('--tree', metavar='F', type='string', action='store',
                  dest='treename1',
                  help='full path of TTree object in each file')
parser.add_option('--tree1', metavar='F', type='string', action='store',
  	      	      default = 'diphotonAnalyzer/fTree2',
                  dest='treename1',
                  help='full path of TTree object in each file')
parser.add_option('--tree2', metavar='F', type='string', action='store',
  	      	      default = 'diphotonAnalyzer/fTree2',
                  dest='treename2',
                  help='full path of TTree object in each file')
parser.add_option('--tree3', metavar='F', type='string', action='store',
  	      	      default = 'diphotonAnalyzer/fTree2',
                  dest='treename3',
                  help='full path of TTree object in each file')
parser.add_option('--tree4', metavar='F', type='string', action='store',
  	      	      default = 'diphotonAnalyzer/fTree2',
                  dest='treename4',
                  help='full path of TTree object in each file')
parser.add_option('--tree5', metavar='F', type='string', action='store',
  	      	      default = 'diphotonAnalyzer/fTree2',
                  dest='treename5',
                  help='full path of TTree object in each file')

# Labeling and Titles
parser.add_option('--title', metavar='F', type='string', action='store',
	    	          default = '',
                  dest='title',
                  help='Title of histogram in canvas')
parser.add_option('--xaxis', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='xaxis',
                  help='xaxis label')
parser.add_option('--leg', metavar='F', type='string', action='store',
                  dest='legend1',
                  help='legend entry label')
parser.add_option('--leg1', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend1',
                  help='legend entry label')
parser.add_option('--leg2', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend2',
                  help='legend entry label')
parser.add_option('--leg3', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend3',
                  help='legend entry label')
parser.add_option('--leg4', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend4',
                  help='legend entry label')
parser.add_option('--leg5', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='legend5',
                  help='legend entry label')

# Math Options
parser.add_option('--logy', action='store_true', default=False,
                  dest='logy',
                  help='logy sacle on y')
parser.add_option('--logx', action='store_true', default=False,
                  dest='logx',
                  help='logx sacle on x')
parser.add_option('--scaled', action='store_true', default=False,
                  dest='scale',
                  help='scale to integral = 100')
parser.add_option('--lumi', type='float', action='store',
  	      	      default = -1.0,
                  dest='lumi',
                  help='luminosity to scale to, if changed from default value')
parser.add_option('--errors', action='store_true', default=False,
                  dest='errors',
                  help='calls Sumw2() on all histograms')
parser.add_option('--error1', action='store_true', default=False,
                  dest='error1',
                  help='calls Sumw2() on sample 1')
parser.add_option('--error2', action='store_true', default=False,
                  dest='error2',
                  help='calls Sumw2() on sample 2')
parser.add_option('--error3', action='store_true', default=False,
                  dest='error3',
                  help='calls Sumw2() on sample 3')
parser.add_option('--error4', action='store_true', default=False,
                  dest='error4',
                  help='calls Sumw2() on sample 4')
parser.add_option('--error5', action='store_true', default=False,
                  dest='error5',
                  help='calls Sumw2() on sample 5')

# visual Apperance
parser.add_option('--legoff', action='store_true', default=False,
                  dest='legoff',
                  help='Turns off legend')
parser.add_option('--color', metavar='F', type='string', action='store',
                  dest='color1',
                  help='color string (kRed, kTeal, etc)')
parser.add_option('--color1', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='color1',
                  help='color string (kRed, kTeal, etc)')
parser.add_option('--color2', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='color2',
                  help='color string (kRed, kTeal, etc)')
parser.add_option('--color3', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='color3',
                  help='color string (kRed, kTeal, etc)')
parser.add_option('--color4', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='color4',
                  help='color string (kRed, kTeal, etc)')
parser.add_option('--color5', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='color5',
                  help='color string (kRed, kTeal, etc)')
parser.add_option('--data_style ', metavar='F', type='string', action='store',
  	      	      default = '',
                  dest='color5',
                  help='color string (kRed, kTeal, etc)')

# Other options
parser.add_option('--twoD', action='store_true', default=False,
                  dest='twoD',
                  help='make 2d plot')
parser.add_option('--noplot', action='store_true', default=False,
                  dest='noplot',
                  help='Do not plot anything')
parser.add_option('--quiet', action='store_true', default=False,
                  dest='quiet',
                  help='less output')
parser.add_option('-n', '--num', type='int', action='store',
                  default=-1,
                  dest='nentries',
                  help='max number of entries to draw from files')
# Saving
parser.add_option('--save', action='store_true', default=False,
                  dest='save',
                  help='save plot')
parser.add_option('--name', metavar='F', type='string', action='store',
    	    	      default = "plot",
                  dest='name',
                  help='name of file when saving')


(options, args) = parser.parse_args()

def rootcolor(color_string):
  if color_string == "Red":
    return ROOT.kRed
  elif color_string == "Blue":
    return ROOT.kBlue
  elif color_string == "Teal":
    return ROOT.kTeal
  elif color_string == "Orange":
    return ROOT.kOrange
  elif color_string == "Black":
    return ROOT.kBlack
  elif color_string == "Pink":
    return ROOT.kPink
  elif color_string == "Cyan":
    return ROOT.kCyan
  elif color_string == "Yellow":
    return ROOT.kYellow
  elif color_string == "Magenta":
    return ROOT.kMagenta
  elif color_string == "Azure":
    return ROOT.kAzure
  elif color_string == "Green":
    return ROOT.kGreen
  elif color_string == "Spring":
    return ROOT.kSpring
  elif color_string == "Gray":
    return ROOT.kGray
  elif color_string == "White":
    return ROOT.kWhite

if not options.quiet:
  print "Begin."

multiple_samples = (not options.sample2 == "") or \
                   (not options.sample3 == "")

samples = []
if not options.sample1 == "":
  sample = {}
  sample['path'] = options.sample1
  sample['tree'] = options.treename1
  sample['label'] = options.legend1
  sample['error'] = options.error1
  if options.color1 == "":
    sample['color'] = ""
  else:
    sample['color'] = rootcolor(options.color1)
  samples.append(sample)
if not options.sample2 == "":
  sample = {}
  sample['path'] = options.sample2
  sample['tree'] = options.treename2
  sample['label'] = options.legend2
  sample['error'] = options.error2
  if options.color1 == "":
    sample['color'] = ""
  else:
    sample['color'] = rootcolor(options.color2)
  samples.append(sample)
if not options.sample3 == "":
  sample = {}
  sample['path'] = options.sample3
  sample['tree'] = options.treename3
  sample['label'] = options.legend3
  sample['error'] = options.error3
  if options.color1 == "":
    sample['color'] = ""
  else:
    sample['color'] = rootcolor(options.color3)
  samples.append(sample)
if not options.sample4 == "":
  sample = {}
  sample['path'] = options.sample4
  sample['tree'] = options.treename4
  sample['label'] = options.legend4
  sample['error'] = options.error4
  if options.color1 == "":
    sample['color'] = ""
  else:
    sample['color'] = rootcolor(options.color4)
  samples.append(sample)
if not options.sample5 == "":
  sample = {}
  sample['path'] = options.sample5
  sample['tree'] = options.treename5
  sample['label'] = options.legend5
  sample['error'] = options.error5
  if options.color1 == "":
    sample['color'] = ""
  else:
    sample['color'] = rootcolor(options.color5)
  samples.append(sample)
if len(samples) == 0:
  print "Must specify at least one sample with --sample"
  sys.exit

# Make collection of TChains
for sample in samples:
  path = sample['path']
  ISrootfile = False
  ISdirectory = False
  ISinputfile = False
  if fnmatch.fnmatch(path, "*.root"):
    if not options.quiet:
      print "It appears ", path, "is a rootfile"
    ISrootfile = True
  if fnmatch.fnmatch(path, "*/"):
    if not options.quiet:
      print "It appears", path, "is a directory to traverse"
    ISdirectory = True
  if fnmatch.fnmatch(path, "*.txt"):
    if not options.quiet:
      print "It appears", path, "is a text file of inputs"
    ISinputfile = True

  if ISrootfile:
    chain = ROOT.TChain(sample['tree'])
    chain.Add(path)
    sample['entries'] = [[chain, 1, 1]]

  if ISdirectory:
    chain = ROOT.TChain(sample['tree'])
    rootfiles = []
    for root, dirnames, filenames in os.walk(path):
      for filename in fnmatch.filter(filenames, '*.root'):
        rootfiles.append(os.path.join(root, filename))
    for rootfile in rootfiles:
      chain.Add(rootfile)
    sample['entries'] = [[chain, 1, 1]]

  if ISinputfile:
    sample['entries'] = []
    inputfile = open(path, 'r')
    for line in inputfile:
      line_list = line.split()
      # Get name, xs, and num from line
      if len(line_list) == 1:
        path_to_file = line_list[0]
        xs = 1
        N = 1
        treename = sample['tree']
      if len(line_list) == 3:
        path_to_file = line_list[0]
        xs = float(line_list[1])
        N = float(line_list[2])
        treename = sample['tree']
      if len(line_list) == 4:
        path_to_file = line_list[0]
        xs = float(line_list[1])
        N = float(line_list[2])
        treename = line_list[3]
      if len(line_list) == 2 or len(line_list) == 0 or len(line_list) > 4:
        print "couldn't parse line from input file", path
        continue
      # add files to chain
      chain = ROOT.TChain(treename)      
      if fnmatch.fnmatch(path, "*.root"):
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
        print "couldn't parse line from input file", path
      sample['entries'].append([chain, xs, N])
     
if not options.quiet:
  print "Drawing into histogram..."

i1 = string.index(options.binning,',')
i2 = string.rindex(options.binning,',')
bins = int(options.binning[0:i1])
low = float(options.binning[i1+1:i2])
high = float(options.binning[i2+1:len(options.binning)])

i1x = string.index(options.binningx,',')
i2x = string.rindex(options.binningx,',')
binsx = int(options.binningx[0:i1x])
lowx = float(options.binningx[i1x+1:i2x])
highx = float(options.binningx[i2x+1:len(options.binningx)])

i1y = string.index(options.binningy,',')
i2y = string.rindex(options.binningy,',')
binsy = int(options.binningy[0:i1y])
lowy = float(options.binningy[i1y+1:i2y])
highy = float(options.binningy[i2y+1:len(options.binningy)])

count = 0
sumcount = 0
for sample in samples:
  sumcount += 1
  if not options.twoD:
    hist_sum = ROOT.TH1F(options.name+"_sum_"+str(sumcount), options.name, bins, low, high)
  else:
    hist_sum = ROOT.TH2F(options.name+"_sum_"+str(sumcount), options.name, binsx, lowx, highx, binsy, lowy, highy)
  for entry in sample['entries']:
    chain = entry[0]
    xs = entry[1]
    N = entry[2]
    count += 1
    if not options.twoD:
      hist = ROOT.TH1F(options.name+"_"+str(count), options.name, bins, low, high)
    else:
      hist = ROOT.TH2F(options.name+"_"+str(count), options.name, binsx, lowx, highx, binsy, lowy, highy)
    if options.nentries == -1:
      if not options.twoD:
        chain.Draw(options.var+">>"+options.name+"_"+str(count),""+options.cut, "goff")
      else:
        chain.Draw(options.vary+":"+options.varx+">>"+options.name+"_"+str(count),""+options.cut, "goff")
    else:
      if not options.twoD:
        chain.Draw(options.var+">>"+options.name+"_"+str(count),""+options.cut, "goff", options.nentries)
      else:
        chain.Draw(options.vary+":"+options.varx+">>"+options.name+"_"+str(count),""+options.cut, "goff", options.nentries)
    entry.append(hist)
    hist.Scale(xs/N)
    hist_sum.Add(hist)
  sample['summed_hist'] = hist_sum
  
# Print Summary
print ""
count = 1
for sample in samples:
  hist = sample['summed_hist']
  print "Entries " + str(count) + "   : ", int(hist.GetEntries())
  if not int(hist.GetBinContent(0)) == 0:
    print "Underflow " + str(count) + " - ", int(hist.GetBinContent(0))
  if not int(hist.GetBinContent(bins+1)) == 0:
    print "Overflow " + str(count) + "  - ", int(hist.GetBinContent(bins+1))
  count += 1
print ""
  
if not options.noplot:
  if not options.quiet:
    print "Plotting..."
  c = TCanvas()
  c.cd()
  if options.logy:
    c.SetLogy()
  if options.logx:
    c.SetLogx()
  colorcount = 1
  for sample in samples:
    hist = sample['summed_hist']
    # Stats
    if sample['color'] == "":
      hist.SetLineColor(colorcount)
      hist.SetMarkerColor(colorcount)
      colorcount+=1
    else:
      hist.SetLineColor(sample['color'])
      hist.SetMarkerColor(sample['color'])
    hist.SetFillColor(0)
    hist.SetLineWidth(1)
    hist.SetStats(0)
    # Scale
    if sample['error'] or options.errors:
      hist.Sumw2()
    else:
      hist.SetMarkerSize(1)
      hist.SetMarkerStyle(2)
    if options.scale:
      if not hist.Integral() == 0:
        hist.Scale(100.0/hist.Integral())

  # Maximum
  maximum = 0
  for sample in samples:
    hist = sample['summed_hist']
    maximum = max(maximum, hist.GetMaximum())
  for sample in samples:
    hist = sample['summed_hist']
    if options.logy:
      hist.SetMaximum(maximum*4)
      if not options.scale:
        # set min if log plot and not scaled
        hist.SetMinimum(0.5)
    else:
      hist.SetMaximum(maximum*1.15)
      hist.SetMinimum(0) 

  # Labels
  for sample in samples:
    hist = sample['summed_hist']
    if not options.title == "":
      hist.SetTitle(options.title)
    elif options.name == "plot":
      if not options.twoD:
        hist.SetTitle(options.var)
      else:
        if options.cut == "":
          hist.SetTitle(options.varx + " vs " + options.vary)
        else:
          hist.SetTitle(options.cut)
    else:
      hist.SetTitle(options.name)
    if not options.twoD:
      # X axis
      hist.GetXaxis().SetTitle(options.var + " w/ " + options.cut)
      if options.cut == "":
        hist.GetXaxis().SetTitle(options.var)
      if not options.xaxis == "":
        hist.GetXaxis().SetTitle(options.xaxis)
      # Y axis
      hist.GetYaxis().SetTitle("Events")
      if options.scale:
        hist.GetYaxis().SetTitle("Scaled to Integral 100")
    else:
      # X axis
      hist.GetXaxis().SetTitle(options.varx)
      # Y axis
      hist.GetYaxis().SetTitle(options.vary)
      
  # Draw()
  count = 0
  for sample in samples:
    hist = sample['summed_hist']
    if count == 0:
      draw_option = ''
    else:
      draw_option = 'same'
    if options.twoD:
      draw_option += 'Colz'
    count += 1
    if not (sample['error'] or options.errors):
      draw_option += ''
    hist.Draw(draw_option)

  # Legend
  leg = ROOT.TLegend(0.55, 0.80, 0.9, 0.9)
  for sample in samples:
    hist = sample['summed_hist']
    if sample['label'] == "":
      leg.AddEntry(hist, sample['path'], "l")
    else:
      leg.AddEntry(hist, sample['label'], "l")  
  if not options.legoff:
    leg.Draw("same")
  # Save
  if options.save == True:
    c.SaveAs(options.name + ".png")

if not options.quiet:
  print "Done."

time_end = time.time()

print "Elapsed Time: ", (time_end - time_begin)

# After plot Commands
if (not options.save) and (not options.noplot):
  hist = samples[0]['summed_hist']
  cmd = "start"
  while not cmd == "":
    print "\nPress [Enter] to finish, type 'options' to see options"
    # parse input
    inp = raw_input()
    i = string.find(inp,' ')
    if i==-1:
      cmd = inp
      opt = ""
    else:
      cmd = inp[0:i]
      opt = inp[i+1:len(inp)]
    # begin commands
    if cmd == "save":
      sys.stdout.write(' ')
      sys.stdout.flush()
      if opt=="":
        c.SaveAs(options.name + ".png")
      else:
        c.SaveAs(opt + ".png")
    elif cmd == "saveas":
      sys.stdout.write(' ')
      sys.stdout.flush()
      if opt=="":
        filename = raw_input("Enter filename: ")
        c.SaveAs(filename + ".png")
      else:
        c.SaveAs(opt + ".png")
    elif cmd == "gaus":
      hist.Fit("gaus")
      hist.Draw("same")
    elif cmd == "fit":
      if opt=="":
        print "Must supply second argument to", cmd
        continue
      hist.Fit(opt)
      hist.Draw("same")
    elif cmd == "vertical":
      if opt=="":
        print "Must supply second argument to", cmd
        continue
      pos = float(opt)
      vert_line = ROOT.TLine(pos, 0, pos, hist.GetMaximum())
      vert_line.Draw("same")
      if not options.legoff:
        leg.Draw("same")
    elif cmd == "horizontal":
      if opt=="":
        print "Must supply second argument to", cmd
        continue
      pos = float(opt)
      horz_line = ROOT.TLine(0, pos, high, pos)
      horz_line.Draw("same")
      if not options.legoff:
        leg.Draw("same")
    elif cmd == "options":
      print "save FILENAME    saves current canvas, optionally with supplied name\n" +\
            "saveas FILENAME  saves current canvas prompting for filename if not given\n" +\
            "gaus             fits to a gaussian\n" +\
            "fit FIT          fits with supplied fitting function\n" +\
            "vertical INT     draws a vertical line at xvalue=INT\n" +\
            "horizontal INT   draws a horizontal line at yvalue=INT\n" +\
            ""
    elif not cmd == "":
      print cmd,"not a valid command"
