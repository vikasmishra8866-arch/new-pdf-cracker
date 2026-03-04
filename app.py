import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | PDF Cracker Pro", layout="centered")

# --- IMPROVED HIGH-CONTRAST CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: #0a0a12; /* Ekdam Dark taaki text chamke */
        color: white;
    }
    
    /* Labels aur Text Input ka rang */
    label, .stMarkdown p, .stSubheader {
        color: #00f2ff !important; /* Neon Cyan Labels */
        font-weight: bold !important;
        text-shadow: 0px 0px 5px rgba(0, 242, 255, 0.5);
    }
    
    /* Input Boxes ka text kaala na dikhe */
    input {
        color: white !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid #00f2ff !important;
    }

    /* Registration Card */
    .login-card {
        background: rgba(15, 52, 96, 0.8);
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #e94560; /* Pinkish Red Border */
        box-shadow: 0px 0px 30px rgba(233, 69, 96, 0.4);
    }

    /* VIP Text for Prices */
    .price-tag {
        font-size: 24px;
        color: #ffcc00; /* Gold color for money */
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE ---
if "users" not in st.session_state:
    st.session_state.users = {"admin": "admin123"}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "Login"

# --- SMART UTR VERIFICATION (Demo Logic) ---
# Asli system mein ye data database se aayega
ADMIN_APPROVED_UTRS = ["236451365213", "987654321098"] 

def generate_upi_qr(upi_id, amount):
    upi_url = f"upi://pay?pa={upi_id}&pn=VikasMishra&am={amount}&cu=INR"
    qr = qrcode.make(upi_url)
    buf = BytesIO()
    qr.save(buf)
    return buf.getvalue()

# --- UI LOGIC ---
st.title("⚡ PDF CRACKER PRO")
st.markdown("<p style='text-align: center; color: #00f2ff;'>POWERED BY VIKAS MISHRA</p>", unsafe_allow_html=True)

if not st.session_state.logged_in:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔐 LOGIN ACCESS"): st.session_state.auth_mode = "Login"
    with col2:
        if st.button("📝 REGISTER NOW"): st.session_state.auth_mode = "Register"

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    if st.session_state.auth_mode == "Login":
        st.subheader("System Authentication")
        u = st.text_input("Username", placeholder="Enter ID")
        p = st.text_input("Password", type="password", placeholder="Enter Password")
        if st.button("BOOT SYSTEM"):
            if u in st.session_state.users and st.session_state.users[u] == p:
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("❌ Access Denied: Galat Details")

    else:
        st.markdown('<p class="price-tag">Registration Fee: ₹200</p>', unsafe_allow_html=True)
        
        # QR Code with instructions
        qr_img = generate_upi_qr("9696159863@ptsbi", 200)
        st.image(qr_img, width=250)
        st.warning("⚠️ Payment ke baad 12-digit UTR yahan bharein. Admin verify karega.")

        utr_input = st.text_input("Transaction ID / UTR", placeholder="Example: 236451365213")
        new_u = st.text_input("Choose Username")
        new_p = st.text_input("Set Password", type="password")
        
        if st.button("VERIFY PAYMENT & REGISTER"):
            # Yahan humne "Smart Check" lagaya hai
            if utr_input in ADMIN_APPROVED_UTRS:
                st.session_state.users[new_u] = new_p
                st.success("✅ Payment Verified! Account Created. Now Go to Login.")
            else:
                st.error("❌ Invalid UTR! Agar aapne payment kar diya hai, toh Admin se contact karein.")
                st.info("💡 Hint for Demo: Use '236451365213' as UTR")

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.sidebar.write(f"Logged in as Admin")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
    st.success("🎯 Aapka PDF Cracker Dashboard yahan khulega!")
