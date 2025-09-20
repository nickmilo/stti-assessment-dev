'use client';

import { useState } from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { questions } from '@/data/questions';
import { calculateScores, determineProfile, Profile } from '@/utils/scoring';
import { FORMSPREE_ENDPOINT } from '@/config/formspree';
import { SITE_CONFIG } from '@/config/site';

type AnswerOption = 'SD' | 'D' | 'A' | 'SA';

interface Answer {
  questionId: number;
  answer: AnswerOption;
}

export default function AssessmentPage() {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState<Record<number, Answer>>({});
  const [email, setEmail] = useState('');
  const [emailSubmitted, setEmailSubmitted] = useState(false);
  const [showResults, setShowResults] = useState(false);


  const handleAnswer = (response: AnswerOption) => {
    // Store answer (overwrite if changing answer)
    const newAnswers = {
      ...answers,
      [currentQuestion]: {
        questionId: questions[currentQuestion].id,
        answer: response
      }
    };
    setAnswers(newAnswers);

    // Auto-advance to next question or show results
    if (currentQuestion < questions.length - 1) {
      setTimeout(() => {
        setCurrentQuestion(currentQuestion + 1);
      }, 400);
    } else {
      // On last question, show results and submit data
      setTimeout(() => {
        const answersArray = Object.values(newAnswers);
        const scores = calculateScores(answersArray);
        const profile = determineProfile(scores);
        submitAssessmentData(email, newAnswers, profile);
        setShowResults(true);
      }, 400);
    }
  };

  const goBack = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  const goForward = () => {
    if (currentQuestion < questions.length - 1 && answers[currentQuestion]) {
      setCurrentQuestion(currentQuestion + 1);
    } else if (currentQuestion === questions.length - 1 && answers[currentQuestion]) {
      // If on last question and it's answered, show results and submit data
      const answersArray = Object.values(answers);
      const scores = calculateScores(answersArray);
      const profile = determineProfile(scores);
      submitAssessmentData(email, answers, profile);
      setShowResults(true);
    }
  };

  const handleEmailSubmit = (submittedEmail: string) => {
    setEmail(submittedEmail);
    setEmailSubmitted(true);
  };

  const shareResults = () => {
    const answersArray = Object.values(answers);
    const scores = calculateScores(answersArray);
    const profile = determineProfile(scores);
    
    const shareText = `I just discovered I'm a ${profile.code} on the STTI Assessment! Find out your sensemaking type at ${SITE_CONFIG.url}`;
    
    if (navigator.share) {
      navigator.share({
        title: `I'm a ${profile.code}! - ${SITE_CONFIG.social.title}`,
        text: shareText,
        url: SITE_CONFIG.url
      }).catch(err => console.log('Error sharing:', err));
    } else if (navigator.clipboard) {
      navigator.clipboard.writeText(shareText)
        .then(() => alert('Share text copied to clipboard!'))
        .catch(() => alert('Unable to copy to clipboard'));
    } else {
      alert(shareText);
    }
  };

  // Submit assessment data to Formspree
  const submitAssessmentData = async (email: string, answers: Record<number, Answer>, profile: Profile) => {
    try {
      const response = await fetch(FORMSPREE_ENDPOINT, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          profile_code: profile.code,
          dominant_archetypes: profile.dominantArchetypes.join(' & '),
          tendency: profile.tendency,
          scores: profile.scores,
          timestamp: new Date().toISOString(),
          answers: Object.values(answers).map(answer => ({
            question_id: answer.questionId,
            question_text: questions.find(q => q.id === answer.questionId)?.text,
            answer: answer.answer,
            archetype: questions.find(q => q.id === answer.questionId)?.archetype
          }))
        })
      });

      if (response.ok) {
        console.log('Assessment data submitted successfully');
      } else {
        console.error('Failed to submit assessment data');
      }
    } catch (error) {
      console.error('Error submitting assessment data:', error);
    }
  };

  // Calculate results for display
  const getResults = () => {
    const answersArray = Object.values(answers);
    const scores = calculateScores(answersArray);
    const profile = determineProfile(scores);
    return { scores, profile };
  };

  // Email capture screen
  if (!emailSubmitted) {
    return (
      <div className="min-h-screen" style={{ background: 'linear-gradient(135deg, #f8f9ff 0%, #fff5f0 100%)' }}>
        {/* Header */}
        <div className="text-center py-8 px-4 relative overflow-hidden flex items-center justify-center gap-8" style={{
          background: 'linear-gradient(135deg, #b9adff 0%, #5dbcd2 100%)',
          color: 'white'
        }}>
          <div className="absolute inset-0 opacity-30" style={{
            backgroundImage: `url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='20' cy='20' r='1' fill='rgba(255,255,255,0.1)'/><circle cx='80' cy='30' r='1' fill='rgba(255,255,255,0.1)'/><circle cx='60' cy='70' r='1' fill='rgba(255,255,255,0.1)'/><line x1='20' y1='20' x2='60' y2='70' stroke='rgba(255,255,255,0.1)' stroke-width='0.5'/><line x1='60' y1='70' x2='80' y2='30' stroke='rgba(255,255,255,0.1)' stroke-width='0.5'/></svg>")`,
            backgroundRepeat: 'repeat'
          }} />
          
          <Image 
            src="/lyt-logo.png" 
            alt="Linking Your Thinking" 
            width={80} 
            height={80}
            className="rounded-full shadow-lg relative z-10"
          />
          
          <div className="flex-1 relative z-10">
            <h1 className="text-4xl md:text-5xl font-medium mb-2" style={{ fontFamily: "'Canela Deck', Helvetica, sans-serif" }}>
              STTI Assessment
            </h1>
            <p className="text-lg md:text-xl opacity-90">
              Discover Your Sensemaking Type & Tendencies
            </p>
          </div>
        </div>

        <div className="max-w-2xl mx-auto px-4 py-16">
          <div className="bg-white rounded-lg shadow-md p-8 border border-purple-200">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4" style={{ fontFamily: "'Canela Deck', sans-serif" }}>
              Get Your Results
            </h2>
            <p className="text-gray-600 mb-6">
              Enter your email to receive your personalized STTI results. We&apos;ll send you a detailed breakdown 
              of your sensemaking type and suggestions for optimization.
            </p>
            
            <div className="space-y-4">
              <input
                type="email"
                placeholder="Enter your email address"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                style={{ fontFamily: "'Space Grotesk', sans-serif" }}
              />
              
              <button
                onClick={() => handleEmailSubmit(email)}
                disabled={!email.includes('@')}
                className="w-full py-3 px-6 rounded-lg font-semibold text-white transition-opacity disabled:opacity-50"
                style={{ 
                  background: 'linear-gradient(135deg, #b9adff 0%, #5dbcd2 100%)',
                  fontFamily: "'Space Grotesk', sans-serif"
                }}
              >
                Start Assessment
              </button>
            </div>
            
            <p className="text-sm text-gray-500 mt-4">
              We respect your privacy. Your email will only be used to send your results.
            </p>
          </div>
        </div>
      </div>
    );
  }

  // Results screen
  if (showResults) {
    const { profile } = getResults();
    const chordImagePath = `/chord-diagrams/Clean_STTI_${profile.code}_Thin.png`;
    
    return (
      <div className="min-h-screen" style={{ background: 'linear-gradient(135deg, #f8f9ff 0%, #fff5f0 100%)' }}>
        {/* Header */}
        <div className="text-center py-8 px-4 relative overflow-hidden flex items-center justify-center gap-8" style={{
          background: 'linear-gradient(135deg, #b9adff 0%, #5dbcd2 100%)',
          color: 'white'
        }}>
          <div className="absolute inset-0 opacity-30" style={{
            backgroundImage: `url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='20' cy='20' r='1' fill='rgba(255,255,255,0.1)'/><circle cx='80' cy='30' r='1' fill='rgba(255,255,255,0.1)'/><circle cx='60' cy='70' r='1' fill='rgba(255,255,255,0.1)'/><line x1='20' y1='20' x2='60' y2='70' stroke='rgba(255,255,255,0.1)' stroke-width='0.5'/><line x1='60' y1='70' x2='80' y2='30' stroke='rgba(255,255,255,0.1)' stroke-width='0.5'/></svg>")`,
            backgroundRepeat: 'repeat'
          }} />
          
          <Image 
            src="/lyt-logo.png" 
            alt="Linking Your Thinking" 
            width={80} 
            height={80}
            className="rounded-full shadow-lg relative z-10"
          />
          
          <div className="flex-1 relative z-10">
            <h1 className="text-4xl md:text-5xl font-medium mb-2" style={{ fontFamily: "'Canela Deck', Helvetica, sans-serif" }}>
              Your STTI Results
            </h1>
            <p className="text-lg md:text-xl opacity-90">
              {profile.code}
            </p>
          </div>
        </div>

        <div className="max-w-4xl mx-auto px-4 py-16">
          <div className="bg-white rounded-lg shadow-md overflow-hidden border border-purple-200">
            {/* Main Content */}
            <div className="p-8">
              <div className="grid md:grid-cols-2 gap-8">
                {/* Chord Diagram */}
                <div className="text-center">
                  <h3 className="text-xl font-semibold mb-4" style={{ fontFamily: "'Canela Deck', sans-serif", color: '#8272d0' }}>
                    Your Sensemaking Pattern
                  </h3>
                  <div className="rounded-lg p-4 inline-block" style={{ background: 'linear-gradient(135deg, #f8f9ff 0%, #fff5f0 100%)' }}>
                    <Image 
                      src={chordImagePath}
                      alt={`${profile.code} Chord Diagram`}
                      width={256}
                      height={256}
                      className="rounded-lg"
                    />
                  </div>
                </div>

                {/* Description */}
                <div>
                  <h3 className="text-xl font-semibold mb-4" style={{ fontFamily: "'Canela Deck', sans-serif", color: '#8272d0' }}>
                    About Your Type
                  </h3>
                  <p className="text-gray-700 mb-6 leading-relaxed">
                    You blend the <strong>{profile.dominantArchetypes[0]}</strong> and <strong>{profile.dominantArchetypes[1]}</strong> approaches with <strong>{profile.tendency}</strong> tendencies. 
                    This unique combination shapes how you process information, make decisions, and navigate complexity in your personal and professional life.
                  </p>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="mt-8 border-t pt-8">
                <div className="flex flex-wrap gap-4 justify-center">
                  <button
                    onClick={shareResults}
                    className="px-6 py-3 rounded-lg font-medium text-white transition-opacity hover:opacity-90"
                    style={{ 
                      background: 'linear-gradient(135deg, #b9adff 0%, #5dbcd2 100%)',
                      fontFamily: "'Space Grotesk', sans-serif"
                    }}
                  >
                    Share your results
                  </button>
                  
                  <Link
                    href="/"
                    className="px-6 py-3 rounded-lg font-medium text-white transition-opacity hover:opacity-90"
                    style={{ 
                      background: 'linear-gradient(135deg, #6b7280 0%, #4b5563 100%)',
                      fontFamily: "'Space Grotesk', sans-serif"
                    }}
                  >
                    Take Again
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Assessment questions
  const question = questions[currentQuestion];
  const progress = ((currentQuestion + 1) / questions.length) * 100;
  const selectedAnswer = answers[currentQuestion]?.answer;

  return (
    <div className="min-h-screen" style={{ background: 'linear-gradient(135deg, #f8f9ff 0%, #fff5f0 100%)' }}>
      {/* Header */}
      <div className="text-center py-8 px-4 relative overflow-hidden flex items-center justify-center gap-8" style={{
        background: 'linear-gradient(135deg, #b9adff 0%, #5dbcd2 100%)',
        color: 'white'
      }}>
        <div className="absolute inset-0 opacity-30" style={{
          backgroundImage: `url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='20' cy='20' r='1' fill='rgba(255,255,255,0.1)'/><circle cx='80' cy='30' r='1' fill='rgba(255,255,255,0.1)'/><circle cx='60' cy='70' r='1' fill='rgba(255,255,255,0.1)'/><line x1='20' y1='20' x2='60' y2='70' stroke='rgba(255,255,255,0.1)' stroke-width='0.5'/><line x1='60' y1='70' x2='80' y2='30' stroke='rgba(255,255,255,0.1)' stroke-width='0.5'/></svg>")`,
          backgroundRepeat: 'repeat'
        }} />
        
        <Image 
          src="/lyt-logo.png" 
          alt="Linking Your Thinking" 
          width={80} 
          height={80}
          className="rounded-full shadow-lg relative z-10"
        />
        
        <div className="flex-1 relative z-10">
          <h1 className="text-4xl md:text-5xl font-medium mb-2" style={{ fontFamily: "'Canela Deck', Helvetica, sans-serif" }}>
            STTI Assessment
          </h1>
          <p className="text-lg md:text-xl opacity-90">
            Discover Your Sensemaking Type & Tendencies
          </p>
        </div>
      </div>

      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="bg-white rounded-lg shadow-md p-8 border border-purple-200">
          {/* Progress */}
          <div className="mb-8">
            <div className="mb-2" style={{ fontFamily: "'DM Mono', monospace", color: '#8272d0', fontSize: '0.9rem' }}>
              Question {currentQuestion + 1} of {questions.length}
            </div>
            <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
              <div 
                className="h-full rounded-full transition-all duration-500"
                style={{ 
                  width: `${progress}%`,
                  background: 'linear-gradient(90deg, #b9adff 0%, #5dbcd2 100%)'
                }}
              />
            </div>
          </div>
          
          {/* Question */}
          <div>
            <h3 className="text-xl mb-8" style={{ 
              fontFamily: "'Space Grotesk', sans-serif", 
              color: '#8272d0',
              fontWeight: '500'
            }}>
              {question.text}
            </h3>
            
            {/* Answer Buttons */}
            <div className="grid grid-cols-4 gap-4 mb-8">
              <button
                onClick={() => handleAnswer('SD')}
                className="p-4 border-2 rounded-lg font-medium transition-all duration-300 hover:opacity-80"
                style={{
                  borderColor: '#8272d0',
                  color: '#8272d0',
                  background: selectedAnswer === 'SD' ? '#8272d0' : 'white',
                  ...(selectedAnswer === 'SD' && { color: 'white' }),
                  fontFamily: "'Space Grotesk', sans-serif"
                }}
              >
                Strongly Disagree
              </button>
              
              <button
                onClick={() => handleAnswer('D')}
                className="p-4 border-2 rounded-lg font-medium transition-all duration-300 hover:opacity-80"
                style={{
                  borderColor: '#c7c400',
                  color: '#c7c400',
                  background: selectedAnswer === 'D' ? '#c7c400' : 'white',
                  ...(selectedAnswer === 'D' && { color: 'white' }),
                  fontFamily: "'Space Grotesk', sans-serif"
                }}
              >
                Disagree
              </button>
              
              <button
                onClick={() => handleAnswer('A')}
                className="p-4 border-2 rounded-lg font-medium transition-all duration-300 hover:opacity-80"
                style={{
                  borderColor: '#5dbcd2',
                  color: '#5dbcd2',
                  background: selectedAnswer === 'A' ? '#5dbcd2' : 'white',
                  ...(selectedAnswer === 'A' && { color: 'white' }),
                  fontFamily: "'Space Grotesk', sans-serif"
                }}
              >
                Agree
              </button>
              
              <button
                onClick={() => handleAnswer('SA')}
                className="p-4 border-2 rounded-lg font-medium transition-all duration-300 hover:opacity-80"
                style={{
                  borderColor: '#d669bc',
                  color: '#d669bc',
                  background: selectedAnswer === 'SA' ? '#d669bc' : 'white',
                  ...(selectedAnswer === 'SA' && { color: 'white' }),
                  fontFamily: "'Space Grotesk', sans-serif"
                }}
              >
                Strongly Agree
              </button>
            </div>
            
            {/* Navigation */}
            <div className="flex justify-between">
              <button
                onClick={goBack}
                disabled={currentQuestion === 0}
                className="w-10 h-10 border rounded-full flex items-center justify-center text-lg font-medium transition-all duration-300 disabled:opacity-30 disabled:cursor-not-allowed"
                style={{
                  borderColor: '#b9adff',
                  color: '#b9adff',
                  background: 'white'
                }}
              >
                ←
              </button>
              
              <button
                onClick={goForward}
                disabled={!answers[currentQuestion]}
                className="w-10 h-10 border rounded-full flex items-center justify-center text-lg font-medium transition-all duration-300 disabled:opacity-30 disabled:cursor-not-allowed"
                style={{
                  borderColor: '#b9adff',
                  color: '#b9adff',
                  background: 'white'
                }}
              >
                →
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}