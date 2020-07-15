"""Wrapper for BFG"""

import os
import subprocess
import argparse


def main():
  parser = argparse.ArgumentParser(
            description='Wrapper script for cleaning up Git commits.',
            )
  #parser.add_argument('delete-files' )
  parser.add_argument('remove-text',)
   
  jar = os.path.abspath('bfg-1.13.0.jar')
  print(jar)




if __name__=='__main__':
  main()
