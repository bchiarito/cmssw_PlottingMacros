import os

mass_windows = [
[0,2000],
[300,500],
[400,600],
[500,700],
[600,800],
[700,900],
[800,1000],
[900,1100],
[1000,1200],
[1100,1300],
[1200,1400],
[1300,1500],
[1400,1600],
[1500,1700],
[1600,1800],
[1700,1900],
[1800,2000],
]


for window in mass_windows:
  lower = window[0]
  higher = window[1]

  lower_gev = lower/1000.0
  higher_gev = higher/1000.0

  command = 'python plotting/plotter.py --var GammaTwoProng.mass --bins 60,0,3000 --logy --error1 --error2 --scaled --sample1 samples/SinglePhoton.txt --sample2 samples/trees_v2.0/signal/ --tree2 diphotonAnalyzer/fTree2 --sample3 samples/GJets.txt --leg1 "SinglePhoton Data 2015+2016" --leg2 "Signal MC" --leg3 "GJets MC" --cut "nTightPhoton>=1 && nPass>=1 && GammaTwoProng.dR>0.3 && GammaTwoProng.dEta<2 && Photon1.pt>200 && TwoProng_pt[0]>200 && TwoProng_Mass[0]>'+str(lower_gev)+' && TwoProng_Mass[0]<'+str(higher_gev)+'" --xaxis "\\text{M}_{\gamma\\text{TwoProng}}" --title "\\text{Mass in '+str(lower)+'-'+str(higher)+' Mev, cut on } \\text{p}_\\text{T}(\gamma) \\text{, p}_\\text{T}(\\text{TwoProng}) \\text{, } \Delta\eta" --quiet --name m_gammatwoprong_'+str(lower)+'_'+str(higher)+' --save'

  print command
  os.system(command)


# Barrel loop
for window in mass_windows:
  lower = window[0]
  higher = window[1]

  lower_gev = lower/1000.0
  higher_gev = higher/1000.0

  command = 'python plotting/plotter.py --var GammaTwoProng.mass --bins 60,0,3000 --logy --error1 --error2 --scaled --sample1 samples/SinglePhoton.txt --sample2 samples/trees_v2.0/signal/ --tree2 diphotonAnalyzer/fTree2 --sample3 samples/GJets.txt --leg1 "SinglePhoton Data 2015+2016" --leg2 "Signal MC" --leg3 "GJets MC" --cut "nTightPhoton>=1 && nPass>=1 && GammaTwoProng.dR>0.3 && GammaTwoProng.dEta<2 && Photon1.pt>200 && TwoProng_pt[0]>200 && TwoProng_Mass[0]>'+str(lower_gev)+' && TwoProng_Mass[0]<'+str(higher_gev)+' && abs(Photon1.scEta)<1.4442" --xaxis "\\text{M}_{\gamma\\text{TwoProng}}" --title "\\text{Mass in '+str(lower)+'-'+str(higher)+' Mev, cut on } \\text{p}_\\text{T}(\gamma) \\text{, p}_\\text{T}(\\text{TwoProng}) \\text{, } \Delta\eta, \\text{, Barrel}" --quiet --name m_gammatwoprong_'+str(lower)+'_'+str(higher)+'_barrel --save'

  print command
  os.system(command)

# Endcap loop
for window in mass_windows:
  lower = window[0]
  higher = window[1]

  lower_gev = lower/1000.0
  higher_gev = higher/1000.0

  command = 'python plotting/plotter.py --var GammaTwoProng.mass --bins 60,0,3000 --logy --error1 --error2 --scaled --sample1 samples/SinglePhoton.txt --sample2 samples/trees_v2.0/signal/ --tree2 diphotonAnalyzer/fTree2 --sample3 samples/GJets.txt --leg1 "SinglePhoton Data 2015+2016" --leg2 "Signal MC" --leg3 "GJets MC" --cut "nTightPhoton>=1 && nPass>=1 && GammaTwoProng.dR>0.3 && GammaTwoProng.dEta<2 && Photon1.pt>200 && TwoProng_pt[0]>200 && TwoProng_Mass[0]>'+str(lower_gev)+' && TwoProng_Mass[0]<'+str(higher_gev)+' && abs(Photon1.scEta)>1.566 && abs(Photon1.scEta)<2.5" --xaxis "\\text{M}_{\gamma\\text{TwoProng}}" --title "\\text{Mass in '+str(lower)+'-'+str(higher)+' Mev, cut on } \\text{p}_\\text{T}(\gamma) \\text{, p}_\\text{T}(\\text{TwoProng}) \\text{, } \Delta\eta, \\text{, Endcap}" --quiet --name m_gammatwoprong_'+str(lower)+'_'+str(higher)+'_endcap --save'

  print command
  os.system(command)

