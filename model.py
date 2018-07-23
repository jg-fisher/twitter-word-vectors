from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        pass

    def fit(self, sentences, min_count=1):
        # word2vec fit words
        self.model = Word2Vec(sentences, min_count=min_count)
        self.words = self.model.wv.vocab
        self.X = self.model[[w for s in sentences for w in s]]

    def plot(self, n=10):

        # pca words for plotting
        pca = PCA(n_components=2)
        result = pca.fit_transform(self.X)
        n_result = result[:n]
        
        # visualize
        plt.scatter(n_result[:, 0], n_result[:, 1])

        for i, word in enumerate(self.words):
            if i == n - 1:
                break
            plt.annotate(word, xy=(n_result[i, 0], n_result[i, 1]))
        plt.show()
