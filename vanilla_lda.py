from time import time
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation


def txt2list(filename):
    print("Loading dataset from {} ...".format(filename))
    t0 = time()
    my_list = []
    with open(filename, 'r') as f:
        for line in f:
            my_list.append(line)
    print("{} entries loaded.\n".format(len(my_list)))
    print("done in %0.3fs." % (time() - t0))
    return my_list


def print_top_words(model, feature_names, num_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-num_top_words - 1:-1]])
        print(message)
    print()


def my_count_vectorizer(dataset, n_samples, max_df, min_df, max_features):
    data_samples = dataset[:n_samples]

    # Use tf (raw term count) features for LDA.
    print("Extracting tf features for LDA...")
    t0 = time()
    tf_vectorizer = CountVectorizer(max_df=max_df, min_df=min_df,
                                    max_features=max_features,
                                    stop_words='english')
    tf = tf_vectorizer.fit_transform(data_samples)
    print("done in %0.3fs.\n" % (time() - t0))
    return tf_vectorizer, tf


def my_lda(tf_vectorizer, tf, n_samples, n_features, n_components, n_top_words, max_iter):
    print("Fitting LDA models with tf features, n_samples={} and n_features={}...".format(n_samples, n_features))
    lda = LatentDirichletAllocation(n_components=n_components, max_iter=max_iter, learning_method='online',
                                    learning_offset=50., random_state=0)
    t0 = time()
    lda.fit(tf)
    print("done in %0.3fs.\n" % (time() - t0))

    print("Topics in LDA model:")
    tf_feature_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names, n_top_words)


def main():
    n_samples = 10000
    n_features = 1000
    n_components = 10
    n_top_words = 20
    max_df = 0.2
    min_df = 2
    max_iter = 20
    dataset = txt2list('machine_learning.txt')
    tf_v, tf = my_count_vectorizer(dataset, n_samples, max_df, min_df, n_features)
    my_lda(tf_v, tf, n_samples, n_features, n_components, n_top_words, max_iter)


if __name__ == '__main__':
    main()
