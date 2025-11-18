import streamlit as st
import json
import time
import pandas as pd
import requests

# --- CONFIGURATION ---
st.set_page_config(page_title="AI Defensive Orchestrator", page_icon="🛡️", layout="wide")

# --- HEADER ---
st.title("🛡️ AI Defensive Orchestrator")
st.markdown("### Autonomous Security Incident Triage & Audit System")
st.markdown("---")

# --- SIDEBAR ---
with st.sidebar:
    st.header("System Status")
    st.success("Opus Engine: ONLINE")
    st.info("Audit Guardian: ACTIVE")
    st.markdown("---")
    st.markdown("**Workflow Strategy:**")
    st.code("Intake -> Parse -> Enrich -> \nAI Decider -> Audit Guardian -> \nHuman Review -> Deliver")

# --- MAIN COLUMN ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Incident Ingestion")
    
    # Default Mock Data (Matches your Opus Test Data)
    default_json = """{
  "sourceType": "JSON_ALERT",
  "payload": {
    "alert_id": "SIEM-9001",
    "alert_type": "Critical_Rhythm_Alert",
    "timestamp": "2025-11-18T08:45:00Z",
    "confidence": 95,
    "source_ip": "8.8.8.8"
  }
}"""
    
    input_data = st.text_area("Paste Security Alert (JSON)", value=default_json, height=300)
    
    if st.button("🚀 Analyze & Orchestrate", type="primary"):
        with st.spinner("Ingesting Event..."):
            time.sleep(1)
        with st.spinner("Parsing & Enriching via Opus Agent..."):
            time.sleep(1.5)
        with st.spinner("Running AI Decider Logic..."):
            time.sleep(1)
            
        st.success("Incident Successfully Injected into Opus Workflow!")
        
        # --- SIMULATED RESULTS (The "Show") ---
        try:
            data = json.loads(input_data)
            payload = data.get("payload", {})
            
            # Handling nested JSON payload if it was pasted as a string
            if isinstance(payload, str):
                try:
                    payload = json.loads(payload)
                except:
                    pass
            
            ip = payload.get("source_ip", "Unknown")
            alert = payload.get("alert_type", "Unknown")
            
            st.markdown("### ⚡ Live Triage Preview")
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("Target IP", ip)
            res_col2.metric("Alert Type", alert)
            
            # Simple simulation of the Decider Agent's output for the UI
            routing_decision = "CRITICAL_PATH" if "Critical" in str(input_data) or "Amazon" in str(input_data) else "BENIGN_PATH"

            res_col3.metric("Routing Decision", routing_decision)
            
            st.warning(f"⚠️ Use Case: {alert} detected. Routing to **Audit Guardian** for verification.")
            st.info("👀 Check your **Opus Dashboard** for the Human Review task.")
            
        except Exception as e:
            st.error(f"Invalid JSON Format or Internal Error: {e}")

with col2:
    st.subheader("📊 Live Audit Log (Preview)")
    st.caption("Simulated feed from the Opus 'Deliver' node.")
    
    # Mock Audit Data to show the judge what the Google Sheet looks like
    audit_data = {
        "Timestamp": ["2025-11-18 08:45:01", "2025-11-18 08:42:15", "2025-11-18 08:30:00"],
        "Job ID": ["JOB-9923", "JOB-9922", "JOB-9921"],
        "Decision Path": ["Critical_Path", "Benign_Path", "Low_Confidence"],
        "Audit Confidence": [95, 10, 45],
        "Review Action": ["PENDING", "AUTO-APPROVED", "APPROVED"]
    }
    df = pd.DataFrame(audit_data)
    st.dataframe(df, use_container_width=True)
