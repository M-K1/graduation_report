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
           command_run_qualimap = "qualimap bamqc -bam {}{}.bam -outdir {}{}/" .format(args.input_dir, file, args.out_dir, file)
           os.system(command_run_qualimap)
