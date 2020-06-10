from ROOT import *

fi_old = TFile('TwoProngNtuplizer_old.root') # old
fi_new = TFile('TwoProngNtuplizer_new.root') # 7120patch3

tree_old = fi_old.Get('twoprongNtuplizer/fTree')
tree_new = fi_new.Get('twoprongNtuplizer/fTree')

n_old_omega = tree_old.Draw("GenOmega_vy[0]:GenOmega_vx[0]","","goff")
graph_old_omega = TGraph(n_old_omega, tree_old.GetV1(), tree_old.GetV2())

n_old_phi = tree_old.Draw("GenPhi_vy[0]:GenPhi_vx[0]","","goff")
graph_old_phi = TGraph(n_old_phi, tree_old.GetV1(), tree_old.GetV2())

n_old_PV = tree_old.Draw("PV_y:PV_x","","goff")
graph_old_PV = TGraph(n_old_PV, tree_old.GetV1(), tree_old.GetV2())

n_old_beamspot = tree_old.Draw("beamspot_y:beamspot_x","","goff")
graph_old_beamspot = TGraph(n_old_beamspot, tree_old.GetV1(), tree_old.GetV2())

n_new_omega = tree_new.Draw("GenOmega_vy[0]:GenOmega_vx[0]","","goff")
graph_new_omega = TGraph(n_new_omega, tree_new.GetV1(), tree_new.GetV2())

n_new_phi = tree_new.Draw("GenPhi_vy[0]:GenPhi_vx[0]","","goff")
graph_new_phi = TGraph(n_new_phi, tree_new.GetV1(), tree_new.GetV2())

n_new_PV = tree_new.Draw("PV_y:PV_x","","goff")
graph_new_PV = TGraph(n_new_PV, tree_new.GetV1(), tree_new.GetV2())

n_new_beamspot = tree_new.Draw("beamspot_y:beamspot_x","","goff")
graph_new_beamspot = TGraph(n_new_beamspot, tree_new.GetV1(), tree_new.GetV2())

c = TCanvas()

graph_old_omega.SetMarkerColor(kGreen)
graph_old_omega.SetMarkerStyle(2)
graph_old_omega.SetMarkerSize(1.2)

graph_old_phi.SetMarkerColor(kBlack)
graph_old_phi.SetMarkerStyle(2)
graph_old_phi.SetMarkerSize(0.2)

graph_old_PV.SetMarkerColor(kYellow)
graph_old_PV.SetMarkerStyle(2)
graph_old_PV.SetMarkerSize(0.2)

graph_old_beamspot.SetMarkerColor(kRed)
graph_old_beamspot.SetMarkerStyle(20)
graph_old_beamspot.SetMarkerSize(1.2)

graph_new_omega.SetMarkerColor(kGreen)
graph_new_omega.SetMarkerStyle(4)
graph_new_omega.SetMarkerSize(0.2)

graph_new_phi.SetMarkerColor(kBlack)
graph_new_phi.SetMarkerStyle(4)
graph_new_phi.SetMarkerSize(0.2)

graph_new_PV.SetMarkerColor(kYellow)
graph_new_PV.SetMarkerStyle(4)
graph_new_PV.SetMarkerSize(0.2)

graph_new_beamspot.SetMarkerColor(kRed)
graph_new_beamspot.SetMarkerStyle(4)
graph_new_beamspot.SetMarkerSize(0.2)


graph_old_omega.GetXaxis().SetLimits(-1.2,1.2)
graph_old_omega.GetHistogram().SetMaximum(1.2)
graph_old_omega.GetHistogram().SetMinimum(-1.2)

graph_old_omega.SetTitle("Vertex for omega, phi, PV, beamspot")
graph_old_omega.GetXaxis().SetTitle("x pos (cm)")
graph_old_omega.GetYaxis().SetTitle("y pos (cm)")

graph_old_PV.Draw('ap')
graph_old_phi.Draw('same p')
graph_old_omega.Draw('same p')
graph_old_beamspot.Draw('same p')

raw_input()
