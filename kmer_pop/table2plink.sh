#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p scpu-p1 
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=24
export LD_LIBRARY_PATH="/public/fzjl/zhanglab/miniconda3/envs/ont-tombo/lib/:$LD_LIBRARY_PATH"
ldd ~/software/kmerGWAS/bin/kmers_table_to_bed

~/software/kmerGWAS/bin/kmers_table_to_bed -t ./kmer_table/all_combined.kmers_table2 -k 31 -p phenotypes.pheno --maf 0.05 --mac 18 -b 2000000000 -o plink_format/plink
