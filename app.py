import streamlit as st

# Page configuration - Official Setup
st.set_page_config(
    page_title="Meta Privacy & Security Audit Tool",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS to mimic Meta Developer / Instagram Internal Support Portal
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #F0F2F5 !important;
    }
    
    /* Meta Branded Top Header */
    .meta-header {
        background: linear-gradient(135deg, #4F46E5 0%, #06B6D4 100%);
        padding: 22px 20px;
        border-radius: 8px 8px 0px 0px;
        color: white;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .meta-title {
        font-size: 20px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin: 0;
        display: flex;
        align-items: center;
    }
    .meta-subtitle {
        font-size: 11px;
        opacity: 0.85;
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Support Box / Container */
    .support-container {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 0px 0px 8px 8px;
        border: 1px solid #E4E4E7;
        border-top: none;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    
    .section-title {
        color: #18181B;
        font-size: 16px;
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 8px;
    }
    
    .section-desc {
        color: #71717A;
        font-size: 13px;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    
    /* Professional Alert Box for the Fake Result */
    .audit-result-box {
        background-color: #FEF2F2;
        border: 1px solid #FEE2E2;
        border-left: 6px solid #EF4444;
        padding: 18px;
        border-radius: 6px;
        margin-top: 25px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    .result-header {
        color: #991B1B;
        font-size: 14.5px;
        font-weight: 700;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }
    
    .result-row {
        margin-bottom: 8px;
        font-size: 13px;
        color: #374151;
        line-height: 1.6;
    }
    
    .label {
        font-weight: 600;
        color: #1F2937;
        display: inline-block;
        width: 130px;
    }
    
    .status-badge {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 12px;
        border: 1px solid #FCA5A5;
    }
    
    .verdict-text {
        margin-top: 12px;
        padding-top: 12px;
        border-top: 1px solid #FCA5A5;
        font-size: 13px;
        color: #7F1D1D;
        font-weight: 500;
        background-color: rgba(239, 68, 68, 0.05);
        padding: 10px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Render Top Header
st.markdown("""
    <div class="meta-header">
        <div class="meta-title">Meta Security & Moderation Operations</div>
        <div class="meta-subtitle">Internal Audit & System Diagnostics Portal</div>
    </div>
""", unsafe_allow_html=True)

# Render Main Input Box Container
st.markdown("""
    <div class="support-container">
        <div class="section-title">Instagram Content & Comment Lifecycle Audit</div>
        <div class="section-desc">
            Enter the verified Instagram Media Object URL (Post Link) to run automated diagnostics on deleted comments, account session authorization logs, and content state updates.
        </div>
    </div>
""", unsafe_allow_html=True)

# Streamlit Text Input (Styled clean)
post_url = st.text_input("Instagram Post URL / Media Link:", placeholder="https://www.instagram.com/p/...")

# Audit Button
if st.button("Run Diagnostics & Fetch Logs", type="primary"):
    if post_url:
        if "instagram.com" in post_url.lower():
            # Creating a fake delay spinner for realism
            with st.spinner("Connecting to Meta Edge Servers & Querying Database Logs..."):
                import time
                time.sleep(2.5) # 2.5 seconds wait time for reality effect in video
                
            # Render the highly technical official-looking response
            st.markdown("""
                <div class="audit-result-box">
                    <div class="result-header">⚠️ DIAGNOSTIC REPORT: CRITICAL MODERATION DISCREPANCY DETECTED</div>
                    <div class="result-row"><span class="label">Object Type:</span> Media_Comment_Lifecycle</div>
                    <div class="result-row"><span class="label">System Status:</span> <span class="status-badge">NO GLITCH / NO BUG</span></div>
                    <div class="result-row"><span class="label">Server Code:</span> HTTP 200 OK (Request Successfully Processed)</div>
                    <div class="result-row"><span class="label">Action Source:</span> Client-Side Manual Request (Device Session)</div>
                    
                    <div class="verdict-text">
                        <b>LOG ANALYSIS VERDICT:</b><br>
                        The comment was successfully removed via an explicit <b>"Delete Request"</b> triggered manually by an authorized user session. This action was NOT caused by an Instagram server exception, background crash, database sync glitch, or automated spam filter. The deletion request originated directly from a device session actively managed on this post.
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Invalid Resource URL. Please input a structured instagram.com/p/ link.")
    else:
        st.warning("Action Required: Please paste the target link before initiating server diagnostics.")
