import streamlit as st
import pikepdf
import itertools
import string
import qrcode
from PIL import Image
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Cracker VIP", layout="centered")

# --- CUSTOM CSS (PREMIUM DARK & NEON) ---
st.markdown("""
    <style>
    .stApp {
        background: #050510;
    }
    label, p, span, .stMarkdown, .stSubheader {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        text-shadow: 0px 0px 10px #00d2ff;
    }
    input {
        color: #00d2ff !important;
        background-color: rgba(0, 210, 255, 0.1) !important;
        border: 2px solid #00d2ff !important;
        border-radius: 10px !important;
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
    /* WhatsApp Button Style */
    .wa-button {
        background-color: #25D366;
        color: white !important;
        padding: 12px 25px;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(37, 211, 102, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE & SESSION ---
# Yahan aap apni pasand ki Access Keys add kar sakte hain
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
st.markdown("<h1 style='text-align: center; color: #00d2ff;'>⚡ PDF CRACKER VIP ACCESS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FFFFFF; font-style: italic;'>Developed by VIKAS MISHRA</p>", unsafe_allow_html=True)

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
                st.success("Access Granted! Opening Dashboard...")
                st.rerun()
            else:
                st.error("Invalid Key! Please get a valid key from Vikas Mishra.")

    else:
        st.subheader("Get Your Access Key")
        st.write("Step 1: Scan QR & Pay ₹200")
        
        qr_img = generate_upi_qr("9696159863@ptsbi", 200)
        st.image(qr_img, width=230)
        
        st.write("Step 2: Click below to get your key on WhatsApp")
        # WhatsApp Link with Custom Message
        wa_link = "https://wa.me/919696159863?text=Hello%20Vikas,%20I%20have%20paid%20200%20for%20PDF%20Cracker.%20Please%20give%20me%20my%20Access%20Key."
        st.markdown(f'<a href="{wa_link}" target="_blank" class="wa-button">🟢 GET ACCESS KEY ON WHATSAPP</a>', unsafe_allow_html=True)
        
        st.info("Payment verify hote hi aapko personal key mil jayegi.")

    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- PDF CRACKER CONTENT ---
    st.sidebar.markdown("<h2 style='color: #00d2ff;'>VIP SYSTEM</h2>", unsafe_allow_html=True)
    if st.sidebar.button("EXIT SYSTEM"):
        st.session_state.logged_in = False
        st.rerun()

    st.subheader("🚀 Start Decrypting Your PDF")
    # Yahan wahi PDF cracking wala code jo maine pehle diya tha...
    pdf_file = st.file_uploader("Upload Target PDF", type="pdf")
    
    if pdf_file:
        st.write("PDF Loaded! Ready to Crack.")
        # Cracking logic starts here...
