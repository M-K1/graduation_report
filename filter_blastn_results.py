import argparse
import os
import sys
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument ('-i',
                '--input_dir',
                metavar='input_directory',
                help='Path to input directory',
                required=True)

args = parser.parse_args()

#create directory when the one given by -o doesn't exist
#Non_existent = args.out_dir
#if not os.path.exists(Non_existent):
#   os.makedirs(Non_existent)

if __name__ == '__main__':
   print ("Ya-! Yattazo! Hatsudou shitazo!")
   for filename in os.listdir(args.input_dir):
      file = filename
      file = file.replace(".tsv", "_filtered.txt")   
      if filename.endswith(".tsv"):
         print("Working on " + filename)
         tsv_file = open(filename)
         read_tsv = pd.read_csv(filename, header=None, delimiter="\t")
         filter_quality = read_tsv.loc[read_tsv[2] >= 85.000]
         filter_length = filter_quality.loc[filter_quality[3] >= 500]
         filter_uniq_name = filter_length[0].unique()
         filter_uniq_name = pd.DataFrame(data=filter_uniq_name)
         if __name__ == '__main__':
            with open(file, 'w') as out:
               original_stdout = sys.stdout
               sys.stdout = out
               filter_uniq_name.to_csv(out, header=None, index=None, sep='\t', mode='a')
               sys.stdout = original_stdout
      