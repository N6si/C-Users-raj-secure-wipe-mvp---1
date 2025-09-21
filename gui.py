# gui.py (styled with ttkbootstrap)
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
import threading
import app
import os
import json

# ------------------ GUI Setup ------------------

app_style = "darkly"  # You can change theme: "flatly", "darkly", "cyborg", "minty", etc.
root = ttk.Window(themename=app_style)
root.title("🛡️ Secure Wipe MVP")
root.geometry("640x520")

# ------------------ Frames ------------------

frm_inputs = ttk.LabelFrame(root, text="🗂️ File Selection", padding=10)
frm_inputs.pack(padx=12, pady=10, fill="x")

frm_meta = ttk.LabelFrame(root, text="📋 Chain of Custody", padding=10)
frm_meta.pack(padx=12, pady=10, fill="x")

frm_buttons = ttk.Frame(root)
frm_buttons.pack(pady=(5, 5))

frm_verify = ttk.LabelFrame(root, text="🔏 Verify Signature", padding=10)
frm_verify.pack(padx=12, pady=10, fill="x")

# ------------------ File Selection ------------------

ttk.Label(frm_inputs, text="File to wipe:").grid(row=0, column=0, sticky="w", padx=5, pady=4)
entry = ttk.Entry(frm_inputs, width=55)
entry.grid(row=0, column=1, padx=5, pady=4)
ttk.Button(frm_inputs, text="Browse", bootstyle="secondary-outline", command=lambda: browse_file(entry)).grid(row=0, column=2, padx=5)

# ------------------ Metadata ------------------

operator_entry = ttk.Entry(frm_meta, width=40)
recipient_entry = ttk.Entry(frm_meta, width=40)
location_entry = ttk.Entry(frm_meta, width=40)

ttk.Label(frm_meta, text="Operator:").grid(row=0, column=0, sticky="w", padx=5, pady=4)
operator_entry.grid(row=0, column=1, padx=5, pady=4)

ttk.Label(frm_meta, text="Recipient:").grid(row=1, column=0, sticky="w", padx=5, pady=4)
recipient_entry.grid(row=1, column=1, padx=5, pady=4)

ttk.Label(frm_meta, text="Location:").grid(row=2, column=0, sticky="w", padx=5, pady=4)
location_entry.grid(row=2, column=1, padx=5, pady=4)

# ------------------ Buttons ------------------

btn_wipe = ttk.Button(
    frm_buttons,
    text="⚠️ Secure Wipe & Issue Certificate",
    bootstyle="danger",
    command=lambda: start_wipe()
)
btn_wipe.pack(ipadx=15, ipady=5, pady=6)

# ------------------ Verify Signature ------------------

verify_entry = ttk.Entry(frm_verify, width=55)
ttk.Label(frm_verify, text="Signed JSON file:").grid(row=0, column=0, sticky="w", padx=5, pady=4)
verify_entry.grid(row=0, column=1, padx=5, pady=4)
ttk.Button(frm_verify, text="Browse", command=lambda: browse_file(verify_entry, [("JSON files", "*.json")])).grid(row=0, column=2, padx=5)

ttk.Button(frm_verify, text="✅ Verify Signature", bootstyle="success", command=lambda: verify_signature()).grid(row=1, column=0, columnspan=3, pady=10)

# ------------------ Progress & Status ------------------

progress = ttk.Progressbar(root, length=500, mode='indeterminate', bootstyle="info-striped")
progress.pack(padx=12, pady=(8, 0))

status_label = ttk.Label(root, text="Ready", anchor="w", font=("Segoe UI", 9), foreground="gray")
status_label.pack(fill="x", padx=12, pady=(4, 10))


# ------------------ Functions ------------------

def browse_file(entry_widget, filetypes=[("All files", "*.*")]):
    path = filedialog.askopenfilename(filetypes=filetypes)
    if path:
        entry_widget.delete(0, "end")
        entry_widget.insert(0, path)

def start_wipe():
    path = entry.get().strip()
    if not path or not os.path.exists(path):
        messagebox.showerror("Error", "Please select a valid file.")
        return

    operator = operator_entry.get().strip()
    recipient = recipient_entry.get().strip()
    location = location_entry.get().strip()

    def job():
        btn_wipe.config(state="disabled")
        progress.start(10)
        status_label.config(text="Wiping in progress...", foreground="blue")

        try:
            j, pdf, s = app.run_wipe_and_issue(
                path,
                privkey="keys/priv.pem",
                passes=1,
                extra_meta={
                    "operator": operator,
                    "recipient": recipient,
                    "location": location
                }
            )
            messagebox.showinfo("✅ Wipe Complete", f"Certificate created:\n\n📄 JSON: {j}\n📄 PDF: {pdf}")
            status_label.config(text="Wipe complete ✅", foreground="green")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            status_label.config(text="Wipe failed ❌", foreground="red")
        finally:
            progress.stop()
            btn_wipe.config(state="normal")

    threading.Thread(target=job, daemon=True).start()

def verify_signature():
    path = verify_entry.get().strip()
    if not path or not os.path.exists(path):
        messagebox.showerror("Error", "Please select a signed JSON file.")
        return

    try:
        with open(path, "r") as f:
            data = json.load(f)

        ok, msg = app.verify_signed_certificate(data, "keys/pub.pem")

        if ok:
            messagebox.showinfo("✅ Signature Verified", "The signature is valid.\n\n" + msg)
            status_label.config(text="Signature verified ✅", foreground="green")
        else:
            messagebox.showerror("❌ Invalid Signature", "Signature check failed.\n\n" + msg)
            status_label.config(text="Signature invalid ❌", foreground="red")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Verification failed ❌", foreground="red")


# ------------------ Run ------------------

root.mainloop()
