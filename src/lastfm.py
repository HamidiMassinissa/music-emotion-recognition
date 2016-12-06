#!/usr/bin/env python
# -*- coding: UTF-8 -*-
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

import pylast
import csv
import io

API_KEY = "f5bb0437db448307296ee1c3be1432ad"
API_SECRET = "3edf86f9a84cb011c5a03dfcfdc70b98"
username = "emodiderot"
password_hash = pylast.md5("ummto@1993")

PATH = "../data/"


def mood_list():
    """
    """

    l = []

    f = open(PATH+"russell_scaled.csv")
    mood_reader = csv.reader(f)

    for mood in mood_reader:
        l.append(mood[0])

    f.close()

    return l


def kept_mood_list():
    """
    """


def fetch_toptracks_persistent():
    """
    """

    # first, create a LastFMNetwork object providing the lastfm api key
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                                   username=username,
                                   password_hash=password_hash)

    # get the list of moods
    # l = mood_list()
    l = ["sad"]
    filename = PATH+"lastfm/toptracks.csv"
    with io.open(filename, mode='w', encoding='utf-8') as f:
        csv_writer = csv.writer(f)

        # fetching actual data from lastfm
        print("fetching data from lastfm  ...")
        for mood in l:
            print "processing mood tag" + mood + " ..."

            tag = network.get_tag(mood)
            topItems = tag.get_top_tracks(limit=1000)

            for topItem in topItems:
                track = topItem[0]
                csv_writer.writerow([mood, track.get_mbid(), track.get_artist(),
                                    track.get_title()])

        f.close()


def fetch_similar_tracks_persistent():
    """
    """

    # first, create a LastFMNetwork object providing the lastfm api key
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                                   username=username,
                                   password_hash=password_hash)



def fetch_toptags_persistent():
    """
        for each track fetched by means of getTopTracks for a particular mood
        tag and the similar tracks, get its top tags
    """

    # first, create a LastFMNetwork object providing the lastfm api key
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                                   username=username,
                                   password_hash=password_hash)





def load_dataset(path):
    """
    """

# get top tracks for a particular mood tag/term
fetch_toptracks_persistent()

# get similar tracks to the previously fetched ones

# for each track get its corresponding top tags
