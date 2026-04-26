import hashlib
import tkinter as tk
from tkinter import filedialog
import os
import gzip

class APOP_Cracker():
    def __init__(self):
        self.wordlist_path = ""
        
        self.Tab = tk.Tk()
        self.Tab.title("APOP Challenge Cracker")
        self.Tab.geometry("500x350")
        
        # 1. Banner Input
        tk.Label(self.Tab, text="1. POP3 Banner (Challenge):", font=("Arial", 9, "bold")).pack(pady=2)
        self.Entry_Banner = tk.Entry(self.Tab, width=60)
        self.Entry_Banner.pack(pady=5)

        # 2. Hash Input
        tk.Label(self.Tab, text="2. Target MD5 Hash:", font=("Arial", 9, "bold")).pack(pady=2)
        self.Entry_Hash = tk.Entry(self.Tab, width=60)
        self.Entry_Hash.pack(pady=5)

        # 3. Wordlist Selection
        tk.Label(self.Tab, text="3. Wordlist Selection:", font=("Arial", 9, "bold")).pack(pady=2)
        self.Path_Label = tk.Label(self.Tab, text="No file selected", fg="gray", wraplength=400)
        self.Path_Label.pack()
        self.Btn_Browse = tk.Button(self.Tab, text="Browse Wordlist", command=self.browse_file)
        self.Btn_Browse.pack(pady=5)
        
        # 4. Status and Run
        self.Status_Label = tk.Label(self.Tab, text="Status: Waiting for input", fg="blue", font=("Arial", 10, "italic"))
        self.Status_Label.pack(pady=15)

        self.Btn_Start = tk.Button(self.Tab, text="RUN ATTACK", command=self.start_attack, 
                                   bg="#d9534f", fg="white", font=("Arial", 10, "bold"), width=20)
        self.Btn_Start.pack(pady=10)
        
        self.Tab.mainloop()

    def browse_file(self):
        # Open file dialog in common wordlist locations
        initial_dir = "/usr/share/wordlists/" if os.path.exists("/usr/share/wordlists/") else os.getcwd()
        file_selected = filedialog.askopenfilename(
            initialdir=initial_dir,
            title="Select Wordlist",
            filetypes=(("Text files", "*.txt"), ("Gzip files", "*.gz"), ("All files", "*.*"))
        )
        if file_selected:
            self.wordlist_path = file_selected
            self.Path_Label.config(text=os.path.basename(file_selected), fg="black")

    def start_attack(self):
        banner = self.Entry_Banner.get().strip()
        target = self.Entry_Hash.get().strip().lower()

        if not self.wordlist_path or not banner or not target:
            self.Status_Label.config(text="Error: Missing Information!", fg="red")
            return

        self.Status_Label.config(text="Cracking... check terminal for progress", fg="orange")
        self.Tab.update()

        # Handle compression automatically
        is_gz = self.wordlist_path.endswith('.gz')
        opener = gzip.open if is_gz else open
        mode = 'rt' if is_gz else 'r'

        try:
            with opener(self.wordlist_path, mode, encoding='latin-1') as f:
                for line in f:
                    password = line.strip()
                    # APOP MD5 Logic
                    attempt = banner + password
                    hashed = hashlib.md5(attempt.encode('utf-8')).hexdigest()
                    
                    if hashed == target:
                        self.Status_Label.config(text=f"SUCCESS: {password}", fg="green")
                        print(f"\n[+] Match Found: {password}")
                        return

            self.Status_Label.config(text="Finished: Password not found.", fg="red")
        except Exception as e:
            self.Status_Label.config(text=f"System Error: {str(e)}", fg="red")

if __name__ == "__main__":
    APOP_Cracker()
