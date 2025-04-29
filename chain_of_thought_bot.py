# chain_of_thought_bot.py

import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Function to load questions
def load_questions(filepath):
    data = pd.read_csv(filepath)
    return data['question'].tolist()

# Function to create normal prompt
def create_normal_prompt(question):
    return f"Answer the following medical question concisely:\n\n{question}"

# Function to create chain-of-thought prompt
def create_cot_prompt(question):
    return f"""You are a careful and professional medical assistant.

First, think step-by-step about the possible causes and related facts based on the question.
Then provide your final answer based on your reasoning.

Question: {question}

Step-by-step reasoning:"""

# Function to query OpenAI
def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # You can also use "gpt-4-turbo" if needed
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        return answer.strip()
    except Exception as e:
        print("Error:", e)
        return "Error fetching response."

# Main execution
def main():
    print("\n--- Chain of Thought Medical QA Bot ---\n")

    # Load questions
    questions = load_questions('data/medical_questions.csv')

    results = []

    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")

        # Normal answer
        normal_prompt = create_normal_prompt(question)
        normal_answer = ask_gpt(normal_prompt)
        
        # Chain of Thought answer
        cot_prompt = create_cot_prompt(question)
        cot_answer = ask_gpt(cot_prompt)

        # Store the results
        results.append({
            "question": question,
            "normal_answer": normal_answer,
            "cot_answer": cot_answer
        })

        # Print sample output
        print("\nNormal Answer:\n", normal_answer)
        print("\nChain of Thought Answer:\n", cot_answer)
        print("-" * 50)

    # Save results
    df = pd.DataFrame(results)
    df.to_csv('data/medical_cot_results.csv', index=False)
    print("\nAll results saved to 'data/medical_cot_results.csv'.")

if __name__ == "__main__":
    main()
