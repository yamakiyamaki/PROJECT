# Create env
```
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
chmod +x Anaconda3-2024.10-1-Linux-x86_64.sh 
./Anaconda3-2024.10-1-Linux-x86_64.sh 
export PATH="$HOME/anaconda3/bin:$PATH"
source ~/.bashrc   # or ~/.zshrc, depending on what you're using
conda --version

conda create -n projectEnv python=3.11
conda activate projectEnv
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

---------------------------------------------------------
# How to add library
!! write library name in requirements.txt first.
conda activate projectEnv
pip install -r requirements.txt

---------------------------------------------------------

# How to run
In terminal 1
```
node proxy.js
```
In terminal 2
```
./llama-server -hf ggml-org/Qwen2.5-VL-3B-Instruct-GGUF --host 0.0.0.0 --port 8080
```
In terminal 3
```
conda activate projectEnv
./execute.sh
```
Access here by HMD: https://161.3.140.22.5000

### manualy
conda activate projectEnv
In a terminal, `python app.py`
In another terminal, `python main.py`
Access here: http://10.1.4.56:5000/ #! if you are in another machin you need to access different url shown on terminal(upper one)

### Maybe not neccessary
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 1 -nodes
- FR 
- Auvergne-Rhône-Alpes 
- Saint-Étienne

---------------------------------------------------------

# ToDo
Fine tune model to answer kid's mathematical question. Or choose another model. Maybe not VLM. 
Access flask by another device(HMD)

---------------------------------------------------------
# node.js setup(without using sudo and npm) to handle http as https
```
cd ~
mkdir -p nginx-prebuilt && cd nginx-prebuilt
curl -LO https://github.com/krallin/tini/releases/download/v0.19.0/tini-static-amd64
chmod +x tini-static-amd64
mv tini-static-amd64 nginx

node -v
npm -v

mkdir -p ~/llama-proxy-manual
cd ~/llama-proxy-manual

curl -L https://registry.npmjs.org/http-proxy/-/http-proxy-1.18.1.tgz -o http-proxy.tgz
tar -xzf http-proxy.tgz
mv package http-proxy

mkdir certs
openssl req -x509 -newkey rsa:2048 -sha256 -days 365 -nodes \
  -keyout certs/privkey.pem -out certs/fullchain.pem \
  -subj "/CN=localhost"

nano proxy.js << {{{{{{{{{{{{{{ !!!It is not command open file and paste this code
const https = require('https');
const http = require('http');
const fs = require('fs');
const httpProxy = require('./http-proxy/lib/http-proxy');

const proxy = httpProxy.createProxyServer({});

const options = {
  key: fs.readFileSync('./certs/privkey.pem'),
  cert: fs.readFileSync('./certs/fullchain.pem')
};

https.createServer(options, (req, res) => {
  if (req.url.startsWith("/v1/")) {
    proxy.web(req, res, { target: 'http://127.0.0.1:8080' });
  } else {
    res.writeHead(404);
    res.end("Not found");
  }
}).listen(8443, () => {
  console.log('✅ HTTPS proxy running at https://localhost:8443');
});
}}}}}}}}}}}}}}

curl -L https://registry.npmjs.org/eventemitter3/-/eventemitter3-4.0.7.tgz -o eventemitter3.tgz
tar -xzf eventemitter3.tgz
mv package node_modules
mv node_modules/eventemitter3* eventemitter3

mkdir -p node_modules  # Ensure the target folder exists
curl -L https://registry.npmjs.org/eventemitter3/-/eventemitter3-4.0.7.tgz -o eventemitter3.tgz
tar -xzf eventemitter3.tgz
mv package node_modules/eventemitter3

curl -L https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.15.6.tgz -o follow-redirects.tgz
tar -xzf follow-redirects.tgz
mv package node_modules/follow-redirects

node proxy.js
```
---------------------------------------------------------

# llama.cpp setup
### How to build
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp/
cmake -B build -DGGML_CUDA=ON
export CUDACXX="/usr/local/cuda/bin/n
export CUDACXX="/usr/local/cuda/bin/nvcc"
cmake -B build -DGGML_CUDA=ON
cd build/
make -j 24

### How to run
cd llama.cpp/build/bin/
./llama-server -hf ggml-org/Qwen2.5-VL-7B-Instruct-GGUF
hf: hugging face
[Pre quantized model list](https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md) --> We just need to use listed command
Models

#### Gemma 3
(tool_name) -hf ggml-org/gemma-3-4b-it-GGUF
(tool_name) -hf ggml-org/gemma-3-12b-it-GGUF
(tool_name) -hf ggml-org/gemma-3-27b-it-GGUF

#### SmolVLM
(tool_name) -hf ggml-org/SmolVLM-Instruct-GGUF
(tool_name) -hf ggml-org/SmolVLM-256M-Instruct-GGUF
(tool_name) -hf ggml-org/SmolVLM-500M-Instruct-GGUF
(tool_name) -hf ggml-org/SmolVLM2-2.2B-Instruct-GGUF
(tool_name) -hf ggml-org/SmolVLM2-256M-Video-Instruct-GGUF
(tool_name) -hf ggml-org/SmolVLM2-500M-Video-Instruct-GGUF

#### Pixtral 12B
(tool_name) -hf ggml-org/pixtral-12b-GGUF

#### Qwen 2 VL
(tool_name) -hf ggml-org/Qwen2-VL-2B-Instruct-GGUF
(tool_name) -hf ggml-org/Qwen2-VL-7B-Instruct-GGUF

#### Qwen 2.5 VL
(tool_name) -hf ggml-org/Qwen2.5-VL-3B-Instruct-GGUF
(tool_name) -hf ggml-org/Qwen2.5-VL-7B-Instruct-GGUF
(tool_name) -hf ggml-org/Qwen2.5-VL-32B-Instruct-GGUF
(tool_name) -hf ggml-org/Qwen2.5-VL-72B-Instruct-GGUF

#### Mistral Small 3.1 24B (IQ2_M quantization)
(tool_name) -hf ggml-org/Mistral-Small-3.1-24B-Instruct-2503-GGUF

#### InternVL 2.5 and 3
(tool_name) -hf ggml-org/InternVL2_5-1B-GGUF
(tool_name) -hf ggml-org/InternVL2_5-4B-GGUF
(tool_name) -hf ggml-org/InternVL3-1B-Instruct-GGUF
(tool_name) -hf ggml-org/InternVL3-2B-Instruct-GGUF
(tool_name) -hf ggml-org/InternVL3-8B-Instruct-GGUF
(tool_name) -hf ggml-org/InternVL3-14B-Instruct-GGUF

#### Llama 4 Scout
(tool_name) -hf ggml-org/Llama-4-Scout-17B-16E-Instruct-GGUF
Go to the provided address.

