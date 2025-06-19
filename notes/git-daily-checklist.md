## 🧼 Git Daily Workflow Checklist (Ubuntu)

Use this checklist each time you restart your computer and want to continue working on your Git project.

---

### 1. Open Terminal and Navigate to Your Project

```bash
cd ~/path/to/your/project  # e.g., cd ~/projects/data-engineering-journey
```

---

### 2. Activate Your Virtual Environment

```bash
source .venv/bin/activate
```

If `.venv` is missing:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Pull Latest Changes from Remote

```bash
git pull origin main  # or 'master' depending on your default branch
```

---

### 4. (Optional) Confirm Git Identity

```bash
git config user.name
git config user.email
```

If not set:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

### 5. Start Working!

Edit code, run scripts, write notes.

---

### 6. Stage, Commit, and Push Your Work

```bash
git add .
git commit -m "Describe what you did"
git push
```

---

### 🔐 If Using SSH

Start SSH agent and add your key:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

Test your connection:

```bash
ssh -T git@github.com
```

---

### ✅ Done!

You're now synced, secure, and ready to build.

