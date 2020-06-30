import argparse
import os
import csv

parser = argparse.ArgumentParser()
parser.add_argument ('-i',
                '--input_dir',
                metavar='input_directory',
                help='Path to input directory',
                required=True)

args = parser.parse_args()

if __name__ == '__main__':
   print ("Ya-! Yattazo! Hatsudou shitazo!")
   for filename in os.listdir(args.input_dir):
      file = filename
      file = file.replace(".fastq", "")
      if filename.endswith(".fastq"):
          command_tellen = " echo $(cat {}{}.fastq | wc -l)/4|bc " .format(args.input_dir, file)
          print(file + " reads:")
          os.system(command_tellen)
          