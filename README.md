# 🔐 Secure Data Wiping MVP  
*A Smart India Hackathon Project – Safe, Verifiable File Erasure for Trustworthy IT Recycling*
---
## 🧩 Overview
India generates over **1.75 million tonnes of e-waste** every year. Many users hesitate to recycle old devices due to **data privacy fears** — deleted data can often be recovered.  
My project provides a **secure, user-friendly, and verifiable data wiping solution** to help users confidently erase files and promote safe IT asset recycling.
---
## 🚀 Features
- 🧹 **Secure File Wiping** – Overwrites file contents with zeros or random data.  
- 🧾 **JSON & PDF Certificates** – Automatically generated proof of erasure.  
- 🔏 **Digital Signature** – Ensures the certificate is tamper-proof.  
- 💻 **Cross-platform Ready** – Works on Windows (MVP); planned Linux/Android support.  
- 📴 **Offline Usability** – Works without an internet connection.  
---

## 🏗️ Tech Stack
| Layer | Technology |
|--------|-------------|
| **Frontend** | (Planned) Electron / Tauri – Desktop GUI |
| **Backend** | Python (MVP), Rust / Go (Full version) |
| **Android App** | (Planned) Kotlin / Java |
| **Infrastructure** | Shell Script for bootable ISO (Full version) |
| **Standards** | NIST SP 800-88 Data Sanitization |
---

## ⚙️ How It Works (MVP)
1. User selects a file to wipe.  
2. Script overwrites the file data (zeros or random bytes).  
3. File is securely deleted from disk.  
4. A **JSON + PDF certificate** is generated with:  
   - File name, size, and timestamp  
   - Wiping method used  
   - Digital signature for authenticity  
5. Certificate can be verified by third parties using a verification script.
---

## 🧠 Future Scope (Full Project)
- Full-disk wiping (HDD/SSD) using **ATA Secure Erase** & **NVMe Format**.  
- Android version for **mobile device erasure**.  
- Blockchain-based **certificate verification**.  
- **One-click GUI** (Electron/Tauri).  
- **Enterprise dashboard** with database tracking.

---
## 🧰 Installation & Usage (for MVP)
1. Clone the repo:  
   ```bash
   git clone https://github.com/<your-username>/secure-data-wiping.git
   cd secure-data-wiping
2. Install dependencies (Python 3.x required):
pip install -r requirements.txt

3. Run the tool:
python wipe_file.py
Follow on-screen instructions to select and wipe a file.

📜 Example Output
Wiped File: testfile.txt

Certificate Files:
certificate.json
certificate.pdf

Signature: SHA256 digital signature for verification

🛡️ License
This project is open-source under the MIT License.
Feel free to fork, improve, and contribute!

📬 Contact
📧 Email: rajsharma61509@email.com
🌐 GitHub: https://github.com/<N6si>/secure-data-wiping
