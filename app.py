import streamlit as st
import pikepdf
import itertools
import string
import qrcode
from PIL import Image
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Cracker Pro", layout="centered")

# --- PREMIUM RGB CSS ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #e94560;
    }
    .login-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #00d2ff;
        box-shadow: 0px 0px 20px #00d2ff, inset 0px 0px 10px #00d2ff;
        backdrop-filter: blur(10px);
    }
    h1, h2, h3 {
        color: #00d2ff !important;
        text-shadow: 2px 2px 10px #00d2ff;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        box-shadow: 0px 5px 15px rgba(0, 210, 255, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 25px #00d2ff;
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

# --- HELPER FUNCTIONS ---
def generate_upi_qr(upi_id, amount):
    upi_url = f"upi://pay?pa={upi_id}&pn=VikasMishra&am={amount}&cu=INR"
    qr = qrcode.make(upi_url)
    buf = BytesIO()
    qr.save(buf)
    return buf.getvalue()

# --- MAIN UI ---
st.title("⚡ PDF CRACKER PRO")
st.caption("ULTIMATE TOOL BY VIKAS MISHRA")

if not st.session_state.logged_in:
    # --- LOGIN / REGISTER TABS ---
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔐 ACCESS LOGIN"): st.session_state.auth_mode = "Login"
    with col2:
        if st.button("📝 NEW REGISTRATION"): st.session_state.auth_mode = "Register"

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    if st.session_state.auth_mode == "Login":
        st.subheader("Admin Login")
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("UNLOCK SYSTEM"):
            if u in st.session_state.users and st.session_state.users[u] == p:
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("Access Denied!")

    else:
        st.subheader("Registration (Charge: ₹200)")
        st.info("Scan QR & Pay to unlock Registration")
        
        # QR Code Display
        qr_img = generate_upi_qr("9696159863@ptsbi", 200)
        st.image(qr_img, width=200, caption="Scan with PhonePe/GPay")
        
        utr_no = st.text_input("Enter 12-digit UTR/Transaction ID after payment")
        new_u = st.text_input("New Username")
        new_p = st.text_input("New Password", type="password")
        
        if st.button("VERIFY & CREATE"):
            if len(utr_no) == 12: # Simple verification
                st.session_state.users[new_u] = new_p
                st.success("Payment Received! Account Active. Please Login.")
            else: st.error("Invalid Transaction ID!")
    
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- CRACKER DASHBOARD ---
    st.sidebar.success("System Online")
    if st.sidebar.button("LOGOUT"):
        st.session_state.logged_in = False
        st.rerun()

    st.subheader("🚀 Advanced PDF Decryptor")
    
    # Input Area
    pdf_file = st.file_uploader("Upload Target PDF", type="pdf")
    
    with st.expander("🛠️ Brute-Force Settings"):
        custom_hint = st.text_input("Hint (Optional: e.g. Rohit)", help="Enter name if you remember part of it")
        digit_count = st.slider("Random Digits to try", 1, 6, 4)
    
    # Indian Name List for Cracking
    indian_names = ["ROHI", "AMIT", "SURA", "VIKA", "RAHU", "ANKE", "DEEP", "PRIY", "NEHA", "SUNI"]

    if pdf_file and st.button("INITIATE CRACKING"):
        found = False
        with st.status("Analyzing Encryption...", expanded=True) as status:
            
            # 1. Try with Hint + Digits
            if custom_hint:
                prefix = custom_hint[:4].upper()
                for d in itertools.product(string.digits, repeat=digit_count):
                    pwd = prefix + "".join(d)
                    try:
                        with pikepdf.open(pdf_file, password=pwd):
                            st.success(f"🎯 FOUND: {pwd}")
                            found = True; break
                    except: continue
            
            # 2. Try with Indian Name List if not found
            if not found:
                for name in indian_names:
                    status.update(label=f"Trying Name Pattern: {name}...")
                    for d in itertools.product(string.digits, repeat=digit_count):
                        pwd = name + "".join(d)
                        try:
                            with pikepdf.open(pdf_file, password=pwd):
                                st.success(f"🎯 FOUND IN LIST: {pwd}")
                                found = True; break
                        except: continue
                    if found: break
            
            if not found: st.error("Could not crack with current patterns.")
            status.update(label="Scanning Complete", state="complete")
