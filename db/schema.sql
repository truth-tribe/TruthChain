
-- 資料表：images
CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255),
    sha256_hash VARCHAR(64),
    phash VARCHAR(64),
    exif_data JSONB,
    feature_vector BYTEA, -- 存放壓縮後的特徵向量
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 資料表：verification_reports
CREATE TABLE verification_reports (
    id SERIAL PRIMARY KEY,
    image_id INT REFERENCES images(id),
    confidence_score FLOAT,
    tampering_risk VARCHAR(50),
    report_path VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
