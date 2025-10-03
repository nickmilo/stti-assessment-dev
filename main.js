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

        const demographicQuestions = [
            {
                id: 54,
                type: 'radio',
                text: 'How familiar are you with linking notes/ideas in digital tools?',
                options: [
                    'Very experienced - I use linking regularly',
                    'Somewhat experienced - I\'ve tried it or use it occasionally',
                    'Familiar with the concept but haven\'t used it much',
                    'Not familiar with linking notes/ideas digitally',
                    'Prefer not to answer'
                ]
            },
            {
                id: 55,
                type: 'radio',
                text: 'What is your age range?',
                options: [
                    'Under 18',
                    '18-24',
                    '25-34',
                    '35-44',
                    '45-54',
                    '55-64',
                    '65+',
                    'Prefer not to answer'
                ]
            },
            {
                id: 56,
                type: 'checkbox-with-text',
                text: 'Have you been diagnosed with any of these neurodivergent conditions? (Select all that apply)',
                options: [
                    'ADHD',
                    'Autism/Autistic',
                    'Dyslexia',
                    'Learning disabilities/differences',
                    { text: 'Prefer to self-describe:', hasInput: true, inputId: 'q56_self_describe' },
                    'I suspect I have something, but I haven\'t been diagnosed',
                    'None of the above',
                    'Prefer not to answer'
                ]
            },
            {
                id: 57,
                type: 'radio-with-text',
                text: 'What is your gender?',
                options: [
                    'Man',
                    'Woman',
                    'Non-binary',
                    { text: 'Prefer to self-describe:', hasInput: true, inputId: 'q57_self_describe' },
                    'Prefer not to answer'
                ]
            },
            {
                id: 58,
                type: 'radio',
                text: 'How would you describe your current approach to using AI tools?',
                options: [
                    'Enthusiastically using - I actively seek out AI tools and integrate them into my work',
                    'Practically using - I use AI tools when they\'re helpful for specific tasks',
                    'Reluctantly using - I use them sometimes but have reservations',
                    'Avoiding use - I prefer not to use AI tools',
                    'Haven\'t had much opportunity to use AI tools yet',
                    'Prefer not to answer'
                ]
            }
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

        let currentQuestion = 0;
        let answers = {};
        let demographicAnswers = {};
        let userEmail = '';
        let hasSubmittedToFormspree = false; // Prevent duplicate API submissions
        let hasRenderedResults = false; // Track rendering state separately
        const TOTAL_QUESTIONS = 58; // 53 STTI + 5 demographic (intro screen is NOT counted as a question)
        
        
        // Simple secret code system - exact copy of what worked with Z key
        let keySequence = '';
        let keyTimer = null;
        
        window.addEventListener('keydown', function(e) {
            // Only work when not in an input field
            if (document.activeElement.tagName === 'INPUT') return;
            
            // Build sequence for 4-digit codes
            if (e.key >= '0' && e.key <= '9') {
                keySequence += e.key;

                // Clear timer
                if (keyTimer) clearTimeout(keyTimer);
                
                // Reset after 3 seconds
                keyTimer = setTimeout(() => {
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
                    keySequence = '';
                    clearTimeout(keyTimer);
                }
            }
            
            // Keep 9 key as backup
            if (e.key === '9' && keySequence === '') {
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
                        chordDiagram.src = `./Assets/Images/Clean_STTI_${code}_Thin.png`;
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
            // STTI questions (0-52)
            if (currentQuestion < questions.length) {
                const question = questions[currentQuestion];
                document.getElementById('questionText').textContent = question.text;
                document.getElementById('progressText').textContent = `Question ${currentQuestion + 1} of ${TOTAL_QUESTIONS}`;

                const progress = ((currentQuestion + 1) / TOTAL_QUESTIONS) * 100;
                document.getElementById('progressBar').style.width = progress + '%';

                // Show assessment screen, hide others
                showScreen('assessmentScreen');

                highlightSelectedAnswer();
                updateNavButtons();
                return;
            }

            // After Q53, show demographic intro screen
            if (currentQuestion === questions.length) {
                showScreen('demographicIntroScreen');
                updateProgressBar();
                return;
            }

            // Demographic questions (54-58)
            const demoIndex = currentQuestion - questions.length - 1;
            if (demoIndex >= 0 && demoIndex < demographicQuestions.length) {
                showScreen('demographicQuestionScreen');
                loadDemographicQuestion(demoIndex);
                return;
            }

            // All questions complete - show results
            showResults();
        }

        function updateProgressBar() {
            // CRITICAL FIX: Calculate correct question number to display
            // - STTI questions (0-52): Display as 1-53 (currentQuestion + 1)
            // - Intro screen (53): Display as 53 (NOT 54 - intro is not a question)
            // - Demo questions (54-58): Display as 54-58 (currentQuestion itself, since already offset)
            let displayQuestion;
            if (currentQuestion < questions.length) {
                // STTI questions: 0-indexed, so add 1
                displayQuestion = currentQuestion + 1;
            } else if (currentQuestion === questions.length) {
                // Intro screen: keep at last STTI question number
                displayQuestion = questions.length;
            } else {
                // Demographic questions: currentQuestion is already the correct question number
                displayQuestion = currentQuestion;
            }

            const progress = (displayQuestion / TOTAL_QUESTIONS) * 100;
            const progressText = `Question ${displayQuestion} of ${TOTAL_QUESTIONS}`;

            // Update main assessment progress bar
            const mainProgressBar = document.getElementById('progressBar');
            const mainProgressText = document.getElementById('progressText');
            if (mainProgressBar) mainProgressBar.style.width = progress + '%';
            if (mainProgressText) mainProgressText.textContent = progressText;

            // Update demographic intro progress bar
            const demoIntroProgressBar = document.getElementById('demoIntroProgressBar');
            const demoIntroProgressText = document.getElementById('demoIntroProgressText');
            if (demoIntroProgressBar) demoIntroProgressBar.style.width = progress + '%';
            if (demoIntroProgressText) demoIntroProgressText.textContent = progressText;

            // Update demographic question progress bar
            const demoQuestionProgressBar = document.getElementById('demoQuestionProgressBar');
            const demoQuestionProgressText = document.getElementById('demoQuestionProgressText');
            if (demoQuestionProgressBar) demoQuestionProgressBar.style.width = progress + '%';
            if (demoQuestionProgressText) demoQuestionProgressText.textContent = progressText;
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
            setTimeout(() => {
                currentQuestion++;
                loadQuestion();
            }, 400);
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

        /**
         * Animates score bars with dynamic range calculation
         * Makes small differences visually prominent
         */
        function animateScoreBars(scores) {
            // Extract archetype scores
            const archetypeScores = [scores.I, scores.S, scores.P, scores.C];
            const minArchetype = Math.min(...archetypeScores);
            const maxArchetype = Math.max(...archetypeScores);
            const archetypeRange = maxArchetype - minArchetype || 1;

            // For visual emphasis, use a "zoomed" range
            const buffer = Math.max(5, archetypeRange * 0.2);
            const visualMin = Math.max(0, minArchetype - buffer);
            const visualMax = maxArchetype + buffer;
            const visualRange = visualMax - visualMin;

            // Animate each archetype bar
            animateBar('score-inner-guide', scores.I, visualMin, visualRange);
            animateBar('score-synthesizer', scores.S, visualMin, visualRange);
            animateBar('score-creative', scores.C, visualMin, visualRange);
            animateBar('score-producer', scores.P, visualMin, visualRange);

            // Tendency bars (use max of both to ensure both show proportionally)
            const tendencyMax = Math.max(scores.A, scores.G);
            animateBar('score-architect', scores.A, 0, tendencyMax);
            animateBar('score-gardener', scores.G, 0, tendencyMax);

            // Update raw scores display
            const rawScoresText = document.getElementById('raw-scores-text');
            if (rawScoresText) {
                rawScoresText.textContent = `I: ${scores.I}, S: ${scores.S}, C: ${scores.C}, P: ${scores.P} | A: ${scores.A}, G: ${scores.G}`;
            }
        }

        function animateBar(scoreId, score, minValue, range) {
            const scoreElement = document.getElementById(scoreId);
            if (!scoreElement) return;

            // Update the numerical value
            scoreElement.textContent = score;

            // Find the corresponding bar
            const wrapper = scoreElement.closest('.score-bar-wrapper');
            const bar = wrapper.querySelector('.score-bar');

            // Calculate percentage width based on dynamic range
            const adjustedScore = score - minValue;
            const percentage = (adjustedScore / range) * 100;

            // Animate the bar width after a short delay
            setTimeout(() => {
                bar.style.width = `${percentage}%`;
            }, 100);
        }

        async function submitToFormspree(profile) {
            try {
                // Format demographic data
                const demographicData = {
                    q54_linking_experience: demographicAnswers[54]?.value || 'Not answered',
                    q55_age_range: demographicAnswers[55]?.value || 'Not answered',
                    q56_neurodivergence: demographicAnswers[56]?.values || [],
                    q56_self_describe: demographicAnswers[56]?.textInputs?.q56_self_describe || '',
                    q57_gender: demographicAnswers[57]?.value || 'Not answered',
                    q57_self_describe: demographicAnswers[57]?.textInput || '',
                    q58_ai_tools: demographicAnswers[58]?.value || 'Not answered'
                };

                const response = await fetch('https://formspree.io/f/meorkprg', {
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
                        })),
                        demographic_data: demographicData
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

        async function showResults() {
            const scores = calculateScores();
            const profile = determineProfile(scores);

            // Submit to Formspree (only once)
            if (!hasSubmittedToFormspree) {
                submitToFormspree(profile);
                hasSubmittedToFormspree = true;
            } else {
                console.log('Results already submitted to Formspree, skipping duplicate submission');
            }

            // Wait for profiles to load before rendering
            try {
                // Ensure profileRenderer exists
                if (!window.profileRenderer) {
                    throw new Error('ProfileRenderer not initialized');
                }

                await window.profileRenderer.waitForProfiles();
            } catch (error) {
                console.error('Failed to load profiles after retries:', error);

                // Show error using fallback if profileRenderer doesn't exist
                if (window.profileRenderer && window.profileRenderer.showCriticalError) {
                    window.profileRenderer.showCriticalError(error);
                } else {
                    alert('Configuration Error: The assessment profiles failed to load. Please refresh the page.');
                }
                return;
            }

            // Update profile code display
            document.getElementById('profileCode').textContent = profile.code;

            // Set orientation title
            const westernerTitle = document.getElementById('westernerTitle');
            westernerTitle.textContent = 'Orientation';

            // Delegate all rendering to helper functions
            setStaticArchetypePills(profile.code);
            setOrientation(profile.code);
            setTendencyPills(profile.code);
            setArchetypeDescription(profile.code);
            setCollapsibleSections(profile.code);
            hideBrokenProfileSections(profile.code);

            // Update chord diagram
            const chordImage = document.getElementById('chordDiagram');
            chordImage.src = `./Assets/Images/Clean_STTI_${profile.code}_Thin.png`;
            chordImage.alt = `${profile.code} Sensemaking Pattern`;

            // Animate score bars
            animateScoreBars(profile.scores);

            hasRenderedResults = true; // Mark results as successfully rendered
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

        // Demographic question functions
        function loadDemographicQuestion(demoIndex) {
            const question = demographicQuestions[demoIndex];
            const questionNumber = question.id;

            updateProgressBar();

            document.getElementById('demoQuestionText').textContent = question.text;
            const optionsContainer = document.getElementById('demoOptionsContainer');
            optionsContainer.innerHTML = '';

            if (question.type === 'radio' || question.type === 'radio-with-text') {
                renderRadioOptions(question, optionsContainer, questionNumber);
            } else if (question.type === 'checkbox' || question.type === 'checkbox-with-text') {
                renderCheckboxOptions(question, optionsContainer, questionNumber);
            }

            // Show/hide navigation
            const demoBackBtn = document.getElementById('demoBackBtn');
            const demoForwardBtn = document.getElementById('demoForwardBtn');
            demoBackBtn.style.display = 'inline-block';
            demoForwardBtn.style.display = 'inline-block';
            demoBackBtn.disabled = false;

            // CRITICAL FIX: Update forward button state after rendering options
            // This ensures button is enabled if user navigates back to an answered question
            updateDemoForwardButton(questionNumber);
        }

        function renderRadioOptions(question, container, questionNumber) {
            question.options.forEach((option, index) => {
                const optionDiv = document.createElement('div');
                optionDiv.className = 'demo-option';

                const isObject = typeof option === 'object';
                const optionText = isObject ? option.text : option;
                const hasInput = isObject && option.hasInput;

                const radioId = `demo_q${questionNumber}_opt${index}`;
                const radio = document.createElement('input');
                radio.type = 'radio';
                radio.name = `demo_q${questionNumber}`;
                radio.value = optionText;
                radio.id = radioId;
                radio.className = 'demo-radio';

                // Check if previously selected
                if (demographicAnswers[questionNumber] && demographicAnswers[questionNumber].value === optionText) {
                    radio.checked = true;
                }

                radio.addEventListener('change', () => {
                    demographicAnswers[questionNumber] = { value: optionText };
                    if (hasInput) {
                        const textInput = document.getElementById(option.inputId);
                        if (textInput) {
                            demographicAnswers[questionNumber].textInput = textInput.value;
                        }
                    }
                    updateDemoForwardButton(questionNumber);
                });

                const label = document.createElement('label');
                label.htmlFor = radioId;
                label.textContent = optionText;
                label.className = 'demo-label';

                optionDiv.appendChild(radio);
                optionDiv.appendChild(label);

                if (hasInput) {
                    const textInput = document.createElement('input');
                    textInput.type = 'text';
                    textInput.id = option.inputId;
                    textInput.className = 'demo-text-input';
                    textInput.placeholder = 'Please specify...';
                    if (demographicAnswers[questionNumber] && demographicAnswers[questionNumber].textInput) {
                        textInput.value = demographicAnswers[questionNumber].textInput;
                    }
                    textInput.addEventListener('input', () => {
                        if (radio.checked && demographicAnswers[questionNumber]) {
                            demographicAnswers[questionNumber].textInput = textInput.value;
                        }
                    });
                    optionDiv.appendChild(textInput);
                }

                container.appendChild(optionDiv);
            });
        }

        function renderCheckboxOptions(question, container, questionNumber) {
            question.options.forEach((option, index) => {
                const optionDiv = document.createElement('div');
                optionDiv.className = 'demo-option';

                const isObject = typeof option === 'object';
                const optionText = isObject ? option.text : option;
                const hasInput = isObject && option.hasInput;

                const checkboxId = `demo_q${questionNumber}_opt${index}`;
                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.value = optionText;
                checkbox.id = checkboxId;
                checkbox.className = 'demo-checkbox';

                // Initialize answer array if needed
                if (!demographicAnswers[questionNumber]) {
                    demographicAnswers[questionNumber] = { values: [], textInputs: {} };
                }

                // Check if previously selected
                if (demographicAnswers[questionNumber].values.includes(optionText)) {
                    checkbox.checked = true;
                }

                checkbox.addEventListener('change', () => {
                    if (!demographicAnswers[questionNumber]) {
                        demographicAnswers[questionNumber] = { values: [], textInputs: {} };
                    }

                    if (checkbox.checked) {
                        if (!demographicAnswers[questionNumber].values.includes(optionText)) {
                            demographicAnswers[questionNumber].values.push(optionText);
                        }
                    } else {
                        const idx = demographicAnswers[questionNumber].values.indexOf(optionText);
                        if (idx > -1) {
                            demographicAnswers[questionNumber].values.splice(idx, 1);
                        }
                        if (hasInput) {
                            delete demographicAnswers[questionNumber].textInputs[option.inputId];
                        }
                    }
                    updateDemoForwardButton(questionNumber);
                });

                const label = document.createElement('label');
                label.htmlFor = checkboxId;
                label.textContent = optionText;
                label.className = 'demo-label';

                optionDiv.appendChild(checkbox);
                optionDiv.appendChild(label);

                if (hasInput) {
                    const textInput = document.createElement('input');
                    textInput.type = 'text';
                    textInput.id = option.inputId;
                    textInput.className = 'demo-text-input';
                    textInput.placeholder = 'Please specify...';
                    if (demographicAnswers[questionNumber] && demographicAnswers[questionNumber].textInputs[option.inputId]) {
                        textInput.value = demographicAnswers[questionNumber].textInputs[option.inputId];
                    }
                    textInput.addEventListener('input', () => {
                        if (checkbox.checked) {
                            if (!demographicAnswers[questionNumber].textInputs) {
                                demographicAnswers[questionNumber].textInputs = {};
                            }
                            demographicAnswers[questionNumber].textInputs[option.inputId] = textInput.value;
                        }
                    });
                    optionDiv.appendChild(textInput);
                }

                container.appendChild(optionDiv);
            });
        }

        function updateDemoForwardButton(questionNumber) {
            const forwardBtn = document.getElementById('demoForwardBtn');
            const answer = demographicAnswers[questionNumber];

            if (answer) {
                if (answer.value !== undefined) {
                    // Radio question - has answer
                    forwardBtn.disabled = false;
                } else if (answer.values !== undefined && answer.values.length > 0) {
                    // Checkbox question - has at least one selection
                    forwardBtn.disabled = false;
                } else {
                    forwardBtn.disabled = true;
                }
            } else {
                forwardBtn.disabled = true;
            }
        }

        function demoGoBack() {
            if (currentQuestion > questions.length) {
                currentQuestion--;
                hasRenderedResults = false; // Allow results to be re-rendered if user returns
                loadQuestion();
            }
        }

        function demoGoForward() {
            const demoIndex = currentQuestion - questions.length - 1;
            const questionNumber = demographicQuestions[demoIndex].id;

            if (demographicAnswers[questionNumber]) {
                // Check if this is the last demographic question
                if (demoIndex === demographicQuestions.length - 1) {
                    // Last demographic question - go directly to results
                    showResults();
                } else {
                    // More demographic questions remain
                    currentQuestion++;
                    loadQuestion();
                }
            }
        }

        function continueToDemographics() {
            currentQuestion++;
            loadQuestion();
        }

        function skipToResults() {
            // Skip demographic questions and show results immediately
            showResults();
        }
