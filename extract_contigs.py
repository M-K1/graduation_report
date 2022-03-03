import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument ('-ic',
                '--input_contigs_dir',
                metavar='input_directory',
                help='Path to input directory',
                required=True)

parser.add_argument ('-l',
                '--list_names',
                metavar='list',
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
   for filename in os.listdir(args.input_dir):
        file = filename
        file = file.replace("_filtered.txt" , "")
        if filename.endswith(".txt"):
           print("Working on " + file + ".fasta")
           command_run_extract_contigs = "cut -c 1- {}{}.txt | xargs -n 1 samtools faidx {}{}.fasta > {}{}.fasta" .format(args.listnames, file, args.input_contigs_dir, file, args.out_dir, file)
           os.system(command_run_extract_contigs)
       




