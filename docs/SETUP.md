# 🔍 Detailed Setup Guide

## API Key Configuration
1. Get your key from [Google AI Studio](https://aistudio.google.com/)
   
For Google AI Studio & Gemini API:

Sign in with your Google account.

Click "Get API key" to generate a key. Keep this key secure!

3. For permanent access:
   ```bash
   # Linux/macOS
   echo 'export GOOGLE_API_KEY="your_key"' >> ~/.bashrc

   # Windows (Powershell)
   [System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY','your_key','User')
   ```

## Error Solutions
| Error | Fix |
|-------|-----|
| `API_KEY not found` | Verify `.env` file or environment variables |
| `Rate limit exceeded` | Check [Google Cloud Quotas](https://console.cloud.google.com/iam-admin/quotas) |
