from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'SkimPhiPi_Summer20UL17_DsPhiPi_ModFilter_Mini_v1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'


config.JobType.psetName = '/lustrehome/fsimone/MINIAOD_ntuplizer/CMSSW_10_6_20/src/SkimTools/SkimPhiPi/test/run_MC2017_DsPhiPiSkimAndTree_cfg.py'

config.Data.inputDataset = '/DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
#config.Data.inputDataset = '/DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'LumiBased'
config.Data.splitting = 'Automatic'
#config.Data.unitsPerJob = 20
#config.Data.runRange = '193093-193999' # '193093-194075'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'SkimPhiPi_Summer20UL17_DsPhiPi_ModFilter_Mini_v1'
config.JobType.allowUndistributedCMSSW = True 
config.Site.storageSite = 'T2_IT_Bari'
config.Site.ignoreGlobalBlacklist  = True

#sample in production!!!
config.Data.allowNonValidInputDataset = True
