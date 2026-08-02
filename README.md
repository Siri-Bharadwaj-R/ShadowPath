# ShadowPath

> **Active Directory Attack Path Analysis Platform**

ShadowPath is a desktop cybersecurity application inspired by BloodHound that analyzes Active Directory environments to identify privilege escalation paths, assess security risks, map findings to the MITRE ATT&CK framework, and generate professional security reports.

Built with **Python** and **PyQt6**, ShadowPath supports both an interactive desktop GUI and a command-line interface for performing Active Directory security assessments.

---

## Features

- Active Directory relationship parsing
- LDAP-based Active Directory data collection
- Relationship graph construction
- Attack path discovery
- Risk scoring engine
- MITRE ATT&CK technique mapping
- Interactive attack graph visualization
- Executive security dashboard
- Professional PDF report generation
- Desktop GUI and Command-Line Interface (CLI)

---

## Screenshots

### Executive Dashboard

<img width="1903" height="1068" alt="image" src="https://github.com/user-attachments/assets/f2c6439d-ce24-457b-95b4-b182b8b59549" />

### MITRE ATT&CK Mapping

<img width="1900" height="1067" alt="image" src="https://github.com/user-attachments/assets/c04054bc-a62e-4a19-8d5f-5e0fcd1e7d08" />

---

## Architecture

```text
┌──────────────────────────┐
│     LDAP Collector       │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│  Relationship Builder    │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     Attack Graph         │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│  Attack Path Discovery   │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│      Risk Engine         │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│  MITRE ATT&CK Mapping    │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│ Actionable Security      │
│ Intelligence             │
└──────────────────────────┘
```

---

## Technology Stack

- Python
- PyQt6
- NetworkX
- LDAP3
- ReportLab
- Matplotlib

---

## Project Structure

```text
ShadowPath/
│
├── data/
│   └── sample_domain.json          # Sample Active Directory dataset
│
├── reports/                        # Generated PDF security reports
│
├── src/
│   │
│   ├── ad/                         # Active Directory collection & parsing
│   │   ├── ldap_collector.py
│   │   ├── relationship_builder.py
│   │   └── ad_models.py
│   │
│   ├── analysis/                   # Security analysis engines
│   │   ├── attack_paths.py
│   │   ├── attack_simulator.py
│   │   ├── risk_engine.py
│   │   ├── mitigation_engine.py
│   │   ├── intelligence_engine.py
│   │   ├── mitre_engine.py
│   │   ├── report_generator.py
│   │   └── security_summary.py
│   │
│   ├── core/                       # Graph construction & data models
│   │   ├── graph_builder.py
│   │   ├── parser.py
│   │   └── models.py
│   │
│   ├── engine/                     # Main orchestration engine
│   │   ├── engine.py
│   │   └── models.py
│   │
│   ├── gui/                        # PyQt6 desktop interface
│   │   ├── pages/
│   │   ├── widgets/
│   │   └── workers/
│   │
│   ├── ui/                         # Dashboard framework & reusable UI components
│   │   ├── dashboard/
│   │   └── framework/
│   │
│   ├── visualization/              # Attack graph visualization
│   │   └── graph_visualizer.py
│   │
│   └── main.py                     # Application entry point
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Platform Overview

ShadowPath provides multiple execution modes to support interactive analysis, automation, and realistic Active Directory security simulations.

### 🖥️ Desktop GUI

Interactive PyQt6 desktop application for visualizing attack paths, assessing Active Directory security posture, exploring MITRE ATT&CK mappings, and generating executive security reports.

### 💻 Command-Line Interface (CLI)

Lightweight terminal interface for rapid security assessments, automation, console-based analysis, and professional PDF report generation.

### 🔄 Simulation Profiles *(Coming in v2.0)*

Analyze realistic enterprise Active Directory environments using built-in security profiles that simulate organizations with varying security postures and attack surfaces.

---

## Future Roadmap

Planned enhancements include:

- Multiple built-in Active Directory scan profiles
- Live LDAP environment scanning
- Custom JSON profile imports
- Enhanced attack graph interaction
- Enterprise-scale Active Directory simulations

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Siri-Bharadwaj-R/ShadowPath.git
```

Navigate into the project:

```bash
cd ShadowPath
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running ShadowPath

ShadowPath can be launched in either graphical or command-line mode.

### 🖥️ Desktop GUI

```bash
python -m src.gui.app
```

### 💻 Command-Line Interface (CLI)

```bash
python -m src.main --cli
```

---

## Inspiration

ShadowPath is inspired by Microsoft's Active Directory security model and the concepts introduced by BloodHound for attack path analysis. It is an educational and portfolio project designed to demonstrate Active Directory security analysis techniques.

---
