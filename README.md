# 🚀 InternAI Agent

## AI-Powered Multi-Agent Internship Recommendation System

InternAI Agent is an intelligent multi-agent system that helps students discover internship opportunities, evaluate eligibility, identify skill gaps, and receive personalized career guidance.

The project was developed to solve a common problem faced by students:

* Internship opportunities are scattered across multiple platforms.
* Eligibility requirements are often unclear.
* Students do not know which skills they are missing.
* Career guidance is usually generic and not personalized.

InternAI Agent addresses these challenges using a Multi-Agent AI architecture that analyzes student profiles and provides tailored internship recommendations.

---

# 🎯 Problem Statement

Students often miss valuable internship opportunities because:

* Opportunities are distributed across different websites.
* Eligibility requirements are difficult to understand.
* Skill gaps are not clearly identified.
* Career guidance lacks personalization.

InternAI Agent uses AI Agents to automate opportunity discovery, eligibility analysis, ranking, and career coaching.

---

# 🏗️ System Architecture

## Multi-Agent Workflow

```text
👤 User
    │
    ▼
📄 Resume Upload
    │
    ▼
👤 Profile Agent
    │
    ▼
🔍 Discovery Agent
    │
    ▼
✅ Eligibility Agent
    │
    ▼
🏆 Ranking Agent
    │
    ▼
🎯 Recommendations
    │
    ▼
📈 Skill Gap Agent
    │
    ▼
🤖 Career Coach Agent
    │
    ▼
💾 Saved Internships
```

---

# 🧠 Agents in the System

## 👤 Profile Agent

Responsibilities:

* Extracts information from uploaded resumes
* Builds student profiles
* Calculates profile score
* Identifies skills, CGPA, and interests

Output:

* Profile Score
* Skills List
* Student Profile

---

## 🔍 Discovery Agent

Responsibilities:

* Loads internship datasets
* Discovers internship opportunities
* Filters opportunities based on user interests

Output:

* Relevant internship opportunities

---

## ✅ Eligibility Agent

Responsibilities:

* Compares user profile with internship requirements
* Checks CGPA eligibility
* Evaluates required skills

Output:

* Eligible internships
* Eligibility status

---

## 🏆 Ranking Agent

Responsibilities:

* Calculates internship match scores
* Ranks opportunities
* Prioritizes best-fit internships

Output:

* Top internship recommendations

---

## 📈 Skill Gap Agent

Responsibilities:

* Identifies missing skills
* Calculates readiness score
* Suggests learning pathways

Output:

* Skill Gap Analysis
* Readiness Score

---

## 🤖 Career Coach Agent

Responsibilities:

* Provides AI-powered career guidance
* Answers career-related questions
* Suggests career paths and preparation strategies

Output:

* Personalized career recommendations

---

# 🎯 Agent Skills

The system implements multiple AI skills:

### 📄 Resume Analysis Skill

* Resume parsing
* Skill extraction
* Profile generation

### 🎯 Eligibility Analysis Skill

* Requirement matching
* Eligibility verification

### 🏆 Recommendation Skill

* Internship ranking
* Match score calculation

### 📈 Skill Gap Analysis Skill

* Missing skill detection
* Readiness evaluation

### 🎤 Interview Preparation Skill

* Interview guidance
* Preparation suggestions

### 🤖 AI Career Coaching Skill

* Personalized career advice
* Career roadmap generation

---

# 👨‍💻 Human-in-the-Loop Design

InternAI Agent follows a Human-in-the-Loop (HITL) approach.

AI assists students by:

* Recommending internships
* Identifying skill gaps
* Generating career insights

The final decision always remains with the student.

Students can:

* Review recommendations
* Analyze opportunities
* Save internships
* Decide their own career path

This ensures transparency and responsible AI usage.

---

# 🔒 Security

Security is built into the system.

### Authentication

* User Registration
* User Login

### Password Protection

* Passwords are hashed using SHA-256
* Credentials are never stored in plain text

### Data Privacy

* User profiles are securely stored
* Personal data remains protected

---

# ⚙️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* SQLite

### Data Processing

* Pandas

### Resume Parsing

* PDFPlumber

### AI Integration

* OpenRouter AI

---

# 📂 Project Structure

```text
InternAI-Agent/
│
├── app.py
│
├── agents/
│   ├── profile_agent.py
│   ├── discovery_agent.py
│   ├── eligibility_agent.py
│   ├── ranking_agent.py
│   └── career_agent.py
│
├── pages/
│   ├── Login.py
│   ├── Register.py
│   ├── Dashboard.py
│   ├── Profile.py
│   ├── Resume_Upload.py
│   ├── Recommendations.py
│   └── Career_Coach.py
│
├── utils/
│   ├── auth.py
│   ├── resume_parser.py
│   └── notifications.py
│
├── database/
│   ├── users.db
│   └── init_db.py
│
├── data/
│   └── internships.csv
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Features

### Current Features

✅ User Authentication

✅ Resume Upload

✅ AI Resume Parsing

✅ Profile Builder

✅ Internship Discovery

✅ Eligibility Analysis

✅ Internship Ranking

✅ Personalized Recommendations

✅ Skill Gap Analysis

✅ Career Coaching

✅ Saved Internships

---

# 🔮 Future Scope

### Live Internship Discovery

Automatically collect opportunities from internship portals.

### Automated Notifications

Send alerts for new matching internships.

### Application Tracking

Track application status and deadlines.

### AI Interview Simulator

Conduct mock interviews and provide feedback.

### Real-Time Opportunity Monitoring

Monitor internship platforms continuously for new opportunities.

---

# 🏆 Impact

InternAI Agent helps students:

* Discover relevant internships faster
* Understand eligibility requirements
* Improve missing skills
* Make informed career decisions
* Increase internship application success rates

---

# 👩‍💻 Developed By

**Sreeja Gurrala**

B.Tech – Computer Science & Engineering (AI & ML)

J.B. Institute of Engineering & Technology (JBIET)

Hyderabad, Telangana, India

---

# ⭐ InternAI Agent

"Helping students discover opportunities, bridge skill gaps, and build successful careers through AI Agents."
