✅ Yes — always start (or create) your virtual environment first before installing dependencies or working on your Python project.

This keeps your project isolated, clean, and avoids conflicts with system-level packages.

🪜 Step-by-Step: Setting Up Virtual Environment

1. Create the Virtual Environment
If you haven’t already:

bash
Copy
Edit
python3 -m venv venv
This creates a folder named venv/ in your project.

2. Activate the Environment

source venv/bin/activate
On Windows:
bash
Copy
Edit
venv\Scripts\activate
You should see (venv) appear in your terminal prompt — that means you're inside the environment.

3. Install Your Requirements
bash
Copy
Edit
pip install -r requirements.txt

source newenv/bin/activate
