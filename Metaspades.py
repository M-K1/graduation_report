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

parser.add_argument ('-t',
                '--threads',
                metavar='amount_of_threads',
                help='Threads to be used during assembly',
                default=10,
                type=int,
                required=False)


args = parser.parse_args()

#create directory when the one given by -o doesn't exist
Non_existent = args.out_dir
if not os.path.exists(Non_existent):
   os.makedirs(Non_existent)

if __name__ == '__main__':
   for filename in os.listdir(args.input_dir):
        file = filename
        if filename.endswith(".fastq"):
         file = file.replace("_1P.fastq", "")
        else:
         file = file.replace("_1P.fastq.gz","")
        if filename.endswith("_1P.fastq.gz"):
           print("Working on " + file + ".fastq.gz")
           command_run_MetaSPAdes = "metaspades.py -1 {}{}_1P.fastq.gz -2 {}{}_2P.fastq.gz -t {} -o {}/{}" .format(args.input_dir, file, args.input_dir, file, args.threads, args.out_dir, file)
           os.system(command_run_MetaSPAdes)
        if filename.endswith("_1P.fastq"):
           print("Working on " + file + ".fastq")
           command_run_MetaSPAdes = "metaspades.py -1 {}{}_1P.fastq -2 {}{}_2P.fastq -t {} -o {}/{}" .format(args.input_dir, file, args.input_dir, file, args.threads, args.out_dir, file)
           os.system(command_run_MetaSPAdes)



