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
   for filename in os.listdir(args.input_dir):
        file = filename
        file = file.replace(".sam", "")
        if filename.endswith(".sam"):
           print("Working on " + file + ".sam")
           command_samtools_view = "samtools view -h {}{}.sam | samtools stats | grep '^SN'| cut -f 2- > {}{}.txt" .format(args.input_dir, file, args.out_dir, file)
           os.system(command_samtools_view)       
