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
process.load('SkimTools.SkimPhiPi.DsPhiPiMuMuPi_BParking_cff')



process.GlobalTag.globaltag = '102X_dataRun2_v11'
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/270000/46876D1C-188D-7841-BE43-EEBD1DDDE57D.root',
        'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/270000/460356CA-50A9-7A46-AE3A-C0C0F623A20A.root',
        'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/00001/D8F22FCD-F590-8F40-B9C2-C3F2271120A2.root',
        'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/00001/DAA5A759-D480-8440-914D-EE76DB5B7ED6.root', 
        'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/00001/DB5545A3-E895-2443-8C3D-2E1295477478.root', 


        #'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/00001/D4353F7D-3875-5B46-BA93-9F4A43B260D1.root', 
        #'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/00001/D2F3BB3B-273F-AD44-8312-6BCD15707B24.root', 
        #'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/00001/D2A95E66-9D34-A742-86A8-A4DFFDE4BA2E.root', 
        #'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/00001/D273EE17-C930-E348-BE9B-FD6C7D3A098D.root', 
        #'root://cmsxrootd.fnal.gov//store/data/Run2018A/ParkingBPH4/MINIAOD/05May2019-v1/00001/D2472933-2798-CA47-A949-760303832EA2.root',
        #'root://xrootd-cms.infn.it//store/data/Run2017B/DoubleMuonLowMass/AOD/23Jun2017-v1/90000/FC4BB0C3-E358-E711-9EFE-0025904B739A.root',
        #'root://xrootd-cms.infn.it//store/data/Run2017F/DoubleMuonLowMass/AOD/09May2018-v1/80000/FEDF5D97-BEB0-E811-95BF-0CC47AD98B94.root',
        #'root://xrootd-cms.infn.it//store/data/Run2017F/DoubleMuonLowMass/AOD/09May2018-v1/80000/AECC4C56-BAB0-E811-B92A-008CFA1979AC.root'
        # 'root://xrootd-cms.infn.it//store/data/Run2018A/ParkingBPH3/AOD/05May2019-v1/100001/34DA0AAD-AA03-2D4D-9E3D-125B9508BCCB.root' 

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
                                 isMcLabel = cms.untracked.bool(False),
                                 isAnaLabel = cms.untracked.bool(True),
                                 is2016Label = cms.untracked.bool(True),
                                 is2017Label = cms.untracked.bool(True),
                                 is2018Label = cms.untracked.bool(True),
                                 isBParkingLabel = cms.untracked.bool(True),
                                 #is3MuLabel = cms.untracked.bool(False),
                                 muonLabel=cms.InputTag("looseMuons"),
                                 VertexLabel=cms.InputTag("offlineSlimmedPrimaryVertices"),
                                 TracksLabel=cms.InputTag("packedPFCandidates"),
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


