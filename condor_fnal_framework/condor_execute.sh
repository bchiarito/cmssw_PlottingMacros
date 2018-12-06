#! /bin/bash
echo 'echo : I am here'
pwd
ls
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
eval `scramv1 project CMSSW CMSSW_10_1_1`
cd CMSSW_10_1_1/src
eval `scramv1 runtime -sh`
echo ""
echo "echo : CMSSW: "$CMSSW_BASE
cd ../..
echo "echo : now copying with xrdcp_files.py"
python xrdcp_files.py $1
echo "echo : now running root analysis"
root -b analysis_all.C
echo ""
ls
echo "echo : done"
