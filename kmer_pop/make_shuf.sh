#!/bin/bash
#SBATCH -o job.%j.out
#SBATCH -p scpu-p1 
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=24

<<!
shuf <(cat plink.*bim) -o 1M.shuf.bim -n 1000000
fgrep -f 1M.shuf.bim plink.0.bim > 1M.shuf.0.bim &
fgrep -f 1M.shuf.bim plink.1.bim > 1M.shuf.1.bim &
fgrep -f 1M.shuf.bim plink.2.bim > 1M.shuf.2.bim
wait

cut -f2 1M.shuf.0.bim > 1M.shuf.0.bim.sites &
cut -f2 1M.shuf.1.bim > 1M.shuf.1.bim.sites &
cut -f2 1M.shuf.2.bim > 1M.shuf.2.bim.sites
wait

plink --bfile plink.0 --recode --extract 1M.shuf.0.bim.sites --transpose --out 1M.shuf.0.out --threads 12 --memory 1000000
plink --bfile plink.1 --recode --extract 1M.shuf.1.bim.sites --transpose --out 1M.shuf.1.out --threads 12 --memory 1000000
plink --bfile plink.2 --recode --extract 1M.shuf.2.bim.sites --transpose --out 1M.shuf.2.out --threads 12

!


#cat 1M.shuf.*tped > 1M.shuf.cat.tped 
#cp 1M.shuf.0.out.tfam 1M.shuf.cat.tfam

plink --tfile 1M.shuf.cat --export vcf --out 1M.shuf.outvcf --threads 24

awk '{if(/^#/){print}else{for(i=1;i<=8;i++){printf $i"\t"};printf $9;for(i=10;i<=NF;i++){if($i==".\/."){printf "\t1\/1"}else{printf "\t"$i}};printf "\n"}}' 1M.shuf.outvcf.vcf > 1M.shuf.outvcf.recode.vcf
