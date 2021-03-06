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
	parser.add_argument('-f','--file', help='GBS raw data', type=str)
	parser.add_argument('-p','--pe', help='input folder', type=str)
	parser.add_argument('-o', '--output', help='output folder', type=str)
    

	return parser


def mapping1(inputfile, pe, file, outputfile):
	enzyme = "C(A|T)GC" #ApeKI
	with open (inputfile) as f:
		for i in f:
			i = i[:-1].split("\t")
			barcode = i[0]
			id = i[1]

			#command = "zcat " + file + " | bioawk -c fastx '{if($seq~/^" + barcode + enzyme + "/){print " + '"' + "@" + '"' + "$name" + '"' + " " + '"' + "$comment" + '"' + "\\n" + '"' + "$seq" + '"' + "\\n+\\n" + '"' + "$qual}}' |gzip - > " + outputfile + "/" + id + "_1.fq.gz &"
			command1 = "seqkit seq --name --only-id " + pe + "/" + id + "_cut_1.fq.gz | seqkit grep --pattern-file - " + file + " -o " + outputfile + "/" + id + "_2.fq.gz &"
			print (command1)
			#zcat $files | bioawk -cfastx '{if($seq~/^'"$line"'/){print "@"$name" "$comment"\n"$seq"\n+\n"$qual}}' |gzip -c - > $3"/"$filename"_f"$n"_1_fastq.txt.gz" &
			#zcat $3"/"$filename"_f"$n"_1_fastq.txt.gz" |cutadapt -u $l -o $4"/"$filename"_f"$n"_1_fastq.txt.gz" - &	
			#seqkit seq --name --only-id $3"/"$filename"_f"$n"_1_fastq.txt.gz" | ~/BIGDATA-1/ymhuang/software/seqkit grep --pattern-file - $files2 -o $4"/"$filename"_f"$n"_2_fastq.txt.gz" &



def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	
	mapping1(args['input'], args['pe'], args['file'], args['output'])


if __name__ == "__main__":
	main()
