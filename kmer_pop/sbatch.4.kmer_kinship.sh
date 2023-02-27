#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p scpu-p1 
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1
export LD_LIBRARY_PATH="/public/fzjl/zhanglab/miniconda3/envs/ont-tombo/lib/:$LD_LIBRARY_PATH"
~/software/kmerGWAS/bin/emma_kinship_kmers -t kmer_table/kmers_table -k 31 --maf 0.05 > kmer_output/kmers_table.kinship
