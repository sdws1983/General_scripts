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
		command = "samtools index -@ 72 " + inputfile
		print (command)
		command1 = "java -Xmx120G -jar /home/jinlab/software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK.jar -T RealignerTargetCreator -R " + ref + ' -I ' + inputfile + ' -o ' + outputfile + ".intervals -minReads 2 -nt 72"
		print (command1)
		command2 = "java -jar /home/jinlab/software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK.jar -T IndelRealigner -R " + ref + " -I " + inputfile + ' -targetIntervals ' + outputfile + '.intervals -o ' + outputfile + ".intervals.bam"
		print (command2)
		#java -jar /public1/home/pg2034/ymhuang/software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK.jar -T RealignerTargetCreator -R /public1/home/pg2034/z-reference/1-coix/JLS_genome_scf_cor.fasta -I $4"/"$filename"_f"$n".sorted.MD.bam" -o $4"/"$filename"_f"$n".intervals" -minReads 2 -nt 20
		#java -jar /public1/home/pg2034/ymhuang/software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK.jar -T IndelRealigner -R /public1/home/pg2034/z-reference/1-coix/JLS_genome_scf_cor.fasta -I $4"/"$filename"_f"$n".sorted.MD.bam" -targetIntervals $4"/"$filename"_f"$n".intervals" -o $5"/"$filename"_f"$n".intervals.bam"

def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['ref'], args['output'])


if __name__ == "__main__":
	main()
