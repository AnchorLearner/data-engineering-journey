# Week 1–2 Log: Setup, Git, Python ETL

## ✅ Week 1 – Setup & Git

### What I Did
- Installed Git, Firefox, Slack on Ubuntu
- Set up a GitHub account and created my first repository
- Learned basic Git commands: `git add`, `commit`, `push`, `pull`

### Issues I Encountered
- Authentication errors with HTTPS
- Error: “Support for password authentication was removed”
- SSH not working: `Permission denied (publickey)`

### Solutions
- Generated an SSH key using `ssh-keygen`
- Added the public key to my GitHub account
- Verified SSH connection with `ssh -T git@github.com`
- Used a virtual environment to isolate Python packages

---

## ✅ Week 2 – Python for ETL

### What I Did
- Created a basic ETL script using `pandas`
- Extracted mock data into a DataFrame
- Added a calculated column
- Saved to CSV (`output.csv`)
- Pushed everything to GitHub using Git

### Issues I Encountered
- `ModuleNotFoundError: No module named 'pandas'`
- ImportError related to NumPy C extensions

### Solutions
- Created a virtual environment using `python3 -m venv .venv`
- Activated it with `source .venv/bin/activate`
- Installed dependencies cleanly using `pip install pandas numpy`
- Confirmed success by running the script

---

## 💡 Key Takeaways

- SSH is the recommended way to interact with GitHub
- Virtual environments prevent system package conflicts
- Always commit `requirements.txt` for reproducibility
- Practice small scripts first before scaling up

