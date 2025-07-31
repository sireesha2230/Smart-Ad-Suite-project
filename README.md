# Smart-Ad-Suite-project
An AI-powered ad campaign assistant that optimizes budget allocation and generates ad copy based on your product, tone, and platform. Built with Streamlit, Python, and OpenAI.
# SmartAd Suite – AI-Driven Ad Campaign Assistant

**SmartAd Suite** is a project I built to explore how AI can simplify digital marketing workflows. The tool is designed for marketers, startups, and small business owners who want to make smarter ad decisions without needing a background in data science or copywriting.

This app brings together two major features:
- **Ad Budget Optimizer** – Helps you allocate ad spend efficiently across platforms
- **AI Ad Copy Generator** – Creates short, catchy ad text using OpenAI’s GPT-3.5

---

## Why I Built This 

I’ve seen how challenging it can be for small businesses to balance their ad budgets or write effective ad content. Most people either rely on gut feeling or expensive marketing agencies. I wanted to build something that makes these tasks simple, data-driven, and accessible — even for someone without a marketing background.

---

## Key Features 

### 1.  Ad Budget Optimizer  
Upload a CSV with your ad metrics — things like CTR, CPC, and conversion rates. The app calculates ROI for each platform and distributes your budget based on those values. You get a clean table and a bar chart to visualize where your money is going.

### 2. AI-Powered Ad Copy  
You can describe your product, choose the tone (funny, professional, persuasive, etc.), and pick the platform. The app connects to OpenAI's GPT-3.5 model and returns a ready-to-use ad — perfect for Facebook, Google, or LinkedIn campaigns.

---

## Sample Input 

Your CSV should look something like this:

```csv
Platform,CTR,CPC,ConversionRate
Google,0.05,0.6,0.10
Facebook,0.04,0.5,0.08
LinkedIn,0.03,0.8,0.12
Upload this through the sidebar, set your total ad budget, and the optimizer takes care of the rest.

How to Run the App Locally :
# Clone the repo
git clone https://github.com/your-username/smartad-suite.git
cd smartad-suite

# (Optional) Set up a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py

About the AI Part :
To use the ad copy generator, you’ll need an OpenAI API key. You can create one at platform.openai.com.
Note: If your free credits are over, you’ll need to enable billing or skip the copy generation part — the optimizer works independently.

Tech Stack:
Python
Streamlit
Pandas, Matplotlib
OpenAI GPT-3.5 API (for copywriting)

## Final Thoughts 
This project helped me get hands-on with integrating AI APIs into real-world use cases. It also sharpened my understanding of digital marketing KPIs and how data can drive better ad decisions.

If you're into marketing tech, AI automation, or just building useful tools, feel free to fork the project or share feedback.
