
from flask import Flask, request, jsonify
import faiss
import numpy as np
import psycopg2

app = Flask(__name__)

# 初始化 FAISS 索引
dimension = 128  # 假設降維後特徵向量為 128 維
index = faiss.IndexFlatL2(dimension)

@app.route('/verify', methods=['POST'])
def verify_image():
    data = request.json
    feature_vector = np.array(data['feature_vector']).astype('float32')
    
    # 查詢相似度
    D, I = index.search(np.expand_dims(feature_vector, axis=0), k=1)
    similarity_score = 1 - D[0][0] / 100  # 簡單轉換為相似度
    
    return jsonify({
        "similarity_score": similarity_score,
        "matched_image_id": int(I[0][0])
    })

if __name__ == '__main__':
    app.run(debug=True)
