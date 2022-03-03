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
   for filename in os.listdir(args.input_dir):
        file = filename
        file = file.replace(".bam", "")
        if filename.endswith(".bam"):
           command_index_bam = "samtools index {}{}.bam {}{}.bam.bai " .format(args.input_dir, file, args.input_dir, file)
           os.system(command_index_bam)
    

