import argparse
from pydub import AudioSegment
from pydub.playback import play
import glob
import time

#
# usage: python main.py --input_file example_docs/test.txt
#        python main.py --input_file example_docs/test.txt --save 1
#
# Takes in a text file parses it and then speaks it using the
# LL Cool J lettering from that song. Samples must be in wav 
# format and should be names in a sequential alphabetical order
#

parser = argparse.ArgumentParser(
                    prog='LL_Speak_and_spell',
                    description='Converts strings to audio in the style of LL Cool J',
                    epilog='Lols')
parser.add_argument('--input_file', type=str,
                    required=True,
                    help='name/location of text file to speak')           # positional argument
parser.add_argument('--sample_dir', type=str,
                    default='example_samples/',
                    help='Location of alphabet samples')           # positional argument
parser.add_argument('--comma_pause', type=int,
                    default=300,
                    help='length of pause to insert for commas and equivalent punctuation')           # positional argument
parser.add_argument('--period_pause', type=int,
                    default=400,
                    help='length of pause to insert for periods and equivalent punctuation')           # positional argument
parser.add_argument('--save', type=int,
                     default=0,
                     help='Whether to save the stream or just play it')           # positional argument

args = parser.parse_args()
# Set some punctuation that should (maybe) trigger some pauses
periods = ('.', ';', ':')
commas = (',')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
samples = {}
for i, file in enumerate(sorted(glob.glob(f"{args.sample_dir}*.wav"))):
    samples[alphabet[i]] = AudioSegment.from_wav(file)

# read in file
document = ''
with open(args.input_file, encoding="utf-8") as fh:
    for line in fh:
        document += line.rstrip()

output = second_of_silence = AudioSegment.silent(duration=0)
#read it out
for letter in document:
    if letter in periods:
        output = output + AudioSegment.silent(duration=args.period_pause)
    elif letter in commas:
        output = output + AudioSegment.silent(duration=args.comma_pause)
    elif letter in samples:
        output = output + samples[letter]

# Should probably let the user decide if they want to play it
# or save it
if args.save:
    output.export("ll_says.wav", format="wav")
else:
    play(output)
