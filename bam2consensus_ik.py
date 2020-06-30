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

parser.add_argument ('-d',
                '--mindepth',
                help='Minimal depth needed (default: 1)',
                default=1,
                type=int,
                required=False)

args = parser.parse_args()

#create directory when the one given by -o doesn't exist
Non_existent = args.out_dir
if not os.path.exists(Non_existent):
   os.makedirs(Non_existent)

if __name__ == '__main__':
   print ("Ya-! Yattazo! Hatsudou shitazo!")
   for filename in os.listdir(args.input_dir):
        file = filename
        file = file.replace(".bam", "")
        if filename.endswith(".bam"):
           print("Working on " + file)
           command_extract_consensus = "python Scripts/bam2consensus.py -i {}{}.bam -o {}{}.fasta -d {}" .format(args.input_dir, file, args.out_dir, file, args.mindepth)
           os.system(command_extract_consensus)       
