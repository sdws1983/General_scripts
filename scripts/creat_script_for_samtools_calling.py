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
	parser.add_argument('-o', '--output', help='output folder', type=str)
    

	return parser


def mapping1(inputfile, ref, outputfile):
		command1 = "/data/jinlab/software/samtools-0.1.19/samtools mpileup -g -E -C50 -Q20 -q20 -DSuf " + ref + ' ' + inputfile + ' | /home/jinlab/software/samtools-0.1.19/bcftools/bcftools view -Nbcvg - > ' + outputfile + ".bcf"
		print (command1)
		command1 = "/data/jinlab/software/samtools-0.1.19/bcftools/bcftools view " + outputfile + ".bcf > " + outputfile + ".vcf"
		print (command1)
		command1 = """awk '{if(/^#/){print}else{if($6>=30){print}}}' """ + outputfile + ".vcf > " + outputfile + ".VQ30.vcf"
		print (command1)
		command1 = "bgzip -@ 72 -c " + outputfile + ".VQ30.vcf > " + outputfile + ".VQ30.vcf.gz"
		print (command1)
		command1 = "tabix " + outputfile + ".VQ30.vcf.gz"
		print (command1)
		#/public1/home/pg2034/ymhuang/software/samtools-0.1.19/samtools mpileup -g -E -C50 -Q20 -q20 -DSuf /public1/home/pg2034/z-reference/1-coix/JLS_genome_scf_cor.fasta ./1-GX.intervals.bam | /public1/home/pg2034/ymhuang/software/samtools-0.1.19/bcftools/bcftools view -Nbcvg - > ./1-GX_R1.bcf

def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['ref'], args['output'])


if __name__ == "__main__":
	main()
