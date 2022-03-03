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
                metavar='threads',
                help='Max amount of threads',
                default=10,
                type=int,
                required=False)

parser.add_argument ('-m',
                '--min_read_length',
                metavar='min_read_length',
                help='Minimal read length used for assembly',
                default=1000,
                type=int,
                required=False)

parser.add_argument ('-ov',
                '--min_overlap_length',
                metavar='min_overlap_length',
                help='Minimal overlap length used in assembly',
                default=500,
                type=int,
                required=False)

parser.add_argument ('-srq',
                '--stop_read_quality',
                help='Stop correction when too many reads are of low quality',
                default=True,
                type=str,
                required=False)


args = parser.parse_args()

#create directory when the one given by -o doesn't exist
Non_existent = args.out_dir
if not os.path.exists(Non_existent):
   os.makedirs(Non_existent)

if __name__ == '__main__':
   for filename in os.listdir(args.input_dir):
      file = filename
      file = file.replace(".fastq", "")
      if filename.endswith(".fastq"):
         command_canu_correct_1 = "canu -d {}{} -correct coroutcoverage=500 cormincoverage=0 cormhapsensitivity=high -p {} genomeSize=1000 stopOnReadQuality={} -maxthreads={} minreadlength={} minoverlaplength={} -usegrid=false -maxmemory=25000 -batmemory=25000 -nanopore-raw {}{}.fastq" .format(args.out_dir, file, file, args.stop_read_quality, args.threads, args.min_read_length, args.min_overlap_length, args.input_dir, file)
         os.system(command_canu_correct_1)

