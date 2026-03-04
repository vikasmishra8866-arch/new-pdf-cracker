import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vikas Mishra | Pro Dashboard", layout="centered")

# --- CUSTOM CSS (Waisa hi look dene ke liye) ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .login-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #6c63ff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIN/REGISTER STATE ---
if "auth_mode" not in st.session_state:
    st.session_state.auth_mode = "Login"

# --- UI DESIGN ---
st.title("🔓 PDF Cracker Dashboard")
st.write("Managed by VIKAS MISHRA")

# Sliding Toggle jaisa feel dene ke liye Tabs ka use
col1, col2 = st.columns(2)
with col1:
    if st.button("🔐 Login"):
        st.session_state.auth_mode = "Login"
with col2:
    if st.button("📝 Register"):
        st.session_state.auth_mode = "Register"

st.markdown('<div class="login-card">', unsafe_allow_html=True)

if st.session_state.auth_mode == "Login":
    st.subheader("Login to your Account")
    user = st.text_input("Username", placeholder="admin")
    pw = st.text_input("Password", type="password", placeholder="••••••••")
    if st.button("Sign In"):
        if user == "admin" and pw == "admin123":
            st.success("Welcome back!")
        else:
            st.error("Ghalat details!")

else:
    st.subheader("Create New Account")
    new_user = st.text_input("Choose Username")
    new_pw = st.text_input("Choose Password", type="password")
    confirm_pw = st.text_input("Confirm Password", type="password")
    if st.button("Create Account"):
        st.success("Account Created! Ab login karein.")

st.markdown('</div>', unsafe_allow_html=True)
