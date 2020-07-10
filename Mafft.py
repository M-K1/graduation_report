import argparse
import os

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
      file = file.replace(".fasta", "")
      if filename.endswith(".fasta"):
         command_mafft = "mafft --maxiterate 1000 --localpair {}{}.fasta > {}{}_aln.fasta" .format(args.input_dir, file, args.input_dir, file)
         os.system(command_mafft)

