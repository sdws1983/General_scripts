#!/bin/bash

header="#!/bin/bash
#PBS -q workq
#PBS -j oe
#PBS -l nodes=1:ppn=10

source /share/home/off_huangyumin/.bashrc
cd \$PBS_O_WORKDIR

echo \"\${PBS_JOBID}.\${PBS_JOBNAME}.\${PBS_O_WORKDIR}\" > ~/qsub_task/job.\`date +\"%Y-%m-%d_%H-%M-%s%N\"\`

exec 1>job.\${PBS_JOBID}.\${PBS_JOBNAME}.stdout
exec 2>job.\${PBS_JOBID}.\${PBS_JOBNAME}.stderr

"

prefix="ROC22"
R=1
Q=1
n=1
m=6

for chr in `seq 1 10`;do
  # 获取所有文件名
  files=($(ls data/*${chr}.fasta))

  # 对文件名进行排序
  sorted_files=($(echo "${files[@]}" | tr ' ' '\n' | sort -n))

  # 遍历所有文件
  for i in "${!sorted_files[@]}"; do
    file1=${sorted_files[$i]}
    # 遍历后面的文件
    for j in "${sorted_files[@]:$i+1}"; do
      if (( n == 1 || n % m == 0 )); then
          t=$n
          echo "$header" > run_aw_$t.sh   
      fi

      file2=$j
      # 处理文件
      #echo "处理 $file1 和 $file2"

      h1=`basename $file1|cut -d"#" -f1`
      h2=`basename $file2|cut -d"#" -f1`
      chr1=`basename $file1|cut -d"#" -f3|cut -d"." -f1`
      chr2=`basename $file2|cut -d"#" -f3|cut -d"." -f1`
      #echo $h1,$h2
      #echo $chr1,$chr2
    
      refprefix=${prefix}_${chr1}${h1}
      qprefix=${prefix}_${chr2}${h2}

      refgff=`echo $file1|sed 's/fasta/gff3/'`
      reffa=$file1

      qfa=$file2
      out=${prefix}_${chr1}${h1}_${chr2}${h2}
      echo -e "~/software/AnchorWave-1.1.1/anchorwave gff2seq -i $refgff -r $reffa -o ${refprefix}.${n}.cds.fa
minimap2 -x splice -t 10 -k 12 -a -p 0.4 -N 20 $qfa ${refprefix}.${n}.cds.fa > ${qprefix}.${n}.sam
minimap2 -x splice -t 10 -k 12 -a -p 0.4 -N 20 $reffa ${refprefix}.${n}.cds.fa > ${refprefix}.${n}.sam
~/software/AnchorWave-1.1.1/anchorwave proali -t 1 -i $refgff -as ${refprefix}.${n}.cds.fa -r $reffa -a ${qprefix}.${n}.sam -ar ${refprefix}.${n}.sam -s $qfa -n ${out}.anchors -R $R -Q $Q -o ${out}.alignment.maf -f ${out}.alignment.f.maf > ${out}.log
rm ${refprefix}.${n}.cds.fa ${qprefix}.${n}.sam ${refprefix}.${n}.sam" >> run_aw_${t}.sh

      n=$(($n+1))

    done
  done
done
