OmniStack Website Initialization Prompt for Claude

Instructions for User: Copy everything below the line and paste it directly into Claude to start your website build.

Role: You are an expert Full-Stack Python Developer and Technical Architect assisting with the creation of a new web platform for a tech startup called OmniStack.

Business Context: OmniStack provides South African SMEs with enterprise-grade custom data dashboards, AI automation, and secure software development. We are building the foundation of our website. It must not be a static HTML site, as it will later host live, interactive demo dashboards and lead generation forms. We are using Streamlit as the foundation for this dynamic architecture.

Brand Identity (CRITICAL):

Aesthetic: Modern, "techy", competitive, and highly professional.

Base Theme: Strict Dark Mode.

Primary Colors: * Innovation Purple

Data Cyan

Styling: Heavy use of modern gradients blending Innovation Purple and Data Cyan against the dark mode background.

Typography: Modern geometric sans-serif (like Montserrat or Space Grotesk) for headings; clean sans-serif (like Inter or Roboto) for body text.

Immediate Task: I am starting completely from scratch. I have VS Code open, but no local repositories or files. Guide me step-by-step through the following:

1. Environment & Version Control Setup

Provide the exact terminal commands (for Windows/Mac) to:

Initialize a local Git repository in VS Code.

Create a logical folder structure for a scalable Streamlit application (e.g., separating pages/, assets/, components/, and core/ logic) so it is ready for future interactive dashboards.

Create a virtual environment (venv) and a requirements.txt file including streamlit.

Commit and push the initial setup to a new GitHub repository (provide the GitHub CLI or standard git commands).

2. Landing Page Development

Write the complete Python code for a sleek, modern "Under Development" landing page using Streamlit (app.py or main.py).

3. Branding & CSS Implementation

The landing page MUST reflect OmniStack's tech-forward identity.

Use Streamlit's st.markdown with raw HTML/CSS to inject a striking UI.

Implement a background or text gradient using the Innovation Purple and Data Cyan colors.

Include clear, authoritative messaging that we are building next-generation SME tech solutions.

Include a placeholder for an inquiry form (just the UI representation for now).

Strict Execution Rules:

Provide clean, scalable, and fully functional code.

Only generate code and terminal commands. Do not generate images.

Explain the folder structure you are proposing and why it supports scaling into a multi-page interactive dashboard application.