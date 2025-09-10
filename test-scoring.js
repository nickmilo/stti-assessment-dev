// Quick test to verify our scoring logic
const { questions } = require('./src/data/questions.ts');

// Test with Keaton's original results
const keatonAnswers = [
  // Sample answers based on our previous work
  { questionId: 30, answer: 'SA' }, // I often spend time reflecting on my life experiences (I+)
  { questionId: 51, answer: 'SA' }, // I feel a strong need to think about my values (I+)
  { questionId: 52, answer: 'SA' }, // I find reflecting on my life energizing (I+)
  { questionId: 45, answer: 'SA' }, // I feel really satisfied when I am making sense of my life (I+)
  
  { questionId: 2, answer: 'SA' },  // I naturally look at topics from many angles (S+)
  { questionId: 32, answer: 'A' },  // I am really satisfied when I make sense out of complex information (S+)
  { questionId: 23, answer: 'SA' }, // I find exploring topics in depth energizing (S+)
  { questionId: 39, answer: 'SA' }, // I enjoy working with a lot of information (S+)
];

console.log('Questions loaded:', questions.length);
console.log('Sample question:', questions[0]);

function calculateTestScores(answers) {
  const scores = {
    innerGuide: 0,
    synthesizer: 0,
    producer: 0,
    creative: 0,
    architect: 0,
    gardener: 0
  };

  answers.forEach(answer => {
    const question = questions.find(q => q.id === answer.questionId);
    if (!question || question.archetype === 'RH') return;

    const archetype = question.archetype;
    const isPositive = archetype.includes('+');
    
    let scoreValue;
    if (isPositive) {
      switch (answer.answer) {
        case 'SD': scoreValue = 1; break;
        case 'D': scoreValue = 2; break;
        case 'A': scoreValue = 3; break;
        case 'SA': scoreValue = 4; break;
        default: scoreValue = 0;
      }
    } else {
      switch (answer.answer) {
        case 'SD': scoreValue = 4; break;
        case 'D': scoreValue = 3; break;
        case 'A': scoreValue = 2; break;
        case 'SA': scoreValue = 1; break;
        default: scoreValue = 0;
      }
    }

    switch (archetype.charAt(0)) {
      case 'I': scores.innerGuide += scoreValue; break;
      case 'S': scores.synthesizer += scoreValue; break;
      case 'P': scores.producer += scoreValue; break;
      case 'C': scores.creative += scoreValue; break;
      case 'A': scores.architect += scoreValue; break;
      case 'G': scores.gardener += scoreValue; break;
    }
  });

  return scores;
}

const testScores = calculateTestScores(keatonAnswers);
console.log('Test scores:', testScores);