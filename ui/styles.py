def load_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
            background-color: #f0f2f5;
            color: #000000 !important; /* Force black for maximum readability */
        }

        /* Gradient Background for Main Area */
        .stApp {
            background: linear-gradient(135deg, #f0f2f5 0%, #e0e7ff 100%);
        }

        /* Glassmorphism Card */
        .card {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
            padding: 24px;
            margin-bottom: 24px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.1);
        }

        /* Headers */
        h1, h2, h3 {
            color: #111827;
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
            border: 1px solid #e5e7eb;
            padding: 10px 12px;
            transition: border-color 0.2s;
        }
        .stTextInput>div>div>input:focus {
            border-color: #4f46e5;
            box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.1);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent sidebar */
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(229, 231, 235, 0.5);
        }

        /* Force dark text in sidebar for readability */
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3, 
        section[data-testid="stSidebar"] p, 
        section[data-testid="stSidebar"] span, 
        section[data-testid="stSidebar"] div,
        section[data-testid="stSidebar"] label {
            color: #111827 !important;
        }
        
        /* Fix Sidebar Input Labels */
        .st-emotion-cache-16idsys p {
            color: #111827 !important;
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
            color: #4b5563;
            font-size: 1.1rem;
            font-weight: 600;
        }

        /* Force Black Text on EVERYTHING */
        html, body, [class*="css"], .stMarkdown, .stText, h1, h2, h3, h4, h5, h6, p, label, span, div {
            color: #000000 !important;
        }
        
        /* Specific overrides for Streamlit widgets to ensure they are black */
        .stRadio label, .stCheckbox label, .stTextInput label, .stSelectbox label, .stFileUploader label {
            color: #000000 !important;
        }
        
        /* Keep the gradient title but ensure it is readable */
        h1 {
            background: linear-gradient(90deg, #2563eb, #7c3aed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            /* Fallback if gradient fails */
            color: #2563eb; 
        }

        /* Tabs - Force dark text */
        .stTabs [data-baseweb="tab"] {
            color: #000000 !important;
        }
        
        /* Sidebar - Force dark text */
        section[data-testid="stSidebar"] * {
            color: #000000 !important;
        }
    </style>
    """
