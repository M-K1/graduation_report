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

parser.add_argument ('-s',
                '--sampling_seed',
                metavar='sampling seed',
                help='Sampling seed',
                default=100,
                type=int,
                required=False)

parser.add_argument ('-S',
                '--sampled_reads',
                metavar='sampled reads',
                help='The amount of reads to be sampled',
                default=100000,
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
        file = file.replace("_1P.fastq.gz", "")
        if filename.endswith("_1P.fastq.gz"):
           print("Working on " + file + ".fastq.gz")
           command_seqtk_subsample_1 = "seqtk sample -s{} {}{}_1P.fastq.gz {} > {}{}_1P.fastq" .format(args.sampling_seed, args.input_dir, file, args.sampled_reads, args.out_dir, file)
           command_seqtk_subsample_2 = "seqtk sample -s{} {}{}_2P.fastq.gz {} > {}{}_2P.fastq" .format(args.sampling_seed, args.input_dir, file, args.sampled_reads, args.out_dir, file)
           os.system(command_seqtk_subsample_1)
           os.system(command_seqtk_subsample_2)       

