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
process.GlobalTag.globaltag = '102X_dataRun2_v13' #data_rereco 
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#Begin processing the 25271st record. Run 320012, Event 56448719, LumiSection 36 on stream 0 at 20-Apr-2020 18:53:30.862 CEST
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_1.root',
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_2.root',
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_3.root',
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_4.root',
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_5.root',
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_6.root',
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_7.root',
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_8.root',
        #'file:///lustre/cms/store/user/fsimone/DoubleMuonLowMass/selected_Run2017C_Mini/200702_170507/0000/pickevents_9.root',
        #data2017C --> /DoubleMuonLowMass/Run2017C-17Nov2017-v1/MINIAOD
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/17Nov2017-v1/60000/DA4C28DA-55EC-E711-9AB0-A4BF0126D1BB.root',
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/17Nov2017-v1/60000/DA23EEFA-5FED-E711-84E4-1866DA87EE25.root',
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/17Nov2017-v1/60000/D8D859E9-E4EC-E711-91D6-842B2B42B582.root',
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/17Nov2017-v1/60000/C8A898B7-85ED-E711-B9BA-0CC47A00934A.root',
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/17Nov2017-v1/60000/C83C4220-1DEC-E711-9FB0-3417EBE7446B.root',
        'root://xrootd-cms.infn.it///store/data/Run2017C/DoubleMuonLowMass/MINIAOD/17Nov2017-v1/60000/C6FB4CCA-32EC-E711-AA06-00266CF3E0BC.root',

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





