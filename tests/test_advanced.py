import unittest
import os
import sys
import numpy as np

# Add src to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.utils.analytics import AnalyticsEngine

class TestAdvancedFeatures(unittest.TestCase):
    
    def test_analytics_forecasting(self):
        """Test the linear regression forecasting logic."""
        history = [50, 60, 70] # Perfect linear trend
        result = AnalyticsEngine.forecast_next_score(history)
        
        self.assertIsNotNone(result['predicted_score'])
        self.assertAlmostEqual(result['predicted_score'], 80.0, delta=0.1)
        self.assertEqual(result['trend'], "Improving 🚀")
        
        history_declining = [90, 80, 70]
        result_declining = AnalyticsEngine.forecast_next_score(history_declining)
        self.assertAlmostEqual(result_declining['predicted_score'], 60.0, delta=0.1)
        self.assertEqual(result_declining['trend'], "Declining 📉")

    def test_analytics_insufficient_data(self):
        history = [10]
        result = AnalyticsEngine.forecast_next_score(history)
        self.assertIsNone(result['predicted_score'])

if __name__ == '__main__':
    unittest.main()
