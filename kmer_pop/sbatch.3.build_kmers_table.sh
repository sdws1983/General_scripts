#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p scpu-p1 
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1
export LD_LIBRARY_PATH="/public/fzjl/zhanglab/miniconda3/envs/ont-tombo/lib/:$LD_LIBRARY_PATH"
~/software/kmerGWAS/bin/build_kmers_table -l kmers_list_paths.txt -k 31 -a kmer_list/Sh.line.kmers_to_use -o kmer_table/kmers_table
