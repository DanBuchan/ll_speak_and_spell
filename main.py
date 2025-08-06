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

def get_document(file):
    document = ''
    with open(file, encoding="utf-8") as fh:
        for line in fh:
            document += line.rstrip()
    return document

def get_ordered_samples(sample_dir):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    samples = {}
    for i, file in enumerate(sorted(glob.glob(f"{sample_dir}*.wav"))):
        samples[alphabet[i]] = AudioSegment.from_wav(file)
    return samples

def render_audio(samples, document, period_pause, comma_pause):
    periods = ('.', ';', ':')
    commas = (',')
    audio = AudioSegment.silent(duration=0)
    #read it out
    for letter in document:
        if letter is '1':
            audio = audio + samples['o']
            audio = audio + samples['n']
            audio = audio + samples['e']
        if letter is '2':
            audio = audio + samples['t']
            audio = audio + samples['w']
            audio = audio + samples['o']
        if letter is '3':
            audio = audio + samples['t']
            audio = audio + samples['h']
            audio = audio + samples['r']
            audio = audio + samples['e']
            audio = audio + samples['e']
        if letter is '4':
            audio = audio + samples['f']
            audio = audio + samples['o']
            audio = audio + samples['u']
            audio = audio + samples['r']
        if letter is '5':
            audio = audio + samples['f']
            audio = audio + samples['i']
            audio = audio + samples['v']
            audio = audio + samples['e']
        if letter is '6':
            audio = audio + samples['s']
            audio = audio + samples['i']
            audio = audio + samples['x']
        if letter is '7':
            audio = audio + samples['s']
            audio = audio + samples['e']
            audio = audio + samples['v']
            audio = audio + samples['e']
            audio = audio + samples['n']
        if letter is '8':
            audio = audio + samples['e']
            audio = audio + samples['i']
            audio = audio + samples['g']
            audio = audio + samples['h']
            audio = audio + samples['t']
        if letter is '9':
            audio = audio + samples['n']
            audio = audio + samples['i']
            audio = audio + samples['n']
            audio = audio + samples['e']
        if letter is '0':
            audio = audio + samples['z']
            audio = audio + samples['e']
            audio = audio + samples['r']
            audio = audio + samples['o']    
        if letter in periods:
            audio = audio + AudioSegment.silent(duration=period_pause)
        elif letter in commas:
            audio = audio + AudioSegment.silent(duration=comma_pause)
        elif letter in samples:
            audio = audio + samples[letter]
    return audio

if __name__ == "__main__":
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
    samples = get_ordered_samples(args.sample_dir)
    document = get_document(args.input_file)
    output = render_audio(samples, document, args.period_pause, args.comma_pause)
    # Play or save the output
    if args.save:
        output.export("ll_says.wav", format="wav")
    else:
        play(output)