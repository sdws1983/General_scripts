#!/usr/bin/env python

import sys
import argparse
import os
import textwrap

def version():
	v = "----"
	return v

def warning(*objs):
	print("WARNING: ", *objs, end='\n', file=sys.stderr)
	sys.exit()

def get_parser():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description=textwrap.dedent(version())
	)

	parser.add_argument('-i','--input', help='inputfile', type=str)
	parser.add_argument('-f','--ref', help='reference', type=str)
	parser.add_argument('-k','--know', help='knowsites', type=str)
	parser.add_argument('-o', '--output', help='output folder', type=str)
    

	return parser


def mapping1(inputfile, ref, know, outputfile):
		command1 = "java -Xmx100G -jar /home/jinlab/software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK.jar -T BaseRecalibrator -R " + ref + ' -I ' + inputfile + ' -o ' + outputfile + ".baseRec -bqsrBAQGOP 30 -knownSites " + know 
		print (command1)
		command2 = "java -jar /home/jinlab/software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK.jar -T PrintReads -R " + ref + " -I " + inputfile + ' -BQSR ' + outputfile + '.baseRec -o ' + outputfile + ".baseRec.bam"
		print (command2)
		#java -Xmx30G -jar /NAS7/home/shijunpeng/software/GATK/GenomeAnalysisTK.jar -T BaseRecalibrator -R /NAS6/shijunpeng/Jinlab/coix-genome-sequence/Coix_liangchengzhi_20180907/JLS_genome_scf_cor.fasta -I ./x002.bam_file_list.intervals.bam -knownSites ./samtools_SNPs/x002.bam_file_list.intervals.VQ20.bed -o ./x002.bam_file_list.intervals.baseRec -bqsrBAQGOP 30
		#java -Xmx20G -jar /NAS7/home/shijunpeng/software/GATK/GenomeAnalysisTK.jar -T PrintReads -R /NAS6/shijunpeng/Jinlab/coix-genome-sequence/Coix_liangchengzhi_20180907/JLS_genome_scf_cor.fasta -I ./x002.bam_file_list.intervals.bam -BQSR ./x002.bam_file_list.intervals.baseRec -o ./x002.bam_file_list.intervals.baseRec.bam

def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['ref'], args['know'], args['output'])


if __name__ == "__main__":
	main()
