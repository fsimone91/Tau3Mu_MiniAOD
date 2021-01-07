import FWCore.ParameterSet.Config as cms

process = cms.Process('Tau3MuSkim')

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load("SkimTools.SkimTau3Mu.Tau3MuSkim_miniAOD_cff")

#process.GlobalTag.globaltag = '94X_mc2017_realistic_v14'
process.GlobalTag.globaltag = '106X_mc2017_realistic_v7' #MC_UL 
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#Begin processing the 25271st record. Run 320012, Event 56448719, LumiSection 36 on stream 0 at 20-Apr-2020 18:53:30.862 CEST
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #MV 2017UL DsTau3Mu --> /DsToTau_To3Mu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM
        'root://xrootd-cms.infn.it///store/mc/RunIISummer19UL17MiniAOD/DsToTau_To3Mu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/70000/76B6C241-16EA-1647-A1F2-82559AC936DE.root',
#        'root://xrootd-cms.infn.it///store/mc/RunIISummer19UL17MiniAOD/DsToTau_To3Mu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/70000/793C348A-5013-4049-8B8F-F3AE291781F5.root',
#        'root://xrootd-cms.infn.it///store/mc/RunIISummer19UL17MiniAOD/DsToTau_To3Mu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/70000/8B62D042-D2DF-5640-8531-7B47FE1CBEFC.root',
#        'root://xrootd-cms.infn.it///store/mc/RunIISummer19UL17MiniAOD/DsToTau_To3Mu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/70000/8B96BB26-7EC7-5D4F-8CEA-B9AD61CDB94A.root',
#        'root://xrootd-cms.infn.it///store/mc/RunIISummer19UL17MiniAOD/DsToTau_To3Mu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/70000/8C9265B3-148E-F843-AAD2-FED1002B93A3.root',
#        'root://xrootd-cms.infn.it///store/mc/RunIISummer19UL17MiniAOD/DsToTau_To3Mu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/70000/8F012BAA-1D58-2B41-8D6E-BCD076D785E6.root',
#        'root://xrootd-cms.infn.it///store/mc/RunIISummer19UL17MiniAOD/DsToTau_To3Mu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/70000/8FE59748-41B7-1440-8511-77A1D463D3E9.root',


    ),
            #eventsToProcess = cms.untracked.VEventRange('320012:56448719')
)


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("TreeData.root"))




process.unpackedPatTrigger = cms.EDProducer("PATTriggerObjectStandAloneUnpacker",
    patTriggerObjectsStandAlone = cms.InputTag( 'slimmedPatTrigger' ),
    triggerResults              = cms.InputTag( 'TriggerResults::HLT' ),
    unpackFilterLabels = cms.bool(True)
)

process.TreeMakerBkg = cms.EDAnalyzer("MiniAnaTau3Mu",
                                      isMcLabel = cms.untracked.bool(True),
                                      isAnaLabel = cms.untracked.bool(True),
                                      is2016Label = cms.untracked.bool(True),
                                      is2017Label = cms.untracked.bool(True),
                                      is2018Label = cms.untracked.bool(True),
                                      isBParkingLabel = cms.untracked.bool(False),
                                      muonLabel=cms.InputTag("looseMuons"),
                                      photonLabel=cms.InputTag("slimmedPhotons"),
                                      VertexLabel=cms.InputTag("offlineSlimmedPrimaryVertices"),
                                      genParticleLabel=cms.InputTag("prunedGenParticles"),
                                      pileupSummary = cms.InputTag("slimmedAddPileupInfo"),
                                      Cand3MuLabel=cms.InputTag("ThreeMuonsVtxKalmanFit"),
                                      triggerResults = cms.InputTag("TriggerResults", "", "HLT"),
                                      objects = cms.InputTag("unpackedPatTrigger"),
                                      AlgInputTag = cms.InputTag( "gtStage2Digis" )
                                      
)




process.Tau3MuSkim = cms.Path(process.ThreeMuonSelSeq*
                              process.unpackedPatTrigger*
                              process.TreeMakerBkg
                     )





