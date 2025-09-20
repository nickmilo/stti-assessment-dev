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
            
            // Set tendency description
            const tendencyDesc = document.getElementById('tendencyDescription');
            if (tendencyDesc) {
                if (tendency === 'Architect') {
                    tendencyDesc.innerHTML = 'The <strong>Architect</strong> is your dominant sensemaking tendency. This means you gravitate towards structuring and organizing the things around you. However, it doesn\'t mean the things around you are organized, only that you prefer clarity and understanding over uncertainty, but sometimes even…opportunities.';
                } else {
                    tendencyDesc.innerHTML = 'The <strong>Gardener</strong> is your dominant sensemaking tendency. This means you gravitate towards nurturing and cultivating the things around you. You prefer organic growth and emergence over rigid structure, allowing ideas and projects to develop naturally while providing gentle guidance.';
                }
            }
        }
        
        function setArchetypeDescription(code) {
            const [archetypes, tendency] = code.split('-');
            const primary = archetypes[0];
            const secondary = archetypes[1];
            
            const archetypeNames = {
                'I': 'Inner Guide',
                'S': 'Synthesizer', 
                'P': 'Producer',
                'C': 'Creative'
            };
            
            const archetypeDesc = document.getElementById('archetypeDescription');
            if (archetypeDesc) {
                const primaryName = archetypeNames[primary];
                const secondaryName = archetypeNames[secondary];
                archetypeDesc.innerHTML = `The <strong>${primaryName}</strong> is your dominant sensemaking archetype, followed by the <strong>${secondaryName}</strong>. This combination shapes how you naturally approach understanding and creating meaning from the world around you.`;
            }
        }
        
        function setCollapsibleSections(code) {
            const [archetypes, tendency] = code.split('-');
            
            // Show collapsible sections for all profiles
            const sections = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection'];
            sections.forEach(sectionId => {
                const section = document.getElementById(sectionId);
                if (section) section.style.display = 'block';
            });
            
            
            
            if (code === 'IS-Architect') {
                // Set overwhelmed content for IS-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They usually double-down on their strengths to analyze, when what they likely need more is to move from reflection to expression.';
                }
                
                // Set stuck/unstuck content for IS-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IS-Architect';
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from reflection to expression is by tapping into your Producer archetype, which aligns with your structured approach.';
                }
                
                // Set prompts content for IS-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to go from West to East as an IS-Architect';
                    promptsContent.innerHTML = 'How can you tie your current activity or problem to a concrete outcome or goal? How can your Producer help pull your work along? Once your Producer is activated, you will likely find it becomes easier to drop into your Creative archetype, allowing you to find unique ways to express your deep insights.';
                }
                return; // Exit early, dont use generic logic
            }
            
            // Handle specific profile codes first
            if (code === 'IS-Gardener') {
                // Set overwhelmed content for IS-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to double-down on reflection and analysis, when what they actually need is to move into expression and action, allowing their insights to manifest in the world.';
                }
                
                // Set stuck/unstuck content for IS-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IS-Gardener';
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with a Gardener tendency, it\'s most difficult to access your Producer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from reflection to expression is by tapping into your Creative archetype, which aligns with your flexible, emergent approach.';
                }
                
                // Set prompts content for IS-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to go from West to East as an IS-Gardener';
                    promptsContent.innerHTML = 'What wants to emerge from your current reflection? How might your Creative archetype express this organically? Once your Creative is activated, you will likely find it becomes easier to move into your Producer archetype, allowing you to find natural ways to manifest your deep insights.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'IP-Architect') {
                // Set overwhelmed content for IP-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can oscillate between deep reflection and intense action, when what they need is to find a sustainable rhythm that honors both their inner wisdom and their drive to create tangible outcomes.';
                }
                
                // Set stuck/unstuck content for IP-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IP-Architect';
                    stuckContent.innerHTML = 'When you combine your Converter archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from meaning to execution is by tapping into your Synthesizer archetype, which aligns with your structured approach to understanding.';
                }
                
                // Set prompts content for IP-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to sustain your conversion rhythm as an IP-Architect';
                    promptsContent.innerHTML = 'How can you create systematic pathways from insight to action? What would a sustainable process look like for converting your deep understanding into concrete outcomes? Once your Synthesizer is activated, you will likely find it becomes easier to move into your Creative archetype, allowing you to find innovative ways to bridge meaning and execution.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'IP-Gardener') {
                // Set overwhelmed content for IP-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can oscillate between deep reflection and intense action, when what they need is to find a sustainable rhythm that honors both their inner wisdom and their drive to create tangible outcomes.';
                }
                
                // Set stuck/unstuck content for IP-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IP-Gardener';
                    stuckContent.innerHTML = 'When you combine your Converter archetypes with a Gardener tendency, it\'s most difficult to access your Synthesizer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from meaning to execution is by tapping into your Creative archetype, which aligns with your flexible, emergent approach.';
                }
                
                // Set prompts content for IP-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to sustain your conversion rhythm as an IP-Gardener';
                    promptsContent.innerHTML = 'What rhythm naturally emerges between your inner knowing and outer creating? How can your Creative help you express insights organically? Once your Creative is activated, you will likely find it becomes easier to move into your Synthesizer archetype, allowing you to make sense of your creative expressions.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'CP-Architect') {
                // Set overwhelmed content for CP-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                }
                
                // Set stuck/unstuck content for CP-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CP-Architect';
                    stuckContent.innerHTML = 'When you combine your Easterner archetypes with an Architect tendency, it\'s most difficult to access your Inner Guide archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from expression to reflection is by tapping into your Creative archetype, which aligns with your structured approach to innovation.';
                }
                
                // Set prompts content for CP-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to go from East to West as a CP-Architect';
                    promptsContent.innerHTML = 'What patterns are emerging from your creative output? How can your Creative help you innovate within your structured approach? Once your Creative is activated, you will likely find it becomes easier to move into your Inner Guide archetype, allowing you to access deeper meaning in your work.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'CP-Gardener') {
                // Set overwhelmed content for CP-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                }
                
                // Set stuck/unstuck content for CP-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CP-Gardener';
                    stuckContent.innerHTML = 'When you combine your Easterner archetypes with a Gardener tendency, it\'s most difficult to access your Synthesizer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from expression to reflection is by tapping into your Producer archetype, which aligns with your flexible approach to getting things done.';
                }
                
                // Set prompts content for CP-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to go from East to West as a CP-Gardener';
                    promptsContent.innerHTML = 'What deeper meaning is your creative work pointing toward? How can your Producer help you organize your creative insights organically? Once your Producer is activated, you will likely find it becomes easier to move into your Synthesizer archetype, allowing you to make sense of your creative expressions.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'CS-Architect') {
                // Set overwhelmed content for CS-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                }
                
                // Set stuck/unstuck content for CS-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CS-Architect';
                    stuckContent.innerHTML = 'When you combine your Translator archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to focus your translation work is by tapping into your Producer archetype, which aligns with your structured approach to getting things done.';
                }
                
                // Set prompts content for CS-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to focus your translation work as a CS-Architect';
                    promptsContent.innerHTML = 'What is the one key insight that most needs to be communicated? How can your Producer help you structure this translation systematically? Once your Producer is activated, you will likely find it becomes easier to move into your Creative archetype, allowing you to find innovative ways to bridge complex concepts.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'CS-Gardener') {
                // Set overwhelmed content for CS-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                }
                
                // Set stuck/unstuck content for CS-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CS-Gardener';
                    stuckContent.innerHTML = 'When you combine your Translator archetypes with a Gardener tendency, it\'s most difficult to access your Producer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to focus your translation work is by tapping into your Creative archetype, which aligns with your flexible approach to innovation.';
                }
                
                // Set prompts content for CS-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to focus your translation work as a CS-Gardener';
                    promptsContent.innerHTML = 'Which perspectives are asking to be bridged right now? How can your Creative help you find innovative ways to connect ideas? Once your Creative is activated, you will likely find it becomes easier to move into your Producer archetype, allowing you to manifest your translations into concrete outcomes.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'PS-Architect') {
                // Set overwhelmed content for PS-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isn\'t perfectly planned.';
                }
                
                // Set stuck/unstuck content for PS-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PS-Architect';
                    stuckContent.innerHTML = 'When you combine your Northerner archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance building with breakthrough is by tapping into your Inner Guide archetype, which aligns with your structured approach to meaning-making.';
                }
                
                // Set prompts content for PS-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance building with breakthrough as a PS-Architect';
                    promptsContent.innerHTML = 'What would happen if you approached this systematically but with creative flair? How can your Inner Guide help you access deeper meaning in your structured process? Once your Inner Guide is activated, you will likely find it becomes easier to move into your Creative archetype, allowing you to inject innovation into your methodical approach.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'PS-Gardener') {
                // Set overwhelmed content for PS-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isn\'t perfectly planned.';
                }
                
                // Set stuck/unstuck content for PS-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PS-Gardener';
                    stuckContent.innerHTML = 'When you combine your Northerner archetypes with a Gardener tendency, it\'s most difficult to access your Inner Guide archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance building with breakthrough is by tapping into your Creative archetype, which aligns with your flexible approach to innovation.';
                }
                
                // Set prompts content for PS-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance building with breakthrough as a PS-Gardener';
                    promptsContent.innerHTML = 'When does your systematic approach serve you, and when might exploration be more valuable? How can your Creative help you find innovative approaches to building? Once your Creative is activated, you will likely find it becomes easier to move into your Inner Guide archetype, allowing you to access the deeper meaning behind your systematic work.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'CI-Architect') {
                // Set overwhelmed content for CI-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Southern feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                }
                
                // Set stuck/unstuck content for CI-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CI-Architect';
                    stuckContent.innerHTML = 'When you combine your Southern archetypes with an Architect tendency, it\'s most difficult to access your Synthesizer archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to ground exploration with direction is by tapping into your Producer archetype, which aligns with your structured approach to creating tangible outcomes.';
                }
                
                // Set prompts content for CI-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to ground exploration with direction as a CI-Architect';
                    promptsContent.innerHTML = 'Which of your creative insights are ready to become concrete outcomes? How can your Producer help you build something tangible from your explorations? Once your Producer is activated, you will likely find it becomes easier to move into your Synthesizer archetype, allowing you to make systematic sense of your discoveries.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'CI-Gardener') {
                // Set overwhelmed content for CI-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Southern feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                }
                
                // Set stuck/unstuck content for CI-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CI-Gardener';
                    stuckContent.innerHTML = 'When you combine your Southern archetypes with a Gardener tendency, it\'s most difficult to access your Producer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to ground exploration with direction is by tapping into your Synthesizer archetype, which aligns with your flexible approach to making sense of discoveries.';
                }
                
                // Set prompts content for CI-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to ground exploration with direction as a CI-Gardener';
                    promptsContent.innerHTML = 'What patterns are emerging from your creative explorations? How can your Synthesizer help you make sense of your discoveries organically? Once your Synthesizer is activated, you will likely find it becomes easier to move into your Producer archetype, allowing you to manifest your insights into meaningful action.';
                }
                
            if (code === 'IC-Architect') {
                // Set overwhelmed content for IC-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Southern feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                }
                
                // Set stuck/unstuck content for IC-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IC-Architect';
                    stuckContent.innerHTML = 'When you combine your Southern archetypes with an Architect tendency, it\'s most difficult to access your Producer archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to ground exploration with structure is by tapping into your Creative archetype, which aligns with your structured approach to innovative expression.';
                }
                
                // Set prompts content for IC-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to ground exploration with structure as an IC-Architect';
                    promptsContent.innerHTML = 'How can you bring more structure to your creative explorations? What systems would help you manifest your innovative insights? Once your Creative is activated, you will likely find it becomes easier to move into your Producer archetype, allowing you to build systematic progress from your discoveries.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'IC-Gardener') {
                // Set overwhelmed content for IC-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Southern feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                }
                
                // Set stuck/unstuck content for IC-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IC-Gardener';
                    stuckContent.innerHTML = 'When you combine your Southern archetypes with a Gardener tendency, it\'s most difficult to access your Synthesizer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to ground exploration with understanding is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.';
                }
                
                // Set prompts content for IC-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to ground exploration with understanding as an IC-Gardener';
                    promptsContent.innerHTML = 'What patterns are emerging from your creative discoveries? How can your Inner Guide help you make deeper sense of your explorations organically? Once your Inner Guide is activated, you will likely find it becomes easier to move into your Synthesizer archetype, allowing you to weave your insights into coherent understanding.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'PC-Architect') {
                // Set overwhelmed content for PC-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                }
                
                // Set stuck/unstuck content for PC-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PC-Architect';
                    stuckContent.innerHTML = 'When you combine your Easterner archetypes with an Architect tendency, it\'s most difficult to access your Inner Guide archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance making with meaning is by tapping into your Producer archetype, which aligns with your structured approach to systematic action.';
                }
                
                // Set prompts content for PC-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance making with meaning as a PC-Architect';
                    promptsContent.innerHTML = 'How can you bring more systematic structure to your creative work? What processes would help you manifest your innovations more effectively? Once your Producer is activated, you will likely find it becomes easier to move into your Inner Guide archetype, allowing you to access deeper meaning in your systematic creations.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'PC-Gardener') {
                // Set overwhelmed content for PC-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                }
                
                // Set stuck/unstuck content for PC-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PC-Gardener';
                    stuckContent.innerHTML = 'When you combine your Easterner archetypes with a Gardener tendency, it\'s most difficult to access your Synthesizer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance making with understanding is by tapping into your Creative archetype, which aligns with your flexible approach to innovative expression.';
                }
                
                // Set prompts content for PC-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance making with understanding as a PC-Gardener';
                    promptsContent.innerHTML = 'What new insights are emerging from your creative work? How can your Creative help you discover unexpected connections in your making process? Once your Creative is activated, you will likely find it becomes easier to move into your Synthesizer archetype, allowing you to weave deeper understanding into your innovative outputs.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'SC-Architect') {
                // Set overwhelmed content for SC-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                }
                
                // Set stuck/unstuck content for SC-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SC-Architect';
                    stuckContent.innerHTML = 'When you combine your Translator archetypes with an Architect tendency, it\'s most difficult to access your Inner Guide archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to bridge perspectives with meaning is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.';
                }
                
                // Set prompts content for SC-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to bridge perspectives with meaning as an SC-Architect';
                    promptsContent.innerHTML = 'What deeper meaning connects the perspectives you\'re translating? How can your Synthesizer help you structure these connections systematically? Once your Synthesizer is activated, you will likely find it becomes easier to move into your Inner Guide archetype, allowing you to access the intrinsic meaning behind your translations.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'SC-Gardener') {
                // Set overwhelmed content for SC-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                }
                
                // Set stuck/unstuck content for SC-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SC-Gardener';
                    stuckContent.innerHTML = 'When you combine your Translator archetypes with a Gardener tendency, it\'s most difficult to access your Producer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to bridge perspectives with action is by tapping into your Creative archetype, which aligns with your flexible approach to innovative expression.';
                }
                
                // Set prompts content for SC-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to bridge perspectives with action as an SC-Gardener';
                    promptsContent.innerHTML = 'What creative expressions could emerge from the perspectives you\'re bridging? How can your Creative help you manifest your translations in innovative ways? Once your Creative is activated, you will likely find it becomes easier to move into your Producer archetype, allowing you to take systematic action on your synthesized insights.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'SP-Architect') {
                // Set overwhelmed content for SP-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isn\'t perfectly planned.';
                }
                
                // Set stuck/unstuck content for SP-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SP-Architect';
                    stuckContent.innerHTML = 'When you combine your Northerner archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance building with innovation is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.';
                }
                
                // Set prompts content for SP-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance building with innovation as an SP-Architect';
                    promptsContent.innerHTML = 'How can you systematically analyze what you\'re building for creative opportunities? What patterns in your work suggest new innovative directions? Once your Synthesizer is activated, you will likely find it becomes easier to move into your Creative archetype, allowing you to inject fresh innovation into your systematic building process.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'SP-Gardener') {
                // Set overwhelmed content for SP-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isnt perfectly planned.';
                }
                
                // Set stuck/unstuck content for SP-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SP-Gardener';
                    stuckContent.innerHTML = 'When you combine your Northerner archetypes with a Gardener tendency, it\'s most difficult to access your Inner Guide archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance building with meaning is by tapping into your Producer archetype, which aligns with your flexible approach to systematic action.';
                }
                
                // Set prompts content for SP-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance building with meaning as an SP-Gardener';
                    promptsContent.innerHTML = 'What meaningful action could emerge organically from your building process? How can your Producer help you manifest progress in ways that feel naturally flowing? Once your Producer is activated, you will likely find it becomes easier to move into your Inner Guide archetype, allowing you to access deeper meaning in your systematic work.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'SI-Architect') {
                // Set overwhelmed content for SI-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to double-down on reflection and analysis, when what they actually need is to move into expression and action, allowing their insights to manifest in the world.';
                }
                
                // Set stuck/unstuck content for SI-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SI-Architect';
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from understanding to expression is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.';
                }
                
                // Set prompts content for SI-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to move from understanding to expression as an SI-Architect';
                    promptsContent.innerHTML = 'How can you structure your insights for systematic creative expression? What frameworks would help you manifest your understanding in innovative ways? Once your Synthesizer is activated, you will likely find it becomes easier to move into your Creative archetype, allowing you to express your deep understanding through original contributions.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'SI-Gardener') {
                // Set overwhelmed content for SI-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to double-down on reflection and analysis, when what they actually need is to move into expression and action, allowing their insights to manifest in the world.';
                }
                
                // Set stuck/unstuck content for SI-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SI-Gardener';
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with a Gardener tendency, it\'s most difficult to access your Producer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from understanding to action is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.';
                }
                
                // Set prompts content for SI-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to move from understanding to action as an SI-Gardener';
                    promptsContent.innerHTML = 'What meaningful action could emerge organically from your understanding? How can your Inner Guide help you sense what wants to be manifested? Once your Inner Guide is activated, you will likely find it becomes easier to move into your Producer archetype, allowing you to take systematic action on your deepest insights.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'PI-Architect') {
                // Set overwhelmed content for PI-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may oscillate too rapidly between reflection and action, when what they need is to find a sustainable rhythm that honors both their need for meaning and their drive to make progress.';
                }
                
                // Set stuck/unstuck content for PI-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PI-Architect';
                    stuckContent.innerHTML = 'When you combine your Converter archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance meaning with execution is by tapping into your Producer archetype, which aligns with your structured approach to systematic action.';
                }
                
                // Set prompts content for PI-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance meaning with execution as a PI-Architect';
                    promptsContent.innerHTML = 'How can you systematically structure your meaningful work for consistent progress? What processes would help you maintain momentum while honoring depth? Once your Producer is activated, you will likely find it becomes easier to move into your Creative archetype, allowing you to innovate within your systematic approach to meaningful action.';
                }
                return; // Exit early, dont use generic logic
            }
            
            if (code === 'PI-Gardener') {
                // Set overwhelmed content for PI-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may oscillate too rapidly between reflection and action, when what they need is to find a sustainable rhythm that honors both their need for meaning and their drive to make progress.';
                }
                
                // Set stuck/unstuck content for PI-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PI-Gardener';
                    stuckContent.innerHTML = 'When you combine your Converter archetypes with a Gardener tendency, it\'s most difficult to access your Synthesizer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance meaning with execution is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.';
                }
                
                // Set prompts content for PI-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance meaning with execution as a PI-Gardener';
                    promptsContent.innerHTML = 'What natural rhythm emerges between meaningful reflection and purposeful action? How can your Inner Guide help you sense when to move between meaning and execution? Once your Inner Guide is activated, you will likely find it becomes easier to move into your Synthesizer archetype, allowing you to weave understanding into your action-oriented approach.';
                }
                return; // Exit early, dont use generic logic
            }
            return; // Exit early, dont use generic logic
            }
            
            // All 24 profiles have specific implementations above
            // No generic fallback needed - if we reach here, it's an error
            console.error('setCollapsibleSections: Unknown profile code:', code);
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
            
            // Archetype names and classes
            const archetypeNames = {
                'I': 'Inner Guide',
                'S': 'Synthesizer', 
                'P': 'Producer',
                'C': 'Creative'
            };
            
            const archetypePillClasses = {
                'I': 'inner-guide-pill',
                'S': 'synthesizer-pill',
                'P': 'producer-pill',
                'C': 'creative-pill'
            };
            
            // Set primary and secondary pills
            const primaryPill = document.getElementById('primaryArchetypePill');
            if (primaryPill) {
                primaryPill.textContent = archetypeNames[primary];
                primaryPill.className = `archetype-pill ${archetypePillClasses[primary]}`;
            }
            
            const secondaryPill = document.getElementById('secondaryArchetypePill');
            if (secondaryPill) {
                secondaryPill.textContent = archetypeNames[secondary];
                secondaryPill.className = `archetype-pill ${archetypePillClasses[secondary]}`;
            }
            
            // Set third and fourth pills (remaining archetypes, faded)
            const remainingArchetypes = ['I', 'S', 'P', 'C'].filter(a => a !== primary && a !== secondary);
            
            const thirdPill = document.getElementById('thirdArchetypePill');
            if (thirdPill && remainingArchetypes[0]) {
                thirdPill.textContent = archetypeNames[remainingArchetypes[0]];
                thirdPill.className = `archetype-pill secondary-archetype ${archetypePillClasses[remainingArchetypes[0]]}`;
            }
            
            const fourthPill = document.getElementById('fourthArchetypePill');
            if (fourthPill && remainingArchetypes[1]) {
                fourthPill.textContent = archetypeNames[remainingArchetypes[1]];
                fourthPill.className = `archetype-pill secondary-archetype ${archetypePillClasses[remainingArchetypes[1]]}`;
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
            
            // Set orientation description
            const westernerDesc = document.getElementById('westernerDescription');
            if (westernerDesc) {
                if (orientation === 'Westerner') {
                    westernerDesc.innerHTML = `As an <strong>${code}</strong>, you have a <strong>Westerner</strong> profile with a tendency to <strong>${tendency === "Architect" ? "architect" : "garden"}</strong> (notice how the image is predominantly focused on the western side). Westerners are known as "philosophers." They often get stuck reflecting and ruminating, and have difficulty moving from thinking to doing.`;
                } else if (orientation === 'Easterner') {
                    westernerDesc.innerHTML = `As an <strong>${code}</strong>, you have an <strong>Easterner</strong> profile with a tendency to <strong>${tendency === "Architect" ? "architect" : "garden"}</strong> (notice how the image is predominantly focused on the eastern side). Easterners are known as "makers." They often get stuck going from expression to reflection, from outward orientation to inward, from doing to thinking. But when Easterners feel overwhelmed, the answer is usually to do less action and more reflection.`;
                } else if (orientation === 'Northerner') {
                    westernerDesc.innerHTML = `As an <strong>${code}</strong>, you have a <strong>Northerner</strong> profile with a tendency to <strong>${tendency === "Architect" ? "architect" : "garden"}</strong> (notice how the image is predominantly focused on the northern side). Northerners are known as "builders." They excel at structured creation and systematic progress, combining productive action with synthesized understanding. When overwhelmed, Northerners benefit from stepping back to gain perspective before diving into execution.`;
                } else if (orientation === 'Southern') {
                    westernerDesc.innerHTML = `As an <strong>${code}</strong>, you have a <strong>Southern</strong> profile with a tendency to <strong>${tendency === "Architect" ? "architect" : "garden"}</strong> (notice how the image is predominantly focused on the southern side). Southern are known as "explorers." They thrive on creative introspection and meaningful discovery, combining inner guidance with creative expression. When stuck, Southern need space for both reflection and creative experimentation.`;
                } else if (orientation === 'Diagonal') {
                    if (sortedArchetypes === 'CS') {
                        westernerDesc.innerHTML = `As an <strong>${code}</strong>, you have a <strong>Diagonal</strong> profile with a tendency to <strong>${tendency === "Architect" ? "architect" : "garden"}</strong> (notice how the image spans diagonally across quadrants). You are known as "translators." You bridge creative expression with systematic synthesis, helping others understand complex ideas. Your diagonal nature gives you unique perspective-shifting abilities.`;
                    } else {
                        westernerDesc.innerHTML = `As an <strong>${code}</strong>, you have a <strong>Diagonal</strong> profile with a tendency to <strong>${tendency === "Architect" ? "architect" : "garden"}</strong> (notice how the image spans diagonally across quadrants). You are known as "converters." You excel at transforming inner insights into productive action, bridging the gap between meaning and execution. Your diagonal nature allows you to move fluidly between reflection and creation.`;
                    }
                } else {
                    westernerDesc.innerHTML = `As an <strong>${code}</strong>, your profile combines multiple orientations, giving you flexibility to move between different modes of sensemaking as needed.`;
                }
            }


        }
        




       function loadProfileByCode(profileCode, profileName, orientation) {
            // Basic profile info
            const codeEl = document.getElementById('profileCode');
            if (codeEl) codeEl.textContent = profileCode;
            
            const subtitleEl = document.getElementById('profileSubtitle');
            if (subtitleEl) subtitleEl.textContent = profileName;
            
            const orientationEl = document.getElementById('orientationPill');
            if (orientationEl) orientationEl.textContent = orientation;
            
            // Extract archetypes and tendency from profile code
            const [archetypes, tendency] = profileCode.split('-');
            const primary = archetypes[0];
            const secondary = archetypes[1];
            
            // Archetype names and pill classes
            const archetypeNames = {
                'I': 'Inner Guide',
                'S': 'Synthesizer', 
                'P': 'Producer',
                'C': 'Creative'
            };
            
            const archetypePillClasses = {
                'I': 'inner-guide-pill',
                'S': 'synthesizer-pill',
                'P': 'producer-pill',
                'C': 'creative-pill'
            };
            
            // Set archetype pills dynamically based on profile
            const primaryPill = document.getElementById('primaryArchetypePill');
            if (primaryPill) {
                primaryPill.textContent = archetypeNames[primary];
                primaryPill.className = `archetype-pill ${archetypePillClasses[primary]}`;
            }
            
            const secondaryPill = document.getElementById('secondaryArchetypePill');
            if (secondaryPill) {
                secondaryPill.textContent = archetypeNames[secondary];
                secondaryPill.className = `archetype-pill ${archetypePillClasses[secondary]}`;
            }
            
            // Set third and fourth pills (faded) - using mock score ranking for now
            const otherArchetypes = ['I', 'S', 'P', 'C'].filter(a => a !== primary && a !== secondary);
            
            const thirdPill = document.getElementById('thirdArchetypePill');
            if (thirdPill && otherArchetypes[0]) {
                thirdPill.textContent = archetypeNames[otherArchetypes[0]];
                thirdPill.className = `archetype-pill secondary-archetype ${archetypePillClasses[otherArchetypes[0]]}`;
            }
            
            const fourthPill = document.getElementById('fourthArchetypePill');
            if (fourthPill && otherArchetypes[1]) {
                fourthPill.textContent = archetypeNames[otherArchetypes[1]];
                fourthPill.className = `archetype-pill secondary-archetype ${archetypePillClasses[otherArchetypes[1]]}`;
            }
            
            // Set archetype description based on combination
            const archetypeDesc = document.getElementById('archetypeDescription');
            if (archetypeDesc) {
                let description = '';
                const sortedArchetypes = archetypes.split('').sort().join('');
                
                if (sortedArchetypes === 'IS') {
                    description = `The <strong>${archetypeNames[primary]}</strong> and <strong>${archetypeNames[secondary]}</strong> combination creates a philosophical approach to sensemaking. You naturally seek deep understanding and meaning, often spending significant time in reflection and analysis. Your strength lies in your ability to synthesize complex ideas and find underlying patterns, though you may sometimes struggle with moving from contemplation to action.`;
                } else if (sortedArchetypes === 'CP') {
                    description = `The <strong>${archetypeNames[primary]}</strong> and <strong>${archetypeNames[secondary]}</strong> combination creates a maker's approach to sensemaking. You thrive on creative expression and productive output, naturally translating ideas into tangible results. Your strength lies in your ability to innovate and execute, though you may sometimes need to balance your action-oriented nature with deeper reflection.`;
                } else if (sortedArchetypes === 'PS') {
                    description = `The <strong>${archetypeNames[primary]}</strong> and <strong>${archetypeNames[secondary]}</strong> combination creates a builder's approach to sensemaking. You excel at systematic creation and structured progress, combining practical action with comprehensive understanding. Your strength lies in your ability to construct robust frameworks and methodologies, making complex projects manageable and sustainable.`;
                } else if (sortedArchetypes === 'CI') {
                    description = `The <strong>${archetypeNames[primary]}</strong> and <strong>${archetypeNames[secondary]}</strong> combination creates an explorer's approach to sensemaking. You thrive on creative discovery and meaningful investigation, naturally seeking novel perspectives and innovative solutions. Your strength lies in your ability to venture into uncharted territory and find unique insights that others might miss.`;
                } else if (sortedArchetypes === 'CS') {
                    description = `The <strong>${archetypeNames[primary]}</strong> and <strong>${archetypeNames[secondary]}</strong> combination creates a translator's approach to sensemaking. You excel at bridging different worlds of understanding, making complex or abstract concepts accessible to others. Your strength lies in your ability to synthesize diverse perspectives and communicate insights across different contexts and audiences.`;
                } else if (sortedArchetypes === 'IP') {
                    description = `The <strong>${archetypeNames[primary]}</strong> and <strong>${archetypeNames[secondary]}</strong> combination creates a converter's approach to sensemaking. You excel at transforming deep insights into practical applications, bridging the gap between meaning and action. Your strength lies in your ability to take abstract understanding and convert it into concrete, productive outcomes.`;
                } else {
                    description = `The <strong>${archetypeNames[primary]}</strong> and <strong>${archetypeNames[secondary]}</strong> combination creates a unique approach to sensemaking that blends their distinctive strengths.`;
                }
                
                archetypeDesc.innerHTML = description;
            }
            
            // Set tendency pills
            const tendencyPill = document.getElementById('tendencyPill');
            if (tendencyPill) {
                tendencyPill.textContent = 'Architect';
                tendencyPill.className = 'tendency-pill architect-pill';
            }
            
            const secondaryTendencyPill = document.getElementById('secondaryTendencyPill');
            if (secondaryTendencyPill) {
                secondaryTendencyPill.textContent = 'Gardener';
                secondaryTendencyPill.className = 'tendency-pill secondary-tendency gardener-pill';
            }
            
            // Set tendency description based on tendency
            const tendencyDesc = document.getElementById('tendencyDescription');
            if (tendencyDesc) {
                if (tendency === 'Architect') {
                    tendencyDesc.innerHTML = 'The <strong>Architect</strong> is your dominant sensemaking tendency. This means you gravitate towards structuring and organizing the things around you. However, it doesn\'t mean the things around you are organized, only that you prefer clarity and understanding over uncertainty, but sometimes even…opportunities.';
                } else {
                    tendencyDesc.innerHTML = 'The <strong>Gardener</strong> is your dominant sensemaking tendency. This means you prefer flexibility and emergent approaches, allowing ideas and projects to develop organically. You thrive in ambiguous situations and are comfortable navigating uncertainty, often discovering unexpected opportunities through exploration.';
                }
            }
            

            
            // Show and populate collapsible sections
            const sections = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection'];
            sections.forEach(sectionId => {
                const section = document.getElementById(sectionId);
                if (section) section.style.display = 'block';
            });
            
            // Removed hardcoded IS-Architect content that was overriding profile-specific content
            // setCollapsibleSections() already sets the correct content for each profile
            
            // Set chord diagram
            const chordDiagram = document.getElementById('chordDiagram');
            if (chordDiagram) {
                chordDiagram.src = '../Assets/Images/Clean_STTI_\1.png';
                chordDiagram.alt = 'IS-Architect Sensemaking Pattern';
            }
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
            // Prevent multiple submissions
            if (hasSubmitted) {
                console.log('Results already submitted, skipping duplicate submission');
                return;
            }
            hasSubmitted = true;

            const scores = calculateScores();
            const profile = determineProfile(scores);
            
            // Set collapsible sections content for this profile
            setCollapsibleSections(profile.code);
            
            // Hide sections for broken profiles
            hideBrokenProfileSections(profile.code);
            
            // Determine orientation based on archetype combinations (used throughout function)
            var orientationArchetypes = profile.dominantArchetypes.sort().join('');
            
            // Submit to Formspree
            submitToFormspree(profile);
            
            // Update results display
            document.getElementById('profileCode').textContent = profile.code;
            
            // Extract archetypes from profile code for description logic
            const [archetypes, tendency] = profile.code.split('-');
            
            const archetypeNames = {
                'I': 'Inner Guide',
                'S': 'Synthesizer', 
                'P': 'Producer',
                'C': 'Creative'
            };

            const archetypeDescriptions = {
                'I': 'naturally focus on things that you find intrinsically meaningful',
                'S': 'having a desire to deeply make sense of those things',
                'P': 'being energized by taking action and making progress on meaningful work',
                'C': 'expressing your unique perspective and creating original contributions'
            };

            const tendencyDescriptions = {
                'Architect': 'gravitate towards structuring and organizing the things around you. However, it doesn\'t mean the things around you are organized, only that you prefer clarity and understanding over uncertainty, but sometimes even…opportunities.',
                'Gardener': 'prefer flexibility and emergent approaches, allowing ideas and projects to develop organically. You thrive in ambiguous situations and are comfortable navigating uncertainty, often discovering unexpected opportunities through exploration.'
            };
            
            // Use score-based rankings for all archetype positions
            const primaryArchetype = archetypeNames[profile.archetypeScores[0][0]];
            const secondaryArchetype = archetypeNames[profile.archetypeScores[1][0]];
            const primaryDesc = archetypeDescriptions[profile.archetypeScores[0][0]];
            const secondaryDesc = archetypeDescriptions[profile.archetypeScores[1][0]];
            const tendencyDesc = tendencyDescriptions[profile.tendency];
            
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
            
            // Create specific archetype combination descriptions
            let archetypeDescription = '';
            
            if (orientationArchetypes === 'IS' || orientationArchetypes === 'SI') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a philosophical approach to sensemaking. You naturally seek deep understanding and meaning, often spending significant time in reflection and analysis. Your strength lies in your ability to synthesize complex ideas and find underlying patterns, though you may sometimes struggle with moving from contemplation to action.`;
            } else if (orientationArchetypes === 'CP' || orientationArchetypes === 'PC') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a maker's approach to sensemaking. You thrive on creative expression and productive output, naturally translating ideas into tangible results. Your strength lies in your ability to innovate and execute, though you may sometimes need to balance your action-oriented nature with deeper reflection.`;
            } else if (orientationArchetypes === 'PS' || orientationArchetypes === 'SP') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a builder's approach to sensemaking. You excel at systematic creation and structured progress, combining practical action with comprehensive understanding. Your strength lies in your ability to construct robust frameworks and methodologies, making complex projects manageable and sustainable.`;
            } else if (orientationArchetypes === 'CI' || orientationArchetypes === 'IC') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates an explorer's approach to sensemaking. You thrive on creative discovery and meaningful investigation, naturally seeking novel perspectives and innovative solutions. Your strength lies in your ability to venture into uncharted territory and find unique insights that others might miss.`;
            } else if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a translator's approach to sensemaking. You excel at bridging different worlds of understanding, making complex or abstract concepts accessible to others. Your strength lies in your ability to synthesize diverse perspectives and communicate insights across different contexts and audiences.`;
            } else if (orientationArchetypes === 'IP' || orientationArchetypes === 'PI') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a converter's approach to sensemaking. You excel at transforming deep insights into practical applications, bridging the gap between meaning and action. Your strength lies in your ability to take abstract understanding and convert it into concrete, productive outcomes.`;
            } else {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> is your dominant sensemaking archetype, followed by the <strong>${secondaryArchetype}</strong>. This combination creates a unique approach to understanding and engaging with the world around you.`;
            }
            
            document.getElementById('archetypeDescription').innerHTML = archetypeDescription;
            
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
            
            // Determine orientation based on archetype combinations
            let orientation = '';
            
            if (orientationArchetypes === 'IS' || orientationArchetypes === 'SI') {
                orientation = 'Westerner';
            } else if (orientationArchetypes === 'CP' || orientationArchetypes === 'PC') {
                orientation = 'Easterner';
            } else if (orientationArchetypes === 'PS' || orientationArchetypes === 'SP') {
                orientation = 'Northerner';
            } else if (orientationArchetypes === 'CI' || orientationArchetypes === 'IC') {
                orientation = 'Southern';
            } else if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                orientation = 'Diagonal';
            } else if (orientationArchetypes === 'IP' || orientationArchetypes === 'PI') {
                orientation = 'Diagonal';
            } else {
                orientation = 'Mixed';
            }
            
            // Legacy variables for backward compatibility
            const isWesterner = (orientation === 'Westerner');
            const isEasterner = (orientation === 'Easterner');
            
            const westernerTitle = document.getElementById('westernerTitle');
            const westernerDescription = document.getElementById('westernerDescription');
            
            // Update identity title, subtitle and description
            const westernerSubtitle = document.getElementById('westernerSubtitle');
            
            // Update profile subtitle (The Philosopher, The Maker, etc.)
            const profileSubtitle = document.getElementById('profileSubtitle');
            
            if (orientationArchetypes === 'IS' || orientationArchetypes === 'SI') {
                profileSubtitle.textContent = 'The Philosopher';
            } else if (orientationArchetypes === 'CP' || orientationArchetypes === 'PC') {
                profileSubtitle.textContent = 'The Maker';
            } else if (orientationArchetypes === 'PS' || orientationArchetypes === 'SP') {
                profileSubtitle.textContent = 'The Builder';
            } else if (orientationArchetypes === 'CI' || orientationArchetypes === 'IC') {
                profileSubtitle.textContent = 'The Explorer';
            } else if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                profileSubtitle.textContent = 'The Translator';
            } else if (orientationArchetypes === 'IP' || orientationArchetypes === 'PI') {
                profileSubtitle.textContent = 'The Converter';
            } else {
                profileSubtitle.textContent = 'The Sensemaker';
            }
            
            // Update orientation pill
            const orientationPill = document.getElementById('orientationPill');
            orientationPill.textContent = orientation;
            
            westernerTitle.textContent = 'Orientation';
            
            if (orientation === 'Westerner') {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Westerner</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image is predominantly focused on the western side). Westerners are known as "philosophers." They often get stuck reflecting and ruminating, and have difficulty moving from thinking to doing.`;
            } else if (orientation === 'Easterner') {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have an <strong>Easterner</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image is predominantly focused on the eastern side). Easterners are known as "makers." They often get stuck going from expression to reflection, from outward orientation to inward, from doing to thinking. But when Easterners feel overwhelmed, the answer is usually to do less action and more reflection.`;
            } else if (orientation === 'Northerner') {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Northerner</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image is predominantly focused on the northern side). Northerners are known as "builders." They excel at structured creation and systematic progress, combining productive action with synthesized understanding. When overwhelmed, Northerners benefit from stepping back to gain perspective before diving into execution.`;
            } else if (orientation === 'Southern') {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Southern</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image is predominantly focused on the southern side). Southern are known as "explorers." They thrive on creative introspection and meaningful discovery, combining inner guidance with creative expression. When stuck, Southern need space for both reflection and creative experimentation.`;
            } else if (orientation === 'Diagonal') {
                if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                    westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Diagonal</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image spans diagonally across quadrants). You are known as "translators." You bridge creative expression with systematic synthesis, helping others understand complex ideas. Your diagonal nature gives you unique perspective-shifting abilities.`;
                } else {
                    westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Diagonal</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image spans diagonally across quadrants). You are known as "converters." You excel at transforming inner insights into productive action, bridging meaning with execution. Your diagonal nature allows you to move fluidly between reflection and creation.`;
                }
            } else {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, your profile combines multiple orientations, giving you flexibility to move between different modes of sensemaking as needed.`;
            }
            
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



        function showTestResults(targetProfile) {
            // Ensure we have userEmail set for the secret codes to work
            if (!userEmail) {
                userEmail = 'test@example.com';
            }
            
            // Show specific profile
            const [targetArchetypes, targetTendency] = targetProfile.split('-');
            const primary = targetArchetypes[0];
            const secondary = targetArchetypes[1];
            
            // Create mock profile object
            const mockScores = { I: 20, S: 15, P: 18, C: 12, A: targetTendency === 'Architect' ? 25 : 15, G: targetTendency === 'Gardener' ? 25 : 15 };
            
            // Create sorted archetype scores for dynamic positioning
            const mockArchetypeScores = [
                ['I', mockScores.I], ['S', mockScores.S], ['P', mockScores.P], ['C', mockScores.C]
            ].sort((a, b) => b[1] - a[1]);
            
            const mockProfile = {
                code: targetProfile,
                dominantArchetypes: [primary, secondary],
                tendency: targetTendency,
                scores: mockScores,
                archetypeScores: mockArchetypeScores
            };
            
            // Fill answers with sample data
            for (let i = 0; i < 48; i++) {
                answers[i] = {
                    questionId: questions[i].id,
                    answer: 'A',
                    archetype: questions[i].archetype
                };
            }
            
            // Directly show the specific profile
            activateProfile(mockProfile.code, 'Test Profile');
        }

        function showSpecificProfile(profile) {
            console.log('showSpecificProfile called with:', profile);
            // Update results display with specific profile
            const profileCodeElement = document.getElementById('profileCode');
            if (!profileCodeElement) {
                console.error('Element with id "profileCode" not found');
                return;
            }
            profileCodeElement.textContent = profile.code;
            
            const archetypeNames = {
                'I': 'Inner Guide',
                'S': 'Synthesizer', 
                'P': 'Producer',
                'C': 'Creative'
            };

            // Determine orientation based on archetype combinations (used throughout function)
            var orientationArchetypes = profile.dominantArchetypes.sort().join('');

            const archetypeDescriptions = {
                'I': 'naturally focus on things that you find intrinsically meaningful',
                'S': 'having a desire to deeply make sense of those things',
                'P': 'being energized by taking action and making progress on meaningful work',
                'C': 'expressing your unique perspective and creating original contributions'
            };

            const tendencyDescriptions = {
                'Architect': 'gravitate towards structuring and organizing the things around you. However, it doesn\'t mean the things around you are organized, only that you prefer clarity and understanding over uncertainty, but sometimes even…opportunities.',
                'Gardener': 'prefer flexibility and emergent approaches, allowing ideas and projects to develop organically. You thrive in ambiguous situations and are comfortable navigating uncertainty, often discovering unexpected opportunities through exploration.'
            };
            
            // Use score-based rankings for all archetype positions
            const primaryArchetype = archetypeNames[profile.archetypeScores[0][0]];
            const secondaryArchetype = archetypeNames[profile.archetypeScores[1][0]];
            const primaryDesc = archetypeDescriptions[profile.archetypeScores[0][0]];
            const secondaryDesc = archetypeDescriptions[profile.archetypeScores[1][0]];
            const tendencyDesc = tendencyDescriptions[profile.tendency];
            
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
            
            // Create specific archetype combination descriptions
            let archetypeDescription = '';
            
            if (orientationArchetypes === 'IS' || orientationArchetypes === 'SI') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a philosophical approach to sensemaking. You naturally seek deep understanding and meaning, often spending significant time in reflection and analysis. Your strength lies in your ability to synthesize complex ideas and find underlying patterns, though you may sometimes struggle with moving from contemplation to action.`;
            } else if (orientationArchetypes === 'CP' || orientationArchetypes === 'PC') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a maker's approach to sensemaking. You thrive on creative expression and productive output, naturally translating ideas into tangible results. Your strength lies in your ability to innovate and execute, though you may sometimes need to balance your action-oriented nature with deeper reflection.`;
            } else if (orientationArchetypes === 'PS' || orientationArchetypes === 'SP') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a builder's approach to sensemaking. You excel at systematic creation and structured progress, combining practical action with comprehensive understanding. Your strength lies in your ability to construct robust frameworks and methodologies, making complex projects manageable and sustainable.`;
            } else if (orientationArchetypes === 'CI' || orientationArchetypes === 'IC') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates an explorer's approach to sensemaking. You thrive on creative discovery and meaningful investigation, naturally seeking novel perspectives and innovative solutions. Your strength lies in your ability to venture into uncharted territory and find unique insights that others might miss.`;
            } else if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a translator's approach to sensemaking. You excel at bridging different worlds of understanding, making complex or abstract concepts accessible to others. Your strength lies in your ability to synthesize diverse perspectives and communicate insights across different contexts and audiences.`;
            } else if (orientationArchetypes === 'IP' || orientationArchetypes === 'PI') {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> and <strong>${secondaryArchetype}</strong> combination creates a converter's approach to sensemaking. You excel at transforming deep insights into practical applications, bridging the gap between meaning and action. Your strength lies in your ability to take abstract understanding and convert it into concrete, productive outcomes.`;
            } else {
                archetypeDescription = `The <strong>${primaryArchetype}</strong> is your dominant sensemaking archetype, followed by the <strong>${secondaryArchetype}</strong>. This combination creates a unique approach to understanding and engaging with the world around you.`;
            }
            
            document.getElementById('archetypeDescription').innerHTML = archetypeDescription;
            
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
            
            // Determine orientation based on archetype combinations
            let orientation = '';
            
            if (orientationArchetypes === 'IS' || orientationArchetypes === 'SI') {
                orientation = 'Westerner';
            } else if (orientationArchetypes === 'CP' || orientationArchetypes === 'PC') {
                orientation = 'Easterner';
            } else if (orientationArchetypes === 'PS' || orientationArchetypes === 'SP') {
                orientation = 'Northerner';
            } else if (orientationArchetypes === 'CI' || orientationArchetypes === 'IC') {
                orientation = 'Southern';
            } else if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                orientation = 'Diagonal';
            } else if (orientationArchetypes === 'IP' || orientationArchetypes === 'PI') {
                orientation = 'Diagonal';
            } else {
                orientation = 'Mixed';
            }
            
            // Legacy variables for backward compatibility
            const isWesterner = (orientation === 'Westerner');
            const isEasterner = (orientation === 'Easterner');
            
            const westernerTitle = document.getElementById('westernerTitle');
            const westernerDescription = document.getElementById('westernerDescription');
            
            // Update identity title, subtitle and description
            const westernerSubtitle = document.getElementById('westernerSubtitle');
            
            // Update profile subtitle (The Philosopher, The Maker, etc.)
            const profileSubtitle = document.getElementById('profileSubtitle');
            
            if (orientationArchetypes === 'IS' || orientationArchetypes === 'SI') {
                profileSubtitle.textContent = 'The Philosopher';
            } else if (orientationArchetypes === 'CP' || orientationArchetypes === 'PC') {
                profileSubtitle.textContent = 'The Maker';
            } else if (orientationArchetypes === 'PS' || orientationArchetypes === 'SP') {
                profileSubtitle.textContent = 'The Builder';
            } else if (orientationArchetypes === 'CI' || orientationArchetypes === 'IC') {
                profileSubtitle.textContent = 'The Explorer';
            } else if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                profileSubtitle.textContent = 'The Translator';
            } else if (orientationArchetypes === 'IP' || orientationArchetypes === 'PI') {
                profileSubtitle.textContent = 'The Converter';
            } else {
                profileSubtitle.textContent = 'The Sensemaker';
            }
            
            // Update orientation pill
            const orientationPill = document.getElementById('orientationPill');
            orientationPill.textContent = orientation;
            
            westernerTitle.textContent = 'Orientation';
            
            if (orientation === 'Westerner') {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Westerner</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image is predominantly focused on the western side). Westerners are known as "philosophers." They often get stuck reflecting and ruminating, and have difficulty moving from thinking to doing.`;
            } else if (orientation === 'Easterner') {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have an <strong>Easterner</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image is predominantly focused on the eastern side). Easterners are known as "makers." They often get stuck going from expression to reflection, from outward orientation to inward, from doing to thinking. But when Easterners feel overwhelmed, the answer is usually to do less action and more reflection.`;
            } else if (orientation === 'Northerner') {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Northerner</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image is predominantly focused on the northern side). Northerners are known as "builders." They excel at structured creation and systematic progress, combining productive action with synthesized understanding. When overwhelmed, Northerners benefit from stepping back to gain perspective before diving into execution.`;
            } else if (orientation === 'Southern') {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Southern</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image is predominantly focused on the southern side). Southern are known as "explorers." They thrive on creative introspection and meaningful discovery, combining inner guidance with creative expression. When stuck, Southern need space for both reflection and creative experimentation.`;
            } else if (orientation === 'Diagonal') {
                if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                    westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Diagonal</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image spans diagonally across quadrants). You are known as "translators." You bridge creative expression with systematic synthesis, helping others understand complex ideas. Your diagonal nature gives you unique perspective-shifting abilities.`;
                } else {
                    westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, you have a <strong>Diagonal</strong> profile with a tendency to <strong>${profile.tendency.toLowerCase()}</strong> (notice how the image spans diagonally across quadrants). You are known as "converters." You excel at transforming inner insights into productive action, bridging meaning with execution. Your diagonal nature allows you to move fluidly between reflection and creation.`;
                }
            } else {
                westernerDescription.innerHTML = `As an <strong>${profile.code}</strong>, your profile combines multiple orientations, giving you flexibility to move between different modes of sensemaking as needed.`;
            }
            
            // Show additional sections for IS-Architect
            const overwhelmedSection = document.getElementById('overwhelmedSection');
            const stuckUnstuckSection = document.getElementById('stuckUnstuckSection');
            const promptsSection = document.getElementById('promptsSection');
            
            // Show additional sections for all profiles and update content
            overwhelmedSection.style.display = 'block';
            stuckUnstuckSection.style.display = 'block';
            promptsSection.style.display = 'block';

            // Use ProfileRenderer to populate sections
            if (window.profileRenderer && window.profileRenderer.hasProfile(profile.code)) {
                window.profileRenderer.renderProfile(profile.code);
            } else {
                // Fallback to hardcoded content for profiles not in JSON
                // Update overwhelmed section content based on orientation
                const overwhelmedTitle = overwhelmedSection.querySelector('.section-title');
                const overwhelmedContent = document.getElementById('overwhelmedContent');

                if (orientation === 'Westerner') {
                    overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to double-down on reflection and analysis, when what they actually need is to move into expression and action, allowing their insights to manifest in the world.';
                } else if (orientation === 'Easterner') {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                } else if (orientation === 'Northerner') {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isn\'t perfectly planned.';
                } else if (orientation === 'Southern') {
                    overwhelmedTitle.textContent = 'When Southern feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                } else if (orientation === 'Diagonal') {
                    if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                        overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                        overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                    } else {
                        overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                        overwhelmedContent.innerHTML = 'They can oscillate between deep reflection and intense action, when what they need is to find a sustainable rhythm that honors both their inner wisdom and their drive to create tangible outcomes.';
                    }
                }

                // Update stuck/unstuck section content based on profile (fallback only)
                const stuckTitle = stuckUnstuckSection.querySelector('.section-title');
                const stuckContent = document.getElementById('stuckUnstuckContent');
            
                stuckTitle.textContent = `Getting stuck and unstuck as a ${profile.code}`;

                if (orientation === 'Westerner') {
                    if (profile.tendency === 'Architect') {
                        stuckContent.innerHTML = 'When you combine your Westerner archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from reflection to expression is by tapping into your Producer archetype, which aligns with your structured approach.';
                    } else {
                        stuckContent.innerHTML = 'As a Westerner with a Gardener tendency, you have natural flexibility in your approach but may get stuck in endless reflection. Your path to expression often flows through your Creative archetype, allowing organic emergence of ideas. Trust the process and let insights unfold naturally into creative output.';
                }
            } else if (orientation === 'Easterner') {
                if (profile.tendency === 'Architect') {
                    stuckContent.innerHTML = 'As an Easterner with an Architect tendency, you naturally move from expression to structure. When stuck, you may over-produce without reflection. Your path to balance is through your Synthesizer archetype, which helps you step back and make sense of your creative output before moving forward.';
                } else {
                    stuckContent.innerHTML = 'As an Easterner with a Gardener tendency, you thrive on creative flow and production. When stuck, it\'s usually because you\'ve been too active without Inner Guide reflection. Allow space for meaning-making and introspection to inform your creative expression.';
                }
            } else if (orientation === 'Northerner') {
                if (profile.tendency === 'Architect') {
                    stuckContent.innerHTML = 'As a Northerner with an Architect tendency, you excel at systematic building but may get stuck in over-planning. Your Creative archetype is your bridge to breakthrough—use it to inject innovation into your structured processes and find novel approaches to execution.';
                } else {
                    stuckContent.innerHTML = 'As a Northerner with a Gardener tendency, you balance structure with flexibility. When stuck, you may need to choose between systematic progress and organic exploration. Trust your Inner Guide to help you discern when to build methodically and when to explore new directions.';
                }
            } else if (orientation === 'Southern') {
                if (profile.tendency === 'Architect') {
                    stuckContent.innerHTML = 'As a Southern with an Architect tendency, you blend creative exploration with structured approach. When stuck, it\'s often because you\'re trying to structure the unstructurable. Lean into your Producer archetype to create concrete outcomes from your creative insights.';
                } else {
                    stuckContent.innerHTML = 'As a Southern with a Gardener tendency, you naturally flow between creativity and introspection. When stuck, you may be exploring without direction. Your Synthesizer archetype can help you make sense of your discoveries and identify meaningful patterns to pursue.';
                }
            } else if (orientation === 'Diagonal') {
                if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                    if (profile.tendency === 'Architect') {
                        stuckContent.innerHTML = 'As a Translator with an Architect tendency, you naturally bridge creative expression with systematic synthesis. When stuck, you may be over-structuring your translations. Lean into your Inner Guide to access the deeper meaning that needs to be communicated.';
                    } else {
                        stuckContent.innerHTML = 'As a Translator with a Gardener tendency, you fluidly move between creative and analytical modes. When stuck, it\'s often because you\'re trying to translate too much at once. Focus on one key insight and let your Producer help you communicate it clearly.';
                    }
                } else {
                    if (profile.tendency === 'Architect') {
                        stuckContent.innerHTML = 'As a Converter with an Architect tendency, you excel at transforming insights into structured action. When stuck, you may be trying to systematize everything. Trust your Creative archetype to find innovative ways to bridge meaning and execution.';
                    } else {
                        stuckContent.innerHTML = 'As a Converter with a Gardener tendency, you naturally flow between reflection and action. When stuck, you may be moving too quickly between modes. Use your Synthesizer to pause and make sense of your insights before converting them to action.';
                    }
                }
            }
            
            // Update prompts section content based on profile
            const promptsTitle = promptsSection.querySelector('.section-title');
            const promptsContent = document.getElementById('promptsContent');
            
            if (orientation === 'Westerner') {
                promptsTitle.textContent = `Prompts to go from West to East as a ${profile.code}`;
                if (profile.tendency === 'Architect') {
                    promptsContent.innerHTML = 'How can you tie your current activity or problem to a concrete outcome or goal? How can your Producer help pull your work along? Once your Producer is activated, you will likely find it becomes easier to drop into your Creative archetype, allowing you to find unique ways to express your deep insights.';
                } else {
                    promptsContent.innerHTML = 'What wants to emerge from your current reflection? How might your Creative archetype express this organically? Trust the natural flow from inner knowing to creative expression, allowing your insights to find their own unique form of manifestation.';
                }
            } else if (orientation === 'Easterner') {
                promptsTitle.textContent = `Prompts to go from East to West as a ${profile.code}`;
                if (profile.tendency === 'Architect') {
                    promptsContent.innerHTML = 'What patterns are emerging from your creative output? How can your Synthesizer help you step back and make sense of what you\'ve created? Take time to analyze and structure your insights before diving into the next creative cycle.';
                } else {
                    promptsContent.innerHTML = 'What deeper meaning is your creative work pointing toward? How can your Inner Guide help you understand the significance of what you\'re creating? Allow space for reflection to inform and enrich your ongoing creative expression.';
                }
            } else if (orientation === 'Northerner') {
                promptsTitle.textContent = `Prompts to balance building with breakthrough as a ${profile.code}`;
                if (profile.tendency === 'Architect') {
                    promptsContent.innerHTML = 'What would happen if you approached this systematically but with creative flair? How can your Creative archetype inject innovation into your structured process? Look for opportunities to build something uniquely yours while maintaining your methodical approach.';
                } else {
                    promptsContent.innerHTML = 'When does your systematic approach serve you, and when might exploration be more valuable? How can your Inner Guide help you discern the right balance? Trust your intuition about when to build methodically and when to explore new possibilities.';
                }
            } else if (orientation === 'Southern') {
                promptsTitle.textContent = `Prompts to ground exploration with direction as a ${profile.code}`;
                if (profile.tendency === 'Architect') {
                    promptsContent.innerHTML = 'Which of your creative insights are ready to become concrete outcomes? How can your Producer archetype help you build something tangible from your explorations? Focus on translating one key discovery into structured, actionable steps.';
                } else {
                    promptsContent.innerHTML = 'What patterns are emerging from your creative explorations? How can your Synthesizer help you make sense of your discoveries? Look for the underlying themes that can guide your next phase of meaningful investigation.';
                }
            } else if (orientation === 'Diagonal') {
                if (orientationArchetypes === 'CS' || orientationArchetypes === 'SC') {
                    promptsTitle.textContent = `Prompts to focus your translation work as a ${profile.code}`;
                    if (profile.tendency === 'Architect') {
                        promptsContent.innerHTML = 'What is the one key insight that most needs to be communicated? How can your Inner Guide help you access the deeper meaning behind this translation? Focus on structuring one clear bridge between complex concepts and accessible understanding.';
                    } else {
                        promptsContent.innerHTML = 'Which perspectives are asking to be bridged right now? How can your Producer help you communicate this synthesis clearly? Trust the organic flow of translation while ensuring your insights reach their intended audience effectively.';
                    }
                } else {
                    promptsTitle.textContent = `Prompts to sustain your conversion rhythm as a ${profile.code}`;
                    if (profile.tendency === 'Architect') {
                        promptsContent.innerHTML = 'How can you create systematic pathways from insight to action? What would a sustainable process look like for converting your deep understanding into concrete outcomes? Design structures that honor both reflection and execution.';
                    } else {
                        promptsContent.innerHTML = 'What rhythm naturally emerges between your inner knowing and outer creating? How can your Synthesizer help you recognize when to reflect and when to act? Trust the organic flow between meaning-making and manifestation.';
                    }
                }
            }
            }

            // Update chord diagram image
            const chordImage = document.getElementById('chordDiagram');
            chordImage.src = `../Assets/Images/Clean_STTI_${profile.code}_Thin.png`;
            chordImage.alt = `${profile.code} Sensemaking Pattern`;

            showScreen('resultsScreen');
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
                const sectionsToHide = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection'];
                sectionsToHide.forEach(sectionId => {
                    const section = document.getElementById(sectionId);
                    if (section) {
                        section.style.display = 'none';
                    }
                });
            }
        }
