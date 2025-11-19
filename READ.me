# AI Defensive Orchestrator (GTG-1002 Counter Protocol)

## 🎯 Project Goal
This project is a strategic defensive response to the threat of **AI-orchestrated cyberattacks**, as documented by Anthropic's GTG-1002 report. Our mission is to automate the security triage process at machine speed and deliver **compliance-grade traceability**.

## 🔴 The Problem: AI Vulnerabilities
AI attackers operate with **inhuman speed** (80-90% autonomous execution), rendering manual SOC triage obsolete. This reliance on large language models also introduces **AI Hallucination**—the risk of false positives being treated as critical threats. Our workflow is designed to mitigate both flaws simultaneously.

## ⚙️ Architecture: The 7-Node Counter-Orchestrator
The entire solution is a supervised workflow built on the Opus platform, showcasing modularity and auditability.

1.  **Workflow Input:** Accepts raw `JSON_ALERT` and defines core logic constants (`Critical_Path`).
2.  **Parser 1 (Agent):** Extracts required variables (`sourceIp`, `alertType`) from the raw payload.
3.  **External Service:** Calls a public REST API (`ipinfo.io`) to enrich the IP address with `orgName` data.
4.  **Parser 2 (Decider Agent):** The central brain. It applies nine separate risk rules (checking for 'Google', 'Amazon', 'Cloud', etc.) to determine the final `decisionPath`.
5.  **Check_if_Critical & Check_if_Low (Routers):** Two sequential `Decision` nodes that act as "dumb routers" to direct the workflow based on the path output by Parser 2.
6.  **Audit Guardian (AI Skeptic Agent):** **Our unique selling point.** This agent performs **agentic validation** on the Critical Path, double-checking the decider's logic and outputting a `confidence` score and `rationale`.
7.  **Human Review Nodes:** Two separate review nodes integrate human oversight for all escalated cases.
8.  **Workflow Output:** Consolidates the final status and job ID into a single system output string.

## 🏆 Prize-Winning Feature: Exemplary Audit Artifact
The primary output of this workflow is the **Exemplary Decision Artifact** (a single JSON string) which is logged upon completion. This artifact:
* Includes **full provenance** (raw input, enriched data, final decision).
* Contains the **Audit Guardian's verbatim rationale and confidence score**, demonstrating a working solution for AI self-correction (anti-hallucination).

## 🛠️ Technology Stack
* **Core:** Opus by AppliedAI (Agentic Workflow, External Service Node, Decision Node)
* **Data & Logic:** LLM, REST API (ipinfo.io), JSON, Python (Streamlit)
* **Front End:** Streamlit Cloud (Operator Console)

---

## 🚀 Setup & Verification

**Required Files for Deployment:** `app.py` and `requirements.txt`.

### 1. Application URL (Operator Console)
The Streamlit application (`app.py`) provides the interactive front-end. The full application and data ingestion are demonstrated live in the video.

### 2. Opus Workflow Execution
The workflow is built for manual job creation. To run a test:
1.  Navigate to the Opus Job Creation screen for the `AI_Defensive_Orchestrator` workflow.
2.  Paste the required four input fields (`sourceType`, `payload`, `constCritical`, `constLow`) and click **"Create Job"** to initiate the autonomous run.

**(The full end-to-end execution of this auditable workflow is demonstrated in the accompanying video presentation.)**
