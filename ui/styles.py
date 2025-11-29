def load_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        /* 
           ==========================================================================
           1. CSS VARIABLES (THEME TOKENS)
           ==========================================================================
        */
        :root {
            /* LIGHT MODE (Default) */
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --text-color: #0f172a;
            --text-secondary: #475569;
            --accent-color: #2563eb;
            --border-color: #e2e8f0;
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            --gradient-start: #2563eb;
            --gradient-end: #4f46e5;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                /* DARK MODE */
                --bg-color: #0f172a;
                --card-bg: #1e293b;
                --text-color: #f8fafc;
                --text-secondary: #94a3b8;
                --accent-color: #818cf8;
                --border-color: #334155;
                --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3);
                --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.5);
                --gradient-start: #818cf8;
                --gradient-end: #c084fc;
            }
        }

        /* 
           ==========================================================================
           2. GLOBAL RESETS & TYPOGRAPHY
           ==========================================================================
        */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
        }

        /* Force Streamlit's Main Container to match */
        .stApp {
            background-color: var(--bg-color);
        }

        h1, h2, h3, h4, h5, h6 {
            color: var(--text-color) !important;
            font-weight: 700;
            letter-spacing: -0.025em;
        }

        p, label, span, div, li {
            color: var(--text-color);
        }
        
        /* Subtitles / Secondary Text */
        .stMarkdown p, .caption {
            color: var(--text-secondary);
        }

        /* 
           ==========================================================================
           3. COMPONENTS
           ==========================================================================
        */

        /* Cards (Glassmorphism / Clean) */
        .card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s ease-in-out;
        }
        
        .card:hover {
            box-shadow: var(--shadow-md);
            border-color: var(--accent-color);
            transform: translateY(-2px);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: var(--card-bg);
            border-right: 1px solid var(--border-color);
        }
        
        section[data-testid="stSidebar"] .block-container {
            padding-top: 2rem;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(90deg, var(--gradient-start), var(--gradient-end));
            color: #ffffff !important;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            transition: opacity 0.2s;
        }
        
        .stButton > button:hover {
            opacity: 0.9;
            box-shadow: var(--shadow-md);
        }

        /* Inputs (Text, Select, File) */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > div,
        .stFileUploader {
            background-color: var(--card-bg);
            color: var(--text-color) !important;
            border: 1px solid var(--border-color);
            border-radius: 8px;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: var(--accent-color);
            box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
        }

        /* Input Labels */
        .stTextInput label, .stSelectbox label, .stFileUploader label {
            color: var(--text-color) !important;
            font-weight: 600;
            font-size: 0.9rem;
        }

        /* Metrics */
        [data-testid="stMetricValue"] {
            color: var(--accent-color) !important;
            font-size: 2.2rem;
        }
        
        [data-testid="stMetricLabel"] {
            color: var(--text-secondary) !important;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: transparent;
            border-bottom: 1px solid var(--border-color);
        }

        .stTabs [data-baseweb="tab"] {
            height: 40px;
            background-color: transparent;
            border-radius: 6px;
            color: var(--text-secondary);
            font-weight: 600;
            border: none;
        }

        .stTabs [aria-selected="true"] {
            background-color: var(--card-bg);
            color: var(--accent-color) !important;
            box-shadow: var(--shadow-sm);
        }

        /* 
           ==========================================================================
           4. UTILITIES
           ==========================================================================
        */
        /* Gradient Text for Title */
        h1 {
            background: linear-gradient(90deg, var(--gradient-start), var(--gradient-end));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }
        
        /* Mobile Adjustments */
        @media only screen and (max-width: 768px) {
            .card { padding: 16px; }
            h1 { font-size: 1.75rem !important; }
        }
    </style>
    """
