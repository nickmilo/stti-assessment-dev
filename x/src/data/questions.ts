export interface Question {
  id: number;
  text: string;
  archetype: 'I+' | 'I-' | 'S+' | 'S-' | 'P+' | 'P-' | 'C+' | 'C-' | 'A+' | 'G+' | 'RH';
  category: 'behavior' | 'values' | 'satisfaction' | 'experience' | 'redherring';
}

export const questions: Question[] = [
  { id: 1, text: "I am really satisfied when I create something that feels original to me.", archetype: 'C+', category: 'satisfaction' },
  { id: 2, text: "I naturally look at topics from many angles.", archetype: 'S+', category: 'behavior' },
  { id: 3, text: "I find working from detailed plans draining.", archetype: 'G+', category: 'experience' },
  { id: 4, text: "I prefer to read summaries, not wade through a lot of information.", archetype: 'S-', category: 'values' },
  { id: 5, text: "I am energized by making progress on tasks.", archetype: 'P+', category: 'experience' },
  { id: 6, text: "If I'm putting something together, I start building before opening the manual.", archetype: 'G+', category: 'behavior' },
  { id: 7, text: "I prefer novels over non-fiction.", archetype: 'RH', category: 'redherring' },
  { id: 8, text: "I feel satisfied when my explorations lead to something unexpected.", archetype: 'G+', category: 'satisfaction' },
  { id: 9, text: "I don't tend to reflect on my life experiences.", archetype: 'I-', category: 'behavior' },
  { id: 10, text: "I am willing to put in the work required for my ideas to have an impact on others.", archetype: 'C+', category: 'values' },
  { id: 11, text: "Working from detailed plans is energizing for me.", archetype: 'A+', category: 'experience' },
  { id: 12, text: "I am not particularly interested in abstract ideas.", archetype: 'S-', category: 'satisfaction' },
  { id: 13, text: "I find exploring without a set path energizing.", archetype: 'G+', category: 'experience' },
  { id: 14, text: "I have a hard time making progress on my goals.", archetype: 'P-', category: 'satisfaction' },
  { id: 15, text: "Taking action on what I learn is important to me.", archetype: 'P+', category: 'values' },
  { id: 16, text: "I am drained by reflecting on my life.", archetype: 'I-', category: 'experience' },
  { id: 17, text: "I rarely share my ideas with others.", archetype: 'C-', category: 'behavior' },
  { id: 18, text: "Mapping out everything ahead of time helps me focus on what matters.", archetype: 'A+', category: 'values' },
  { id: 19, text: "I prefer classic literature over sci-fi or fantasy.", archetype: 'RH', category: 'redherring' },
  { id: 20, text: "I feel really satisfied when I get a lot of things done in a day.", archetype: 'P+', category: 'satisfaction' },
  { id: 21, text: "I dive in without a plan when starting a new project.", archetype: 'G+', category: 'behavior' },
  { id: 22, text: "I'm more extrovert than introvert.", archetype: 'RH', category: 'redherring' },
  { id: 23, text: "I find exploring topics in depth energizing.", archetype: 'S+', category: 'experience' },
  { id: 24, text: "Creating something original doesn't give me particular satisfaction.", archetype: 'C-', category: 'satisfaction' },
  { id: 25, text: "Having a clear plan at the start of something new is important to me.", archetype: 'A+', category: 'values' },
  { id: 26, text: "I am not particularly interested in personal reflection.", archetype: 'I-', category: 'satisfaction' },
  { id: 27, text: "I am energized by expressing my unique perspective.", archetype: 'C+', category: 'experience' },
  { id: 28, text: "If I'm putting something together, I read the manual first.", archetype: 'A+', category: 'behavior' },
  { id: 29, text: "There will always be more to do. I don't stress about getting stuff done.", archetype: 'P-', category: 'satisfaction' },
  { id: 30, text: "I often spend time reflecting on my life experiences.", archetype: 'I+', category: 'behavior' },
  { id: 31, text: "Being able to do something with my learning isn't that important to me.", archetype: 'P-', category: 'values' },
  { id: 32, text: "I am really satisfied when I make sense out of complex information.", archetype: 'S+', category: 'satisfaction' },
  { id: 33, text: "Exploring without a set path drains me.", archetype: 'A+', category: 'experience' },
  { id: 34, text: "I find expressing my unique perspective draining.", archetype: 'C-', category: 'experience' },
  { id: 35, text: "I consistently take action on the tasks and plans of the day.", archetype: 'P+', category: 'behavior' },
  { id: 36, text: "Trying to map out everything ahead of time is a waste of time.", archetype: 'G+', category: 'values' },
  { id: 37, text: "I prefer a mountain hike rather than a beach stroll.", archetype: 'RH', category: 'redherring' },
  { id: 38, text: "I feel satisfied when I execute a well-structured plan.", archetype: 'A+', category: 'satisfaction' },
  { id: 39, text: "I enjoy working with a lot of information.", archetype: 'S+', category: 'values' },
  { id: 40, text: "I am not particularly interested in taking detours without a high-level picture.", archetype: 'A+', category: 'satisfaction' },
  { id: 41, text: "I think introspection is overrated. I'm content to take life as it comes.", archetype: 'I-', category: 'values' },
  { id: 42, text: "Executing a structured plan doesn't appeal to me.", archetype: 'G+', category: 'satisfaction' },
  { id: 43, text: "I find working on tasks draining.", archetype: 'P-', category: 'experience' },
  { id: 44, text: "Having flexibility at the start of something new is important to me.", archetype: 'G+', category: 'values' },
  { id: 45, text: "I feel really satisfied when I am making sense of my life.", archetype: 'I+', category: 'satisfaction' },
  { id: 46, text: "I'm more introvert than extrovert.", archetype: 'RH', category: 'redherring' },
  { id: 47, text: "I often share my ideas with others.", archetype: 'C+', category: 'behavior' },
  { id: 48, text: "While it would be nice to impact others with my original creations, I have more pressing priorities.", archetype: 'C-', category: 'values' },
  { id: 49, text: "I am drained by exploring topics in depth.", archetype: 'S-', category: 'experience' },
  { id: 50, text: "When beginning a new project, I usually start by making a plan.", archetype: 'A+', category: 'behavior' },
  { id: 51, text: "I feel a strong need to think about my values and what really matters to me.", archetype: 'I+', category: 'values' },
  { id: 52, text: "I find reflecting on my life energizing.", archetype: 'I+', category: 'experience' },
  { id: 53, text: "I don't feel the need to exhaustively explore an idea.", archetype: 'S-', category: 'behavior' }
];

export type AnswerOption = 'SD' | 'D' | 'A' | 'SA';

export interface Answer {
  questionId: number;
  answer: AnswerOption;
}