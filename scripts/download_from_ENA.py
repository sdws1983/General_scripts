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

	parser.add_argument('-i','--input', help='data list', type=str)
	parser.add_argument('-t','--ttype', help='download type (single or project)', default="single", type=str)
	parser.add_argument('-s','--short', help='short id (from 000 to 009)', type=str)
	parser.add_argument('-p','--paired', help='paired or single', default="paired", type=str)
	parser.add_argument('-o','--output', help='output folder', type=str)
	parser.add_argument('-f','--ftp', help='using ftp download(yes or no)', type=str, default="yes")
    

	return parser


def mapping1(inputfile, ttype, short, paired, outputfile, ftp):
	if ttype == "single":
		if paired == "paired":
			cmd1 = "~/.aspera/cli/bin/ascp  -QT -l 3000m -P33001 -i " + \
			" ~/.aspera/cli/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq/" + \
			inputfile[:6] + "/" + short + "/" + inputfile + "/" + inputfile + "_1.fastq.gz " + outputfile
			cmd2 = "~/.aspera/cli/bin/ascp  -QT -l 3000m -P33001 -i " + \
			" ~/.aspera/cli/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq/" + \
			inputfile[:6] + "/" + short + "/" + inputfile + "/" + inputfile + "_2.fastq.gz " + outputfile
			if ftp == "yes":
				cmd1 = "wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/" + \
				inputfile[:6] + "/" + short + "/" + inputfile + "/" + inputfile + "_1.fastq.gz " + outputfile
				cmd2 = "wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/" + \
				inputfile[:6] + "/" + short + "/" + inputfile + "/" + inputfile + "_2.fastq.gz " + outputfile

			print (cmd1)
			print (cmd2)
		if paired == "single":
			cmd1 = "~/.aspera/cli/bin/ascp  -QT -l 3000m -P33001 -i " + \
			" ~/.aspera/cli/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq/" + \
			inputfile[:6] + "/" + short + "/" + inputfile + "/" + inputfile + ".fastq.gz " + outputfile
			if ftp == "yes":
				cmd1 = "wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/" + \
				inputfile[:6] + "/" + short + "/" + inputfile + "/" + inputfile + ".fastq.gz " + outputfile
                                
			print (cmd1)

	if ttype == "project":
		if paired == "paired":
			with open (inputfile) as f:
				for i in f:
					s = i[-2]
					cmd1 = "~/.aspera/cli/bin/ascp  -QT -l 3000m -P33001 -i " + \
					" ~/.aspera/cli/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq/" + \
					i[:6] + "/00" + s + "/" + i[:-1] + "/" + i[:-1] + "_1.fastq.gz " + outputfile
					cmd2 = "~/.aspera/cli/bin/ascp  -QT -l 3000m -P33001 -i " + \
					" ~/.aspera/cli/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq/" + \
					i[:6] + "/00" + s + "/" + i[:-1] + "/" + i[:-1] + "_2.fastq.gz " + outputfile
					if ftp == "yes":
						cmd1 = "wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/" + \
						i[:6] + "/00" + s + "/" + i[:-1] + "/" + i[:-1] + "_1.fastq.gz " + outputfile
						cmd2 = "wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/" + \
						i[:6] + "/00" + s + "/" + i[:-1] + "/" + i[:-1] + "_2.fastq.gz " + outputfile

					print (cmd1)
					print (cmd2)
		if paired == "single":
			with open (inputfile) as f:
				for i in f:
					s = i[-2]
					cmd1 = "~/.aspera/cli/bin/ascp  -QT -l 3000m -P33001 -i " + \
					" ~/.aspera/cli/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq/" + \
					i[:6] + "/00" + s + "/" + i[:-1] + "/" + i[:-1] + ".fastq.gz " + outputfile
					if ftp == "yes":
						cmd1 = "wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/" + \
						i[:6] + "/00" + s + "/" + i[:-1] + "/" + i[:-1] + ".fastq.gz " + outputfile
					print (cmd1)


def main():
	parser = get_parser()
	args = vars(parser.parse_args())

	if args['input'] is not None:
		print(version())

	mapping1(args['input'], args['ttype'], args['short'], args['paired'], args['output'], args['ftp'])


if __name__ == "__main__":
	main()
