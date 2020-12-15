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
	parser.add_argument('-o', '--output', help='output folder', type=str)
	parser.add_argument('-g','--gtf', help='reference annotation file (gtf)', type=str)
    

	return parser


def mapping1(inputfile, trim, ref, outputfile, gtf):
	with open (inputfile) as f:
		for i in f:
			i = i[:-1].split("\t")
			name = i[0]
			id = i[1]

			command1 = "python ~/ymhuang/pipelines/flair/flair.py align -v1.3 -sam /usr/bin/samtools -t 72 -m ~/software/minimap2-2.17_x64-linux/minimap2 -g " + ref + " -r " + trim + "/" + name + " -o " + outputfile + "/" + name
			print (command1)
			command2 = "python ~/ymhuang/pipelines/flair/flair.py correct -t 72 -c /data/jinlab/reference/B73_AGPv4/Zea_mays.AGPv4.chromsizes -f " + gtf + " -g " + ref + " -q " + outputfile + "/" + name + ".bed -o " + outputfile + "/" + name
			print (command2)
			#command3 = "python ~/ymhuang/pipelines/flair/bin/bed_to_psl.py /data/jinlab/reference/B73_AGPv4/Zea_mays.AGPv4.chromsizes X837-N01_clean.fastq.gz_all_corrected.bed X837-N01_clean.fastq.gz_all_corrected.p " + gtf + " -g " + ref + " -q " + outputfile + "/" + name + ".bed -o " + outputfile + "/" + name
			#bwa mem -t 24 -M -R "@RG\tID:$name\tSM:$name\tPL:illumina\tLB:$name" /public1/home/pg2034/1-coix/3-Chro-coix/4-Chr-v3-used/z-genome-file/BJCoxi_reference.V1.fasta $5"/"$filename"_f"$n"_1P.fq.gz" $5"/"$filename"_f"$n"_2P.fq.gz"| ~/0-software/samtools-1.8/samtools view -bS -q20 - |~/0-software/samtools-1.8/samtools sort -T $filename"_v1_f"$n -o $6"/"$filename"_f"$n".sorted.bam" - 


def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['trim'], args['ref'], args['output'], args['gtf'])


if __name__ == "__main__":
	main()
