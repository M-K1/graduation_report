#importeer meneer
import argparse
import os

#command line options
parser = argparse.ArgumentParser()
parser.add_argument ('-r',
                '--input_reads_dir',
                metavar='input_directory',
                help='Path to input directory of the reads',
                required=True)

parser.add_argument ('-ref',
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

#let's do this shit, shall we?
if __name__ == '__main__':
   for filename in os.listdir(args.input_reads_dir):
      file = filename
      file = file.replace(".fastq", "")
      if filename.endswith(".fastq"):
          command_minimap2 = "minimap2 -a {}{}.fasta {}{}.fastq > {}{}.sam" .format(args.reference_dir, file, args.input_reads_dir, file, args.out_dir, file)
          os.system(command_minimap2)

