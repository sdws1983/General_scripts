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
		command1 = "java -Djava.io.tmpdir=/data -jar /home/jinlab/software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK.jar -T UnifiedGenotyper -R " + ref + ' -I ' + inputfile + ' -o ' + outputfile + " -A AlleleBalance -stand_call_conf 4.0 -mbq 20 -out_mode EMIT_ALL_CONFIDENT_SITES -glm BOTH -nt 80" 
		print (command1)
		#java -jar /home/yumin/2-software/GenomeAnalysisTK-3.8-0/GenomeAnalysisTK.jar -T UnifiedGenotyper	

def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['ref'], args['output'])


if __name__ == "__main__":
	main()
