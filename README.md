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

# How to add library
!! write library name in requirements.txt first.
conda activate projectEnv
pip install -r requirements.txt


# How to run
### easy way with .sh
conda activate projectEnv
In a terminal, `./execute.sh`

### manualy
conda activate projectEnv
In a terminal, `python app.py`
In another terminal, `python main.py`
Access here: http://10.1.4.56:5000/ #! if you are in another machin you need to access different url shown on terminal(upper one)

### Check in HMD
Open hotspot in the workstation.
Connect another device to the hotspot
run ./execute.sh
Access http://161.3.140.22:5000 by smartphone or HMD. This address is shown in the treminal(lower one of two url)

# ToDo
Fine tune model to answer kid's mathematical question. Or choose another model. Maybe not VLM. 
Access flask by another device(HMD)


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
cd build/bin/
ll
check available execution
./llama-server
./llama-server --help
./llama-server -m ../../models/
./llama-server -m ../../../models/Qwen2.5-VL-7B-Instruct-Q8_0.gguf
[hugging face ggml-org](https://huggingface.co/ggml-org) --> download model from here and move it to TY/models
--> Error: Multimodal is not supported, So use next command
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

