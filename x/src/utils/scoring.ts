import { Answer, AnswerOption, questions } from '@/data/questions';

export interface ArchetypeScores {
  innerGuide: number;
  synthesizer: number;
  producer: number;
  creative: number;
  architect: number;
  gardener: number;
}

export interface Profile {
  code: string;
  dominantArchetypes: [string, string];
  tendency: 'Architect' | 'Gardener';
  scores: ArchetypeScores;
}

const getScoreValue = (answer: AnswerOption, isPositive: boolean): number => {
  if (isPositive) {
    // Positive questions: SD=1, D=2, A=3, SA=4
    switch (answer) {
      case 'SD': return 1;
      case 'D': return 2;
      case 'A': return 3;
      case 'SA': return 4;
      default: return 0;
    }
  } else {
    // Negative questions: SD=4, D=3, A=2, SA=1 (reversed scoring)
    switch (answer) {
      case 'SD': return 4;
      case 'D': return 3;
      case 'A': return 2;
      case 'SA': return 1;
      default: return 0;
    }
  }
};

export const calculateScores = (answers: Answer[]): ArchetypeScores => {
  const scores: ArchetypeScores = {
    innerGuide: 0,
    synthesizer: 0,
    producer: 0,
    creative: 0,
    architect: 0,
    gardener: 0
  };

  answers.forEach(answer => {
    const question = questions.find(q => q.id === answer.questionId);
    if (!question || question.archetype === 'RH') return; // Skip red herrings

    const archetype = question.archetype;
    const isPositive = archetype.includes('+');
    const scoreValue = getScoreValue(answer.answer, isPositive);

    // Map archetype codes to score properties
    switch (archetype.charAt(0)) {
      case 'I':
        scores.innerGuide += scoreValue;
        break;
      case 'S':
        scores.synthesizer += scoreValue;
        break;
      case 'P':
        scores.producer += scoreValue;
        break;
      case 'C':
        scores.creative += scoreValue;
        break;
      case 'A':
        scores.architect += scoreValue;
        break;
      case 'G':
        scores.gardener += scoreValue;
        break;
    }
  });

  return scores;
};

export const determineProfile = (scores: ArchetypeScores): Profile => {
  // Find top 2 archetypes
  const archetypeScores = [
    { name: 'Inner Guide', score: scores.innerGuide, code: 'I' },
    { name: 'Synthesizer', score: scores.synthesizer, code: 'S' },
    { name: 'Producer', score: scores.producer, code: 'P' },
    { name: 'Creative', score: scores.creative, code: 'C' }
  ];

  archetypeScores.sort((a, b) => b.score - a.score);
  const topTwo = archetypeScores.slice(0, 2);

  // Determine tendency
  const tendencyScore = scores.architect - scores.gardener;
  const tendency = tendencyScore > 0 ? 'Architect' : 'Gardener';

  // Create profile code
  const profileCode = `${topTwo[0].code}${topTwo[1].code}-${tendency}`;

  return {
    code: profileCode,
    dominantArchetypes: [topTwo[0].name, topTwo[1].name],
    tendency,
    scores
  };
};