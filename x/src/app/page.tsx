import Link from "next/link";
import Image from "next/image";

export default function Home() {
  return (
    <div className="min-h-screen">
      {/* Header */}
      <div className="text-center py-8 px-4 bg-gradient-to-br from-[#b9adff] to-[#5dbcd2] text-white relative overflow-hidden flex items-center justify-center gap-8">
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

      <div className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto text-center">
          {/* Hero Section */}
          <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-6" style={{ fontFamily: "'Canela Deck', sans-serif" }}>
            Discover Your Sensemaking Type
          </h2>
          
          <p className="text-xl text-gray-600 mb-8 leading-relaxed">
            The STTI (Sensemaking Types and Tendencies Indicator) reveals how you process 
            information, make decisions, and navigate complexity in your personal and professional life.
          </p>

          {/* Key Benefits */}
          <div className="grid md:grid-cols-3 gap-8 mb-12">
            <div className="bg-white rounded-lg p-6 shadow-sm border border-[#b9adff]/20">
              <div className="w-12 h-12 bg-[#b9adff]/10 rounded-lg flex items-center justify-center mx-auto mb-4">
                <svg className="w-6 h-6 text-[#8272d0]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2" style={{ fontFamily: "'Canela Deck', sans-serif" }}>Self-Awareness</h3>
              <p className="text-gray-600">Understand your unique cognitive patterns and decision-making style.</p>
            </div>

            <div className="bg-white rounded-lg p-6 shadow-sm border border-[#5dbcd2]/20">
              <div className="w-12 h-12 bg-[#5dbcd2]/10 rounded-lg flex items-center justify-center mx-auto mb-4">
                <svg className="w-6 h-6 text-[#5dbcd2]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2" style={{ fontFamily: "'Canela Deck', sans-serif" }}>Team Dynamics</h3>
              <p className="text-gray-600">Improve collaboration by understanding different thinking styles.</p>
            </div>

            <div className="bg-white rounded-lg p-6 shadow-sm border border-[#d669bc]/20">
              <div className="w-12 h-12 bg-[#d669bc]/10 rounded-lg flex items-center justify-center mx-auto mb-4">
                <svg className="w-6 h-6 text-[#d669bc]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2" style={{ fontFamily: "'Canela Deck', sans-serif" }}>Personal Growth</h3>
              <p className="text-gray-600">Identify areas for development and leverage your natural strengths.</p>
            </div>
          </div>

          {/* CTA Section */}
          <div className="bg-white rounded-lg p-8 shadow-sm mb-12 border border-[#b9adff]/20">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4" style={{ fontFamily: "'Canela Deck', sans-serif" }}>
              Ready to discover your sensemaking type?
            </h2>
            <p className="text-gray-600 mb-6">
              The assessment takes 10-15 minutes and provides personalized insights 
              into your cognitive preferences and information processing style.
            </p>
            
            <Link 
              href="/assessment"
              className="inline-block bg-gradient-to-r from-[#b9adff] to-[#5dbcd2] text-white px-8 py-4 rounded-lg text-lg font-semibold hover:opacity-90 transition-opacity"
            >
              Take the STTI Assessment
            </Link>
          </div>

          {/* About Section */}
          <div className="text-left max-w-3xl mx-auto">
            <h2 className="text-2xl font-semibold text-gray-900 mb-4" style={{ fontFamily: "'Canela Deck', sans-serif" }}>About the STTI</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              The Sensemaking Types and Tendencies Indicator (STTI) identifies four core archetypes 
              of information processing: Inner Guide (reflection and values), Synthesizer (connecting ideas), 
              Producer (action and results), and Creative (originality and expression).
            </p>
            <p className="text-gray-600 leading-relaxed">
              Additionally, the assessment reveals your tendency toward either Architect (structured, planned) 
              or Gardener (flexible, emergent) approaches to organizing and implementing ideas.
            </p>
          </div>
        </div>
      </div>

      {/* Footer */}
      <div className="bg-gradient-to-r from-gray-800 to-gray-700 text-white py-12 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h3 className="text-xl font-medium mb-4 text-purple-400" style={{ fontFamily: "'Canela Deck', sans-serif" }}>
            Educational Licensing & Research Opportunities
          </h3>
          <p className="mb-4 opacity-90">
            Interested in using the STTI Assessment in your classroom, research, or academic program? 
            This validated instrument is perfect for case studies, rigorous academic testing, and educational research initiatives.
          </p>
          <p className="mb-8">
            <a href="mailto:hello@linkingyourthinking.com" className="text-cyan-400 hover:text-purple-400 font-medium">
              Contact us at hello@linkingyourthinking.com
            </a> to inquire about classroom licenses, research partnerships, and institutional access.
          </p>
          <div className="border-t border-white/30 pt-8 text-sm opacity-80">
            © 2025 Linking Your Thinking. The STTI Assessment is proprietary and protected by copyright.<br />
            All rights reserved. | <a href="https://www.linkingyourthinking.com" className="text-cyan-400 hover:text-purple-400">linkingyourthinking.com</a>
          </div>
        </div>
      </div>
    </div>
  );
}