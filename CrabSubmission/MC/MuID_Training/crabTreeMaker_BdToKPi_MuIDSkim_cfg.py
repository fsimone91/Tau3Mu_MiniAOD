from CRABClient.UserUtilities import config, getUsername
config = config()

config.General.requestName = 'SkimMuID_BdToKPi_SoftQCDnonD_2017_CMSSW_10_2_18'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/lustrehome/fsimone/MINIAOD_ntuplizer/CMSSW_10_2_18/src/SkimTools/SkimMuonId/test/run_MuonIdBkg_PatAndTree_cfg.py'
config.Data.inputDataset = '/BdToKPi_BMuonFilter_SoftQCDnonD_TuneCP5_13TeV-pythia8-evtgen/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.publication = True
config.Data.outputDatasetTag = 'SkimMuID_BdToKPi_SoftQCDnonD_2017_CMSSW_10_2_18'

config.Site.storageSite = 'T2_IT_Bari'
config.JobType.allowUndistributedCMSSW = True
config.Site.ignoreGlobalBlacklist  = True
