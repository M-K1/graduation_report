import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument ('-i',
                '--input_dir',
                metavar='input_directory',
                help='Path to input directory',
                required=True)

parser.add_argument ('-o',
                '--out_dir',
                metavar='output_directory',
                help='Path to output directory',
                required=True)

args = parser.parse_args()

if __name__ == '__main__':
   print ("Ya-! Yattazo! Hatsudou shitazo!")
   for filename in os.listdir(args.input_dir):
      file = filename
      file = file.replace(".fastq", "")
      if filename.endswith(".fastq"):
          command_qcat = "qcat --trim --guppy -f {}/{}.fastq -b {}/{}/ -t 16" .format(args.input_dir, file, args.out_dir, file)
          os.system(command_qcat)

