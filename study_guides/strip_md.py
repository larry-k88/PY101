input_file = './SPOT wiki.md'
output_file = './SPOT_wiki_clean.md'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if not line.lstrip().startswith('>'):
            outfile.write(line)