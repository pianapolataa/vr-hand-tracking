
First git clone the repository:
```bash
git clone --recurse-submodules https://github.com/joliachen/Ruka-Teach.git
```

Then set up conda environment:
```bash
cd Ruka-Teach
conda env create -f conda_env.yaml
conda activate ruka_teach
bash setup.sh
```
Make sure you stay around to enter your sudo password and 0.13.3 as the libfranka version when prompted
