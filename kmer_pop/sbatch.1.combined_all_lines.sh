#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p scpu-p1 
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=2
export LD_LIBRARY_PATH="/public/fzjl/zhanglab/miniconda3/envs/ont-tombo/lib/:$LD_LIBRARY_PATH"
ldd ~/software/kmerGWAS/bin/list_kmers_found_in_multiple_samples
~/software/kmerGWAS/bin/list_kmers_found_in_multiple_samples -l all_combined.kmers_list_paths.txt -k 31 --mac 18 -p 0.2 -o kmer_list/all_combined.kmers_to_use
~/software/kmerGWAS/bin/build_kmers_table -l all_combined.kmers_list_paths.txt -k 31 -a kmer_list/all_combined.kmers_to_use -o kmer_table/all_combined.kmers_table
