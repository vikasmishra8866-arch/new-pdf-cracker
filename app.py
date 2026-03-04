import streamlit as st
import pikepdf
import itertools
import string
import qrcode
from PIL import Image
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Cracker Pro", layout="centered")

# --- IMPROVED HIGH-CONTRAST NEON CSS ---
st.markdown("""
    <style>
    /* Sabse pehle background aur global text colour fix */
    .stApp {
        background: radial-gradient(circle, #1a1a2e 0%, #111122 100%);
    }
    
    /* Sare labels aur text ko Force White karna */
    label, p, span, .stMarkdown, .stSubheader, .stCaption {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        text-shadow: 0px 0px 8px rgba(0, 210, 255, 0.4);
    }

    /* Input box ke andar ka text white karna */
    input {
        color: #FFFFFF !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
    }

    /* Card design with Neon Border */
    .login-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #00d2ff;
        box-shadow: 0px 0px 25px #00d2ff;
        backdrop-filter: blur(15px);
        margin-top: 20px;
    }

    /* Buttons Style */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #00d2ff, #3a7bd5);
        color: #FFFFFF !important;
        border: none;
        padding: 10px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE & SESSION ---
if "users" not in st.session_state:
    st.session_state.users = {"admin": "admin123"}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "Login"

# --- MANUAL UTR LIST (Admin Approvals) ---
# Yahan wo UTR dalo jinhone sach mein pay kiya hai
APPROVED_UTRS = ["236451365213", "112233445566"] 

# --- HELPER FUNCTIONS ---
def generate_upi_qr(upi_id, amount):
    upi_url = f"upi://pay?pa={upi_id}&pn=VikasMishra&am={amount}&cu=INR"
    qr = qrcode.make(upi_url)
    buf = BytesIO()
    qr.save(buf)
    return buf.getvalue()

# --- MAIN UI ---
st.markdown("<h1 style='text-align: center; color: #00d2ff;'>⚡ PDF CRACKER PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FFFFFF;'>MANAGED BY VIKAS MISHRA</p>", unsafe_allow_html=True)

if not st.session_state.logged_in:
    # --- LOGIN / REGISTER TABS ---
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔐 ACCESS LOGIN"): st.session_state.auth_mode = "Login"
    with col2:
        if st.button("📝 NEW REGISTRATION"): st.session_state.auth_mode = "Register"

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    if st.session_state.auth_mode == "Login":
        st.subheader("Login to Dashboard")
        u = st.text_input("Username", key="login_u")
        p = st.text_input("Password", type="password", key="login_p")
        if st.button("UNLOCK NOW"):
            if u in st.session_state.users and st.session_state.users[u] == p:
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("Access Denied! Galat Username ya Password.")

    else:
        st.subheader("Register (Access Fee: ₹200)")
        
        # QR Code Display
        qr_img = generate_upi_qr("9696159863@ptsbi", 200)
        st.image(qr_img, width=220)
        st.info("Scan QR with GPay/PhonePe & enter UTR below.")
        
        utr_no = st.text_input("Enter 12-digit UTR No.", placeholder="Example: 236451365213")
        new_u = st.text_input("Choose Username")
        new_p = st.text_input("Set Password", type="password")
        
        if st.button("VERIFY & REGISTER"):
            if utr_no in APPROVED_UTRS:
                st.session_state.users[new_u] = new_p
                st.success("Payment Verified! Account Created. Ab Login karein.")
            else: 
                st.error("Invalid UTR! Pehle payment karein ya Admin se contact karein.")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- CRACKER DASHBOARD ---
    st.sidebar.markdown("<h3 style='color: #00d2ff;'>System Online</h3>", unsafe_allow_html=True)
    if st.sidebar.button("LOGOUT"):
        st.session_state.logged_in = False
        st.rerun()

    st.subheader("🚀 Advanced PDF Decryptor")
    pdf_file = st.file_uploader("Upload Password Protected PDF", type="pdf")
    
    with st.expander("🛠️ Brute-Force Settings"):
        custom_hint = st.text_input("Hint (Name of person)", help="Start with 4 letters")
        digit_count = st.slider("Digits to try (0000-9999)", 1, 6, 4)
    
    indian_names = ["ROHI", "AMIT", "SURA", "VIKA", "RAHU", "ANKE", "DEEP", "PRIY", "NEHA", "SUNI"]

    if pdf_file and st.button("START CRACKING"):
        found = False
        with st.status("Cracking...", expanded=True) as status:
            # Logic: Name + Digits
            search_list = [custom_hint[:4].upper()] if custom_hint else indian_names
            
            for name in search_list:
                status.update(label=f"Trying Pattern: {name}...")
                for d in itertools.product(string.digits, repeat=digit_count):
                    pwd = name + "".join(d)
                    try:
                        with pikepdf.open(pdf_file, password=pwd):
                            st.balloons()
                            st.success(f"🎯 PASSWORD FOUND: {pwd}")
                            found = True; break
                    except: continue
                if found: break
            
            if not found: st.error("Nahi mila! Pattern change karke try karein.")
            status.update(label="Scanning Finished", state="complete")
