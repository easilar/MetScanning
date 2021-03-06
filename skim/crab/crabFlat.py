from CRABClient.UserUtilities import config
#submit with 'python crab.py'
#Don't write to my directory (schoef), though

## define only these variables here

production = "/afs/cern.ch/work/c/cheidegg/crab3/2015-07-13_filters_runb_flat/"
json       = "json/json_DCSONLY_Run2015B.txt"
site       = "T3_CH_PSI"
outdir     = "/store/user/cheidegg/crab3/2015-07-13_filters_runb_flat/"


## do not touch beyond this point

config = config()
config.General.requestName   = 'ZeroBias1_Run2015A-PromptReco-v1_RECO'
config.General.workArea      = production

config.JobType.outputFiles   = ['tuple.root']
config.JobType.pluginName    = 'Analysis'
config.JobType.psetName      = '../python/skimFlat.py'

config.Data.inputDataset     = '/ZeroBias1/Run2015A-PromptReco-v1/RECO'
config.Data.inputDBS         = 'global'
config.Data.lumiMask         = json
config.Data.splitting        = 'LumiBased'
config.Data.unitsPerJob      = 20

config.Data.publication      = False
#config.Data.outLFNDirBase   = '' 
#config.Data.publishDataName = ''

config.Data.outLFNDirBase    = outdir
config.Site.storageSite      = 'T3_CH_PSI'

datasets=[
'/ExpressPhysics/Run2015B-Express-v1/FEVT',
'/BTagCSV/Run2015B-PromptReco-v1/RECO',
'/BTagMu/Run2015B-PromptReco-v1/RECO',
'/DoubleEG/Run2015B-PromptReco-v1/RECO',
'/EGamma/Run2015B-PromptReco-v1/RECO',
'/Jet/Run2015B-PromptReco-v1/RECO',
'/JetHT/Run2015B-PromptReco-v1/RECO',
'/HighMultiplicity/Run2015B-PromptReco-v1/RECO',
'/HTMHT/Run2015B-PromptReco-v1/RECO',
'/MET/Run2015B-PromptReco-v1/RECO',
'/SingleElectron/Run2015B-PromptReco-v1/RECO',
'/SingleMu/Run2015B-PromptReco-v1/RECO',
'/SinglePhoton/Run2015B-PromptReco-v1/RECO',
'/ZeroBias/Run2015B-PromptReco-v1/RECO',
'/ZeroBias1/Run2015B-PromptReco-v1/RECO',
'/ZeroBias2/Run2015B-PromptReco-v1/RECO',
'/ZeroBias3/Run2015B-PromptReco-v1/RECO',
'/ZeroBias4/Run2015B-PromptReco-v1/RECO',
'/ZeroBias5/Run2015B-PromptReco-v1/RECO',
'/ZeroBias6/Run2015B-PromptReco-v1/RECO',
'/ZeroBias7/Run2015B-PromptReco-v1/RECO',
'/ZeroBias8/Run2015B-PromptReco-v1/RECO',
]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for dataset in datasets:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.rstrip('/').lstrip('/').replace('/','_') + "_flat"
#        print config.General.requestName
        crabCommand('submit', config = config)



