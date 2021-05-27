from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'SkimTau3Mu_Summer19UL18_WTau3Mu_Mini_v2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'


config.JobType.psetName = '/lustrehome/fsimone/MINIAOD_ntuplizer/CMSSW_10_6_20/src/SkimTools/SkimTau3Mu/test/run_MC2018UL_PatAndTree_cfg.py'

config.Data.inputDataset = '/W_ToTau_ToMuMuMu_TuneCP5_13TeV-pythia8/RunIISummer19UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 20
#config.Data.runRange = '193093-193999' # '193093-194075'
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'SkimTau3Mu_Summer19UL18_WTau3Mu_Mini_v2'
config.JobType.allowUndistributedCMSSW = True 
config.Site.storageSite = 'T2_IT_Bari'
config.Site.ignoreGlobalBlacklist  = True

#sample in production!!!
config.Data.allowNonValidInputDataset = True