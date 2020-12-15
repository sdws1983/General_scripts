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

	parser.add_argument('-i','--input', help='input folder', type=str)
	parser.add_argument('-o', '--output', help='output folder', type=str)
	parser.add_argument('-p', '--pattern', help='common pattern (default=.R1.fastq.gz)', type=str, default=".R1.fastq.gz")
        
    

	return parser


def mapping1(inputfile, outputfile, pattern):
        file_list = os.popen("ls " + inputfile + "/*gz").read()[:-1].split("\n")
        pattern2 = pattern.replace("1","2")
        for i in file_list:    
                if pattern in i:
                        pe = i.replace(pattern, pattern2)
                        output = outputfile + "/" + i.split("/")[-1].split(pattern)[0]
                        command1 = "cutadapt --cores=64 -a TACACTCTTTCCCTACACGACGCTCTTCCGATCT -A GTGACTGGAGTTCAGACGTGTGCTCTTCCGATCT -O 5 -e 0 --minimum-length 36 -o " + output + ".trimmed_1.fq.gz -p " + output + ".trimmed_2.fq.gz " + i + " " + pe
                        print (command1)
                else:
                        continue



def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	
	mapping1(args['input'], args['output'], args['pattern'])


if __name__ == "__main__":
	main()
