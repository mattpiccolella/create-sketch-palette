import sys

COMPATIBLE_VERSION = "1.4"
PLUGIN_VERSION = "1.4"
PALETTE_FORMAT_STRING = "{\"compatibleVersion\":\"%s\",\"pluginVersion\":\"%s\",\"colors\":%s}"
COLOR_FORMAT_STRING = "{\"red\":%f,\"green\":%f,\"blue\":%f,\"alpha\":%f}"

def convert_colors_from_file(file_name):
    lines = [line.rstrip('\n') for line in open(file_name)]
    updated_color_string = "["
    for index, line in enumerate(lines):
        # If we include the pound sign, strip it.
        if len(line) == 7:
            line = line[1:len(line)]

        # Breaks the hex RGB code into chunks of two for each color.
        colors = [line[i:i+2] for i in range(0, len(line), 2)]
        red_val = int(colors[0], 16)
        green_val = int(colors[1], 16)
        blue_val = int(colors[2], 16)

        color_string = COLOR_FORMAT_STRING % ((red_val / 255.0), (green_val / 255.0), (blue_val / 255.0), 1.0)
        updated_color_string += color_string

        # Add a comma only if it's not the last item in the list.
        if index != len(lines) - 1:
            updated_color_string += ','

    updated_color_string += ']'
    return updated_color_string

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('USAGE: python %s [input_file_name] [output_file_name]' % sys.argv[0])

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    color_portion = convert_colors_from_file(sys.argv[1])

    palette_string = PALETTE_FORMAT_STRING % (COMPATIBLE_VERSION, PLUGIN_VERSION, color_portion)

    with open(output_file_name, 'w') as output_file:
        output_file.write(palette_string)
        print 'Successfully created %s' % (output_file_name)
