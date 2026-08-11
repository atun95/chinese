FROM python:3.10-slim

WORKDIR /app

# Cài đặt curl và Node.js (cần thiết nếu sử dụng package.json/npm)
RUN apt-get update && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements và cài đặt Python dependencies
COPY requirements.txt .
# Bỏ qua cài đặt pathlib và datetime vì đây là các thư viện mặc định của Python, 
# chỉ cài đặt streamlit (và các package hợp lệ khác nếu có)
RUN grep -v -E '^(pathlib|datetime)$' requirements.txt > req_filtered.txt && pip install --no-cache-dir -r req_filtered.txt

# Copy package.json và cài đặt Node dependencies
COPY package.json .
# Cài đặt npm nếu có package-lock.json hoặc package.json
RUN npm install

# Copy toàn bộ mã nguồn vào container
COPY . .

# Expose port mặc định của Streamlit
EXPOSE 8501

# Chạy ứng dụng Streamlit
CMD ["streamlit", "run", "a.py", "--server.port=8501", "--server.address=0.0.0.0"]
