from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'SingleElectron_Run2016B_PromptReco_v1_RECO'
config.General.workArea = 'crab3/Run2016B/'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.outputFiles   = ['tuple.root']

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/skim_Electron.py'

config.Data.inputDataset = '/SingleElectron/Run2016B-PromptReco-v1/RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/DCSOnly/json_DCSONLY.txt'
#config.Data.runRange = '193093-193999' # '193093-194075'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'SingleElectron_Run2016B_PromptReco_v1_RECO'

config.Site.storageSite = "T2_AT_Vienna"

