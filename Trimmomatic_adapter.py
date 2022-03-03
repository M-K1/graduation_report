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

parser.add_argument ('-T',
                '--Tailing',
                metavar='Tailing_quality',
                help='Phred score to trim end of read with',
                default=5,
                type=int,
                required=False)

parser.add_argument ('-M',
                '--Min_len',
                metavar='Minimal_length_of_read',
                help='The minimal length a read should have after trimming',
                default=20,
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
        file = file.replace("_R1_001.fastq.gz", "")
        if filename.endswith("R1_001.fastq.gz"):
           print("Working on " + file + ".fastq.gz")
           command_run_trimmomatic = "trimmomatic PE -baseout {}{}.fastq.gz -threads 20 {}{}_R1_001.fastq.gz {}{}_R2_001.fastq.gz ILLUMINACLIP:/home/matthijskon/Data/Illumina_Run_43/adapter_seq.fa:1:20:10 TRAILING:{} MINLEN:{} SLIDINGWINDOW:4:20" .format(args.out_dir, file, args.input_dir, file, args.input_dir, file, args.Tailing, args.Min_len)
           os.system(command_run_trimmomatic)
       

