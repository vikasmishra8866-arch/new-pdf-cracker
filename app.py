import streamlit as st
import pikepdf
import itertools
import string
import qrcode
from PIL import Image
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Cracker VIP", layout="centered")

# --- CUSTOM CSS (ONLY TEXT COLOR & VISIBILITY MODIFIED) ---
st.markdown("""
    <style>
    .stApp {
        background: #050510;
    }
    
    /* Global Text Color: Premium White for high visibility */
    label, p, span, div, .stMarkdown, .stSubheader, .stCaption {
        color: #FFFFFF !important; 
        font-weight: 700 !important;
        text-shadow: 0px 0px 5px rgba(0, 210, 255, 0.3);
    }
    
    /* Heading Color: Premium Neon Cyan */
    h1, h2, h3 {
        color: #00f2ff !important;
        text-shadow: 0px 0px 15px #00f2ff;
    }

    /* Input Box Text: Sharp Cyan */
    input {
        color: #00f2ff !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid #00f2ff !important;
    }

    .login-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #e94560;
        box-shadow: 0px 0px 30px #e94560;
        backdrop-filter: blur(15px);
        text-align: center;
    }

    .wa-button {
        background-color: #25D366;
        color: white !important;
        padding: 12px 25px;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE & SESSION ---
if "valid_keys" not in st.session_state:
    st.session_state.valid_keys = ["VIKAS-786", "CRACK-2026", "VIP-USER"]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "Login"

# --- HELPER FUNCTIONS ---
def generate_upi_qr(upi_id, amount):
    upi_url = f"upi://pay?pa={upi_id}&pn=VikasMishra&am={amount}&cu=INR"
    qr = qrcode.make(upi_url)
    buf = BytesIO()
    qr.save(buf)
    return buf.getvalue()

# --- MAIN UI ---
st.markdown("<h1 style='text-align: center;'>⚡ PDF CRACKER VIP ACCESS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic;'>Developed by VIKAS MISHRA</p>", unsafe_allow_html=True)

if not st.session_state.logged_in:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔑 LOGIN WITH KEY"): st.session_state.auth_mode = "Login"
    with col2:
        if st.button("💳 GET KEY / REGISTER"): st.session_state.auth_mode = "Register"

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    if st.session_state.auth_mode == "Login":
        st.subheader("Enter Your Access Key")
        access_key = st.text_input("Access Key", type="password", placeholder="Paste your key here...")
        
        if st.button("AUTHENTICATE & ENTER"):
            if access_key in st.session_state.valid_keys:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Key!")

    else:
        st.subheader("Get Your Access Key")
        st.write("Step 1: Scan QR & Pay ₹200")
        
        qr_img = generate_upi_qr("9696159863@ptsbi", 200)
        st.image(qr_img, width=230)
        
        st.write("Step 2: Click below to get your key on WhatsApp")
        wa_link = "https://wa.me/919696159863?text=Hello%20Vikas,%20I%20have%20paid%20200%20for%20PDF%20Cracker."
        st.markdown(f'<a href="{wa_link}" target="_blank" class="wa-button">🟢 GET ACCESS KEY ON WHATSAPP</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Dashboard Content
    st.sidebar.markdown("## VIP SYSTEM")
    if st.sidebar.button("EXIT SYSTEM"):
        st.session_state.logged_in = False
        st.rerun()
    st.subheader("🚀 Ready to Crack PDF")
    pdf_file = st.file_uploader("Upload Target PDF", type="pdf")
