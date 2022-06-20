import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ("python")
options.register("input", "", VarParsing.multiplicity.singleton, VarParsing.varType.string, "")

process = cms.Process("GENANA")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

# Source
readFiles = [
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_0.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_1.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_2.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_3.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_4.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_5.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_6.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_7.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_8.root',
'root://cmseosmgm01.fnal.gov:1094//store/user/jferrant/siggen_Phi_omega/run_02_2022Feb14/miniaod/PHI_300_RUN_unweighted_events_Phi_300_omega_0p5/miniAOD_9.root'
]
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring( readFiles ),
#                            eventsToProcess = cms.untracked.VEventRange('1:206-1:206',)
)
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

# Dumps list of gen particles 
process.printList = cms.EDAnalyzer("ParticleListDrawer",
                     src = cms.InputTag("prunedGenParticles"),
                     maxEventsToPrint  = cms.untracked.int32(-1),
                     printVertex = cms.untracked.bool(True)
)

# Draws gen particle decay chain
process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
                                   src = cms.InputTag("prunedGenParticles"),                                                                 
                                   printStatus = cms.untracked.bool(True),
                                   printP4 = cms.untracked.bool(False),
                                   printPtEtaPhi = cms.untracked.bool(False),
                                   printVertex = cms.untracked.bool(False),
                                   printIndex = cms.untracked.bool(False),
                                   #status = cms.untracked.vint32( 3 )
)

process.path = cms.Path(process.printTree)
