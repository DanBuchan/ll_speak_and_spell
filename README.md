# LL's Speak And Spell

The A, The B, The C, The D, The E, The F...

Have you ever wanted LL Cool J to read out your texts? Now's your chance. Using no machine learning at all you can have LL Cool J recite any text you want. Just provide a text document in utf-8 and off he'll go

## Usage:

``` bash
usage: LL_Speak_and_spell [-h] --input_file INPUT_FILE
                          [--sample_dir SAMPLE_DIR]
                          [--comma_pause INT]
                          [--period_pause INT] [--save 1/0]

Converts strings to audio in the style of LL Cool J

options:
  -h, --help            show this help message and exit
  --input_file INPUT_FILE
                        name/location of text file to speak
  --sample_dir SAMPLE_DIR
                        Location of alphabet samples
  --comma_pause INT
                        length of pause to insert for commas and equivalent
                        punctuation
  --period_pause INT
                        length of pause to insert for periods and equivalent
                        punctuation
  --save 1/0           Whether to save the stream or just play it
```