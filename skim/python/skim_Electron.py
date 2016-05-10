import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("SKIM")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
#process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")


##___________________________Global_Tag_______________________________________||
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'GR_P_V56::All'
from RecoLuminosity.LumiProducer.bunchSpacingProducer_cfi import *
process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v8'
#80X_dataRun2_Express_v5'


##___________________________Input_Files______________________________________||
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/023/00000/6CA4547E-D40F-E611-BC48-02163E014581.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/617/00000/92F06E50-6C14-E611-9C9D-02163E011D07.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/674/00000/EA467EA0-B314-E611-8372-02163E012576.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/680/00000/F0E4C9E8-EE14-E611-86AC-02163E0139C1.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/681/00000/C079BD6A-D814-E611-A4DF-02163E0118BB.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/682/00000/9AD330AF-CE14-E611-B102-02163E013444.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/728/00000/381312AC-4415-E611-85F4-02163E011A2E.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/729/00000/D03D4098-4415-E611-B96B-02163E011CA6.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/748/00000/04D5A670-6715-E611-9F9B-02163E013620.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/750/00000/12374F06-6915-E611-AB65-02163E01473C.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/760/00000/9655218F-7015-E611-8426-02163E011DA5.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/761/00000/C265BE74-7515-E611-AF34-02163E0142E7.root",
"/store/data/Run2016B/SingleElectron/RECO/PromptReco-v1/000/272/762/00000/36317016-D315-E611-87D3-02163E0119CD.root",
)
    )


##___________________________EDM_Output_File__________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('skim.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
#        'keep *_pfClusterMet_*_*', 'keep *_CSCTightHaloFilter_*_*', 'keep *_HBHENoiseFilterResultProducer_*_*'
        )
    )


##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


##___________________________CSC_Halo_Filter__________________________________||
process.load('RecoMET.METFilters.CSCTightHaloFilter_cfi')
process.CSCTightHaloFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.CSCTightHalo2015Filter_cfi')
process.CSCTightHalo2015Filter.taggingMode = cms.bool(True)
process.load('RecoMET.METFilters.CSCTightHaloTrkMuUnvetoFilter_cfi')
process.CSCTightHaloTrkMuUnvetoFilter.taggingMode = cms.bool(True)

##___________________________Global_Halo_Filter__________________________________||
process.load('RecoMET.METFilters.globalTightHalo2016Filter_cfi')
process.globalTightHalo2016Filter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.globalSuperTightHalo2016Filter_cfi')
process.globalSuperTightHalo2016Filter.taggingMode = cms.bool(True)

##___________________________HCAL_Noise_Filter________________________________||
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.HBHENoiseFilterResultProducer.minZeros = cms.int32(99999)
process.HBHENoiseFilterResultProducer.IgnoreTS4TS5ifJetInLowBVRegion=cms.bool(False)


#process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
#    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
#    reverseDecision = cms.bool(False)
#)
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')

process.load('RecoMET.METFilters.HcalStripHaloFilter_cfi')
process.HcalStripHaloFilter.taggingMode = cms.bool(True)


##___________________________PFClusterMet_____________________________________||
process.load('RecoMET.METProducers.PFClusterMET_cfi')
process.pfClusterRefsForJetsHCAL = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHCAL'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsECAL = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterECAL'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsHF = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHF'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJetsHO = cms.EDProducer("PFClusterRefCandidateProducer",
  src          = cms.InputTag('particleFlowClusterHO'),
  particleType = cms.string('pi+')
)
process.pfClusterRefsForJets = cms.EDProducer("PFClusterRefCandidateMerger",
  src = cms.VInputTag("pfClusterRefsForJetsHCAL", "pfClusterRefsForJetsECAL", "pfClusterRefsForJetsHF", "pfClusterRefsForJetsHO")
)
process.pfClusterMetSequence = cms.Sequence(
 process.particleFlowRecHitECAL*
 process.particleFlowRecHitHBHE*
 process.particleFlowRecHitHF*
 process.particleFlowRecHitHO*
 process.particleFlowClusterECALUncorrected*
 process.particleFlowClusterECAL*
 process.particleFlowClusterHBHE*
 process.particleFlowClusterHCAL*
 process.particleFlowClusterHF*
 process.particleFlowClusterHO*
 process.pfClusterRefsForJetsHCAL*
 process.pfClusterRefsForJetsECAL*
 process.pfClusterRefsForJetsHF*
 process.pfClusterRefsForJetsHO*
 process.pfClusterRefsForJets*
#   process.ak4PFClusterJets
 process.pfClusterMet
)


##___________________________PFCaloMet_____________________________________||
process.hltParticleFlowBlock = cms.EDProducer("PFBlockProducer",
  debug = cms.untracked.bool(False),
  verbose = cms.untracked.bool(False),
  elementImporters = cms.VPSet(
      cms.PSet(
          source = cms.InputTag("particleFlowClusterECAL"),
          #source = cms.InputTag("particleFlowClusterECALUncorrected"), #we use uncorrected
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHCAL"),
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHO"),
          importerName = cms.string('GenericClusterImporter')
      ),
      cms.PSet(
          source = cms.InputTag("particleFlowClusterHF"),
          importerName = cms.string('GenericClusterImporter')
      )
  ),
  linkDefinitions = cms.VPSet(
      cms.PSet(
          linkType = cms.string('ECAL:HCAL'),
          useKDTree = cms.bool(False),
          #linkerName = cms.string('ECALAndHCALLinker')
          linkerName = cms.string('ECALAndHCALCaloJetLinker') #new ECal and HCal Linker for PFCaloJets
      ),
      cms.PSet(
          linkType = cms.string('HCAL:HO'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('HCALAndHOLinker')
      ),
      cms.PSet(
          linkType = cms.string('HFEM:HFHAD'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('HFEMAndHFHADLinker')
      ),
      cms.PSet(
          linkType = cms.string('ECAL:ECAL'),
          useKDTree = cms.bool(False),
          linkerName = cms.string('ECALAndECALLinker')
      )
   )
)
from RecoParticleFlow.PFProducer.particleFlow_cfi import particleFlowTmp
process.hltParticleFlow = particleFlowTmp.clone(
    GedPhotonValueMap = cms.InputTag(""),
    useEGammaFilters = cms.bool(False),
    useEGammaElectrons = cms.bool(False), 
    useEGammaSupercluster = cms.bool(False),
    rejectTracks_Step45 = cms.bool(False),
    usePFNuclearInteractions = cms.bool(False),  
    blocks = cms.InputTag("hltParticleFlowBlock"), 
    egammaElectrons = cms.InputTag(""),
    useVerticesForNeutral = cms.bool(False),
    PFEGammaCandidates = cms.InputTag(""),
    useProtectionsForJetMET = cms.bool(False),
    usePFConversions = cms.bool(False),
    rejectTracks_Bad = cms.bool(False),
    muons = cms.InputTag(""),
    postMuonCleaning = cms.bool(False),
    usePFSCEleCalib = cms.bool(False)
    )
process.load("RecoMET.METProducers.PFMET_cfi")
process.pfCaloMet = process.pfMet.clone(
  src = cms.InputTag("hltParticleFlow"),
  alias = cms.string('pfCaloMet')
)
process.pfCaloMetSequence = cms.Sequence(
   process.hltParticleFlowBlock *
   process.hltParticleFlow *
   process.pfCaloMet
)

process.goodVertices = cms.EDFilter(
  "VertexSelector",
  filter = cms.bool(False),
  src = cms.InputTag("offlinePrimaryVertices"),
  cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
)
process.load('RecoMET.METFilters.trackingFailureFilter_cfi')
process.trackingFailureFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi')
process.EcalDeadCellTriggerPrimitiveFilter.taggingMode = cms.bool(True)

process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.eeBadScFilter.taggingMode = cms.bool(True)

process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4) ,
                                           maxAbsZ = cms.double(24),
                                           maxd0 = cms.double(2)
                                           )

process.load('RecoMET.METFilters.EcalDeadCellBoundaryEnergyFilter_cfi')
process.EcalDeadCellBoundaryEnergyFilter.taggingMode = cms.bool(True)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEB=cms.vint32(12, 13, 14)
process.EcalDeadCellBoundaryEnergyFilter.limitDeadCellToChannelStatusEE=cms.vint32(12, 13, 14)

process.condMETSelector = cms.EDProducer(
   "CandViewShallowCloneCombiner",
   decay = cms.string("caloMet pfMet"),
   cut = cms.string("(daughter(0).pt > 100) || (daughter(1).pt > 100)" ) 
   )

process.metCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("condMETSelector"),
    minNumber = cms.uint32(1),
    )


##___________________________Flat_Tuple________________________________________||
process.metScanNtupleMaker = cms.EDAnalyzer("METScanningNtupleMaker",
                                            rootOutputFile=cms.string("tuple.root"),
                                            pfCandidates=cms.InputTag("particleFlow"),
                                            pfJets=cms.InputTag("ak4PFJets"),
                                            caloMET=cms.InputTag("caloMet"),
                                            pfCaloMET=cms.InputTag("pfCaloMet"),
                                            pfClusterMET=cms.InputTag("pfClusterMet"),
                                            pfMET=cms.InputTag("pfMet"),
                                            EcalPFClusterCollection=cms.InputTag("particleFlowClusterECAL"),
                                            HcalPFClusterCollection=cms.InputTag("particleFlowClusterHCAL"),
                                            HBHEPFClusterCollection=cms.InputTag("particleFlowClusterHBHE"),
                                            HOPFClusterCollection=cms.InputTag("particleFlowClusterHO"),
                                            HFPFClusterCollection=cms.InputTag("particleFlowClusterHF"),
                                            tracksCollection=cms.InputTag("generalTracks"),
                                            TRKfilterLETMC=cms.InputTag("logErrorTooManyClusters"),
                                            TRKfilterLETMS=cms.InputTag("logErrorTooManySeeds"),
                                            TRKfilterMSC=cms.InputTag("manystripclus53X"),
                                            TRKfilterTMSC=cms.InputTag("toomanystripclus53X"),
                                            CSC2015filter=cms.InputTag("CSCTightHalo2015Filter"),
                                            GlobalHalofilterTight=cms.InputTag("globalTightHalo2016Filter"),
                                            GlobalHalofilterSuperTight=cms.InputTag("globalSuperTightHalo2016Filter"),
                                            HcalStripHaloFilter=cms.InputTag("HcalStripHaloFilter"),
                                            HBHEfilterR1=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
                                            HBHEfilterR2L=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Loose"),
                                            HBHEfilterR2T=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun2Tight"),
                                            HBHEfilterISO=cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResultRun1"),
                                            ECALTPfilter=cms.InputTag("EcalDeadCellTriggerPrimitiveFilter"),
                                            ECALSCfilter=cms.InputTag("eeBadScFilter"),
                                            EBRecHits=cms.InputTag("reducedEcalRecHitsEB"),
                                            EERecHits=cms.InputTag("reducedEcalRecHitsEE"),
                                            ESRecHits=cms.InputTag("reducedEcalRecHitsES"),
                                            HcalNoise=cms.InputTag("hcalnoise")
)

# This part is needed if you want to update the BeamHaloSummary information
from RecoMET.METProducers.CSCHaloData_cfi import *
from RecoMET.METProducers.EcalHaloData_cfi import *
from RecoMET.METProducers.HcalHaloData_cfi import *
from RecoMET.METProducers.GlobalHaloData_cfi import *
from RecoMET.METProducers.BeamHaloSummary_cfi import *

process.BeamHaloId = cms.Sequence(CSCHaloData*EcalHaloData*HcalHaloData*GlobalHaloData*BeamHaloSummary)




##___________________________PATH______________________________________________||
process.p = cms.Path(
#    process.BeamHaloId* #Uncomment this if you want to rerun the BeamHaloSummary. By default this line should remain commented
    process.primaryVertexFilter*
    process.bunchSpacingProducer *
    process.condMETSelector *
#    process.metCounter* #uncomment this line to apply a met cut
    process.CSCTightHaloFilter*
    process.HBHENoiseFilterResultProducer* #produces bools    
#    process.ApplyBaselineHBHENoiseFilter* 
    process.EcalDeadCellTriggerPrimitiveFilter*
    process.pfClusterMetSequence*
    process.pfCaloMetSequence*
    process.eeBadScFilter*
    process.goodVertices*
    process.trackingFailureFilter*
    process.EcalDeadCellBoundaryEnergyFilter*
    process.CSCTightHalo2015Filter*
    process.CSCTightHaloTrkMuUnvetoFilter*
    process.globalTightHalo2016Filter * 
    process.globalSuperTightHalo2016Filter * 
    process.HcalStripHaloFilter*

    process.metScanNtupleMaker ##CH: writes a flat tree
    )

process.e1 = cms.EndPath(
    process.out ##CH: write the skimmed edm file 
    )

##____________________________________________________________________________||





