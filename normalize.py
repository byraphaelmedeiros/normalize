"""File NORMALIZER and RENAME

This script allows the user to NORMALIZER and RENAME files in a directory
and your subdirectories.

Args:
    walk_directory (str): The directory path location


"""

import os
import sys
import string
import datetime

walk_directory = sys.argv[1]

print('File NORMALIZER and RENAME version 1.0')
print('by Raphael Medeiros (raphael.medeiros@gmail.com)\n')

print("Walk directory: {0}".format(walk_directory))


def format_filename(s):
    """
    Take a string and return a valid filename constructed from the string.
    Uses a whitelist approach: any characters not present in valid_chars are
    removed. Also spaces are replaced with underscores.

    Note: this method may produce invalid filenames such as ``, `.` or `..`
    When I use this method I prepend a date string like '2009_01_15_19_46_32_'
    and append a file extension like '.txt', so I avoid the potential of using
    an invalid filename.

    Ref1: https://support.office.com/en-us/article/invalid-file-names-and-file-types-in-onedrive-onedrive-for-business-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa#invalidfilefoldernames
    """

    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

    name = ''.join(c for c in s if c in valid_chars)
    name = ' '.join(name.split())  # double spaces

    # OneDrive (see Ref1)
    name = name.replace('_vti', '')

    name = name.replace('.lock', '')

    name = name.replace('CON', '')
    name = name.replace('PRN', '')
    name = name.replace('AUX', '')
    name = name.replace('NUL', '')

    name = name.replace('COM1', '')
    name = name.replace('COM2', '')
    name = name.replace('COM3', '')
    name = name.replace('COM4', '')
    name = name.replace('COM5', '')
    name = name.replace('COM6', '')
    name = name.replace('COM7', '')
    name = name.replace('COM8', '')
    name = name.replace('COM9', '')

    name = name.replace('LPT1', '')
    name = name.replace('LPT2', '')
    name = name.replace('LPT3', '')
    name = name.replace('LPT4', '')
    name = name.replace('LPT5', '')
    name = name.replace('LPT6', '')
    name = name.replace('LPT7', '')
    name = name.replace('LPT8', '')
    name = name.replace('LPT9', '')

    # name = name.replace(' ', '_')  # I don't like spaces in file names.

    return name


print('')
for root, subdirs, files in os.walk(walk_directory):
    print('\t- Working on {0}...'.format(root))

    for filename in files:
        old_file = os.path.join(root, filename)

        file_name, file_extension = os.path.splitext(filename)

        new_file_name = format_filename(file_name).strip()

        if len(new_file_name) <= 0:
            today = datetime.datetime.today()
            formatted_today = today.strftime('%Y-%m-%d_%H-%M-%S-%f')
            new_file_name = 'no_name_' + formatted_today + file_extension
        else:
            if len(new_file_name) > 120:  # OneDrive (see Ref1)
                new_file_name = new_file_name[:120]

            new_file_name = new_file_name + file_extension

        new_file = os.path.join(root, new_file_name)

        # print('\t- Length and File ({0}) {1}...'.format(len(new_file), new_file))

        os.rename(old_file, new_file)
