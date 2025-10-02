# STTI Assessment Web Application

## Overview
The Sensemaking Types and Tendencies Indicator (STTI) is an interactive web assessment that identifies individual cognitive patterns and information processing styles.

## Features

### ✅ Completed
- **Landing Page**: Professional introduction with assessment overview
- **Assessment Flow**: 53 questions with auto-advance on answer selection
- **Progress Tracking**: Visual progress bar showing completion status
- **Scoring Logic**: Automatic calculation of archetype and tendency scores
- **Results Display**: Profile identification with chord diagram visualization
- **Responsive Design**: Mobile-friendly interface

### 🚧 In Progress
- **Profile Descriptions**: Personalized content for all 24 profile types
- **Data Collection**: Formspree integration for response analytics
- **Sharing Features**: Social media and email sharing functionality

### 📋 TODO
- **Email Results**: Send detailed results to user email
- **Deployment**: Vercel deployment with GitHub integration
- **Analytics**: User behavior tracking and assessment analytics

## Technology Stack
- **Frontend**: Next.js 15 with TypeScript
- **Styling**: Tailwind CSS
- **Images**: 24 pre-generated chord diagrams (thin versions)
- **Deployment**: Vercel (planned)
- **Data Collection**: Formspree (planned)

## Assessment Structure
- **53 Questions**: 48 assessment + 5 red herrings
- **4 Archetypes**: Inner Guide, Synthesizer, Producer, Creative
- **2 Tendencies**: Architect (structured) vs Gardener (emergent)
- **24 Possible Profiles**: All combinations of top 2 archetypes + tendency

## Scoring System
- **4-point Likert Scale**: Strongly Disagree, Disagree, Agree, Strongly Agree
- **Positive Questions**: SD=1, D=2, A=3, SA=4
- **Negative Questions**: SD=4, D=3, A=2, SA=1 (reverse scoring)

## File Structure
```
src/
├── app/
│   ├── page.tsx                 # Landing page
│   └── assessment/
│       └── page.tsx             # Assessment flow
├── components/
│   ├── QuestionCard.tsx         # Individual question display
│   ├── ProgressBar.tsx          # Progress tracking
│   └── ResultsPage.tsx          # Results display
├── data/
│   ├── questions.ts             # All 53 questions with coding
│   └── profiles.ts              # 24 profile descriptions
└── utils/
    └── scoring.ts               # Scoring and profile determination logic
```

## Development

### Running Locally
```bash
npm run dev
```
Open [http://localhost:3000](http://localhost:3000) to view the application.

### Building for Production
```bash
npm run build
npm start
```

## Profile Types
The assessment identifies 24 possible profiles based on:
- **Top 2 Archetypes** (12 combinations)
- **Tendency** (Architect or Gardener)

Examples: IS-Architect, CP-Gardener, IP-Architect, etc.

## Next Steps
1. Complete profile descriptions for all 24 types
2. Set up Formspree for data collection
3. Deploy to Vercel with custom domain
4. Add comprehensive sharing functionality
5. Implement email results feature

---

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).