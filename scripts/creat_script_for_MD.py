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
        parser.add_argument('-i','--input', help='bam file folder', type=str)
        parser.add_argument('-o','--output', help='MD output file', type=str)
        parser.add_argument('-r','--remove', help='remove duplication', type=str, default="false")
        
        return parser


def mapping1(inputfile, outputfile, remove):
	bam = os.popen("ls " + inputfile + "/*bam").read()[:-1].split("\n")
	all_input = ""
	for i in bam:
		i = i
		command1 = "samtools index -@ 72 " + i
		#print (command1)
		all_input = all_input + "I=" + i + " "
		#samtools index $3"/"$filename"_f"$n".sorted.bam" && java -Xmx100G -jar /public1/home/pg2034/ymhuang/software/GenomeAnalysisTK-3.8-0/picard.jar MarkDuplicates I=$3"/"$filename"_f"$n".sorted.bam" O=$4"/"$filename"_f"$n".sorted.MD.bam" M=$4"/"$filename"_f"$n".sorted.MD.metrics" AS=true VALIDATION_STRINGENCY=SILENT
	o = outputfile + ".MD.bam"
	m = outputfile + ".MD.metrics"
	command2 = 'java -Xmx120G -jar /home/jinlab/software/GenomeAnalysisTK-3.8-0/picard.jar MarkDuplicates ' + all_input + ' O=' + o + " M=" + m + " REMOVE_SEQUENCING_DUPLICATES=" + remove + " AS=true VALIDATION_STRINGENCY=SILENT" + " TMP_DIR=" + os.popen("pwd").read()[:-1]
	print (command2)

def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['output'], args['remove'])


if __name__ == "__main__":
	main()
