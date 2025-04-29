# 🌟 Gemini Command-Line Tool

Search anything using Google's Gemini AI directly from your terminal!

## 🚀 Features
- Instant answers to any query
- Supports text/images (WIP)
- Cross-platform (Windows/Linux/macOS)

## ⚡ Quick Start
```bash
# Clone repo
git clone https://github.com/techivivek/gemini-cli.git
cd gemini-cli

# Install dependencies
pip install -r requirements.txt

# Set API key (Linux/macOS)
export GOOGLE_API_KEY="your_key_here"

# Windows (CMD)
setx GOOGLE_API_KEY "your_key_here"

# Run!
python src/gemini.py "Explain quantum physics"
