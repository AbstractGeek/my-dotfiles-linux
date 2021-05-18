#!/usr/bin/env python
import argparse
import os
import yaml
import re
import fileinput
from pprint import pprint

def get_line(uid, title):
    """A function to generate zettels links for the index."""
    return '[[{0}]]: {1}\n'.format(uid, title)

def get_existing(line, uid):
    """A function to get the old/existing zettel link."""
    match_string = r'\[\[{0}\]\]: [\W \w]*\s*\n'.format(uid)
    return re.search(match_string, line).group()

def main():
    """Runs through the main zettelkasten folder and creates index files/structure notes."""

    # Parse arguments and set useful variables
    parser = argparse.ArgumentParser(
        description=(
            'Checks if every note in the zettelkasten folder is present in the index file'))
    parser.add_argument("location", nargs='?', default=os.getcwd(), help="set zettelkasten location")
    args = parser.parse_args()
    base_folder = args.location

    # List zettels and index zettels
    zettels = []
    ind_zettels = []
    for file in os.listdir(base_folder):
        if file.endswith(".ind.md"):
            ind_zettels.append(file)
        elif file.endswith(".md"):
            zettels.append(file)

    # Make a dictionary of zettel UIDs and titles
    uid_titles = {}
    for z in zettels:
        with open(os.path.join(base_folder, z)) as f:
            front_matter = next(yaml.load_all(f, Loader=yaml.FullLoader))
        uid_titles[z.split('.')[0]] = front_matter['title']

    # Get index page text to find new/modified zettels
    ind_zettels.sort()
    index_content = []
    for iz in ind_zettels:
        with open(os.path.join(base_folder, iz)) as f:
            content = f.readlines()
        index_content = index_content + content

    # create replace and append lists
    uid_replace = []
    uid_append = []
    for uid in sorted(uid_titles.keys()):
        line_number = [num for num, line in enumerate(index_content) if uid in line]
        if line_number:
            for num in line_number:
                existing_line = get_existing(index_content[num], uid)
                new_line = get_line(uid, uid_titles[uid])
                if not existing_line == new_line:
                    uid_replace.append((existing_line, new_line))
        else:
            uid_append.append(get_line(uid, uid_titles[uid]))

    # replace existing lines with modified titles
    if uid_replace:   
        # Print replacement details
        print("Replacing titles of the following zettels (old - new):")
        pprint(uid_replace)
        # backup original
        original_file = os.path.join(base_folder, ind_zettels[0])
        backup_file = os.path.join(base_folder, ind_zettels[0]+'.bak')
        os.rename(original_file, backup_file)
        # rewrite original
        with open(backup_file, 'r') as input_file, open(original_file, 'w') as output_file:
            for line in input_file:
                replacement = [(old_line, new_line) for old_line, new_line in uid_replace if old_line in line]
                if replacement:
                    output_file.write(line.replace(replacement[0][0], replacement[0][1]))
                else:
                    output_file.write(line)

    # append new zettels into the index file
    if uid_append:
        # Print replacement details
        print("Appending the following new zettels:")
        pprint(uid_append)
        # Appending new zettels.
        with open(os.path.join(base_folder, ind_zettels[0]), 'a') as ind_file:
            ind_file.write('# New zettels \n')
            for line in uid_append:
                ind_file.write('- ' + line)
            ind_file.write('\n')



if __name__ == '__main__':
    main()
