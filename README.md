Set up driver
In NUC,
create a new tmux session and launch driver
```bash
tmux
cd workspace/franka_controller/deoxys_control/deoxys
./auto_scripts/auto_arm.sh config/franka_single.yml
```



```bashrc
start_new_franka="ssh -NL localhost:8000:172.16.0.2:443 nuc"
```
password to nuc is `dexpilot123`

First git clone the repository:
```bash
git clone --recurse-submodules https://github.com/joliachen/vr-hand-tracking.git
```

Then set up conda environment:
```bash
cd vr-hand-tracking
conda env create -f conda_env.yaml
conda activate frankateach
bash setup.sh
```
Make sure you stay around to enter your sudo password and 0.13.3 as the libfranka version when prompted




pip install matplotlib ffmpeg-python
pip install open3d imageio
