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

# How to run
conda activate projectEnv
In a terminal, `python app.py`
In another terminal, `python main.py`
Access here: http://10.1.4.56:5000/

# How to add library
!! write library name in requirements.txt first.
conda activate projectEnv
pip install -r requirements.txt

# ToDo
Fine tune model to answer kid's mathematical question. Or choose another model. Maybe not VLM. 
Access flask by another device(HMD)


