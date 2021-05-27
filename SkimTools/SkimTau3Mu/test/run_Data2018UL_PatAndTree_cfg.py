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
process.GlobalTag.globaltag = '106X_dataRun2_v32' #data_UL 
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#Begin processing the 25271st record. Run 320012, Event 56448719, LumiSection 36 on stream 0 at 20-Apr-2020 18:53:30.862 CEST
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #data2017C_UL --> /DoubleMuonLowMass/Run2017C-09Aug2019_UL2017-v1/MINIAOD
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/610000/4603E970-ACF8-A640-9501-CB5727E9BD60.root',
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/610000/1D194051-678D-304B-B012-69E360D5071A.root',
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/FF50898A-594A-AF4A-81FA-9EF6B0AE5129.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/FC530C6B-0F8F-0C4E-8A07-3FD243545371.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/FC102916-691E-914F-80ED-0D51A09CFBA0.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/FB539E58-A888-FB47-90F1-BCBF34B6951F.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/FA2F1158-CFC5-E041-8936-CFD5CD0DCE0E.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/F9FAE2FB-4CD1-C943-B183-4492CB46550B.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/F944770B-93B1-4946-AD5C-67302FEEFF8F.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/F72DCED8-1E26-124C-ACBC-E989EDD93DE3.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/F698615F-5893-4542-A35C-E76DFDE6A881.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/F5F6CDC3-64E9-D54F-9B55-4BB0C8C477E9.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/F57F883E-60D2-AA4F-982C-B485BA53EE41.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/F53BBA28-0A1E-7048-AD3C-0881FD031FB6.root',
#        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/09Aug2019_UL2017-v1/60000/F42FAED4-E185-314A-978A-DD17FF21DA7A.root',

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
                                      isMcLabel = cms.untracked.bool(False),
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





