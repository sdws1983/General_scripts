#!/bin/bash


t=24
k=31

cat Sh.line.txt| while read line; do
	#echo $line
	#mkdir -p tmp/${line}
	echo -e "~/software/kmerGWAS/external_programs/kmc_v3 -t${t} -k${k} -ci3 @input/${line}.inputfile.txt kmer_counts/${line}.output_kmc_canon tmp/${line} 1> logs/1.${line}.kmc_canon.1 2> logs/1.${line}.kmc_canon.2"
	echo -e "~/software/kmerGWAS/external_programs/kmc_v3 -t${t} -k${k} -ci0 -b @input/${line}.inputfile.txt kmer_counts/${line}.output_kmc_all tmp/${line} 1> logs/1.${line}.kmc_all.1 2> logs/1.${line}.kmc_all.2"
	echo -e "~/software/kmerGWAS/bin/kmers_add_strand_information -c kmer_counts/${line}.output_kmc_canon -n kmer_counts/${line}.output_kmc_all -k ${k} -o kmer_counts/${line}.kmers_with_strand"
done
