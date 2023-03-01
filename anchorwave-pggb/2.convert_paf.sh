#!/bin/bash
#PBS -q workq
#PBS -j oe
#PBS -l nodes=1:ppn=1

source /share/home/off_huangyumin/.bashrc
cd $PBS_O_WORKDIR

echo "${PBS_JOBID}.${PBS_JOBNAME}.${PBS_O_WORKDIR}" > ~/qsub_task/job.`date +"%Y-%m-%d_%H-%M-%s%N"`

exec 1>job.${PBS_JOBID}.${PBS_JOBNAME}.stdout
exec 2>job.${PBS_JOBID}.${PBS_JOBNAME}.stderr


n = 1
for i in `ls *alignment.maf`;do
	prefix=`echo $i|awk -F '.maf' '{print $1}'`
	echo $prefix
	python2 ~/software/maf-convert sam -d $i | sed 's/[0-9]\+H//g' > ${prefix}.sam
	~/software/k8-0.2.4/k8-Linux ~/software/paftools.js sam2paf -L ${prefix}.sam > ${prefix}.paftools
	sed '1,2d' ${prefix}.sam |cut -f1-6 |paste - <(grep "^s" ${i}|cut -f1-6|xargs -n 12)|awk '{print $8"\t"$9"\t"$9+$10"\t"$14"\t"$15"\t"$15+$16"\t"$6"\t"$17"\t"$12"\t"$18}' > ${prefix}.cut
	paste <(awk '{print $4"\t"$10"\t"$5"\t"$6}' ${prefix}.cut) <(cut -f5- ${prefix}.paftools) > ${prefix}.paf
	n=$(($n+1))
done
