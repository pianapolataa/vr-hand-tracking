## Env Setup
Set up driver
In NUC, create a new tmux session and launch driver
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

## Start teleoperation:
Start franka server:
```bash
cd Franka-Teach
python franka_server.py
```

Start Manus streaming:
```bash
cd RUKA
cd ./submodules/Bidex_Manus_Teleop/MANUS_Core_2.4.0_SDK/SDKClient_Linux
./SDKClient_Linux.out
cd ..
```

Choose the option [1] Core Integrated - This will run standalone without the need for a MANUS Core connection, then navigate to the Glove Menu. You should see the joint angles change as you move your fingers.

Before starting teleoperation, specify the parameters in `./Franka-Teach/configs/teleop.yaml`.
Example:
```yaml
use_oculus_stick: false   # set to true if you want to use vr stick for arm tracking
use_hand_tracking: true   # set to false if you only want arm tracking
```

Start Teleoperation:
Start Unity in the oculus headset, detailed start up can be found in [Open-Teach VR setup guide](https://github.com/aadhithya14/Open-Teach/blob/main/docs/vr.md). Then in Minerva:
```bash
python teleop.py
```

（Still working on the data collection pipeline)