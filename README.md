# create-sketch-palette
A simple script to convert a list of hex color codes into a `.sketchpalette` file. The `.sketchpalette` format is taken from [sketch-palettes](https://github.com/andrewfiorillo/sketch-palettes), and you can add the files to Sketch using that library. 

I found it easier to do this than to manually select the colors in the Sketch color picker and then save the file, so I wrote the script.

## Usage
```bash
$ python create-sketch-palette.py [input_file_name] [output_file_name]
```

The input file should be a text file with a hex code on each line. The output file should end with the extension `.sketchpalette`. Sample input and output files are provided here.

## Why doesn't my file work?
I have hardcoded the version for sketch-palettes at the top of the file in two constants: `COMPATIBLE_VERSION` and `PLUGIN_VERSION`. If for some reason your file doesn't load into Sketch, it's likely because these version numbers need to be changed.