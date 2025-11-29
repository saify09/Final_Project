import numpy as np
import pandas as pd
from typing import List, Dict, Any

class AnalyticsEngine:
    """
    Handles predictive analytics and forecasting for student performance.
    """
    
    @staticmethod
    def forecast_next_score(history: List[int]) -> Dict[str, Any]:
        """
        Predicts the next quiz score using simple linear regression (Least Squares).
        """
        if len(history) < 2:
            return {
                "predicted_score": None,
                "trend": "Insufficient Data",
                "confidence": 0.0
            }
        
        # X axis: Attempt numbers (1, 2, 3...)
        X = np.array(range(1, len(history) + 1))
        # Y axis: Scores
        y = np.array(history)
        
        # Calculate slope (m) and intercept (b)
        A = np.vstack([X, np.ones(len(X))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        
        # Predict next value
        next_attempt = len(history) + 1
        predicted_score = m * next_attempt + c
        
        # Clip score to realistic bounds (e.g., 0 to max score seen or 100%)
        # Assuming max score is roughly consistent, let's cap at max(history) + buffer or 100% if we knew the denominator.
        # For now, just raw prediction.
        
        trend = "Improving 🚀" if m > 0.1 else "Declining 📉" if m < -0.1 else "Stable ⚖️"
        
        return {
            "predicted_score": round(predicted_score, 2),
            "trend": trend,
            "slope": m
        }
