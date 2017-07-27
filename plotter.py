import os
import glob
import fnmatch
import math
import ROOT
import string
import sys
import time
from optparse import OptionParser
from optparse import OptionGroup
from optparse import SUPPRESS_HELP

time_begin = time.time()
usage = "Usage: %prog [options] sample1 sample2 sample3 ... -v VAR -b BINNING -c CUT"
parser = OptionParser(usage=usage)

# Basic options
parser.add_option('-v', '--var', type='string', action='store', dest='var', help='variable in TTree to plot')
parser.add_option('-b', '--bin', '--bins', type='string', metavar='NUM,LOW,HIGH', action='store', default='100,0,100', dest='binning', help='')
parser.add_option('-c', '--cut', type='string', action='store', default='', dest='cut', metavar='CUT_STRING', help='')
parser.add_option('--noplot', action='store_true', default=False, dest='noplot', help='do not plot anything, just gives cutflow')
parser.add_option('--save', '--saveas', type='string',action='store', dest='save', metavar='ROOTFILE.root', help='')
parser.add_option('--saveplot', type='string',action='store', dest='saveplot', metavar='FILE.ext', help='')
parser.add_option('-q','--quiet', action='store_true', default=False, dest='quiet', help='less output and omit command prompt at end of running')
parser.add_option('-n', '--num', type='int', action='store', default=-1, dest='nentries', metavar='MAX_ENTRIES', help='')
parser.add_option('--tree', '--trees', type='string', action='store', dest='treename', metavar='PATH_TO_TREE', help='')

# doublevar options
doublevar_options = OptionGroup(parser, 'Double Variable Options', 'Setting these puts plotter in double variable mode')
doublevar_options.add_option('--var1', type='string', action='store', dest='var1', help='')
doublevar_options.add_option('--var2', type='string', action='store', dest='var2', help='')

# 2D options
twod_options = OptionGroup(parser, '2D Plot Options', 'Setting these puts plotter in 2D mode')
twod_options.add_option('--varx', type='string', action='store', dest='varx', help='')
twod_options.add_option('--vary', type='string', action='store', dest='vary', help='')
twod_options.add_option('--binx', '--binsx', type='string', action='store', dest='binningx', help='')
twod_options.add_option('--biny', '--binsy', type='string', action='store', dest='binningy', help='')

# Visual options
visual_options = OptionGroup(parser, 'Visual Options', '')
visual_options.add_option('--title', type='string', action='store', dest='title', help='title')
visual_options.add_option('--xaxis', type='string', action='store', dest='xaxis', help='xaxis label')
visual_options.add_option('--yaxis', type='string', action='store', dest='yaxis', help='yaxis label')
visual_options.add_option('--legoff', action='store_true', default=False, dest='legoff', help='turns off the legend')
visual_options.add_option('--stacked', action='store_true', default=False, dest='stacked', help='stacked histograms using THStack')
visual_options.add_option('--sidebyside', action='store_true', default=False, dest='sidebyside', help='stacked histograms using THStack and Draw("nostackb")')
visual_options.add_option('--noline', action='store_true', default=False, dest='noline', help='do not connect histogram with line')
visual_options.add_option('--errors', '--error',action='store_true', default=False, dest='errors', help='calls Sumw2() on all histograms')
visual_options.add_option('--logz', action='store_true', default=False, dest='logz', help='log scale on z')
visual_options.add_option('--logy', action='store_true', default=False, dest='logy', help='log scale on y')
visual_options.add_option('--logx', action='store_true', default=False, dest='logx', help='log scale on x')
visual_options.add_option('--scaled', action='store_true', default=False, dest='scale', help='scale to integral = 100')
visual_options.add_option('--mcweight', action='store_true', default=False, dest='mcweight', help='weight entries by XS and Ngen')
visual_options.add_option('--smallrun', action='store', dest='smallrun', help='correct mcN if small run')
visual_options.add_option('--lumi', type='float', action='store', dest='lumi', default=1.0, help='integrated luminosity to scale to (pb^1)')
visual_options.add_option('--2016lumi', action='store_true', default=False, dest='lumi_set_to_2016', help='set integreated luminiosity to 2016 total')

# Individual sample options
sample_options = OptionGroup(parser, 'Individual Sample Options', 'Set individual sample options with --treeN --errorN --legN --colorN.')
sample_options.add_option('--tree1', type='string', action='store', default='diphotonAnalyzer/fTree2', dest='treename1', help=SUPPRESS_HELP)
sample_options.add_option('--tree2', type='string', action='store', default='diphotonAnalyzer/fTree2', dest='treename2', help=SUPPRESS_HELP)
sample_options.add_option('--tree3', type='string', action='store', default='diphotonAnalyzer/fTree2', dest='treename3', help=SUPPRESS_HELP)
sample_options.add_option('--tree4', type='string', action='store', default='diphotonAnalyzer/fTree2', dest='treename4', help=SUPPRESS_HELP)
sample_options.add_option('--tree5', type='string', action='store', default='diphotonAnalyzer/fTree2', dest='treename5', help=SUPPRESS_HELP)
sample_options.add_option('--error1', action='store_true', default=False, dest='error1', help=SUPPRESS_HELP)
sample_options.add_option('--error2', action='store_true', default=False, dest='error2', help=SUPPRESS_HELP)
sample_options.add_option('--error3', action='store_true', default=False, dest='error3', help=SUPPRESS_HELP)
sample_options.add_option('--error4', action='store_true', default=False, dest='error4', help=SUPPRESS_HELP)
sample_options.add_option('--error5', action='store_true', default=False, dest='error5', help=SUPPRESS_HELP)
sample_options.add_option('--leg', '--leg1', type='string', action='store', dest='legend1', help=SUPPRESS_HELP)
sample_options.add_option('--leg2', type='string', action='store', dest='legend2', help=SUPPRESS_HELP)
sample_options.add_option('--leg3', type='string', action='store', dest='legend3', help=SUPPRESS_HELP)
sample_options.add_option('--leg4', type='string', action='store', dest='legend4', help=SUPPRESS_HELP)
sample_options.add_option('--leg5', type='string', action='store', dest='legend5', help=SUPPRESS_HELP)
sample_options.add_option('--color', '--color1', type='string', action='store', dest='color1', help=SUPPRESS_HELP)
sample_options.add_option('--color2', type='string', action='store', dest='color2', help=SUPPRESS_HELP)
sample_options.add_option('--color3', type='string', action='store', dest='color3', help=SUPPRESS_HELP)
sample_options.add_option('--color4', type='string', action='store', dest='color4', help=SUPPRESS_HELP)
sample_options.add_option('--color5', type='string', action='store', dest='color5', help=SUPPRESS_HELP)

parser.add_option_group(visual_options)
parser.add_option_group(doublevar_options)
parser.add_option_group(twod_options)
parser.add_option_group(sample_options)
(options, args) = parser.parse_args()

ind_treenames = False
if (not options.treename1==None) or \
   (not options.treename2==None) or \
   (not options.treename3==None) or \
   (not options.treename4==None) or \
   (not options.treename5==None):
  ind_treenames = True

ind_errors = False
if (not options.error1==None) or \
   (not options.error2==None) or \
   (not options.error3==None) or \
   (not options.error4==None) or \
   (not options.error5==None):
  ind_errors = True

twod_mode = False
if (not options.varx==None) or \
   (not options.vary==None) or \
   (not options.binningx==None) or \
   (not options.binningy==None):
  twod_mode = True

doublevar_mode = False
if (not options.var1==None) or \
   (not options.var2==None):
  doublevar_mode = True

if doublevar_mode and twod_mode:
  print "Double varialbe mode and 2D plot mode not compatible"
  sys.exit()

if not doublevar_mode and not twod_mode and options.var == None:
  print "Must supply the name of the variable to be plotted with --var"
  sys.exit()

if doublevar_mode and (options.var1==None or options.var2==None):
  print "Must supply the name of the variables to be plotted with --var1 and --var2"
  sys.exit()

if twod_mode and (options.varx==None or options.vary==None or options.binningx==None or options.binningy==None):
  print "Must supply options --varx, --vary, --binsx, --binsy for use with 2D plotting mode"
  sys.exit()

if options.lumi_set_to_2016:
  lumi = 41010.0
else:
  lumi = options.lumi

samples = []
for i in range(len(args)):
  sample = {}
  sample['path'] = args[i]
  if not ind_treenames:
    sample['tree'] = options.treename
  else:
    sample['tree'] = eval("options.treename"+str(i+1))
  if not ind_errors:
    sample['error'] = options.errors
  else:
    sample['error'] = eval("options.error"+str(i+1))
  sample['label'] = eval("options.legend"+str(i+1))
  sample['color'] = eval("options.color"+str(i+1))
  samples.append(sample)

if len(samples) == 0:
  print "Must specify at least one sample as arugment"
  sys.exit()

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
  elif fnmatch.fnmatch(path, "*/"):
    if not options.quiet:
      print "It appears", path, "is a directory to traverse"
    ISdirectory = True
  elif fnmatch.fnmatch(path, "*.dat"):
    if not options.quiet:
      print "It appears", path, "is a text file of inputs"
    ISinputfile = True
  else:
    print "Do not recognize", path, ", must end with /, .root, or .dat"
    sys.exit()

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
        N = max( float(line_list[2]) , options.nentries)
        treename = sample['tree']
      if len(line_list) == 4:
        path_to_file = line_list[0]
        xs = float(line_list[1])
        N = max( float(line_list[2]) , options.nentries)
        treename = line_list[3]
      if len(line_list) == 2 or len(line_list) == 0 or len(line_list) > 4:
        print "couldn't parse this line from input file", path
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
      sample['entries'].append([chain, xs, N])
     
if not options.quiet:
  print "Drawing into histogram..."

i1 = string.index(options.binning,',')
i2 = string.rindex(options.binning,',')
bins = int(options.binning[0:i1])
low = float(options.binning[i1+1:i2])
high = float(options.binning[i2+1:len(options.binning)])

if twod_mode:
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
  # main hist
  if twod_mode:
    hist_sum = ROOT.TH2F("hist"+"_sum_"+str(sumcount), "hist", binsx, lowx, highx, binsy, lowy, highy)
  elif doublevar_mode:
    hist_sum1 = ROOT.TH1F("hist1"+"_sum_"+str(sumcount), "hist", bins, low, high)
    hist_sum2 = ROOT.TH1F("hist2"+"_sum_"+str(sumcount), "hist", bins, low, high)
  else:
    hist_sum = ROOT.TH1F("hist"+"_sum_"+str(sumcount), "hist", bins, low, high)
  for entry in sample['entries']:
    chain = entry[0]
    xs = entry[1]
    N = entry[2]
    count += 1
    # entry hist
    if twod_mode:
      hist = ROOT.TH2F("hist"+"_"+str(count), "hist", binsx, lowx, highx, binsy, lowy, highy)
    elif doublevar_mode:
      hist1 = ROOT.TH1F("hist1"+"_"+str(count), "hist", bins, low, high)
      hist2 = ROOT.TH1F("hist2"+"_"+str(count), "hist", bins, low, high)
    else:
      hist = ROOT.TH1F("hist"+"_"+str(count), "hist", bins, low, high)
    # TTree.Draw()
    if twod_mode:
      draw_string = options.vary+":"+options.varx
    else:
      draw_string = options.var
    draw_string = draw_string + ">>"+"hist"+"_"+str(count)

    if options.cut == "" or options.cut == None:
      cut_string = "1"
    else:
      cut_string = options.cut
    if options.mcweight and not options.smallrun == None:
      cut_string = "("+cut_string+")*(mcXS/min(mcN,"+options.smallrun+"))"
    elif options.mcweight and options.smallrun == None:
      cut_string = "("+cut_string+")*(mcXS/mcN)"

    if options.nentries == -1:
      chain.Draw(draw_string, cut_string, "goff")
    else:
      chain.Draw(draw_string, cut_string, "goff", options.nentries)

    entry.append(hist)
    hist.Scale(xs/N)
    hist_sum.Add(hist)
  sample['summed_hist'] = hist_sum
  
# Print Summary
count = 1
if not doublevar_mode:
  for sample in samples:
    hist = sample['summed_hist']
    print "Entries " + str(count) + "   : ", int(hist.GetEntries())
    if not twod_mode:
      if not int(hist.GetBinContent(0)) == 0:
        print "Underflow " + str(count) + " - ", int(hist.GetBinContent(0))
      if not int(hist.GetBinContent(bins+1)) == 0:
        print "Overflow " + str(count) + "  - ", int(hist.GetBinContent(bins+1))
    count += 1
else:
  for sample in samples:
    hist1 = sample['summed_hist1']
    hist2 = sample['summed_hist2']
    print "Entries var1 " + str(count) + "   : ", int(hist1.GetEntries())
    print "Entries var2 " + str(count) + "   : ", int(hist2.GetEntries())
    if not int(hist1.GetBinContent(0)) == 0:
      print "Underflow var1 " + str(count) + " - ", int(hist1.GetBinContent(0))
    if not int(hist2.GetBinContent(0)) == 0:
      print "Underflow var2 " + str(count) + " - ", int(hist2.GetBinContent(0))
    if not int(hist1.GetBinContent(bins+1)) == 0:
      print "Overflow var1 " + str(count) + "  - ", int(hist1.GetBinContent(bins+1))
    if not int(hist2.GetBinContent(bins+1)) == 0:
      print "Overflow var2 " + str(count) + "  - ", int(hist2.GetBinContent(bins+1))
    count += 1

if options.noplot:
  time_end = time.time()
  print "Elapsed Time: ", (time_end - time_begin)
  sys.exit()

if not options.save == None:
  outfilename = options.save
  print "Writing histogram(s) to file " + outfilename + ".root..."
  outputfile = ROOT.TFile(outfilename+'.root',"recreate")
  outputfile.cd()
  for sample in samples:
    sample['summed_hist'].Write()
  if options.stacked or options.sidebyside:
    hs.Write()
  outputfile.Close()

  time_end = time.time()
  print "Elapsed Time: ", (time_end - time_begin)
  sys.exit()
  
if not options.quiet:
  print "Plotting..."
c = ROOT.TCanvas()
c.cd()
if options.logz:
  c.SetLogz()
if options.logy:
  c.SetLogy()
if options.logx:
  c.SetLogx()
colorcount = 1
for sample in samples:
  hist = sample['summed_hist']
  if doublevar_mode:
    hist = sample['summed_hist1']
  # Color
  if sample['color'] == None:
    hist.SetLineColor(colorcount)
    hist.SetMarkerColor(colorcount)
    if options.stacked or options.sidebyside:
      hist.SetFillColor(colorcount)
    else:
      hist.SetFillColor(0)
    colorcount+=1
  else:
    exec('hist.SetLineColor(' + sample['color'] + ')')
    exec('hist.SetMarkerColor(' + sample['color'] + ')')
    if options.stacked or options.sidebyside:
      exec('hist.SetFillColor(' + sample['color'] + ')')
    else:
      hist.SetFillColor(0)
  hist.SetFillColor(0)
  # Width
  hist.SetLineWidth(1)
  # Stats
  hist.SetStats(0)
  # Scale
  if sample['error']:
    hist.Sumw2()
  else:
    hist.SetMarkerSize(1)
    hist.SetMarkerStyle(2)
  if options.scale:
    if not hist.Integral() == 0:
      hist.Scale(100.0/hist.Integral())

if options.stacked or options.sidebyside:
  if doublevar_mode:
    print "double variable mode incompatible with --stacked and --sidebyside"
    sys.exit()
  hs = ROOT.THStack('hs','')
  for sample in samples:
    hist = sample['summed_hist']
    hs.Add(hist)
  if options.save == None:
    if options.stacked:
      hs.Draw('hist')
    elif options.sidebyside:
      hs.Draw('hist nostackb')

# Maximum
maximum = 0
for sample in samples:
  if doublevar_mode:
    hist1 = sample['summed_hist1']
    hist2 = sample['summed_hist2']
    maximum = max(maximum, hist1.GetMaximum(), hist2.GetMaximum())
  else:
    hist = sample['summed_hist']
    maximum = max(maximum, hist.GetMaximum())
for sample in samples:
  hist = sample['summed_hist']
  if doublevar_mode:
    hist = sample['summed_hist1']
  if options.logy:
    hist.SetMaximum(maximum*4)
  else:
    hist.SetMaximum(maximum*1.15)
    hist.SetMinimum(0)

# Labels
for sample in samples:
  hist = sample['summed_hist']
  if doublevar_mode:
    hist = sample['summed_hist1']
  title = ''
  xaxis = ''
  yaxis = ''
  # Title
  if not options.title == None:
    title = options.title
  else:
    if not twod_mode and not doublevar_mode:
      title = options.var
    elif not twod_mode and doublevar_mode:
      title = options.var1 + " and " + options.var2 
    else:
      if options.cut == '':
        title = options.varx + " vs " + options.vary
      else:
        title = options.cut
  if not twod_mode:
    # X axis
    if doublevar_mode:
      xaxis = options.var1 + " and " + options.var2 + " w/ " + options.cut
    else:
      xaxis = options.var + " w/ " + options.cut
    if options.cut == '':
      if doublevar_mode:
        xaxis = options.var1 + " and " + options.var2
      else:
        xaxis = options.var
    if not options.xaxis == None:
      xaxis = options.xaxis
    # Y axis
    if not options.yaxis == None:
      yaxis = options.yaxis
    elif options.scale:
      yaxis = "Scaled to Integral 100"
    else:
      yaxis = "Events"
  else:
    # X axis
    if not options.xaxis == None:
      xaxis = options.xaxis
    else:
      xaxis = options.varx
    # Y axis
    if not options.yaxis == None:
      yaxis = options.yaxis
    else:
      yaxis = options.vary
  hist.SetTitle(title)
  hist.GetXaxis().SetTitle(xaxis)
  hist.GetYaxis().SetTitle(yaxis)
  if options.stacked or options.sidebyside:
    hs.SetTitle(title)
    hs.GetXaxis().SetTitle(xaxis)
    hs.GetYaxis().SetTitle(yaxis)
    
# Draw()
if options.save == None:
  if twod_mode:
    ROOT.gStyle.SetPalette(55)
  if options.stacked or options.sidebyside:
    c.Modified()
  else:  
    for sample in samples:
      if doublevar_mode:
        hist1 = sample['summed_hist1']
        hist2 = sample['summed_hist2']
        if options.noline:
          draw_option = 'same'
        else:
          draw_option = 'hist same'
        if sample['error'] or options.errors:
          draw_option += ' e'
        hist1.Draw(draw_option)
        hist2.Draw(draw_option) 
      else:
        hist = sample['summed_hist']
        if options.noline:
          draw_option = 'same'
        else:
          draw_option = 'hist same'
        if twod_mode:
          draw_option += ' Colz'
        if sample['error'] or options.errors:
          draw_option += ' e'
        hist.Draw(draw_option)
  # Legend
  leg = ROOT.TLegend(0.55, 0.80, 0.9, 0.9)
  for sample in samples:
    hist = sample['summed_hist']
    if doublevar_mode:
      hist = sample['summed_hist1']
    if sample['label'] == None:
      leg.AddEntry(hist, sample['path'], "l")
    else:
      leg.AddEntry(hist, sample['label'], "l")  
  if not options.legoff:
    leg.Draw("same")

if not options.saveplot == None:
  print "Writing plot to file " + options.saveplot + "..."
  filename = options.saveplot
  c.SaveAs(filename)

if not options.quiet:
  time_end = time.time()
  print "Elapsed Time: ", (time_end - time_begin)

if not options.saveplot == None:
  sys.exit()

if options.quiet:
  raw_input()
  sys.exit()

# After plot Commands
hists = []
for sample in samples:
  samples[0]['summed_hist']

cmd = "start"
while not cmd == "":
  print "\nPress [Enter] to finish, type 'options' to see options:"
  # parse input
  inp = raw_input()
  i = string.find(inp,' ')
  if i==-1:
    cmd = inp
    opt = ""
  else:
    cmd = inp[0:i]
    opt = inp[i+1:len(inp)]

  # setup
  hist = samples[0]['summed_hist']

  # begin commands
  if cmd == "save" or cmd == "saveas":
    if opt=="":
      sys.stdout.write(' ')
      sys.stdout.flush()
      filename = raw_input("Enter filename: ")
      c.SaveAs(filename)
    else:
      c.SaveAs(opt)
  elif cmd == "title":
    if opt=="":
      sys.stdout.write(' ')
      sys.stdout.flush()
      new_title = raw_input("Enter title for plot: ")
      hist.SetTitle(new_title)
      c.Modified()
    else:  
      hist.SetTitle(opt)
      c.Modified()
  elif cmd == "fit":
    if opt=="":
      print "Must supply second argument to", cmd
      continue
    hist.Fit(opt)
    c.Modified()
  elif cmd == "vertical":
    if opt=="":
      print "Must supply second argument to", cmd
      continue
    pos = float(opt)
    vert_line = ROOT.TLine(pos, 0, pos, hist.GetMaximum())
    vert_line.Draw("same")
    #if not options.legoff:
    #  leg.Draw("same")
  elif cmd == "horizontal":
    if opt=="":
      print "Must supply second argument to", cmd
      continue
    pos = float(opt)
    horz_line = ROOT.TLine(0, pos, high, pos)
    horz_line.Draw("same")
    #if not options.legoff:
    #  leg.Draw("same")
  elif cmd == "options":
    print "save FILENAME    saves current canvas, optionally with supplied name\n" +\
          "saveas           alias for save\n" +\
          "fit FIT          fits with supplied fitting function, only fits sample1\n" +\
          "vertical NUM     draws a vertical line at xvalue=NUM\n" +\
          "horizontal NUM   draws a horizontal line at yvalue=NUM\n" +\
          "title NEW_TITLE  changes plot title to NEW_TITLE\n" +\
          ""
  elif not cmd == "":
    print cmd,"not a valid command"
