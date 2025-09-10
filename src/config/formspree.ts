// Formspree Configuration
// To set up:
// 1. Go to https://formspree.io/
// 2. Create a new form
// 3. Replace YOUR_FORM_ID below with your actual form ID
// 4. Deploy the changes

export const FORMSPREE_ENDPOINT = 'https://formspree.io/f/xvgblrvw';

// Data structure that will be sent to Formspree:
// {
//   email: string,
//   profile_code: string (e.g., "IP-Architect"),
//   dominant_archetypes: string (e.g., "Inner Guide & Producer"),
//   tendency: string ("Architect" or "Gardener"),
//   scores: object with all archetype scores,
//   timestamp: ISO date string,
//   answers: array of all 53 question responses with:
//     - question_id: number
//     - question_text: string 
//     - answer: "SD" | "D" | "A" | "SA"
//     - archetype: string (e.g., "I+", "S-", etc.)
// }