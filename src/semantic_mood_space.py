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

from sklearn.feature_extraction.text import TfIdfVectorizer
from lastfm import kept_mood_list, load_dataset


PATH = "../data/lastfm/"


def document_term_matrix():
    """
        construct a sparse tf-idf matrix which consists of tracks as columns
        and mood tags as rows [1], [2]

        Args:

        Returns:
            X:

        [1] Cyril François Laurier et al. Automatic Classification of musical
        mood by content-based analysis. PhD thesis, Universitat Pompeu Fabra,
        2011.

        [2] Saari, Pasi, and Tuomas Eerola. "Semantic computing of moods based
        on tags in social media of music." IEEE Transactions on Knowledge and
        Data Engineering 26.10 (2014): 2548-2560.
    """

    terms_list = kept_mood_list()
    tfidf = TfIdfVectorizer(vocabulary=terms_list)

    X = tfidf.fit_transform()

    return X.T


def mood_space():
    """
    """

    # read data from lastfm directory
    data = load_dataset(PATH)
