import streamlit as st
from modules import symptom_checker, first_aid_guide, provider_connector, health_education
from PIL import Image
import base64

# Configure page
st.set_page_config(
    page_title="RemoteCare",
    page_icon="🏥",
    layout="wide"
)

# Image loader with caching
@st.cache_data
def load_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Low-bandwidth mode toggle
low_bandwidth = st.sidebar.checkbox("Low-bandwidth mode", value=True)

# Dark Theme CSS
def load_css():
    st.markdown(f"""
    <style>
        /* Dark Theme */
        :root {{
            --primary: #1a1a2e;
            --secondary: #16213e;
            --accent: #0f3460;
            --text: #ffffff;
            --highlight: #00b4d8;
        }}
        
        .stApp {{
            background-color: var(--primary);
            color: var(--text);
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            color: var(--highlight);
        }}
        
        .feature-card {{
            background: var(--secondary);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            border-left: 3px solid var(--highlight);
            color: var(--text);
        }}
        
        .stMetric {{
            background: var(--secondary);
            border-radius: 10px;
            padding: 15px;
            color: var(--text);
        }}
        
        .stButton>button {{
            background: var(--highlight);
            color: var(--primary);
            border: none;
            border-radius: 8px;
        }}
        
        [data-testid="stSidebar"] {{
            background: var(--secondary) !important;
        }}
        
        /* Low-bandwidth overrides */
        {'* { color: white !important; background-color: #121212 !important; }' if low_bandwidth else ''}
    </style>
    """, unsafe_allow_html=True)

load_css()

# App Header with two-column layout
header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.title("RemoteCare Telemedicine")
    st.markdown("**Connecting remote communities to healthcare**")
    
    if not low_bandwidth:
        st.markdown("---")
        # Metrics row
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        with metric_col1:
            st.metric("Patients Served", "1,024+", "28 this week")
        with metric_col2:
            st.metric("Avg Response Time", "23 mins")
        with metric_col3:
            st.metric("Coverage Area", "42 villages")

with header_col2:
    if not low_bandwidth:
        # Medical icon graphic
        st.markdown("""
        <div style="text-align: center; 
                    background: rgba(0, 180, 216, 0.1);
                    border-radius: 12px;
                    padding: 15px;
                    margin-top: 10px;
                    border: 1px solid rgba(0, 180, 216, 0.3)">
            <span style="font-size: 48px; color: #00b4d8">🏥</span>
            <h4 style="color: #00b4d8; margin-top: 5px">24/7 Access</h4>
            <p style="font-size: 14px">Immediate medical guidance</p>
        </div>
        """, unsafe_allow_html=True)

# Main Menu with icons
menu_items = {
    "Symptom Checker": {"icon": "🩺", "color": "#00b4d8", "function": symptom_checker.show},
    "First Aid Guide": {"icon": "🚑", "color": "#00b4d8", "function": first_aid_guide.show},
    "Find Doctors": {"icon": "👨‍⚕️", "color": "#00b4d8", "function": provider_connector.show},
    "Health Education": {"icon": "📚", "color": "#00b4d8", "function": health_education.show}
}

# Sidebar navigation
st.sidebar.markdown("## Navigation")
choice = st.sidebar.radio(
    "Menu",
    options=list(menu_items.keys()),
    format_func=lambda x: f"{menu_items[x]['icon']} {x}",
    key="main_menu"
)

# Feature highlights (only in normal mode)
if not low_bandwidth:
    st.markdown("## Key Features")
    features = st.columns(3)
    with features[0]:
        with st.container(border=True):
            st.markdown("**🩺 Symptom Analysis**")
            st.markdown("AI-powered preliminary diagnosis")
    with features[1]:
        with st.container(border=True):
            st.markdown("**📱 Low-Bandwidth Mode**")
            st.markdown("Works on 2G networks")
    with features[2]:
        with st.container(border=True):
            st.markdown("**👨‍⚕️ Doctor Matching**")
            st.markdown("Connect with local providers")

# Call the selected module with visual enhancements
if not low_bandwidth:
    st.markdown(f"""
    <div style="background:{menu_items[choice]['color']}20; 
                padding:15px; 
                border-radius:12px;
                border-left:4px solid {menu_items[choice]['color']};
                margin-bottom:20px">
        <h2 style="color:{menu_items[choice]['color']}">{menu_items[choice]['icon']} {choice}</h2>
    </div>
    """, unsafe_allow_html=True)

menu_items[choice]["function"](low_bandwidth)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px">
    <p>Not a substitute for professional medical care</p>
    <p style="font-size: 14px; color: #94a3b8">
        Emergency Contact: Call 108 in India
    </p>
</div>
""", unsafe_allow_html=True)

