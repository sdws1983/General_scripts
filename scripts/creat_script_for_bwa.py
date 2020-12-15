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

	parser.add_argument('-i','--input', help='barcode file, col1 is bacode, col2 is id', type=str)
	parser.add_argument('-t','--trim', help='clean data folder', type=str)
	parser.add_argument('-f','--ref', help='reference', type=str)
	parser.add_argument('-p','--paired', help='paired or single', type=str, default="paired")
	parser.add_argument('-o', '--output', help='output folder', type=str)
    

	return parser


def mapping1(inputfile, trim, ref, paired, outputfile):
	with open (inputfile) as f:
		for i in f:
			i = i[:-1].split("\t")
			name = i[0]
			id = i[1]
			if paired == "paired":
				command1 = "bwa mem -t 72 -R " + '"@RG\\tID:' + id + '\\tSM:' + id + '\\tPL:illumina\\tLB:' + id + '" ' + ref + \
				" " + trim + "/" + name + ".trimmed_1.fq.gz " + trim + "/" + name + ".trimmed_2.fq.gz | samtools view -@ 72 -bS -q 20 - | samtools sort -@ 72 -T " + \
				outputfile + "/"+ name + " -o " + outputfile + "/" + name + ".q20.sorted.bam -"
			else:
				command1 = "bwa mem -t 72 -R " + '"@RG\\tID:' + id + '\\tSM:' + id + '\\tPL:illumina\\tLB:' + id + '" ' + ref + \
				" " + trim + "/" + name + ".trimmed.fq.gz | samtools view -@ 72 -bS -q 20 - | samtools sort -@ 72 -T " + \
				outputfile + "/"+ name + " -o " + outputfile + "/" + name + ".q20.sorted.bam -"
			print (command1)
			#bwa mem -t 24 -M -R "@RG\tID:$name\tSM:$name\tPL:illumina\tLB:$name" /public1/home/pg2034/1-coix/3-Chro-coix/4-Chr-v3-used/z-genome-file/BJCoxi_reference.V1.fasta $5"/"$filename"_f"$n"_1P.fq.gz" $5"/"$filename"_f"$n"_2P.fq.gz"| ~/0-software/samtools-1.8/samtools view -bS -q20 - |~/0-software/samtools-1.8/samtools sort -T $filename"_v1_f"$n -o $6"/"$filename"_f"$n".sorted.bam" - 


def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['trim'], args['ref'], args['paired'], args['output'])


if __name__ == "__main__":
	main()
