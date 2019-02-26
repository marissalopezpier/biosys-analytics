#!/usr/bin/env python3
"""
Author : Marissa Pier <mal1@email.arizona.edu>
Date   : 2.25.2019
Purpose: Python program to firstlines program
"""
import os
import sys

def main():
	args = parse_args()

	for d in args.directories:
		if not os.path.isdir((d)):
			warn('"{}" is not a directory'.format(d))
			continue
		print(d)
		line2file = {}
		for filename in os.listdir(d):
			filepath = os.path.join(d,filename)
			f = open(filepath)
			first_line = f.readline()
			f.close()
			first_line = first_line.rstrip()
			line2file[first_line] = filename
		sorted_lines = sorted(line2file.keys())
		for line in sorted_lines:
			print_line( line, line2file[line], args.w )

def print_line( line, file, length ):
	ndots = length - len(line) - len(file)
	print(line + " " + "."*ndots + " " + file)

def warn( message ):
	print(message,file=sys.stderr)

def parse_args():
	from argparse import ArgumentParser
	parser = ArgumentParser()# description='' )
	parser.add_argument('-w',metavar='int',type=int,default=50)
	parser.add_argument('directories',metavar='DIR',nargs='+')
	args = parser.parse_args()
	return args

if __name__=='__main__':
	main()

