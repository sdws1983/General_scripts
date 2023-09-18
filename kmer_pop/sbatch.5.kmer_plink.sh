#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p scpu-p1 
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=28
export LD_LIBRARY_PATH="/public/fzjl/zhanglab/miniconda3/envs/ont-tombo/lib/:$LD_LIBRARY_PATH"
~/software/kmerGWAS/bin/kmers_table_to_bed -t kmer_table/kmers_table -k 31 -p kmer_output/kmers_table.phenotype --maf 0.05 --mac 5 -b 4000000000 -o kmer_output/kmers_plink_merged
#ls kmer_output/kmers_plink.*bed|awk -F '.bed' '{print $1}' |fgrep -v -w "kmer_output/kmers_plink.0" > kmer_output/batch.txt
#plink --merge-list kmer_output/batch.txt --make-bed --out kmer_output/kmer_merged --allow-extra-chr --double-id --bfile kmer_output/kmers_plink.0 --id-delim + --threads 28
#
