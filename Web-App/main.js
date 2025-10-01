        const questions = [
            { id: 1, text: "I am really satisfied when I create something that feels original to me.", archetype: 'C+' },
            { id: 2, text: "I naturally look at topics from many angles.", archetype: 'S+' },
            { id: 3, text: "I find working from detailed plans draining.", archetype: 'G+' },
            { id: 4, text: "I prefer to read summaries, not wade through a lot of information.", archetype: 'S-' },
            { id: 5, text: "I am energized by making progress on tasks.", archetype: 'P+' },
            { id: 6, text: "If I'm putting something together, I start building before opening the manual.", archetype: 'G+' },
            { id: 7, text: "I prefer novels over non-fiction.", archetype: 'RH' },
            { id: 8, text: "I feel satisfied when my explorations lead to something unexpected.", archetype: 'G+' },
            { id: 9, text: "I don't tend to reflect on my life experiences.", archetype: 'I-' },
            { id: 10, text: "I am willing to put in the work required for my ideas to have an impact on others.", archetype: 'C+' },
            { id: 11, text: "Working from detailed plans is energizing for me.", archetype: 'A+' },
            { id: 12, text: "I am not particularly interested in abstract ideas.", archetype: 'S-' },
            { id: 13, text: "I find exploring without a set path energizing.", archetype: 'G+' },
            { id: 14, text: "I have a hard time making progress on my goals.", archetype: 'P-' },
            { id: 15, text: "Taking action on what I learn is important to me.", archetype: 'P+' },
            { id: 16, text: "I am drained by reflecting on my life.", archetype: 'I-' },
            { id: 17, text: "I rarely share my ideas with others.", archetype: 'C-' },
            { id: 18, text: "Mapping out everything ahead of time helps me focus on what matters.", archetype: 'A+' },
            { id: 19, text: "I prefer classic literature over sci-fi or fantasy.", archetype: 'RH' },
            { id: 20, text: "I feel really satisfied when I get a lot of things done in a day.", archetype: 'P+' },
            { id: 21, text: "I dive in without a plan when starting a new project.", archetype: 'G+' },
            { id: 22, text: "I'm more extrovert than introvert.", archetype: 'RH' },
            { id: 23, text: "I find exploring topics in depth energizing.", archetype: 'S+' },
            { id: 24, text: "Creating something original doesn't give me particular satisfaction.", archetype: 'C-' },
            { id: 25, text: "Having a clear plan at the start of something new is important to me.", archetype: 'A+' },
            { id: 26, text: "I am not particularly interested in personal reflection.", archetype: 'I-' },
            { id: 27, text: "I am energized by expressing my unique perspective.", archetype: 'C+' },
            { id: 28, text: "If I'm putting something together, I read the manual first.", archetype: 'A+' },
            { id: 29, text: "There will always be more to do. I don't stress about getting stuff done.", archetype: 'P-' },
            { id: 30, text: "I often spend time reflecting on my life experiences.", archetype: 'I+' },
            { id: 31, text: "Being able to do something with my learning isn't that important to me.", archetype: 'P-' },
            { id: 32, text: "I am really satisfied when I make sense out of complex information.", archetype: 'S+' },
            { id: 33, text: "Exploring without a set path drains me.", archetype: 'A+' },
            { id: 34, text: "I find expressing my unique perspective draining.", archetype: 'C-' },
            { id: 35, text: "I consistently take action on the tasks and plans of the day.", archetype: 'P+' },
            { id: 36, text: "Trying to map out everything ahead of time is a waste of time.", archetype: 'G+' },
            { id: 37, text: "I prefer a mountain hike rather than a beach stroll.", archetype: 'RH' },
            { id: 38, text: "I feel satisfied when I execute a well-structured plan.", archetype: 'A+' },
            { id: 39, text: "I enjoy working with a lot of information.", archetype: 'S+' },
            { id: 40, text: "I am not particularly interested in taking detours without a high-level picture.", archetype: 'A+' },
            { id: 41, text: "I think introspection is overrated. I'm content to take life as it comes.", archetype: 'I-' },
            { id: 42, text: "Executing a structured plan doesn't appeal to me.", archetype: 'G+' },
            { id: 43, text: "I find working on tasks draining.", archetype: 'P-' },
            { id: 44, text: "Having flexibility at the start of something new is important to me.", archetype: 'G+' },
            { id: 45, text: "I feel really satisfied when I am making sense of my life.", archetype: 'I+' },
            { id: 46, text: "I'm more introvert than extrovert.", archetype: 'RH' },
            { id: 47, text: "I often share my ideas with others.", archetype: 'C+' },
            { id: 48, text: "While it would be nice to impact others with my original creations, I have more pressing priorities.", archetype: 'C-' },
            { id: 49, text: "I am drained by exploring topics in depth.", archetype: 'S-' },
            { id: 50, text: "When beginning a new project, I usually start by making a plan.", archetype: 'A+' },
            { id: 51, text: "I feel a strong need to think about my values and what really matters to me.", archetype: 'I+' },
            { id: 52, text: "I find reflecting on my life energizing.", archetype: 'I+' },
            { id: 53, text: "I don't feel the need to exhaustively explore an idea.", archetype: 'S-' }
        ];

        // Global constants for archetype configuration
        const ARCHETYPE_NAMES = {
            'I': 'Inner Guide',
            'S': 'Synthesizer',
            'P': 'Producer',
            'C': 'Creative'
        };

        const ARCHETYPE_PILL_CLASSES = {
            'I': 'inner-guide-pill',
            'S': 'synthesizer-pill',
            'P': 'producer-pill',
            'C': 'creative-pill'
        };

        const ARCHETYPE_DESCRIPTIONS = {
            'I': 'naturally focus on things that you find intrinsically meaningful',
            'S': 'having a desire to deeply make sense of those things',
            'P': 'being energized by taking action and making progress on meaningful work',
            'C': 'expressing your unique perspective and creating original contributions'
        };

        const TENDENCY_DESCRIPTIONS = {
            'Architect': 'gravitate towards structuring and organizing the things around you. However, it doesn\'t mean the things around you are organized, only that you prefer clarity and understanding over uncertainty, but sometimes even…opportunities.',
            'Gardener': 'prefer flexibility and emergent approaches, allowing ideas and projects to develop organically. You thrive in ambiguous situations and are comfortable navigating uncertainty, often discovering unexpected opportunities through exploration.'
        };

        let currentQuestion = 0;
        let answers = {};
        let userEmail = '';
        let hasSubmitted = false; // Prevent multiple form submissions
        
        
        // Simple secret code system - exact copy of what worked with Z key
        let keySequence = '';
        let keyTimer = null;
        
        window.addEventListener('keydown', function(e) {
            // Only work when not in an input field
            if (document.activeElement.tagName === 'INPUT') return;
            
            // Build sequence for 4-digit codes
            if (e.key >= '0' && e.key <= '9') {
                keySequence += e.key;
                console.log('Building sequence:', keySequence);
                
                // Clear timer
                if (keyTimer) clearTimeout(keyTimer);
                
                // Reset after 3 seconds
                keyTimer = setTimeout(() => {
                    console.log('Resetting sequence');
                    keySequence = '';
                }, 3000);
                
                // Check for exact matches
                if (keySequence === '0001') {
                    activateProfile('IP-Architect', 'The Converter');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0002') {
                    activateProfile('IP-Gardener', 'The Converter');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0003') {
                    activateProfile('IS-Architect', 'The Philosopher');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0004') {
                    activateProfile('IS-Gardener', 'The Philosopher');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0005') {
                    activateProfile('IC-Architect', 'The Explorer');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0006') {
                    activateProfile('IC-Gardener', 'The Explorer');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0007') {
                    activateProfile('PI-Architect', 'The Converter');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0008') {
                    activateProfile('PI-Gardener', 'The Converter');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0009') {
                    activateProfile('PS-Architect', 'The Builder');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0010') {
                    activateProfile('PS-Gardener', 'The Builder');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0011') {
                    activateProfile('PC-Architect', 'The Maker');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0012') {
                    activateProfile('PC-Gardener', 'The Maker');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0013') {
                    activateProfile('SI-Architect', 'The Philosopher');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0014') {
                    activateProfile('SI-Gardener', 'The Philosopher');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0015') {
                    activateProfile('SP-Architect', 'The Builder');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0016') {
                    activateProfile('SP-Gardener', 'The Builder');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0017') {
                    activateProfile('SC-Architect', 'The Translator');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0018') {
                    activateProfile('SC-Gardener', 'The Translator');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0019') {
                    activateProfile('CI-Architect', 'The Explorer');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0020') {
                    activateProfile('CI-Gardener', 'The Explorer');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0021') {
                    activateProfile('CP-Architect', 'The Maker');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0022') {
                    activateProfile('CP-Gardener', 'The Maker');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0023') {
                    activateProfile('CS-Architect', 'The Translator');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0024') {
                    activateProfile('CS-Gardener', 'The Translator');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence.length >= 4) {
                    console.log('4+ digits, resetting');
                    keySequence = '';
                    clearTimeout(keyTimer);
                }
            }
            
            // Keep 9 key as backup
            if (e.key === '9' && keySequence === '') {
                console.log('9 key backup');
                activateProfile('IS-Architect', 'The Philosopher');
            }
        });
        
        function setTendencyPills(code) {
            const [archetypes, tendency] = code.split('-');

            // Set primary tendency pill
            const tendencyPill = document.getElementById('tendencyPill');
            if (tendencyPill) {
                tendencyPill.textContent = tendency;
                tendencyPill.className = `tendency-pill ${tendency === "Architect" ? "architect" : "gardener"}-pill`;
            }

            // Set secondary tendency pill (opposite of primary)
            const secondaryTendencyPill = document.getElementById('secondaryTendencyPill');
            if (secondaryTendencyPill) {
                const secondaryTendency = tendency === 'Architect' ? 'Gardener' : 'Architect';
                secondaryTendencyPill.textContent = secondaryTendency;
                secondaryTendencyPill.className = `tendency-pill secondary-tendency ${secondaryTendency === "Architect" ? "architect" : "gardener"}-pill`;
            }

            // Set tendency description using ProfileRenderer
            if (window.profileRenderer && window.profileRenderer.isReady && window.profileRenderer.hasProfile(code)) {
                const profile = window.profileRenderer.profiles[code];
                if (profile && profile.tendencyDescription) {
                    const tendencyDesc = document.getElementById('tendencyDescription');
                    if (tendencyDesc) {
                        tendencyDesc.innerHTML = profile.tendencyDescription.content;
                        return;
                    }
                }
            }

            // ProfileRenderer should always be available - log error if not
            console.error(`❌ setTendencyPills: ProfileRenderer not ready or missing for ${code}`);
        }
        
        function setArchetypeDescription(code) {
            // Use ProfileRenderer for profile-specific descriptions
            if (window.profileRenderer && window.profileRenderer.isReady && window.profileRenderer.hasProfile(code)) {
                const profile = window.profileRenderer.profiles[code];
                if (profile && profile.archetypeDescription) {
                    const archetypeDesc = document.getElementById('archetypeDescription');
                    if (archetypeDesc) {
                        archetypeDesc.innerHTML = profile.archetypeDescription.content;
                        return;
                    }
                }
            }

            // ProfileRenderer should always be available - log error if not
            console.error(`❌ setArchetypeDescription: ProfileRenderer missing for ${code}`);
        }
        
        function setCollapsibleSections(code) {
            // Show collapsible sections for all profiles
            const sections = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection', 'archetypesSynergySection'];
            sections.forEach(sectionId => {
                const section = document.getElementById(sectionId);
                if (section) section.style.display = 'block';
            });

            // Use ProfileRenderer for all profile content
            if (window.profileRenderer && window.profileRenderer.isReady && window.profileRenderer.hasProfile(code)) {
                const success = window.profileRenderer.renderProfile(code);
                if (success) {
                    console.log(`✅ setCollapsibleSections: Rendered ${code} using ProfileRenderer`);
                    return;
                }
            }

            // Fallback error if ProfileRenderer fails
            console.error(`❌ setCollapsibleSections: ProfileRenderer failed for ${code} - no fallback available`);
        }

        function activateProfile(code, name) {
            try {
                // Hide all screens
                document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
                
                // Show results screen
                const resultsScreen = document.getElementById('resultsScreen');
                if (resultsScreen) {
                    resultsScreen.classList.add('active');
                    
                    // Set basic profile info
                    const profileCode = document.getElementById('profileCode');
                    if (profileCode) profileCode.textContent = code;
                    
                    const profileSubtitle = document.getElementById('profileSubtitle');
                    if (profileSubtitle) profileSubtitle.textContent = name;
                    
                    // Set chord diagram for all profiles
                    const chordDiagram = document.getElementById('chordDiagram');
                    if (chordDiagram) {
                        chordDiagram.src = `../Assets/Images/Clean_STTI_${code}_Thin.png`;
                        chordDiagram.alt = `${code} Sensemaking Pattern`;
                    }
                    
                    // Set static archetype pills for all profiles
                    setStaticArchetypePills(code);
                    
                    // Set orientation for all profiles
                    setOrientation(code);
                    
                    // Set tendency pills and descriptions for all profiles
                    setTendencyPills(code);
                    
                    // Set archetype description for all profiles
                    setArchetypeDescription(code);
                    
                    // Set collapsible sections content for all profiles
                    setCollapsibleSections(code);
                    
                    // Hide sections for broken profiles
                    hideBrokenProfileSections(code);
                    
                    // Load full content based on profile

                    // TODO: Add other profiles here one by one
                    
                    console.log(`${code} activated successfully`);
                }
            } catch (err) {
                console.error('Error:', err);
                alert('Error: ' + err.message);
            }
        }
        
        function setStaticArchetypePills(code) {
            // Extract archetypes from profile code
            const archetypes = code.split('-')[0]; // Gets "IS", "CP", etc.
            const primary = archetypes[0];
            const secondary = archetypes[1];

            // Set primary and secondary pills
            const primaryPill = document.getElementById('primaryArchetypePill');
            if (primaryPill) {
                primaryPill.textContent = ARCHETYPE_NAMES[primary];
                primaryPill.className = `archetype-pill ${ARCHETYPE_PILL_CLASSES[primary]}`;
            }

            const secondaryPill = document.getElementById('secondaryArchetypePill');
            if (secondaryPill) {
                secondaryPill.textContent = ARCHETYPE_NAMES[secondary];
                secondaryPill.className = `archetype-pill ${ARCHETYPE_PILL_CLASSES[secondary]}`;
            }

            // Set third and fourth pills (remaining archetypes, faded)
            const remainingArchetypes = ['I', 'S', 'P', 'C'].filter(a => a !== primary && a !== secondary);

            const thirdPill = document.getElementById('thirdArchetypePill');
            if (thirdPill && remainingArchetypes[0]) {
                thirdPill.textContent = ARCHETYPE_NAMES[remainingArchetypes[0]];
                thirdPill.className = `archetype-pill secondary-archetype ${ARCHETYPE_PILL_CLASSES[remainingArchetypes[0]]}`;
            }

            const fourthPill = document.getElementById('fourthArchetypePill');
            if (fourthPill && remainingArchetypes[1]) {
                fourthPill.textContent = ARCHETYPE_NAMES[remainingArchetypes[1]];
                fourthPill.className = `archetype-pill secondary-archetype ${ARCHETYPE_PILL_CLASSES[remainingArchetypes[1]]}`;
            }
        }
        
        function setOrientation(code) {
            // Extract archetypes from profile code
            const [archetypes, tendency] = code.split('-');
            const sortedArchetypes = archetypes.split('').sort().join('');

            // Determine orientation based on archetype combination
            let orientation = '';

            if (sortedArchetypes === 'IS') {
                orientation = 'Westerner';
            } else if (sortedArchetypes === 'CP') {
                orientation = 'Easterner';
            } else if (sortedArchetypes === 'PS') {
                orientation = 'Northerner';
            } else if (sortedArchetypes === 'CI') {
                orientation = 'Southern';
            } else if (sortedArchetypes === 'CS') {
                orientation = 'Diagonal';
            } else if (sortedArchetypes === 'IP') {
                orientation = 'Diagonal';
            } else {
                orientation = 'Mixed';
            }

            // Set orientation pill
            const orientationPill = document.getElementById('orientationPill');
            if (orientationPill) orientationPill.textContent = orientation;

            // Use ProfileRenderer for orientation description
            if (window.profileRenderer && window.profileRenderer.isReady && window.profileRenderer.hasProfile(code)) {
                const profile = window.profileRenderer.profiles[code];
                if (profile && profile.orientationDescription) {
                    const westernerDesc = document.getElementById('westernerDescription');
                    if (westernerDesc) {
                        westernerDesc.innerHTML = profile.orientationDescription.content;
                        return;
                    }
                }
            }

            // ProfileRenderer should always be available - log error if not
            console.error(`❌ setOrientation: ProfileRenderer missing for ${code}`);
        }

        function setProfileSubtitle(code) {
            // Extract archetypes from profile code
            const [archetypes] = code.split('-');
            const sortedArchetypes = archetypes.split('').sort().join('');

            // Determine subtitle based on orientation
            let subtitle = '';

            if (sortedArchetypes === 'IS') {
                subtitle = 'The Philosopher';
            } else if (sortedArchetypes === 'CP') {
                subtitle = 'The Maker';
            } else if (sortedArchetypes === 'PS') {
                subtitle = 'The Builder';
            } else if (sortedArchetypes === 'CI') {
                subtitle = 'The Explorer';
            } else if (sortedArchetypes === 'CS') {
                subtitle = 'The Translator';
            } else if (sortedArchetypes === 'IP') {
                subtitle = 'The Converter';
            } else {
                subtitle = 'The Sensemaker';
            }

            // Set profile subtitle
            const profileSubtitle = document.getElementById('profileSubtitle');
            if (profileSubtitle) profileSubtitle.textContent = subtitle;
        }
        





        // Check for email in URL params or localStorage (but exclude demo/test values)
        (function() {
            const urlParams = new URLSearchParams(window.location.search);
            const emailFromURL = urlParams.get('email');
            const emailFromStorage = localStorage.getItem('userEmail');
            
            const prefilledEmail = emailFromURL || emailFromStorage || '';
            // Don't prefill with demo/test values
            if (prefilledEmail && !prefilledEmail.toLowerCase().includes('demo') && !prefilledEmail.toLowerCase().includes('test')) {
                document.getElementById('emailInput').value = prefilledEmail;
                userEmail = prefilledEmail;
                // Enable start button if email is valid
                if (prefilledEmail.includes('@') && prefilledEmail.length > 5) {
                    document.getElementById('startBtn').disabled = false;
                }
            }
        })();

        // Email validation and start
        const emailInput = document.getElementById('emailInput');
        const startBtn = document.getElementById('startBtn');

        emailInput.addEventListener('input', function() {
            const email = this.value;
            const isValid = email.includes('@') && email.length > 5;
            startBtn.disabled = !isValid;
            // Save to localStorage for persistence
            if (email) {
                localStorage.setItem('userEmail', email);
            }
        });

        startBtn.addEventListener('click', function() {
            userEmail = emailInput.value;
            showScreen('assessmentScreen');
            loadQuestion();
        });

        function showScreen(screenId) {
            document.querySelectorAll('.screen').forEach(screen => {
                screen.classList.remove('active');
            });
            document.getElementById(screenId).classList.add('active');
        }

        function updateNavButtons() {
            const backBtn = document.getElementById('backBtn');
            const forwardBtn = document.getElementById('forwardBtn');
            
            backBtn.disabled = currentQuestion === 0;
            forwardBtn.disabled = !answers[currentQuestion];
        }

        function loadQuestion() {
            if (currentQuestion >= questions.length) {
                showResults();
                return;
            }

            const question = questions[currentQuestion];
            document.getElementById('questionText').textContent = question.text;
            document.getElementById('progressText').textContent = `Question ${currentQuestion + 1} of ${questions.length}`;
            
            const progress = ((currentQuestion + 1) / questions.length) * 100;
            document.getElementById('progressBar').style.width = progress + '%';
            
            highlightSelectedAnswer();
            updateNavButtons();
        }

        function highlightSelectedAnswer() {
            document.querySelectorAll('.answer-btn').forEach(btn => {
                btn.style.opacity = '1';
                btn.style.transform = 'scale(1)';
            });
            
            if (answers[currentQuestion]) {
                const selectedBtn = document.querySelector(`[onclick="selectAnswer('${answers[currentQuestion].answer}')"]`);
                if (selectedBtn) {
                    selectedBtn.style.opacity = '0.8';
                    selectedBtn.style.transform = 'scale(0.95)';
                }
            }
        }

        function selectAnswer(response) {
            // Bounds check to prevent accessing undefined question
            if (currentQuestion >= questions.length) {
                console.error('selectAnswer called with currentQuestion out of bounds:', currentQuestion);
                return;
            }
            
            answers[currentQuestion] = {
                questionId: questions[currentQuestion].id,
                answer: response,
                archetype: questions[currentQuestion].archetype
            };
            console.log('Q53 DEBUG: Answer selected for question', currentQuestion + 1, 'of', questions.length);
            
            // Visual feedback
            document.querySelectorAll('.answer-btn').forEach(btn => {
                btn.style.transform = 'scale(1)';
            });
            
            const selectedBtn = event.target.closest('.answer-btn');
            if (selectedBtn) {
                selectedBtn.style.transform = 'scale(0.95)';
            }

            updateNavButtons();
            
            // Auto-advance after a short delay
            if (currentQuestion < questions.length - 1) {
                setTimeout(() => {
                    currentQuestion++;
                    loadQuestion();
                }, 400);
            } else {            console.log('Q53 DEBUG: On last question, calling showResults in 400ms');
            
                setTimeout(() => {
                    showResults();
                }, 400);
            }
        }

        function goBack() {
            if (currentQuestion > 0) {
                currentQuestion--;
                loadQuestion();
            }
        }

        function goForward() {
            if (currentQuestion < questions.length - 1 && answers[currentQuestion]) {
                currentQuestion++;
                loadQuestion();
            } else if (currentQuestion === questions.length - 1 && answers[currentQuestion]) {
                showResults();
            }
        }

        function calculateScores() {
            const scores = { I: 0, S: 0, P: 0, C: 0, A: 0, G: 0 };
            
            Object.values(answers).forEach(answer => {
                if (answer.archetype === 'RH') return; // Skip red herrings
                
                const archetype = answer.archetype.substring(0, 1);
                const polarity = answer.archetype.substring(1);
                
                let score = 0;
                switch (answer.answer) {
                    case 'SD': score = polarity === '+' ? 1 : 4; break;
                    case 'D': score = polarity === '+' ? 2 : 3; break;
                    case 'A': score = polarity === '+' ? 3 : 2; break;
                    case 'SA': score = polarity === '+' ? 4 : 1; break;
                }
                
                scores[archetype] += score;
            });
            
            return scores;
        }

        function determineProfile(scores) {
            // Get all 4 archetypes sorted by score (highest to lowest)
            const archetypeScores = [
                ['I', scores.I], ['S', scores.S], ['P', scores.P], ['C', scores.C]
            ].sort((a, b) => b[1] - a[1]);
            
            // Determine tendency
            const tendency = scores.A > scores.G ? 'Architect' : 'Gardener';
            
            const dominantArchetypes = [archetypeScores[0][0], archetypeScores[1][0]];
            const code = dominantArchetypes.join('') + '-' + tendency;
            
            return { code, dominantArchetypes, tendency, scores, archetypeScores };
        }

        async function submitToFormspree(profile) {
            try {
                const response = await fetch('https://formspree.io/f/xvgblrvw', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        email: userEmail,
                        profile_code: profile.code,
                        dominant_archetypes: profile.dominantArchetypes.join(' & '),
                        tendency: profile.tendency,
                        scores: profile.scores,
                        timestamp: new Date().toISOString(),
                        answers: Object.values(answers).map(answer => ({
                            question_id: answer.questionId,
                            question_text: questions.find(q => q.id === answer.questionId)?.text,
                            answer: answer.answer,
                            archetype: answer.archetype
                        }))
                    })
                });
                
                if (response.ok) {
                    console.log('Data submitted to Formspree successfully');
                } else {
                    console.error('Failed to submit to Formspree');
                }
            } catch (error) {
                console.error('Error submitting to Formspree:', error);
            }
        }

        function showResults() {
            console.log('Q53 DEBUG: showResults() called, hasSubmitted =', hasSubmitted);

            const scores = calculateScores();
            const profile = determineProfile(scores);

            // Prevent multiple submissions to Formspree
            if (hasSubmitted) {
                console.log('Results already submitted, skipping duplicate Formspree submission');
                // Still show the results screen even if it's a duplicate
                showScreen('resultsScreen');
                return;
            }
            hasSubmitted = true;
            
            // Set collapsible sections content for this profile
            setCollapsibleSections(profile.code);
            
            // Hide sections for broken profiles
            hideBrokenProfileSections(profile.code);

            // Submit to Formspree
            submitToFormspree(profile);
            
            // Update results display
            document.getElementById('profileCode').textContent = profile.code;
            
            // Extract archetypes from profile code for description logic
            const [archetypes, tendency] = profile.code.split('-');

            // Use score-based rankings for all archetype positions
            const primaryArchetype = ARCHETYPE_NAMES[profile.archetypeScores[0][0]];
            const secondaryArchetype = ARCHETYPE_NAMES[profile.archetypeScores[1][0]];
            const primaryDesc = ARCHETYPE_DESCRIPTIONS[profile.archetypeScores[0][0]];
            const secondaryDesc = ARCHETYPE_DESCRIPTIONS[profile.archetypeScores[1][0]];
            const tendencyDesc = TENDENCY_DESCRIPTIONS[profile.tendency];
            
            // Update archetype pills
            document.getElementById('primaryArchetypePill').textContent = primaryArchetype;
            document.getElementById('secondaryArchetypePill').textContent = secondaryArchetype;
            
            // Update pill classes based on archetype types
            const primaryPill = document.getElementById('primaryArchetypePill');
            const secondaryPill = document.getElementById('secondaryArchetypePill');
            
            // Reset classes
            primaryPill.className = 'archetype-pill';
            secondaryPill.className = 'archetype-pill';
            
            // Add appropriate color classes
            if (primaryArchetype === 'Inner Guide') primaryPill.classList.add('inner-guide-pill');
            else if (primaryArchetype === 'Synthesizer') primaryPill.classList.add('synthesizer-pill');
            else if (primaryArchetype === 'Producer') primaryPill.classList.add('producer-pill');
            else if (primaryArchetype === 'Creative') primaryPill.classList.add('creative-pill');
            
            if (secondaryArchetype === 'Inner Guide') secondaryPill.classList.add('inner-guide-pill');
            else if (secondaryArchetype === 'Synthesizer') secondaryPill.classList.add('synthesizer-pill');
            else if (secondaryArchetype === 'Producer') secondaryPill.classList.add('producer-pill');
            else if (secondaryArchetype === 'Creative') secondaryPill.classList.add('creative-pill');
            
            // Update third and fourth archetype pills using actual score rankings
            const thirdArchetype = archetypeNames[profile.archetypeScores[2][0]];
            const fourthArchetype = archetypeNames[profile.archetypeScores[3][0]];
            
            const thirdPill = document.getElementById('thirdArchetypePill');
            const fourthPill = document.getElementById('fourthArchetypePill');
            
            thirdPill.textContent = thirdArchetype;
            fourthPill.textContent = fourthArchetype;
            
            // Reset and add classes for third pill
            thirdPill.className = 'archetype-pill secondary-archetype';
            if (thirdArchetype === 'Inner Guide') thirdPill.classList.add('inner-guide-pill');
            else if (thirdArchetype === 'Synthesizer') thirdPill.classList.add('synthesizer-pill');
            else if (thirdArchetype === 'Producer') thirdPill.classList.add('producer-pill');
            else if (thirdArchetype === 'Creative') thirdPill.classList.add('creative-pill');
            
            // Reset and add classes for fourth pill
            fourthPill.className = 'archetype-pill secondary-archetype';
            if (fourthArchetype === 'Inner Guide') fourthPill.classList.add('inner-guide-pill');
            else if (fourthArchetype === 'Synthesizer') fourthPill.classList.add('synthesizer-pill');
            else if (fourthArchetype === 'Producer') fourthPill.classList.add('producer-pill');
            else if (fourthArchetype === 'Creative') fourthPill.classList.add('creative-pill');

            // Set archetype description using ProfileRenderer
            setArchetypeDescription(profile.code);

            // Update tendency pill
            const tendencyPill = document.getElementById('tendencyPill');
            tendencyPill.textContent = profile.tendency;
            tendencyPill.className = 'tendency-pill ' + (profile.tendency === 'Architect' ? 'architect-pill' : 'gardener-pill');
            
            // Update secondary tendency pill (show opposite tendency)
            const secondaryTendencyPill = document.getElementById('secondaryTendencyPill');
            const secondaryTendency = profile.tendency === 'Architect' ? 'Gardener' : 'Architect';
            secondaryTendencyPill.textContent = secondaryTendency;
            secondaryTendencyPill.className = 'tendency-pill secondary-tendency ' + (secondaryTendency === 'Architect' ? 'architect-pill' : 'gardener-pill');
            
            document.getElementById('tendencyDescription').innerHTML =
                `The <strong>${profile.tendency}</strong> is your dominant sensemaking tendency. This means you ${tendencyDesc}`;

            // Set orientation title
            const westernerTitle = document.getElementById('westernerTitle');
            westernerTitle.textContent = 'Orientation';

            // Set profile subtitle and orientation using helper functions
            setProfileSubtitle(profile.code);
            setOrientation(profile.code);
            
            // Show additional sections for all profiles
            const overwhelmedSection = document.getElementById('overwhelmedSection');
            const stuckUnstuckSection = document.getElementById('stuckUnstuckSection');
            const promptsSection = document.getElementById('promptsSection');
            
            // Always show the collapsible sections - they contain profile-specific content
            overwhelmedSection.style.display = 'block';
            stuckUnstuckSection.style.display = 'block';
            promptsSection.style.display = 'block';
            
            // Update chord diagram image
            const chordImage = document.getElementById('chordDiagram');
            chordImage.src = `../Assets/Images/Clean_STTI_${profile.code}_Thin.png`;
            chordImage.alt = `${profile.code} Sensemaking Pattern`;
            
            showScreen('resultsScreen');
        }

        function shareResults() {
            const profileCode = document.getElementById('profileCode').textContent;
            const shareText = `I just discovered I'm a ${profileCode} on the STTI Assessment! Find out your sensemaking type at https://nickmilo.github.io/stti-assessment/`;
            
            if (navigator.share) {
                navigator.share({
                    title: `I'm a ${profileCode}! - STTI Assessment`,
                    text: shareText,
                    url: 'https://nickmilo.github.io/stti-assessment/'
                }).catch(err => console.log('Error sharing:', err));
            } else if (navigator.clipboard) {
                navigator.clipboard.writeText(shareText)
                    .then(() => alert('Share text copied to clipboard!'))
                    .catch(() => alert('Unable to copy to clipboard'));
            } else {
                alert(shareText);
            }
        }

        function toggleShareDropdown(button) {
            const dropdown = button.nextElementSibling;
            const isVisible = dropdown.classList.contains('show');
            
            // Close all other dropdowns first
            document.querySelectorAll('.share-dropdown.show').forEach(d => {
                d.classList.remove('show');
            });
            
            // Toggle current dropdown
            if (!isVisible) {
                dropdown.classList.add('show');
            }
        }

        function shareToTwitter() {
            const profileCode = document.getElementById('profileCode').textContent;
            const subtitle = document.getElementById('profileSubtitle').textContent;
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent(`I just discovered I'm an ${profileCode} - ${subtitle}! Find out your sensemaking type:`);
            
            window.open(`https://twitter.com/intent/tweet?text=${text}&url=${url}`, '_blank');
            closeAllDropdowns();
        }


        function copyResultsLink() {
            const url = window.location.href;
            
            if (navigator.clipboard) {
                navigator.clipboard.writeText(url)
                    .then(() => {
                        alert('Link copied to clipboard!');
                        closeAllDropdowns();
                    })
                    .catch(() => {
                        alert('Unable to copy to clipboard');
                        closeAllDropdowns();
                    });
            } else {
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = url;
                document.body.appendChild(textArea);
                textArea.select();
                try {
                    document.execCommand('copy');
                    alert('Link copied to clipboard!');
                } catch (err) {
                    alert('Unable to copy to clipboard');
                }
                document.body.removeChild(textArea);
                closeAllDropdowns();
            }
        }

        function shareViaEmail() {
            const profileCode = document.getElementById('profileCode').textContent;
            const subtitle = document.getElementById('profileSubtitle').textContent;
            const url = window.location.href;
            const subject = encodeURIComponent(`Check out my STTI Assessment results!`);
            const body = encodeURIComponent(`I just discovered I'm an ${profileCode} - ${subtitle}! Find out your sensemaking type at: ${url}`);
            
            window.open(`mailto:?subject=${subject}&body=${body}`, '_blank');
            closeAllDropdowns();
        }

        function closeAllDropdowns() {
            document.querySelectorAll('.share-dropdown.show').forEach(dropdown => {
                dropdown.classList.remove('show');
            });
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function(event) {
            if (!event.target.closest('.share-dropdown-container')) {
                closeAllDropdowns();
            }
        });

        function toggleSection(contentId, titleElement) {
            const content = document.getElementById(contentId);
            const isCollapsed = content.classList.contains('collapsed');
            
            if (isCollapsed) {
                // Expand
                content.classList.remove('collapsed');
                content.classList.add('expanded');
                titleElement.classList.remove('collapsed');
            } else {
                // Collapse
                content.classList.remove('expanded');
                content.classList.add('collapsed');
                titleElement.classList.add('collapsed');
            }
        }





        // Image modal functionality
        document.addEventListener('click', function(event) {
            // Check if clicked on chord diagram
            if (event.target.id === 'chordDiagram') {
                const modal = document.getElementById('imageModal');
                const modalImage = document.getElementById('modalImage');
                modalImage.src = event.target.src;
                modal.classList.add('active');
            }
            
            // Close modal when clicking anywhere on it
            if (event.target.closest('#imageModal')) {
                document.getElementById('imageModal').classList.remove('active');
            }
        });

        // Hide collapsible sections for broken profiles
        function hideBrokenProfileSections(profileCode) {
            const brokenProfiles = ['IC-Architect', 'IC-Gardener', 'PI-Architect', 'PI-Gardener', 'PC-Architect', 'SI-Architect', 'SI-Gardener', 'SP-Architect', 'SP-Gardener', 'SC-Architect', 'SC-Gardener'];
            
            if (brokenProfiles.includes(profileCode)) {
                const sectionsToHide = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection', 'archetypesSynergySection'];
                sectionsToHide.forEach(sectionId => {
                    const section = document.getElementById(sectionId);
                    if (section) {
                        section.style.display = 'none';
                    }
                });
            }
        }
