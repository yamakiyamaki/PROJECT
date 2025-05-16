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


