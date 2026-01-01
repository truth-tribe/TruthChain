
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compare_phash(phash1, phash2):
    # 計算漢明距離
    return sum(c1 == c2 for c1, c2 in zip(phash1, phash2)) / len(phash1)

def compare_feature_vectors(vec1, vec2):
    return cosine_similarity([vec1], [vec2])[0][0]

if __name__ == "__main__":
    # 假設已經從資料庫讀取特徵
    phash_original = "1010101010101010..."
    phash_suspect = "1010101011101010..."
    print("pHash Similarity:", compare_phash(phash_original, phash_suspect))

    vec_original = np.random.rand(128)
    vec_suspect = np.random.rand(128)
    print("Feature Vector Similarity:", compare_feature_vectors(vec_original, vec_suspect))
