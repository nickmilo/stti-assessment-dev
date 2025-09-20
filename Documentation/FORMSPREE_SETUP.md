# Formspree Setup Guide

## Quick Setup (5 minutes)

1. **Go to Formspree**: https://formspree.io/
2. **Sign up** for a free account
3. **Create a new form**:
   - Name: "STTI Assessment Results"
   - Description: "Captures STTI assessment responses and results"
4. **Copy your Form ID** (looks like `xjkmnpqr`)
5. **Update the config file**:
   - Open: `src/config/formspree.ts`
   - Replace `YOUR_FORM_ID` with your actual Form ID
   - Save the file
6. **Deploy the update** (git push, Vercel auto-deploys)

## Data You'll Receive

For each assessment completion, you'll get:

- **Email**: User's email address
- **Profile Code**: e.g., "IP-Architect" 
- **Archetypes**: e.g., "Inner Guide & Producer"
- **Tendency**: "Architect" or "Gardener"
- **Scores**: Raw scores for all archetypes
- **Timestamp**: When assessment was completed
- **All 53 Answers**: Complete response data with:
  - Question text
  - User's answer (SD/D/A/SA) 
  - Archetype coding

## Formspree Features

- **Free tier**: 50 submissions/month
- **Paid plans**: Unlimited submissions + integrations
- **Notifications**: Email alerts for new submissions
- **Integrations**: Connect to Google Sheets, Zapier, etc.
- **Export**: Download all data as CSV/JSON

## Example Data Format

```json
{
  "email": "user@example.com",
  "profile_code": "IP-Architect", 
  "dominant_archetypes": "Inner Guide & Producer",
  "tendency": "Architect",
  "scores": {
    "innerGuide": 42,
    "synthesizer": 31,
    "producer": 38,
    "creative": 25,
    "architect": 28,
    "gardener": 20
  },
  "timestamp": "2025-01-09T18:30:00.000Z",
  "answers": [
    {
      "question_id": 1,
      "question_text": "I am really satisfied when I create something that feels original to me.",
      "answer": "SA",
      "archetype": "C+"
    }
    // ... all 53 responses
  ]
}
```

This gives you complete visibility into user responses for research and analysis!