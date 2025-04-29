# High Risk Project

## 🧠 Overview
**High Risk Project** is an AI-powered application designed to tackle complex decision-making in high-risk environments using large language models and intelligent automation. It leverages advanced reasoning, medical prompt workflows (e.g., Chain-of-Thought prompting), and contextual understanding to provide reliable, step-by-step outputs for sensitive scenarios such as healthcare, legal assistance, or emergency analysis.

---

## 🚀 Features

- 🏥 Medical Question Answering with Normal vs Chain-of-Thought Prompting
- 🔍 Step-by-step reasoning for improved transparency
- 🧾 Integration with OpenAI APIs for natural language understanding
- 🔐 Environment variable support for secure API key handling
- 📊 (Optional) Result visualizations and evaluation metrics

---
## ⚙️ Installation

1. **Clone the repository:**
   
   git clone https://github.com/Kaushikselvaraju/High_Risk_Project.git
   cd High_Risk_Project

2.Create and activate a virtual environment:

  python3 -m venv venv
  source venv/bin/activate  # For Windows: venv\Scripts\activate

3.Install dependencies:

pip install -r requirements.txt

4.Set up .env: Create a file .env with:

OPENAI_API_KEY=your_api_key_here

5.You can choose between:

Normal Prompt: Direct response

Chain-of-Thought Prompt: Step-by-step reasoning

6.📈 Example Output
Q: What are the symptoms of diabetes?
Normal Answer: Frequent urination, increased thirst, and blurred vision.
CoT Answer: Let's break this down step-by-step. Diabetes affects blood sugar levels, which causes increased thirst... (continues)

7.🔐 Security Notes
Do not commit .env files or API keys to GitHub.

This project uses GitHub's Push Protection to prevent accidental secret exposure.
