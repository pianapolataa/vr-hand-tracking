# 📦 How to Build and Install Unity APK to Meta Quest Headset

## 🚀 Prerequisites

- Unity version **2021.3.5f1** (recommended for clean builds)
- Meta Quest headset with **Developer Mode** enabled
- USB-C cable to connect Quest to PC
- Meta Quest Developer Hub (MQDH) account (optional but helpful)
- Android Build Support installed in Unity (including SDK + NDK + OpenJDK)

## 🛠 Setup Steps

### 1. Open Unity Project

- Download and unzip the provided Unity project.
- Open Unity Hub, click `Open`, and select the unzipped folder.
- Use **Unity 2021.3.5f1** (or compatible version).
- Wait for Unity to load and compile.

### 2. Configure Build Settings

Go to:
File > Build Settings

arduino
Copy
Edit
Or press:
Cmd + Shift + B (Mac) / Ctrl + Shift + B (Windows)

markdown
Copy
Edit

In the Build Settings window:
- Select `Android` as platform.
- Click `Switch Platform` if needed.
- Click `Add Open Scenes` to include your current scene.
- Plug in your Quest headset via USB — it should appear under **Run Device**.

### 3. Player Settings

Click `Player Settings` at the bottom of Build Settings. Then check the following:

**Other Settings:**
- Package Name: `com.yourname.appname`
- Minimum API Level: `API Level 23 or higher`
- Target API Level: `Automatic (highest installed)`
- Scripting Backend: `IL2CPP`
- Target Architectures: ✅ `ARM64` only (uncheck ARMv7)

**XR Plugin Management:**
- Go to `Edit > Project Settings > XR Plug-in Management`
- Install and enable **Oculus** for Android

### Step 4: Save Your Scene
Go to:
File > Save As...

2. Save your scene as something like:
Assets/Scenes/MainScene.unity
(You can create a `Scenes/` folder manually if needed.)


### Step 2: Add Scene to Build

1. Go to:
File > Build Settings
2. Click:
Add Open Scenes

✅ This will add your newly saved `.unity` scene to the build list.

---

### 5. Build and Run

- Return to `File > Build Settings`
- Ensure your Quest is connected and visible under **Run Device**
- Click `Build and Run`
- Choose an output folder for temporary APK file

Unity will:
- Build the APK
- Install it to your Quest headset
- Launch it automatically

---

## 🎮 How to Launch the App on Quest

On your Quest headset:
1. Go to **Apps**
2. Filter by **Unknown Sources**
3. Find and launch your app

---

## 🧪 Troubleshooting

- If build fails, make sure:
  - Android modules are installed in Unity Hub
  - Developer Mode is enabled on Quest
  - USB debugging is allowed (check headset prompt)
- Use `adb devices` to verify connection
- Use `adb install -r your_app.apk` for manual install

---

## ✅ Notes

- APK files cannot be opened directly in Unity.
- Always use the Unity source project (`Assets/`, `ProjectSettings/`, etc.) to make edits and rebuild.
