export interface ProfileDescription {
  code: string;
  name: string;
  archetypes: [string, string];
  tendency: 'Architect' | 'Gardener';
  description: string;
  strengths: string[];
  challenges: string[];
  suggestions: string[];
}

// Placeholder descriptions - we'll fill these in together
export const profileDescriptions: Record<string, ProfileDescription> = {
  'IS-Architect': {
    code: 'IS-Architect',
    name: 'Inner Guide & Synthesizer - Architect',
    archetypes: ['Inner Guide', 'Synthesizer'],
    tendency: 'Architect',
    description: 'You blend deep personal reflection with systematic information processing...',
    strengths: ['Strategic thinking', 'Pattern recognition', 'Self-awareness'],
    challenges: ['Analysis paralysis', 'Over-planning'],
    suggestions: ['Set time limits for research', 'Practice decisive action']
  },
  'IS-Gardener': {
    code: 'IS-Gardener',
    name: 'Inner Guide & Synthesizer - Gardener',
    archetypes: ['Inner Guide', 'Synthesizer'],
    tendency: 'Gardener',
    description: 'You explore meaning and connections with an open, emergent approach...',
    strengths: ['Adaptive thinking', 'Intuitive insights', 'Holistic perspective'],
    challenges: ['Lack of structure', 'Difficulty finishing'],
    suggestions: ['Create loose frameworks', 'Set gentle milestones']
  },
  // Add placeholders for all 24 profiles
  'IP-Architect': {
    code: 'IP-Architect',
    name: 'Inner Guide & Producer - Architect',
    archetypes: ['Inner Guide', 'Producer'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'IP-Gardener': {
    code: 'IP-Gardener',
    name: 'Inner Guide & Producer - Gardener',
    archetypes: ['Inner Guide', 'Producer'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'IC-Architect': {
    code: 'IC-Architect',
    name: 'Inner Guide & Creative - Architect',
    archetypes: ['Inner Guide', 'Creative'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'IC-Gardener': {
    code: 'IC-Gardener',
    name: 'Inner Guide & Creative - Gardener',
    archetypes: ['Inner Guide', 'Creative'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'SP-Architect': {
    code: 'SP-Architect',
    name: 'Synthesizer & Producer - Architect',
    archetypes: ['Synthesizer', 'Producer'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'SP-Gardener': {
    code: 'SP-Gardener',
    name: 'Synthesizer & Producer - Gardener',
    archetypes: ['Synthesizer', 'Producer'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'SC-Architect': {
    code: 'SC-Architect',
    name: 'Synthesizer & Creative - Architect',
    archetypes: ['Synthesizer', 'Creative'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'SC-Gardener': {
    code: 'SC-Gardener',
    name: 'Synthesizer & Creative - Gardener',
    archetypes: ['Synthesizer', 'Creative'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'PC-Architect': {
    code: 'PC-Architect',
    name: 'Producer & Creative - Architect',
    archetypes: ['Producer', 'Creative'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'PC-Gardener': {
    code: 'PC-Gardener',
    name: 'Producer & Creative - Gardener',
    archetypes: ['Producer', 'Creative'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  // Reverse order combinations
  'SI-Architect': {
    code: 'SI-Architect',
    name: 'Synthesizer & Inner Guide - Architect',
    archetypes: ['Synthesizer', 'Inner Guide'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'SI-Gardener': {
    code: 'SI-Gardener',
    name: 'Synthesizer & Inner Guide - Gardener',
    archetypes: ['Synthesizer', 'Inner Guide'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'PI-Architect': {
    code: 'PI-Architect',
    name: 'Producer & Inner Guide - Architect',
    archetypes: ['Producer', 'Inner Guide'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'PI-Gardener': {
    code: 'PI-Gardener',
    name: 'Producer & Inner Guide - Gardener',
    archetypes: ['Producer', 'Inner Guide'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'CI-Architect': {
    code: 'CI-Architect',
    name: 'Creative & Inner Guide - Architect',
    archetypes: ['Creative', 'Inner Guide'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'CI-Gardener': {
    code: 'CI-Gardener',
    name: 'Creative & Inner Guide - Gardener',
    archetypes: ['Creative', 'Inner Guide'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'PS-Architect': {
    code: 'PS-Architect',
    name: 'Producer & Synthesizer - Architect',
    archetypes: ['Producer', 'Synthesizer'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'PS-Gardener': {
    code: 'PS-Gardener',
    name: 'Producer & Synthesizer - Gardener',
    archetypes: ['Producer', 'Synthesizer'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'CS-Architect': {
    code: 'CS-Architect',
    name: 'Creative & Synthesizer - Architect',
    archetypes: ['Creative', 'Synthesizer'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'CS-Gardener': {
    code: 'CS-Gardener',
    name: 'Creative & Synthesizer - Gardener',
    archetypes: ['Creative', 'Synthesizer'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'CP-Architect': {
    code: 'CP-Architect',
    name: 'Creative & Producer - Architect',
    archetypes: ['Creative', 'Producer'],
    tendency: 'Architect',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  },
  'CP-Gardener': {
    code: 'CP-Gardener',
    name: 'Creative & Producer - Gardener',
    archetypes: ['Creative', 'Producer'],
    tendency: 'Gardener',
    description: 'Placeholder description...',
    strengths: [],
    challenges: [],
    suggestions: []
  }
};