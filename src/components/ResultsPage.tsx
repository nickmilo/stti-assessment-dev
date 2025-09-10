'use client';

import { Profile } from '@/utils/scoring';
import { ProfileDescription } from '@/data/profiles';
import Image from 'next/image';
import Link from 'next/link';

interface ResultsPageProps {
  profile: Profile;
  profileData: ProfileDescription;
  email?: string;
}

export default function ResultsPage({ profile, profileData }: ResultsPageProps) {
  const handleShare = async () => {
    if (navigator.share) {
      try {
        await navigator.share({
          title: `I'm an ${profile.code}!`,
          text: `I just discovered I'm an ${profile.code} on the STTI assessment. Find out your sensemaking type!`,
          url: window.location.origin
        });
      } catch (err) {
        console.log('Error sharing:', err);
      }
    } else {
      // Fallback to clipboard
      const shareText = `I just discovered I'm an ${profile.code} on the STTI assessment! Find out your sensemaking type at ${window.location.origin}`;
      navigator.clipboard.writeText(shareText);
      alert('Share text copied to clipboard!');
    }
  };

  const handleEmailResults = async () => {
    // TODO: Implement email results functionality
    alert('Email results feature coming soon!');
  };

  const chordImagePath = `/chord-diagrams/Clean_STTI_${profile.code}_Thin.png`;

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4">
        <div className="bg-white rounded-lg shadow-md overflow-hidden">
          {/* Header */}
          <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-8 text-center">
            <h1 className="text-4xl font-bold mb-2">Your STTI Results</h1>
            <h2 className="text-2xl font-semibold">{profile.code}</h2>
            <p className="text-blue-100 mt-2">
              {profile.dominantArchetypes.join(' & ')} • {profile.tendency}
            </p>
          </div>

          {/* Main Content */}
          <div className="p-8">
            <div className="grid md:grid-cols-2 gap-8">
              {/* Chord Diagram */}
              <div className="text-center">
                <h3 className="text-xl font-semibold mb-4">Your Sensemaking Pattern</h3>
                <div className="bg-gray-100 rounded-lg p-4 inline-block">
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
                <h3 className="text-xl font-semibold mb-4">About Your Type</h3>
                <p className="text-gray-700 mb-6 leading-relaxed">
                  {profileData?.description || `You are an ${profile.code}, combining ${profile.dominantArchetypes.join(' and ')} approaches with a ${profile.tendency} tendency.`}
                </p>

                {profileData?.strengths && profileData.strengths.length > 0 && (
                  <div className="mb-4">
                    <h4 className="font-semibold text-green-700 mb-2">Strengths:</h4>
                    <ul className="list-disc list-inside text-gray-700 space-y-1">
                      {profileData.strengths.map((strength, index) => (
                        <li key={index}>{strength}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {profileData?.challenges && profileData.challenges.length > 0 && (
                  <div className="mb-4">
                    <h4 className="font-semibold text-orange-700 mb-2">Growth Areas:</h4>
                    <ul className="list-disc list-inside text-gray-700 space-y-1">
                      {profileData.challenges.map((challenge, index) => (
                        <li key={index}>{challenge}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {profileData?.suggestions && profileData.suggestions.length > 0 && (
                  <div>
                    <h4 className="font-semibold text-blue-700 mb-2">Suggestions:</h4>
                    <ul className="list-disc list-inside text-gray-700 space-y-1">
                      {profileData.suggestions.map((suggestion, index) => (
                        <li key={index}>{suggestion}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>

            {/* Action Buttons */}
            <div className="mt-8 border-t pt-8">
              <div className="flex flex-wrap gap-4 justify-center">
                <button
                  onClick={handleShare}
                  className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors font-medium"
                >
                  Share Results
                </button>
                
                <button
                  onClick={handleEmailResults}
                  className="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 transition-colors font-medium"
                >
                  Email Results
                </button>
                
                <Link
                  href="/"
                  className="bg-gray-600 text-white px-6 py-3 rounded-lg hover:bg-gray-700 transition-colors font-medium"
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