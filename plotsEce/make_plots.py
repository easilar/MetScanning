import ROOT
import os,sys

#path = "/afs/hephy.at/user/e/easilar/www/METPhiScanning/SingleElectron/plots/"
path = "/afs/hephy.at/user/e/easilar/www/METPhiScanning/DoubleMuon/plots/"
if not os.path.exists(path):
  os.makedirs(path)

plot_vars = ["pfMETPt","pfMETPhi","pfMETSumEt","caloMETPt","caloMETPhi","caloMETSumEt","pfJet_pt[0]","pfJet_phi[0]"]
#plot_vars = ["pfMETPt","pfMETSumEt","caloMETPt","caloMETSumEt","pfJet_pt"]
#plot_vars = ["pfJet_phi","pfMETPhi","caloMETPhi"]
plot_vars_2D = ["pfMETPt:pfJet_pt[0]","pfMETPhi:pfJet_phi[0]"]

filters = ["filter_csc2015","filter_globaltighthalo2016","filter_globalsupertighthalo2016","filter_hcalstriphalo",\
          "filter_hbher2l","filter_hbher2t","filter_ecaltp","filter_ecalsc","filter_hbheiso"] #,"filter_badChCand"]

all_filters_cut = "(1)" 
for filter_c in filters:  #+additional_cuts:
     all_filters_cut = "&&".join([filter_c,all_filters_cut])
print all_filters_cut
#additional_cuts = ["(pfMETPt>=1000||caloMETPt>=1000)"]
additional_cuts = ["(pfMETPt>=100||caloMETPt>=100)"]

c = ROOT.TChain("tree")  
c.Add("/data/easilar/METScaning/DoubleMuon/all_tuples.root")
#c.Add("/data/easilar/METScaning/SingleElectron/all_tuples.root")

plotting =True  ##1D 
multi = True
plotting2D = False ##2D
filter_flow = False
iterative = False ##If this is True: It will add the filters on top of eachother
scan = False

inv_mass_leplep = "sqrt( 2*pfLepton_pt[0]*pfLepton_pt[1]*(cosh(pfLepton_eta[0]-pfLepton_eta[1])-cos(pfLepton_phi[0]-pfLepton_phi[1]) ))" 
muon_cut = "((pfLepton_pdgId[0]*pfLepton_pdgId[1])<0)&&abs(pfLepton_pdgId)==13"
Z_mass_window = "(abs("+inv_mass_leplep+"-91.2)<15)&&((pfLepton_pdgId[0]*pfLepton_pdgId[1])<0)"
#Z_mass_window = "(1)"
###Plotting
if plotting:

  if multi:
    for plot in plot_vars:
        cb = ROOT.TCanvas("cb","cb",600,600,600,600)
        ROOT.gPad.SetLogy()
        c.Draw(plot,Z_mass_window+"&&"+all_filters_cut+"&&!(filter_badChCand)")
        cb.SaveAs(path+plot+"_pass_filters_notBadCharge.png") 
        cb.SaveAs(path+plot+"_pass_filters_notBadCharge.root")
        cb.SaveAs(path+plot+"_pass_filters_notBadCharge.pdf")
  else:
    for plot in plot_vars:
      cb = ROOT.TCanvas("cb","cb",600,600,600,600)
      ROOT.gPad.SetLogy()
      leg = ROOT.TLegend(0.6,0.6,0.9,0.7)
      leg.SetBorderSize(1)
      histo1 = ROOT.TH1F("histo1","histo1",50,-4,4)
      histo2 = ROOT.TH1F("histo2","histo2",50,-4,4)
      c.Draw(plot+">>histo1",Z_mass_window)
      c.Draw(plot+">>histo2",Z_mass_window+"&&filter_badChCand","same")
      histo2.SetLineColor(ROOT.kRed)
      histo1.SetTitle("")
      histo2.SetTitle("")
      histo1.GetXaxis().SetTitle(plot)
      histo2.GetXaxis().SetTitle(plot)
      leg.AddEntry(histo1,"without filter_badChCand","l")
      leg.AddEntry(histo2,"with filter_badChCand","l")
      leg.SetFillColor(0)
      leg.Draw()
      cb.SaveAs(path+plot+"_Comp.png")
      cb.SaveAs(path+plot+"_Comp.root")
      cb.SaveAs(path+plot+"_Comp.pdf")


if plotting2D:
  for plot in plot_vars_2D:
    cb = ROOT.TCanvas("cb","cb",600,600,600,600)
    c.Draw(plot,"(1)","colz")
    plot_name = plot.replace(":","vs")
    cb.SaveAs(path+plot_name+".png")
    cb.SaveAs(path+plot_name+".pdf")
    cb.SaveAs(path+plot_name+".root")
  
###Filter flow
#path_cutflow = "/afs/hephy.at/user/e/easilar/www/METPhiScanning/SingleElectron/filter_flow/"
path_cutflow = "/afs/hephy.at/user/e/easilar/www/METPhiScanning/DoubleMuon/filter_flow/"
if not os.path.exists(path_cutflow):
  os.makedirs(path_cutflow)
ofile = file(path_cutflow+'filterflow.tex','w')
if filter_flow:
  cut = Z_mass_window
  label = "Z_mass_window"
  #label = "(1)"
  f_yield = c.GetEntries(cut)
  orig_f_yield = f_yield
  line = label+":\t"+str(f_yield)+"\n"
  ofile.write(line)
  
  for filter_c in filters:  #+additional_cuts:
     cut = "&&".join([filter_c,cut]) 
     label = filter_c
     f_yield = c.GetEntries(cut)
     print f_yield
     percentage = (float(f_yield)/float(orig_f_yield))*100
     percentage = format(percentage,".2f")
     line = label+":\t"+str(f_yield)+"\t"+str(percentage)+"\n"
     ofile.write(line)
     if not iterative : cut = Z_mass_window

  if scan:
    c.SetScanField(0)
    c.GetPlayer().SetScanRedirect(1)
    #c.GetPlayer().SetScanFileName("/afs/hephy.at/user/e/easilar/www/METPhiScanning/SingleElectron/filter_flow/scan_result.txt")
    c.GetPlayer().SetScanFileName("/afs/hephy.at/user/e/easilar/www/METPhiScanning/DoubleMuon/filter_flow/scan_result.txt")
    scan_string = ":".join([filter_n for filter_n in filters])
    #c.Scan("run:lumi:event:caloMETPt:pfMETPt:"+scan_string,"(pfMETPt>=90||caloMETPt>=90)&&!(filter_hbheiso)")
    c.Scan("run:lumi:event:caloMETPt:pfMETPt:"+scan_string,"!(filter_badChCand)&&"+additional_cuts[0]+"&&"+Z_mass_window,"colsize=12")
    #c.Scan("run:lumi:event:caloMETPt:pfMETPt",cut)

ofile.write("\n")
ofile.close()
print "Written", ofile.name

