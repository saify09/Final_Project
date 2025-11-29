import os
import random
import json

def create_synthetic_data():
    data_dir = "data/synthetic"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # 1. Create Dummy Content Files
    topics = {
        "ML_Intro.md": "# Introduction to Machine Learning\nMachine learning is a field of inquiry devoted to understanding and building methods that 'learn'...",
        "Python_Basics.txt": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability...",
        "Data_Science.md": "# Data Science\nData science is an interdisciplinary academic field that uses statistics, scientific computing, scientific methods, processes, algorithms and systems..."
    }

    for filename, content in topics.items():
        with open(os.path.join(data_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)
    
    print(f"Created {len(topics)} synthetic documents in {data_dir}")

    # 2. Create Synthetic Logs
    logs = []
    for i in range(50):
        logs.append({
            "session_id": i,
            "score": random.randint(0, 5),
            "total": 5,
            "timestamp": f"2023-11-{random.randint(1, 30):02d}"
        })
    
    with open(os.path.join(data_dir, "logs.json"), "w") as f:
        json.dump(logs, f)
    
    print("Created synthetic logs.")

if __name__ == "__main__":
    create_synthetic_data()
