import streamlit as st
import pikepdf
import itertools
import string

# --- PAGE CONFIG ---
st.set_page_config(page_title="PDF Cracker | Vikas Mishra", page_icon="🔓")

# --- INITIALIZE DATABASE (Temporary) ---
if "users" not in st.session_state:
    st.session_state.users = {"admin": "admin123"} # Default user
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- HEADER ---
def draw_header():
    st.title("🔓 PDF Cracker")
    st.caption("Managed by VIKAS MISHRA © 2026")
    st.markdown("---")

# --- LOGIN & REGISTER LOGIC ---
def auth_page():
    draw_header()
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])
    
    with tab1:
        st.subheader("Login Dashboard")
        l_user = st.text_input("Username", key="l_user")
        l_pass = st.text_input("Password", type="password", key="l_pass")
        if st.button("Login"):
            if l_user in st.session_state.users and st.session_state.users[l_user] == l_pass:
                st.session_state.logged_in = True
                st.success("Welcome back, Vikas!")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

    with tab2:
        st.subheader("Create New Account")
        r_user = st.text_input("Choose Username", key="r_user")
        r_pass = st.text_input("Choose Password", type="password", key="r_pass")
        if st.button("Register"):
            if r_user and r_pass:
                st.session_state.users[r_user] = r_pass
                st.success("Registration Successful! Please Login.")
            else:
                st.warning("Details toh fill karo bhai!")

# --- PDF CRACKER ENGINE ---
def cracker_page():
    draw_header()
    st.sidebar.success(f"Logged in as Admin")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    uploaded_file = st.file_uploader("Upload Password Protected PDF", type="pdf")
    name_prefix = st.text_input("Name Prefix (e.g., ROHI)", "ROHI").upper()

    if uploaded_file and st.button("🚀 Start Cracking"):
        with st.status("Cracking in progress...", expanded=True) as status:
            found = False
            # Generating combinations: Prefix + 4 digits (0000-9999)
            for digits in itertools.product(string.digits, repeat=4):
                password = name_prefix + "".join(digits)
                try:
                    with pikepdf.open(uploaded_file, password=password) as pdf:
                        st.balloons()
                        st.success(f"🎯 Password Found: **{password}**")
                        found = True
                        break
                except pikepdf.PasswordError:
                    continue
            
            if not found:
                st.error("Password nahi mila. Try another prefix.")
            status.update(label="Process Complete!", state="complete")

# --- MAIN APP FLOW ---
if not st.session_state.logged_in:
    auth_page()
else:
    cracker_page()
