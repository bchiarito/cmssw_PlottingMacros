#! /bin/sh
echo 'I am here'
pwd
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
#cd /users/h2/chiarito/scratch/CMSSW_10_1_1/src
eval `scramv1 runtime -sh`
#cd /cms/chiarito/work/hcal/CMSSW_10_1_1/test
echo 'now trying root with' $1
root -b $1
