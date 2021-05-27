import FWCore.ParameterSet.Config as cms

process = cms.Process('DsPhiPiSkim')

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
#process.load('DsPhiPiTreeMaker.DsPhiPiTreeMaker.DsPhiPiSkimAOD_cff')
#process.load('DsPhiPiTreeMaker.DsPhiPiTreeMaker.DsPhiPiMuMuPi_BParking_cff')
process.load('SkimTools.SkimPhiPi.DsPhiPiMuMuPi_miniAOD_cff')

process.GlobalTag.globaltag = '106X_mc2017_realistic_v8' #Ultra Legacy MC2017
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #Ultra Legacy MC DsPhiPi 2017 --> /DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v1/MINIAODSIM
        '/store/mc/RunIISummer19UL17MiniAOD/DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/100000/F9EA01FD-4ADD-4345-8C79-A0CF8C374874.root',
        #'/store/mc/RunIISummer19UL17MiniAOD/DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/100000/EAD02CB9-A464-BE44-8070-50D4DABCC748.root',
        #'/store/mc/RunIISummer19UL17MiniAOD/DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/100000/E5263AEA-98B5-8441-BDB0-824EF9B5DF50.root',
        #'/store/mc/RunIISummer19UL17MiniAOD/DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/100000/DC594D98-303A-674E-A6BD-7A919BD860F8.root',
        #'/store/mc/RunIISummer19UL17MiniAOD/DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/100000/CE4078D7-73C8-B545-ACC9-271DDDE50829.root',
        '/store/mc/RunIISummer19UL17MiniAOD/DsToPhiPi_ToMuMu_MuFilter_TuneCP5_13TeV-pythia8-evtgen/MINIAODSIM/106X_mc2017_realistic_v6-v1/100000/C1DFF8E6-A217-A749-9502-2744F3D43C88.root'

	)
)


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("Tree_PhiPi.root"))



process.unpackedPatTrigger = cms.EDProducer("PATTriggerObjectStandAloneUnpacker",
    patTriggerObjectsStandAlone = cms.InputTag( 'slimmedPatTrigger' ),
    triggerResults              = cms.InputTag( 'TriggerResults::HLT' ),
    unpackFilterLabels = cms.bool(True)
)

process.Tree3Mu = cms.EDAnalyzer("DsPhiPiTreeMakerMINI",
                                 isMcLabel = cms.untracked.bool(True),
                                 isAnaLabel = cms.untracked.bool(True),
                                 is2016Label = cms.untracked.bool(True),
                                 is2017Label = cms.untracked.bool(True),
                                 is2018Label = cms.untracked.bool(True),
                                 isBParkingLabel = cms.untracked.bool(False),
                                 #is3MuLabel = cms.untracked.bool(False),
                                 muonLabel=cms.InputTag("looseMuons"),
                                 VertexLabel=cms.InputTag("offlineSlimmedPrimaryVertices"),
                                 TracksLabel=cms.InputTag("LooseTrack"),
                                 genParticleLabel=cms.InputTag("prunedGenParticles"),
                                 #Cand3MuLabel=cms.InputTag("ThreeMuonsVtxKalmanFit"),
                                 Cand2Mu1TrackLabel=cms.InputTag("TwoMuonsOneTrackKalmanVtxFit"),
                                 DiMuonLabel=cms.InputTag("DiMuonsVtxFit"),
                                 pileupSummary = cms.InputTag("slimmedAddPileupInfo"),
                                 triggerResults = cms.InputTag("TriggerResults", "", "HLT"),
                                 #triggerSummary = cms.InputTag("hltTriggerSummaryAOD", "", "HLT"),
                                 objects = cms.InputTag("unpackedPatTrigger"),
                                 AlgInputTag = cms.InputTag( "gtStage2Digis" )
)



process.DsPhiPiSkim = cms.Path( process.TwoMuOneTrackSelSeq*
                                process.unpackedPatTrigger* 
                                process.Tree3Mu
)



