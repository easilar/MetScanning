import ROOT
import os,sys

path = "/afs/hephy.at/user/e/easilar/www/METPhiScanning/plots/"
if not os.path.exists(path):
  os.makedirs(path)

#plot_vars = ["pfMETPt","pfMETPhi","pfMETSumEt","caloMETPt","caloMETPhi","caloMETSumEt","pfJet_pt","pfJet_phi"]
#plot_vars = ["pfMETPt","pfMETSumEt","caloMETPt","caloMETSumEt","pfJet_pt"]
plot_vars = ["pfJet_phi"]
plot_vars_2D = ["pfMETPt:pfJet_pt[0]","pfMETPhi:pfJet_phi[0]"]

filters = ["filter_csc2015","filter_globaltighthalo2016","filter_globalsupertighthalo2016","filter_hcalstriphalo",\
          "filter_hbher2l","filter_hbher2t","filter_ecaltp","filter_ecalsc","filter_hbheiso"]

additional_cuts = ["(pfMETPt>=90||caloMETPt>=90)"]

c = ROOT.TChain("tree")  
c.Add("tuple.root")

plotting = False  ##1D 
plotting2D = False ##2D
filter_flow = True
scan = True


###Plotting
if plotting:
  for plot in plot_vars:
      cb = ROOT.TCanvas("cb","cb",600,600,600,600)
      #ROOT.gPad.SetLogy()
      c.Draw(plot)
      cb.SaveAs(path+plot+".png") 
      cb.SaveAs(path+plot+".root")
      cb.SaveAs(path+plot+".pdf")

if plotting2D:
  for plot in plot_vars_2D:
    cb = ROOT.TCanvas("cb","cb",600,600,600,600)
    c.Draw(plot,"(1)","colz")
    plot_name = plot.replace(":","vs")
    cb.SaveAs(path+plot_name+".png")
    cb.SaveAs(path+plot_name+".pdf")
    cb.SaveAs(path+plot_name+".root")
  
###Filter flow
path_cutflow = "/afs/hephy.at/user/e/easilar/www/METPhiScanning/filter_flow/"
if not os.path.exists(path_cutflow):
  os.makedirs(path_cutflow)
ofile = file(path_cutflow+'filterflow.tex','w')
if filter_flow:
  cut = "(1)"
  label = cut
  f_yield = c.GetEntries(cut)
  line = label+":     "+str(f_yield)+"\n"
  ofile.write(line)

  for filter_c in filters+additional_cuts:
     cut = "&&".join([filter_c,cut]) 
     label = filter_c
     f_yield = c.GetEntries(cut)
     print f_yield
     line = label+":     "+str(f_yield)+"\n"
     ofile.write(line)

  if scan:
    c.SetScanField(0)
    c.GetPlayer().SetScanRedirect(1)
    c.GetPlayer().SetScanFileName("/afs/hephy.at/user/e/easilar/www/METPhiScanning/filter_flow/scan_result.txt")
    scan_string = ":".join([filter_n for filter_n in filters])
    #c.Scan("run:lumi:event:caloMETPt:pfMETPt:"+scan_string,"(pfMETPt>=90||caloMETPt>=90)&&!(filter_hbheiso)")
    c.Scan("run:lumi:event:caloMETPt:pfMETPt:"+scan_string,"!(filter_hbheiso)")
    #c.Scan("run:lumi:event:caloMETPt:pfMETPt",cut)

ofile.write("\n")
ofile.close()
print "Written", ofile.name

