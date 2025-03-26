# 🔐 Firebase Keylogger (Educational Purpose Only)

> ⚠️ **Disclaimer**: This project is created strictly for **educational and ethical testing** purposes.  
> Unauthorized usage of this software to monitor others without their **explicit consent** may violate privacy laws and result in legal consequences.  
> You are fully responsible for how you use this code.

---

## 📦 Features

- Monitors and logs keyboard input on the host machine
- Stores data both locally and in Firebase Realtime Database
- Web interface to view and display captured keystroke logs

---

## 🚀 Setup Instructions

### 🔧 Backend: Python Keylogger

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/keylogger-firebase.git
   cd keylogger-firebase

2. **Install Python dependencies**:

    pip install pynput firebase-admin

3. **Get your Firebase serviceAccountKey.json file**:

    Go to the Firebase Console
        👉 https://console.firebase.google.com

    Select your Firebase project

    If you don't have one, click "Add Project" and follow the steps.

    Go to "Project Settings"

    Click the ⚙️ gear icon in the left sidebar next to "Project Overview".

    Select "Project Settings".

    Go to the "Service Accounts" tab

    Click the “Generate new private key” button.

    Firebase will download a file named serviceAccountKey.json automatically.

4. **Update Firebase Database URL in krylog.py:**:   

        firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com/'  ## Replace with your Firebase database URL
})

5. **Run the keylogger script**:
    python krylog.py


# 🌐 Frontend: View Logs in Browser

    1. Open index.html in your browser

Make sure to update the Firebase configuration in index.html:
Your browser will load and display keystroke logs from Firebase.



Project Structure

/keylogger-firebase
├── krylog.py                # Python keylogger
├── index.html               # Frontend to view keystrokes
├── serviceAccountKey.json   # 🔐 Your private Firebase credentials (DO NOT SHARE)
└── README.md


# 🔒 Security Guidelines

Do not upload serviceAccountKey.json to GitHub or share it publicly

Add this to .gitignore:
    
    serviceAccountKey.json

Secure your Firebase Database with rules. Example:

    {
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
        }
    }

