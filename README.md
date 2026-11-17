# Arirama Selvam M — Professional Portfolio

[![Live Portfolio](https://img.shields.io/badge/Live_Site-GitHub_Pages-00f2fe?style=for-the-badge&logo=github&logoColor=black)](https://ariproject9787.github.io/portfolio/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Firebase](https://img.shields.io/badge/Firebase-Firestore_%26_Auth-FFA611?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-v3.0-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

Welcome to the official portfolio and engineering showcase of **Arirama Selvam M**, Computer Science Engineer, Python Developer, and Network Administrator based in Tamil Nadu, India.

This repository hosts a high-performance, single-page application (SPA) featuring real-time telemetry, AI voice synthesis, an interactive Linux CLI shell, a dual-mode certifications carousel, and an authentication-gated security telemetry dashboard.

---

## 🌐 Live Website

- **Production URL**: [https://ariproject9787.github.io/portfolio/](https://ariproject9787.github.io/portfolio/)
- **Canonical Domain**: `https://ariproject9787.github.io/portfolio/`

---

## 🚀 Key Features

### 1. Android & Mobile Navigation Drawer
- **Touch-Optimized Slide-Out Drawer**: An Android Material-inspired slide-out navigation drawer with smooth backdrop blur, tactile touch feedback, and swift one-tap navigation across all sections.
- **Quick Mobile Actions**: Integrated direct triggers for downloading the Python Developer Resume and launching the terminal simulator directly from mobile screens.

### 2. Dual-Mode Verified Certifications Showcase
- **Horizontal Scroll Carousel**: Smooth horizontal touch swipe with snap alignment (`snap-x snap-mandatory`), custom neon cyber-scrollbars, and keyboard/arrow chevron navigation.
- **Grid Layout Switcher**: Instantly toggle between continuous horizontal scrolling and a responsive multi-column grid layout.
- **Interactive Domain Filter**: Filter 15+ industry certifications by domain (*Python & AI*, *Cybersecurity & Networks*, *Web & Databases*).
- **Lightbox Inspection Modal**: High-resolution certificate previews with direct access to printable PDF credentials.

### 3. Python Developer Resume Integration
- **Direct PDF Dispatch**: Instant download of [`res/cv/python_developer_resume.pdf`](res/cv/python_developer_resume.pdf).
- **Real-Time Telemetry Tracking**: Automatically increments the global download counter in Firebase Firestore and renders an interactive toast feedback banner.
- **Terminal Shell Command**: Type `resume` in the CLI terminal to trigger the download programmatically.

### 4. Interactive Linux Terminal CLI Simulator
- **In-Browser Terminal Shell**: Emulates a Unix terminal interface (`ari@system:~$`) supporting commands:
  - `help`: Lists all terminal capabilities
  - `about`: High-level profile summary
  - `skills`: Technical competencies across languages, networking, and frameworks
  - `projects`: Index of highlighted engineering solutions
  - `cert`: Overview of 15+ verified credentials
  - `resume`: Dispatches the Python Developer Resume PDF
  - `contact`: Official email and social networking handles
  - `clear`: Flushes the terminal buffer

### 5. AI Voice Introduction Synthesizer
- **Web Speech API Engine**: Native browser voiceover speech synthesis reading an introduction of Arirama Selvam's technical background.
- **Dynamic Waveform Visualizer**: Real-time HTML5 Canvas visualizer rendering frequency waveforms synchronized to audio playback.

### 6. Contact Form with Anti-Spam Protection
- **Formspree Endpoint Integration**: Asynchronous `fetch` submission to Formspree (`https://formspree.io/f/xppdpojp`) preventing full-page redirects.
- **Dual Cloud Logging**: Inquiries are simultaneously backed up into Firebase Firestore's `contact_messages` collection.
- **Honeypot Anti-Spam Shield**: Hidden `_gotcha` field catches and silently drops automated bot submissions without interrupting legitimate visitors.

### 7. Live Telemetry & Portfolio Metrics
- **Footer Telemetry Dashboard**: Real-time metrics tracking *Profile Views*, *Interactive Events*, *Resume Dispatches*, *Certifications*, and *Research Papers*.
- **Admin Telemetry Dashboard**: Password-protected portal powered by Firebase Authentication with IP blocklist management, visitor telemetry logs, and contact message inbox.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend Framework** | HTML5 (Semantic), Tailwind CSS (CDN), Custom CSS Glassmorphism |
| **Typography & Icons** | JetBrains Mono, Inter, Font Awesome 6.5 Pro/Free Icons |
| **Audio & Graphics** | Web Speech API (`SpeechSynthesisUtterance`), HTML5 Canvas 2D |
| **Cloud Database** | Firebase Firestore v10 (Real-time NoSQL) |
| **Authentication** | Firebase Auth (Email/Password Admin Gateway) |
| **Form Processing** | Formspree REST API + Firestore Cloud Storage |
| **Hosting & CI/CD** | GitHub Pages, Git Version Control |

---

## 🔒 Security Architecture & API Key Protection

### Understanding Client-Side Firebase Keys
In Firebase Web applications, the `apiKey` included in `firebaseConfig` is a **public project identifier**, not a secret administrative token. Security is enforced through **Firebase Security Rules** and **Google Cloud Console Restrictions**.

### Hardening Steps Implemented

#### 1. Google Cloud Console API Key Restrictions (Recommended Setup)
To lock down your Firebase API Key (`AIzaSyAB1-fJkHg1T2RmyF1vmjK8ddTCdoPHLdU`):
1. Navigate to [Google Cloud Console Credentials](https://console.cloud.google.com/apis/credentials).
2. Select your Firebase project: `userdata-9787`.
3. Locate the **Browser Key** / API Key and click **Edit**.
4. Under **Application restrictions**, select **Websites (HTTP referrers)** and add:
   - `https://ariproject9787.github.io/*`
   - `https://ariproject9787.github.io/portfolio/*`
   - `http://localhost:*` *(for local development)*
   - `http://127.0.0.1:*` *(for local development)*
5. Under **API restrictions**, choose **Restrict key** and limit it strictly to:
   - `Cloud Firestore API`
   - `Identity Toolkit API` *(Firebase Auth)*
   - `Firebase Installations API`
6. Click **Save**. Any unauthorized domain attempting to execute calls with your API key will be blocked at Google's edge proxy.

#### 2. Firestore Production Security Rules (`firestore.rules`)
The database is guarded by strict field-level and role-based policies defined in [`firestore.rules`](firestore.rules):
- **`blocklist`**: Public read-only; writes restricted strictly to authenticated administrators.
- **`portfolio_stats`**: Public can only read and increment telemetry counters (`profile_views`, `events`, `downloads`); full document overwrite or deletion requires administrative authentication.
- **`visitor_logs`**: Public write-only with payload schema validation; querying and deletion restricted strictly to the administrator.
- **`contact_messages`**: Public write-only with field sanitization; reading the inbox requires administrator credentials.
- **All other collections**: Closed by default (`allow read, write: if request.auth != null;`).

#### 3. Client-Side Security Headers & Protections
- **MIME Sniffing Prevention**: `<meta http-equiv="X-Content-Type-Options" content="nosniff">`
- **Referrer Privacy Policy**: `<meta name="referrer" content="strict-origin-when-cross-origin">`
- **Reverse Tabnabbing Mitigation**: All external hyperlinks enforce `rel="noopener noreferrer"`.
- **XSS Defense**: User input in the CLI terminal and form inputs are sanitized using HTML entity escaping (`escapeHtml`).
- **Formspree Honeypot**: Hidden `_gotcha` input prevents automated bots from depleting submission limits.

---

## 📈 Search Engine Optimization (SEO) & Indexing

The portfolio includes comprehensive SEO optimization:

### 1. Structured Data (Schema.org JSON-LD)
- **`WebSite` Schema**: Declares canonical search properties and naming.
- **`Person` Schema**: Specifies Arirama Selvam M's official identifiers, alumni affiliation (*Dr. G.U. Pope College of Engineering*), skills, and social channels (*GitHub, LinkedIn, Credly, Instagram*).
- **`ScholarlyArticle` Schemas**: Full bibliographic citations for two published research papers:
  - *Automated Gastrointestinal Disease Detection Using Deep Learning with CNN and U-Net Architectures* (IJERT, DOI: `10.17577/IJERTCONV14IS030014`)
  - *A Multimodal Deep Learning Framework for Early Detection of Parkinson's Disease* (IJEASM)

### 2. Search Engine & AI Crawler Policy (`robots.txt`)
[`robots.txt`](robots.txt) welcomes all primary search engine indexers and explicit AI search crawlers:
- **Search Engines**: `Googlebot`, `Bingbot`, `DuckDuckBot`, `Yandex`, `Baiduspider`
- **AI Bots & LLMs**: `OAI-SearchBot`, `ChatGPT-User`, `Claude-Web`, `PerplexityBot`, `YouBot`, `Applebot`, `GPTBot`, `ClaudeBot`, `Google-Extended`
- Explicit allowance for all PDF resumes and certificate credentials under `/res/`.

### 3. XML Sitemap with Image Extensions (`sitemap.xml`)
[`sitemap.xml`](sitemap.xml) provides Google and Bing with direct priority endpoints:
- Homepage (`priority 1.0`) with Google Image XML metadata for portrait indexing.
- Direct PDF resume link (`priority 0.85`).
- Official PDF certificates (`priority 0.7`).

---

## 📂 Project Directory Structure

```plaintext
portfolio/
├── index.html                   # Core single-page portfolio application
├── robots.txt                   # Search & AI crawler discovery policies
├── sitemap.xml                  # XML sitemap with image extensions
├── firestore.rules              # Firebase Firestore cloud security rules
├── requirements.txt             # Project environment manifest
├── README.md                    # Comprehensive documentation
├── google5b7bdd4391b711bf.html   # Google Search Console domain verification
└── res/
    ├── arirama_selvam.jpeg      # Profile portrait (root fallback)
    ├── img/
    │   ├── arirama_selvam.jpeg  # High-resolution official profile photo
    │   └── profile.png          # Alternate avatar graphic
    ├── cv/
    │   ├── python_developer_resume.pdf  # Primary Python Developer Resume
    │   ├── all_in_one_resume.pdf
    │   ├── full_stack_resume.pdf
    │   ├── linux_administrator_resume.pdf
    │   ├── Network_Administrator.pdf
    │   └── cyber_security_resume.pdf
    └── certificate/
        ├── pantech/             # Python, AI & ML internship credentials & PDFs
        ├── corizo/              # Cybersecurity specialist credential & PDF
        ├── novitech/            # Ethical hacking & R&D technical certificates
        ├── eduprep/             # Python, SQL, React, JS, Java, C certificates
        ├── guvi/                # AI & ChatGPT masterclass certification
        ├── college/             # Power BI & academic degree certifications
        └── others/              # Cisco / Networking basics certifications
```

---

## 💻 Local Development Setup

To test and review the portfolio locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AriProject9787/portfolio.git
   cd portfolio
   ```

2. **Launch a local static server**:
   Using Python:
   ```bash
   python -m http.server 8000
   ```
   Or using Node.js `npx serve`:
   ```bash
   npx serve .
   ```

3. **Open in your browser**:
   Navigate to `http://localhost:8000`.

---

## 📬 Contact & Social Profiles

- **Email**: [ariramaselvam9787@gmail.com](mailto:ariramaselvam9787@gmail.com)
- **GitHub**: [github.com/AriProject9787](https://github.com/AriProject9787)
- **LinkedIn**: [linkedin.com/in/ariramaselvam](https://linkedin.com/in/ariramaselvam)
- **Credly**: [credly.com/users/arirama-selvam-m](https://www.credly.com/users/arirama-selvam-m/)
- **Instagram**: [@arirama_selvam](https://instagram.com/arirama_selvam) / [@hack_tech_tamil](https://instagram.com/hack_tech_tamil)

---

*© 2026 Arirama Selvam M. All rights reserved.*
