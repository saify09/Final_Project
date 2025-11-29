import random
import re
from typing import List, Dict

class QuizGenerator:
    def __init__(self):
        pass

    def generate_mcq(self, text: str, num_questions: int = 5) -> List[Dict]:
        """
        Generates MCQs from text using simple keyword masking.
        """
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        sentences = [s for s in sentences if len(s) > 50 and len(s) < 200]
        
        if len(sentences) < num_questions:
            selected_sentences = sentences
        else:
            selected_sentences = random.sample(sentences, num_questions)
            
        quiz = []
        for sentence in selected_sentences:
            words = sentence.split()
            # Simple heuristic: pick a long word as the answer
            candidates = [w for w in words if len(w) > 5 and w.isalpha()]
            if not candidates:
                continue
                
            answer = random.choice(candidates)
            question_text = sentence.replace(answer, "______")
            
            # Generate distractors (random words from other sentences)
            all_words = [w for w in text.split() if len(w) > 5 and w.isalpha() and w != answer]
            distractors = random.sample(all_words, 3) if len(all_words) >= 3 else ["Option A", "Option B", "Option C"]
            
            options = distractors + [answer]
            random.shuffle(options)
            
            quiz.append({
                "question": question_text,
                "options": options,
                "answer": answer
            })
            
        return quiz

    def generate_short_answer(self, text: str, num_questions: int = 5) -> List[Dict]:
        """
        Generates short answer questions (placeholder logic).
        """
        # For now, just return sentences as "Explain this..."
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
        sentences = [s for s in sentences if len(s) > 60]
        
        if len(sentences) < num_questions:
            selected = sentences
        else:
            selected = random.sample(sentences, num_questions)
            
        quiz = []
        for s in selected:
            quiz.append({
                "question": f"Explain the context of: '{s[:30]}...'",
                "answer": s
            })
        return quiz
