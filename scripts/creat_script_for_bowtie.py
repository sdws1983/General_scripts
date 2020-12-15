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
    

	return parser


def mapping1(inputfile, trim, ref, outputfile):
	with open (inputfile) as f:
		for i in f:
                    i = i[:-1].split("\t")
                    name = i[0]
                    id = i[1]
                    command1 = "bowtie -m 1 -v 2 -p 72 -S --chunkmbs 1024 " + ref + " -1 " + trim + "/" + name + "_1P.fq -2 " + trim + "/" + name + "_2P.fq " + outputfile + "/" + name + ".sam > " + outputfile + "/" + name + ".log"
                    print (command1)


def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['trim'], args['ref'], args['output'])


if __name__ == "__main__":
	main()
