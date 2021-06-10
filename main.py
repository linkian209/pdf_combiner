import argparse
import sys
import os
from PyPDF2 import PdfFileMerger

if __name__ == '__main__':
    # Set up argparse
    parser = argparse.ArgumentParser(description='Combine PDFs into one. If configured, will loop through directories an concatinate all pdfs in each.')
    parser.add_argument('files', type=str, nargs='+',
                        help='The files, in order, to combine')
    parser.add_argument('-d','--dir', action='store_true', help='Interpret the input as directories')
    parser.add_argument('-o', '--output', type=str, nargs='?', default='output.pdf',
                        help='Output filename, defaults to \'output.pdf\'')
    args = parser.parse_args()


    # Create merger
    merger = PdfFileMerger()

    # Set up loop inputs
    files = []
    if(args.dir):
        # For directories, get all files in each directory
        for cur_dir in args.files:
            for cur_file in os.listdir(path=cur_dir):
                if cur_file.endswith(".pdf"):
                    files.append(os.path.join(cur_dir, cur_file))
    else:
        # Otherwise, just get all pdfs in the input
        files = [x for x in args.files if x.endswith('.pdf')]

    # Sanity check
    if(len(files) == 0):
        print("No PDFs in input")
        sys.exit(1)
    
    # Now loop through and merge
    for cur_file in files:
        merger.append(cur_file)
        
    # Done!
    with open(args.output, 'wb') as f:
        merger.write(f)