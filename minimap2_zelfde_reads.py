#import
import argparse
import os

#command line options
parser = argparse.ArgumentParser()
parser.add_argument ('-ir',
                '--input_reads',
                metavar='input_reads',
                help='Path to input reads',
                required=True)

parser.add_argument ('-r',
                '--reference_dir',
                metavar='input_directory',
                help='Path to input directory of the reference',
                required=True)

parser.add_argument ('-o',
                '--out_dir',
                metavar='output_directory',
                help='Path to output directory',
                required=True)


args = parser.parse_args()

#create directory when the one given by -o doesn't exist
Non_existent = args.out_dir
if not os.path.exists(Non_existent):
   os.makedirs(Non_existent)

#run
if __name__ == '__main__':
   for filename in os.listdir(args.reference_dir):
      file = filename
      file = file.replace(".fasta", "")
      if filename.endswith(".fasta"):
          command_minimap2 = "minimap2 -a {}{}.fasta {} > {}{}.sam" .format(args.reference_dir, file, args.input_reads, args.out_dir, file)
          os.system(command_minimap2)


