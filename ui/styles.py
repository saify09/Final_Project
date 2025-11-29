def load_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

        /* Native Theme Integration */
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
            background-color: var(--background-color);
            color: var(--text-color);
        }

        /* Main App Background - Uses Streamlit's native background */
        .stApp {
            background-color: var(--background-color);
            /* Optional: Add a subtle texture or gradient that works in both modes if desired, 
               but sticking to native bg is safest for "efficiency" and correctness. */
        }

        /* Glassmorphism Card - Adaptive */
        .card {
            background-color: var(--secondary-background-color);
            border: 1px solid var(--secondary-background-color);
            border-radius: 16px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 24px;
            margin-bottom: 24px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
        }

        /* Headers */
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-color) !important;
            font-weight: 700;
        }
        
        /* Gradient Title - Kept as it usually looks good on both */
        h1 {
            background: linear-gradient(90deg, #2563eb, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            /* Fallback */
            color: #2563eb; 
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: var(--secondary-background-color);
            border-right: 1px solid var(--secondary-background-color);
        }
        
        section[data-testid="stSidebar"] * {
            color: var(--text-color) !important;
        }

        /* Inputs */
        .stTextInput>div>div>input, .stSelectbox>div>div>div, .stFileUploader {
            background-color: var(--secondary-background-color);
            color: var(--text-color);
            border: 1px solid var(--text-color); /* Subtle border */
            border-radius: 10px;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #2563eb, #4f46e5);
            color: white !important; /* Always white on this specific blue gradient */
            border: none;
            border-radius: 12px;
            padding: 12px 28px;
            font-weight: 600;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab"] {
            color: var(--text-color);
            background-color: transparent;
        }
        
        .stTabs [aria-selected="true"] {
            color: #4f46e5 !important;
            border-bottom-color: #4f46e5;
        }
        
        /* Metrics */
        [data-testid="stMetricValue"] {
            color: #4f46e5 !important;
        }

        /* Mobile Responsiveness */
        @media only screen and (max-width: 768px) {
            .card {
                padding: 16px;
                margin-bottom: 16px;
            }
            h1 {
                font-size: 1.8rem !important;
            }
            .stButton>button {
                width: 100%;
            }
        }
    </style>
    """
