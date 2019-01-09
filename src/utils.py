# ## Copyright (C) 2016 Massinissa Hamidi, Hossam Gaci, Van Luan Nguyen

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import json


def load_mood_tags(filename):
    lines = []
    f = open(filename)

    for line in f.readline():
        lines.append(line)

    f.close()

    return lines


def recursive_visiting(dir, method):
    """
    walks a directory, and executes a callback on each file

    Args:
        dir: the directory to walk through
        method: a method to be called on each file
    """

    dir = os.path.abspath(dir)
    for root, dirs, files in os.walk(dir):
        for dirname in dirs:
            recursive_visiting(dirname, method)
        for filename in files:
            filename = os.path.join(root, filename)
            print(filename)
            method(filename)


def moodtag_list(filename):
    """
    process json file so as to get track_id as well as the associated
    list of mood tags

    Args:
        filename: a file path.
    Returns:
        a list of (track_id, tags_list).
    """

    tags_list = []

    f = open(filename)
    data = json.load(f)

    track_id = data["track_id"]
    tags_list = [lst[0] for lst in data["tags"]]

    f.close()

    return (track_id, tags_list)
