import argparse
import os
import sys

# Create the parser
bc_parser = argparse.ArgumentParser(description='braincell cli utility')
subparsers = bc_parser.add_subparsers(help='sub-command help')

# create the parser for the "a" command
load_parser = subparsers.add_parser('load', help='load help')
load_parser.add_argument('file', type=open, help='file help')
args = bc_parser.parse_args()
