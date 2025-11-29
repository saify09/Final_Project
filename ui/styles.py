def load_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

        /* Theme-Aware Base Styles */
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
            /* Use Streamlit's native variables for theme adaptability */
            background-color: var(--background-color);
            color: var(--text-color);
        }

        /* Gradient Background - Adapts to Theme */
        .stApp {
            /* Light Mode Gradient */
            background: linear-gradient(135deg, #f0f2f5 0%, #e0e7ff 100%);
        }
        
        /* Dark Mode Override for Background */
        @media (prefers-color-scheme: dark) {
            .stApp {
                background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
            }
        }

        /* Glassmorphism Card - Theme Aware */
        .card {
            background: rgba(255, 255, 255, 0.7); /* Light mode default */
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
            padding: 24px;
            margin-bottom: 24px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        /* Dark Mode Card */
        @media (prefers-color-scheme: dark) {
            .card {
                background: rgba(31, 41, 55, 0.7); /* Dark mode card */
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            }
        }

        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
        }

        /* Headers */
        h1, h2, h3 {
            color: var(--text-color); /* Adapt to theme */
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        h1 {
            background: linear-gradient(90deg, #2563eb, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #2563eb, #4f46e5);
            color: white;
            border-radius: 12px;
            border: none;
            padding: 12px 28px;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #1d4ed8, #4338ca);
            box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3);
            transform: translateY(-1px);
        }

        /* Inputs */
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 1px solid var(--secondary-background-color);
            padding: 10px 12px;
            transition: border-color 0.2s;
            background-color: var(--secondary-background-color);
            color: var(--text-color);
        }
        .stTextInput>div>div>input:focus {
            border-color: #4f46e5;
            box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.1);
        }

        /* Sidebar - Theme Aware */
        section[data-testid="stSidebar"] {
            background-color: var(--secondary-background-color);
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(229, 231, 235, 0.1);
        }
        
        /* Sidebar Text */
        section[data-testid="stSidebar"] * {
            color: var(--text-color) !important;
        }
        
        /* Metrics */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            font-weight: 700;
            color: #4f46e5;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
            background-color: transparent;
        }

        .stTabs [data-baseweb="tab"] {
            height: 50px;
            white-space: pre-wrap;
            background-color: transparent;
            border-radius: 4px;
            color: var(--text-color);
            font-size: 1.1rem;
            font-weight: 600;
        }

        .stTabs [aria-selected="true"] {
            background-color: transparent;
            color: #4f46e5;
            border-bottom: 2px solid #4f46e5;
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
            
            .stTabs [data-baseweb="tab"] {
                font-size: 0.9rem;
                padding: 0 8px;
                gap: 8px;
            }
            
            .stButton>button {
                width: 100%;
                padding: 10px 20px;
            }
        }
    </style>
    """
