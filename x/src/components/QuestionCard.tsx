'use client';

import { Question, AnswerOption } from '@/data/questions';

interface QuestionCardProps {
  question: Question;
  onAnswer: (answer: AnswerOption) => void;
}

const answerOptions = [
  { value: 'SD' as AnswerOption, label: 'Strongly Disagree', color: 'bg-red-100 hover:bg-red-200 border-red-300' },
  { value: 'D' as AnswerOption, label: 'Disagree', color: 'bg-orange-100 hover:bg-orange-200 border-orange-300' },
  { value: 'A' as AnswerOption, label: 'Agree', color: 'bg-green-100 hover:bg-green-200 border-green-300' },
  { value: 'SA' as AnswerOption, label: 'Strongly Agree', color: 'bg-emerald-100 hover:bg-emerald-200 border-emerald-300' }
];

export default function QuestionCard({ question, onAnswer }: QuestionCardProps) {
  return (
    <div className="bg-white rounded-lg shadow-md p-8">
      <div className="mb-8">
        <p className="text-lg text-gray-900 leading-relaxed font-medium">
          {question.text}
        </p>
      </div>
      
      <div className="space-y-3">
        {answerOptions.map((option) => (
          <button
            key={option.value}
            onClick={() => onAnswer(option.value)}
            className={`w-full p-4 text-left border-2 rounded-lg transition-all duration-200 ${option.color} hover:scale-[1.02] active:scale-[0.98]`}
          >
            <span className="font-medium text-gray-800">{option.label}</span>
          </button>
        ))}
      </div>
      
      <div className="mt-6 text-center">
        <p className="text-sm text-gray-500">
          Click your response to continue
        </p>
      </div>
    </div>
  );
}