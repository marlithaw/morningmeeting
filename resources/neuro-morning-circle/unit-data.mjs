// Data for "The 15-Minute Neuro-Regulated Morning Circle" — Quarter 1 Core Curriculum.
// Grounded in Lori Desautels' brain-aligned practices and the Matchbook Morning Meeting sequence.
// This week runs the first four lessons for each grade band: Monday Aug 31 – Thursday Sep 3, 2026.

export const unitMeta = {
  title: 'Neuro-Regulated Morning Circle',
  subtitle: 'A 15-minute trauma-responsive Morning Circle that regulates the body before instruction begins.',
  duration: '15 minutes',
  dates: 'Monday, August 31 – Thursday, September 3, 2026',
  friday: 'Friday, September 4, 2026 · Choice-Point Integration and Friday Cypher celebration — not a fifth lesson.',
  framework: ['Emotional Temperature Check', 'Mindful Breathing', 'Cultural Wisdom & Shared Stories', 'Daily Intention Setting'],
  phases: ['Regulate', 'Orient', 'Connect', 'Practice', 'Commit', 'Transition'],
  sources: [
    { label: 'Lori Desautels · Brain-Aligned & Trauma-Responsive Practices', url: 'https://revelationsineducation.com/' },
    { label: 'Stephen W. Porges (2011) · The Polyvagal Theory', url: 'https://wwnorton.com/books/9780393707007' },
    { label: 'Matchbook Morning Meeting · ROAR Values (Safe · Respectful · Responsible)', url: 'https://marlithaw.github.io/morningmeeting/' }
  ]
};

export const bands = {
  k2: { label: 'Grades K–2', short: 'K–2', code: 'k2', engine: 'Sensory Engine', focusSystem: 'Brainstem & sensory-motor' },
  '35': { label: 'Grades 3–5', short: '3–5', code: '35', engine: 'Coping Toolkit', focusSystem: 'Limbic & emotional-identification' },
  '68': { label: 'Grades 6–8', short: '6–8', code: '68', engine: 'Independence Toolkit', focusSystem: 'Self-awareness & respectful independence' }
};

export const common = {
  disclosure: 'If a student shares a current concern of harm, hunger, or crisis, respond with warm empathy, protect privacy, do not process it in front of peers, and route the student privately to support services the same day.',
  warmDemander: 'Warm Demander logic balances unconditional positive regard with absolute procedural accountability. When a student is pushed outside the Window of Tolerance, de-escalate the biology (Regulate) before addressing accountability (Reason).',
  window: 'Every routine exists to widen the Window of Tolerance — the zone where a student is calm enough to think, learn, and connect.'
};

// OpenMoji (CC BY-SA 4.0) served from jsDelivr, pinned to release 15.0.0.
const IMG = 'https://cdn.jsdelivr.net/gh/hfg-gmuend/openmoji@15.0.0/color/svg';
export const imageCredit = 'Illustrations: OpenMoji — the open-source emoji and icon project · License: CC BY-SA 4.0';
const pic = (code, label) => ({ src: `${IMG}/${code}.svg`, label });
const ICON = {
  sun: () => pic('2600', 'Sunny · calm'),
  cloud: () => pic('2601', 'Cloudy'),
  rain: () => pic('1F327', 'Rainy'),
  storm: () => pic('26C8', 'Stormy'),
  snowman: () => pic('26C4', 'Freeze & melt'),
  hand: (l = 'Breathing hand') => pic('1F590', l),
  star: (l = 'My star') => pic('2B50', l),
  feather: () => pic('1FAB6', 'Slow like a feather'),
  wave: (l = 'Calm hands') => pic('1F44B', l),
  heart: (l = 'Hand on heart') => pic('2764', l),
  hearts: () => pic('1F495', 'Kindness echo'),
  speak: (l = 'Say it kindly') => pic('1F5E3', l),
  shake: (l = 'Turn to a partner') => pic('1F91D', l),
  tree: (l = 'Grow like a tree') => pic('1F333', l),
  ear: () => pic('1F442', 'Listening ears'),
  lotus: (l = 'Calm breathing') => pic('1F9D8', l)
};

export const lessons = [
  // ============================ DAY 1 ============================
  {
    day: 1,
    date: 'Monday, August 31, 2026',
    step: 'Emotional Temperature Check',
    value: 'Safe',
    summary: 'Name the body’s internal weather and build a felt sense of safety in the circle.',
    bands: {
      k2: {
        focus: 'Body Weather Report',
        iCan: 'I can notice my “body weather” and know that every feeling is safe in our circle.',
        somaticGoal: 'Connect internal physical arousal to relatable weather symbols to self-identify stress.',
        somatic: 'Sit with a tall spine, both hands flat on the tummy. Close eyes or look at shoes. “Breathe into your hands. Feel your tummy rise and fall. Is it warm and calm like a sunny day, fluttery like a wind gust, or tight like a stormy cloud?”',
        phases: {
          regulate: { teacher: '“Settle in, hands on your belly. Breathe in soft and slow… let it out like wind. Let’s do three tummy breaths.”', student: 'Places hands on stomach; sits quietly and mimics breathing.', ifThen: 'If energy is high or squirmy, then do not publicly call out. Extend the breathing sways to align heart rates.', img: [ICON.sun()] },
          orient: { teacher: '“Today we check our Body Weather. At Matchbook, our circle is Safe. Weather is just weather—it is okay to feel stormy here.”', student: 'Points to the weather chart on the board (Sun, Clouds, Rain, Storm).', ifThen: 'If a student refuses to look up, then protect their space. Use a soft, non-demanding vocal tone.', img: [ICON.sun(), ICON.cloud(), ICON.rain(), ICON.storm()] },
          connect: { teacher: '“I’m going to pass our talking ball. When you get it, say your body weather: ‘My weather is [sunny / cloudy / stormy].’ You can also pass.”', student: 'Receives ball, speaks weather zone using visual supports, or passes ball.', ifThen: 'If a student passes, then say: “Thank you for passing. Your silence is safe here.” Protect emotional safety first.', img: [ICON.speak('My weather is…'), ICON.cloud()] },
          practice: { teacher: '“Stormy weather can make our bodies shake. Let’s shake our hands fast for 5 seconds, then freeze and melt like a snowman.”', student: 'Shakes hands vigorously, then freezes completely, releasing muscle tension.', ifThen: 'If a student crashes or screams during the shake, then do a calm reset: “My bad, I didn’t show the freeze signal. Settle down. Let’s try again.”', img: [ICON.snowman()] },
          commit: { teacher: '“Today, I commit to being Safe. If my weather turns stormy, I can draw a picture of a sun on my paper. Whisper your safe commitment.”', student: 'Whispers commitment to a partner or draws weather state.', ifThen: 'If vague (“I’ll be good”), then reframe: “Safe means keeping hands to ourselves. Can you commit to hands in lap?”', img: [ICON.sun('Draw a sun')] },
          transition: { teacher: '“We are ready to learn. Stand on the one. Move like a slow cloud to your table for our drawing task.”', student: 'Chants “On the one!” and walks slowly, keeping a regulated physical pace.', ifThen: 'If running or desk-touching occurs, then reset the transition silently with a hand cue. Re-practice the cloud-walk.', img: [ICON.cloud('Move like a cloud')] }
        }
      },
      '35': {
        focus: 'Safety Thermometer & Early Warning Signals',
        iCan: 'I can find my early warning signals and read my Safety Thermometer before I boil over.',
        somaticGoal: 'Develop internal interoception by mapping early physiological distress markers (heart rate, muscle tension, butterflies).',
        somatic: 'Place two fingers on the neck or wrist to locate the pulse. Close eyes and count beats for 10 seconds. “Is your heartbeat steady and cool, or is it racing up the thermometer?”',
        phases: {
          regulate: { teacher: '“Locate your pulse. Settle your breath. Let’s count our heartbeat… [pause 10s]. Breathe out all the way. Settle.”', student: 'Tracks pulse, sitting upright with feet flat on the floor.', ifThen: 'If a pulse cannot be found, then say: “Place your hand flat on your chest instead. Just feel the rise of your breath.”' },
          orient: { teacher: '“Today we build our Coping Toolkit. At Matchbook, we are Safe. Safe means knowing our Early Warning Signals before we boil over.”', student: 'Reads the Safety Thermometer board (Blue, Green, Yellow, Red).', ifThen: 'If students joke about the thermometer, then reframe: “Our bodies are biological. Thermometers measure real heat. Let’s learn our biology.”' },
          connect: { teacher: '“What is an early warning signal in your body when you feel stressed? ‘When I am stressed, my [heart races / tummy feels tight].’ Share.”', student: 'Shares physical indicators with a partner using the target sentence frame.', ifThen: 'If major behavior issues are shared, then redirect to routine physical signals to keep it safe and low-stakes.' },
          practice: { teacher: '“Let’s practice the Cool-Down Check. Tighten your fists as hard as you can for 5 seconds… now open your hands and let them go loose.”', student: 'Tenses facial and hand muscles, then completely relaxes them, releasing tension.', ifThen: 'If students throw hands or make contact, then do-over: “My bad, I didn’t specify personal space. Reset. Keep hands in your lap.”' },
          commit: { teacher: '“Write on your Toolkit slip: ‘If my heart rate goes up, I will…’ Pin it to your commitment board.”', student: 'Writes a specific, observable coping commitment and posts it.', ifThen: 'If vague (“I’ll try to be calm”), then coach: “What tool will you use? ‘I will take three deep breaths.’ Write that tool down.”' },
          transition: { teacher: '“We carry our steady heartbeat into the day. Stand on the one.”', student: 'Transitions instantly on the verbal cue, moving silently.', ifThen: 'If chatting occurs, then callback: “Check your thermometer. Settle your voice before taking your seat.”' }
        }
      },
      '68': {
        focus: 'Check-In: Reading My Early Warning Signals',
        iCan: 'I can read my early warning signals and name where stress shows up in my body before it takes over.',
        somaticGoal: 'Build body awareness by noticing early stress signals — racing heart, tight muscles, shallow breath — before they escalate.',
        somatic: 'Sit tall, feet flat. Close your eyes or look down. Take a slow breath and scan from your shoulders to your hands to your stomach. Notice one place that feels tight and one place that feels calm.',
        phases: {
          regulate: { teacher: '“Settle in. Feet flat, shoulders down. Slow breath in… and a longer breath out. Quick body scan—where are you holding stress today?”', student: 'Sits still, breathes slowly, and scans the body for tension.', ifThen: 'If a student is talking or laughing, then do not call them out publicly. Keep the calm pace and model the scan.' },
          orient: { teacher: '“At Matchbook, we are Safe. Safe starts with knowing your early warning signals—the signs your body gives before you hit your limit.”', student: 'Reads the check-in scale on the board (Calm, Okay, Tense, Overloaded).', ifThen: 'If a student is defiant, then use a Warm Demander cue: “Assigned seat, quick check-in, then we start. Settle in.”' },
          connect: { teacher: '“What’s one early warning signal you feel when stress builds? ‘When I’m stressed, my ___ (heart races / jaw tightens / hands clench).’ Share with a partner.”', student: 'Shares a personal stress signal with a partner using the sentence frame.', ifThen: 'If a student shares something heavy, then thank them, keep it low-key, and follow up privately later.' },
          practice: { teacher: '“Let’s practice a reset. Tighten your fists and shoulders for 5 seconds… now release and let them drop. Feel the difference.”', student: 'Tenses and releases the fists and shoulders, noticing the change.', ifThen: 'If students make contact with others, then do-over: “My bad, I didn’t set the space. Reset—hands to yourself.”' },
          commit: { teacher: '“On your check-in card, finish this: ‘When my early warning signal shows up, I will ___.’ Post it where you can see it.”', student: 'Writes a specific, doable plan on a card and posts it.', ifThen: 'If vague (“I’ll calm down”), then coach: “Name the exact move—‘I’ll take three slow breaths.’ Write that.”' },
          transition: { teacher: '“Carry your check-in into the day. Stand on the one.”', student: 'Stands and transitions on the cue, moving calmly and quietly.', ifThen: 'If chatting starts, then callback: “Quick check-in—settle your voice before you move.”' }
        }
      }
    }
  },
  // ============================ DAY 2 ============================
  {
    day: 2,
    date: 'Tuesday, September 1, 2026',
    step: 'Mindful Breathing',
    value: 'Safe',
    summary: 'Stabilize autonomic arousal with a portable breathing tool the body can carry all day.',
    bands: {
      k2: {
        focus: 'Five-Finger Breathing Beats',
        iCan: 'I can use my breathing hand to slow my body down whenever my engine runs too fast.',
        somaticGoal: 'Use multi-sensory bilateral touch to slow the rate of respiration and quiet the autonomic nervous system.',
        somatic: 'Hold out one hand like a star. Using the index finger of the other hand, trace up the thumb on the inhale, pause at the tip, and trace down on the exhale. Repeat for all five fingers.',
        phases: {
          regulate: { teacher: '“Hold your breathing hand up high. Trace up… breathe in. Trace down… breathe out. Feel your heart slow down.”', student: 'Sits tall, traces the hand, focuses on tactile input and slow breath.', ifThen: 'If tracing too fast, then physically model slower tracing. Say: “Breathe slowly, like a feather drifting down.”', img: [ICON.hand('Trace your hand')] },
          orient: { teacher: '“Our value is Safe. Our breathing hand is a tool we always carry in our pocket. We can use it anytime our engine runs too fast.”', student: 'Repeats the definition of safe: keeping ourselves and our friends from harm.', ifThen: 'If a student is crying, then do not address it publicly. Keep leading the trace to co-regulate the room.', img: [ICON.hand('Always in my pocket')] },
          connect: { teacher: '“Who does your hand remind you of? Share with your partner: ‘My hand makes me think of [name / my dog / a star].’”', student: 'Turns to a partner and shares using the simplified sentence starter.', ifThen: 'If a student struggles with speech or words, then invite them to show their star hand or draw the person’s initial.', img: [ICON.star('My star hand')] },
          practice: { teacher: '“Let’s walk in our spot. Lift your knees slow. Trace up as you lift your left knee, down as you lift your right.”', student: 'Practices bilateral gross-motor coordination integrated with breath.', ifThen: 'If balance is lost or squirming starts, then simplify: “Sit down and let’s trace our toes instead. Slow and steady.”', img: [ICON.feather()] },
          commit: { teacher: '“Draw a quick hand-star on your sticky note. Place it on your desk as your commitment to use your breathing tool today.”', student: 'Traces the hand or draws a star on a sticky note, posting it on their workspace.', ifThen: 'If a student gets frustrated and tears their note, then respond neutrally: “Paper can rip. Let’s get a fresh one. Settle first.”', img: [ICON.star('Draw a hand-star')] },
          transition: { teacher: '“Bring your calm hands with you to your seats. Stand on the one.”', student: 'Stands instantly and transitions to their seats without vocalization.', ifThen: 'If chatting starts, then callback the trace: “Trace your index finger once… let’s sit in silence and begin.”', img: [ICON.wave()] }
        }
      },
      '35': {
        focus: 'Calm-Down Sound Anchor',
        iCan: 'I can use a calming sound to stretch my exhale and quiet my brain’s smoke detector.',
        somaticGoal: 'Use a calming auditory anchor to extend exhalations and settle hyperaroused brain activity (amygdala).',
        somatic: 'Play a short calming, kid-friendly clip (soft music or nature sounds — see the linked clip). Close eyes and listen, letting each exhale grow longer as the sound plays. When it ends, raise a hand and notice how your body feels.',
        phases: {
          regulate: { teacher: '“Close your eyes. Listen to our calming sound. Let each breath out grow longer than the one before. Inhale rise… exhale slow.”', student: 'Sits in calm silence, listening to the clip with eyes closed.', ifThen: 'If a student is sensitive to the sound, then lower the volume or let them focus on breathing sways instead.' },
          orient: { teacher: '“Our value is Safe. A calming sound is our anchor. When we focus on it, we quiet our brain’s smoke detector.”', student: 'Looks at the brain diagram on the board showing the Amygdala.', ifThen: 'If students are hyperactive or talkative, then sit in silence for a moment before the clip. Let the quiet co-regulate first.' },
          connect: { teacher: '“With your partner, share: what helped you stay focused on the sound? ‘The [music / quiet / slow beat] helped me stay anchored.’”', student: 'Discusses sensory-motor focus strategies with a circle partner.', ifThen: 'If they drop the sentence frame, then pause and re-model: “Great thought — let’s lock it into the frame.”' },
          practice: { teacher: '“Now we breathe with the sound. Inhale as it rises, and stretch a long, quiet exhale as it fades. No talking—just breath.”', student: 'Matches slow breathing to the rise and fall of the calming clip.', ifThen: 'If breathing turns into silly noises, then stop: “My bad, I didn’t model the quiet breath. Stop. Settle. Slow exhale with me. Go.”' },
          commit: { teacher: '“Write on a sticky note: ‘Today I will stay in my Window of Tolerance by…’ and post it on our circle board.”', student: 'Writes a specific commitment incorporating a breathing or listening anchor.', ifThen: 'If short on time, then skip writing and do a verbal circle commitment to preserve pacing and transition.' },
          transition: { teacher: '“Move silently, like the last of our calming sound fading out. Stand on the one.”', student: 'Stands and transitions silently, carrying a calm physical posture.', ifThen: 'If clattering or noise occurs, then callback the sound: “Just like the sound faded to quiet… let’s move in silence. Ready.”' }
        }
      },
      '68': {
        focus: 'Box Breathing',
        iCan: 'I can use box breathing to slow my heart rate and calm my body when I feel stressed.',
        somaticGoal: 'Use a steady, even breathing pattern (box breathing) to calm the body and mind.',
        somatic: 'Trace a square in the air or on the desk. Breathe in for 4 as you trace up, hold for 4 across the top, breathe out for 4 down, hold for 4 across the bottom. Repeat four times.',
        phases: {
          regulate: { teacher: '“Let’s breathe in a square. Trace up—breathe in, 2, 3, 4. Hold across, 2, 3, 4. Down—breathe out, 2, 3, 4. Hold, 2, 3, 4.”', student: 'Traces the square and matches the breathing count.', ifThen: 'If students rush the count, then slow your own voice and trace slower. Keep it steady.' },
          orient: { teacher: '“Our value is Safe. Box breathing is a tool you can use anytime—before a test, after a conflict, or when your body feels too fast.”', student: 'Follows the box-breathing diagram on the board.', ifThen: 'If the room is high-energy, then add another round of breathing before moving on. Don’t rush.' },
          connect: { teacher: '“How did your body feel after box breathing? ‘After box breathing, my body felt ___ (steadier / calmer / slower).’ Share with a partner.”', student: 'Shares how their body felt using the sentence frame.', ifThen: 'If students joke about the frame, then reframe: “This is practice. Rehearsing it now makes it real later. Use the frame.”' },
          practice: { teacher: '“Let’s do one more round on our own. Place a hand on your chest and feel your breathing slow down.”', student: 'Runs one round of box breathing independently, hand on chest.', ifThen: 'If students get restless, then shorten to two rounds and keep the pace calm.' },
          commit: { teacher: '“On your card, write: ‘I will use box breathing when I ___.’ Name a real moment today.”', student: 'Writes a specific moment when they will use box breathing.', ifThen: 'If a student writes a joke, then hand a fresh card: “We own our commitments here. Settle and write a real one.”' },
          transition: { teacher: '“Bring that calm with you. Stand on the one.”', student: 'Stands and moves calmly and quietly on the cue.', ifThen: 'If the transition is loud, then reset: “Reset—too much noise. Stand on the one. Move calm. Go.”' }
        }
      }
    }
  },
  // ============================ DAY 3 ============================
  {
    day: 3,
    date: 'Wednesday, September 2, 2026',
    step: 'Cultural Wisdom & Shared Stories',
    value: 'Respectful',
    summary: 'Settle the social-emotional nervous system and build relational capital through respect.',
    bands: {
      k2: {
        focus: 'The Kindness Echo',
        iCan: 'I can send a kind echo and show respect so everyone knows they belong in our circle.',
        somaticGoal: 'Settle the social-emotional nervous system through the vocal resonance of warm, rhythmic peer affirmations.',
        somatic: 'Place the right hand over the chest to feel the heartbeat. Turn the chin to the left and take a deep breath, then to the right and exhale. Model a warm, relaxed facial expression.',
        phases: {
          regulate: { teacher: '“Hand on your heart. Breathe in warm feelings… breathe out kind words. Feel your heart beat in your chest.”', student: 'Keeps a hand on the chest, sways gently side-to-side, stabilizing breath.', ifThen: 'If a student is poking a neighbor, then use a non-verbal prompt. Separate seats quietly without a verbal lecture.', img: [ICON.heart()] },
          orient: { teacher: '“At Matchbook, we are Respectful. Respectful means protecting dignity and voice. Today we practice ‘The Kindness Echo.’”', student: 'Listens to the definition of Respectful: protecting our classroom’s shared voice.', ifThen: 'If a student mimics or laughs, then reframe neutrally: “Dignity means our words make others feel strong. Let’s practice that.”', img: [ICON.hearts()] },
          connect: { teacher: '“I will whisper a kind word to Partner A. Partner A echoes it to Partner B. Echo around: ‘You belong in our circle.’”', student: 'Whispers the kind echo to a peer, using passing gestures.', ifThen: 'If a student is selectively mute or highly anxious, then allow them to pass a gentle thumbs-up echo instead.', img: [ICON.speak('You belong')] },
          practice: { teacher: '“Let’s practice the Respectful Look. Eyes to shoes, now slow eyes to your partner. Soft smile. Turn your shoulders. Echo.”', student: 'Practices turning shoulders fully and making brief, comfortable eye contact.', ifThen: 'If a student turns completely away, then do not force contact. Invite them to look at the partner’s hands or shoulder instead.', img: [ICON.shake('Turn to your partner')] },
          commit: { teacher: '“Today, I commit to being Respectful by… whisper your kind commitment to our echo partner.”', student: 'Whispers a commitment: “I will use kind words when someone drops their pencil.”', ifThen: 'If the commitment is too general, then guide: “What is one kind word you can use today? Yes — ‘Thank you.’ Commit to that.”', img: [ICON.heart('Kind commitment')] },
          transition: { teacher: '“Take that respect with you. Stand on the one. Walk like a quiet helper. Go.”', student: 'Stands and transitions to their seats, carrying a posture of respect.', ifThen: 'If students clump or push, then reset the circle transition: “My bad, I didn’t guide the spacing. Let’s retry.”', img: [ICON.wave('Quiet helper')] }
        }
      },
      '35': {
        focus: 'The Perspective Lens',
        iCan: 'I can use a perspective lens and respectful bridging phrases to protect someone else’s experience.',
        somaticGoal: 'Settle interpersonal arousal and build limbic connection through perspective-taking.',
        somatic: 'Place hands on opposite shoulders, giving a gentle, reassuring squeeze. Breathe in through the nose, feel the squeeze, and let the shoulders drop on the exhale.',
        phases: {
          regulate: { teacher: '“Give yourself a gentle shoulder squeeze. Breathe in warmth… let your shoulders drop down… breathe out and let go.”', student: 'Performs the shoulder squeeze with steady breathing sways.', ifThen: 'If a student refuses to squeeze or seems resistant, then permit a hand-massage or silent posture instead. Avoid compliance struggles.' },
          orient: { teacher: '“At Matchbook, we are Respectful. Today we use our Perspective Lens to understand how we impact others’ experiences.”', student: 'Reads the “Three E’s” board (Event, Experience, Effect).', ifThen: 'If students struggle with the terminology, then clarify: “An event is what happened; an experience is how it made us feel.”' },
          connect: { teacher: '“Think of a time you felt respected by a classmate. ‘I felt respected when [name] did [action] because…’ Share.”', student: 'Shares positive, evidence-based peer respect stories using the talking piece.', ifThen: 'If peer conflict is brought up, then redirect: “We will resolve that privately. Right now, focus on times you felt safe.”' },
          practice: { teacher: '“Let’s practice the Perspective Frame. Turn to a partner and share an opinion. Partner B uses: ‘I hear your opinion, and…’”', student: 'Practices listening actively and using respectful bridging phrases.', ifThen: 'If an argument or bickering starts, then reset: “My bad, I didn’t clarify the listener’s job. Sit down. Try again. Settle.”' },
          commit: { teacher: '“Commit: ‘Today I will protect someone’s experience by…’ Write it on a toolkit card.”', student: 'Writes a specific perspective-taking commitment and posts it on the board.', ifThen: 'If the commitment is compliance-coded, then reframe: “Make it about empathy. ‘I will invite someone sitting alone to join me.’”' },
          transition: { teacher: '“Bring your respect into the day ahead. Stand on the one.”', student: 'Stands instantly and transitions cleanly to their seats.', ifThen: 'If chatting erupts during transition, then callback: “Just like we practiced. Respectful transition. Reset your voice.”' }
        }
      },
      '68': {
        focus: 'Perspective & Respect',
        iCan: 'I can take another person’s perspective and disagree respectfully without putting them down.',
        somaticGoal: 'Settle social stress and build connection by practicing perspective-taking and respectful disagreement.',
        somatic: 'Cross your arms and give your own shoulders a gentle squeeze. Breathe in, feel the squeeze, and let your shoulders drop as you breathe out.',
        phases: {
          regulate: { teacher: '“Cross your arms and give your shoulders a gentle squeeze. Breathe in… and let your shoulders drop as you breathe out. Reset your body.”', student: 'Does the shoulder squeeze with slow breathing.', ifThen: 'If a student won’t participate, then allow a still, quiet posture instead. Don’t force it.' },
          orient: { teacher: '“At Matchbook, we are Respectful. Respect means protecting someone’s dignity—even when we disagree. Today we practice seeing another perspective.”', student: 'Reads the respect frames on the board (Agree · Add on · Disagree).', ifThen: 'If students talk over each other, then reset: “Respect protects voice. One person at a time.”' },
          connect: { teacher: '“Think of a time a classmate showed you respect. ‘I felt respected when ___ because ___.’ Share with a partner.”', student: 'Shares a real example of feeling respected using the frame.', ifThen: 'If a student brings up a conflict, then redirect: “We’ll handle that privately—right now, focus on times you felt respected.”' },
          practice: { teacher: '“Let’s practice respectful disagreement. Partner A shares an opinion. Partner B replies: ‘I hear you, and I see it differently because…’ Keep your tone level.”', student: 'Practices disagreeing respectfully with the sentence frame and a calm tone.', ifThen: 'If it turns into an argument, then reset: “My bad, I didn’t set the listener’s job. Level tone. Try again.”' },
          commit: { teacher: '“On your card, finish: ‘Today I will show respect by ___.’ Make it something you can actually do.”', student: 'Writes a specific, doable respect commitment.', ifThen: 'If it’s vague, then reframe: “Make it real—‘I’ll invite someone sitting alone to join us.’ Commit to that.”' },
          transition: { teacher: '“Take your respect into the day. Stand on the one.”', student: 'Stands and transitions calmly and quietly on the cue.', ifThen: 'If running occurs, then a Warm Demander cue: “Assigned seats, then we begin. Settle.”' }
        }
      }
    }
  },
  // ============================ DAY 4 ============================
  {
    day: 4,
    date: 'Thursday, September 3, 2026',
    step: 'Daily Intention Setting',
    value: 'Responsible',
    summary: 'Restore agency and own the next step by choosing a tool and a specific, observable intention.',
    bands: {
      k2: {
        focus: 'My Learning Superpowers',
        iCan: 'I can choose a Learning Superpower and be Responsible for my next step today.',
        somaticGoal: 'Use visual choices and gross-motor movements to restore personal agency and reduce learned helplessness under stress.',
        somatic: '“Grounding Roots Stretch.” Stretch hands all the way up like tall trees reaching for the sun, take a deep breath, then exhale and press both feet flat into the carpet.',
        phases: {
          regulate: { teacher: '“Stand tall. Reach for the sky… breathe in. Melt your hands down, press your roots into the floor… breathe out. Melt.”', student: 'Performs the grounding roots stretch, focusing on balance and weight.', ifThen: 'If a student is jumping or falling over, then modify: “Sit down and press your hands flat into the floor like deep roots.”', img: [ICON.tree()] },
          orient: { teacher: '“At Matchbook, we are Responsible. Responsible means owning our next step. Today we choose our Learning Superpower.”', student: 'Looks at the visual superpower chart (Listening Ears, Helping Hands, Calm Breathing).', ifThen: 'If a student is distracted by materials, then use a quiet proximity cue. Gently guide focus back to the visual chart.', img: [ICON.ear(), ICON.shake('Helping hands'), ICON.lotus()] },
          connect: { teacher: '“Select your superpower. Point to the board: ‘My superpower is [Ears / Hands / Breathing].’ Tell your circle partner.”', student: 'Points to a visual selection, sharing their chosen daily focus.', ifThen: 'If a student cannot choose or shuts down, then provide a simplified choice of two: “Hands or breathing?”', img: [ICON.star('My superpower')] },
          practice: { teacher: '“Let’s practice using our superpower. If we make a mistake, we say: ‘My bad, I’ll fix it.’ Rehearse that in a calm tone.”', student: 'Practices saying “My bad, I’ll fix it” with a neutral facial expression.', ifThen: 'If the tone is sarcastic, then call it out gently: “The words are right, but the tone is silliness. Let’s make it calm and neutral.”', img: [ICON.lotus('Calm reset')] },
          commit: { teacher: '“Draw your superpower symbol on your commitment sheet. Hold it up to commit to yourself.”', student: 'Draws a symbol of ears, hands, or spiral breath, showing the circle.', ifThen: 'If drawing is delayed, then allow a verbal commitment or a pre-made sticker to preserve time and reduce anxiety.', img: [ICON.star('Draw your symbol')] },
          transition: { teacher: '“Let’s take our superpowers into our day. Stand on the one. Melt to your seats.”', student: 'Moves silently to their seats on the call-and-response cue.', ifThen: 'If transition takes >60 seconds, then do not interrupt academics now. Note the transition speed for tomorrow’s practice.', img: [ICON.tree('Grounded steps')] }
        }
      },
      '35': {
        focus: 'Pothole Filling & Intention',
        iCan: 'I can name a “pothole” shrinking my window and choose a tool to fill it today.',
        somaticGoal: 'Mitigate toxic-stress spikes by mapping physical states to actionable self-care needs (sleep, hunger, sensory input).',
        somatic: '“5-Senses Grounding Tool.” Sit flat. Find 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste.',
        phases: {
          regulate: { teacher: '“Ground your feet. Let’s do our 5-senses check. Find 5 things you can see… 4 you can touch… breathe and stay present.”', student: 'Practices 5-senses sensory grounding, anchoring attention.', ifThen: 'If students get distracted or silly, then guide focus directly: “Touch your desk. Feel the cold wood. Breathe. Focus.”' },
          orient: { teacher: '“At Matchbook, we are Responsible. Today we talk about ‘Pothole Filling’—how sleep, food, and quiet time expand our window.”', student: 'Looks at the “Pothole Filling” poster showing sleep and nutrition.', ifThen: 'If a student mentions high family stress or hunger, then respond with warm empathy. Route them privately to support services.' },
          connect: { teacher: '“What is a ‘pothole’ shrinking your Window of Tolerance today? ‘My window is small today because [lack of sleep / hunger].’”', student: 'Identifies personal stressors and shares with a partner using the frame.', ifThen: 'If selectively mute or anxious, then permit a visual check-in: “Draw a pothole on your card and slide it to me.”' },
          practice: { teacher: '“Let’s practice choosing a tool to fill the pothole. If tired, I will stretch. If restless, I will do a fist-squeeze. Go.”', student: 'Rehearses selecting and applying somatic tools from the coping toolkit.', ifThen: 'If students make wild movements, then do-over: “Pause. Somatic tools are quiet and controlled. Let’s practice fist-squeezes again.”' },
          commit: { teacher: '“Write your pothole commitment: ‘If my window shrinks, I will use [tool].’ Post it on your desk.”', student: 'Writes an observable commitment and tapes it to their desk space.', ifThen: 'If the commitment is vague, then prompt: “Be specific. Which exact tool from your toolkit will you use?”' },
          transition: { teacher: '“Fill your last pothole. Walk like a quiet investigator to your seats. Stand on the one.”', student: 'Stands and walks smoothly, avoiding physical contact or chatter.', ifThen: 'If clattering or shouting occurs, then callback the grounding cue: “Stop. Feel your feet. Settle your pulse. Take your seats.”' }
        }
      },
      '68': {
        focus: 'Know Your Needs, Own Your Next Step',
        iCan: 'I can name what’s draining my focus and choose a tool and a next step to stay on track.',
        somaticGoal: 'Notice what is affecting focus — sleep, hunger, stress — and choose a tool plus a specific next step.',
        somatic: 'Do a quick 5-senses reset. Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you can taste. Then take one slow breath.',
        phases: {
          regulate: { teacher: '“Let’s ground with our senses. Name 5 things you see… 4 you can touch… 3 you hear. Breathe and come back to right now.”', student: 'Runs the 5-senses reset, anchoring attention to the present.', ifThen: 'If students get silly, then guide directly: “Hands on your desk. Feel it. Breathe. Focus.”' },
          orient: { teacher: '“At Matchbook, we are Responsible. Responsible means owning your next step—even on a hard day. First, know what’s draining your focus.”', student: 'Reads the “What’s draining my focus?” list (sleep, food, stress, conflict).', ifThen: 'If a student mentions hunger or a hard home situation, then respond with warmth and route them privately to support.' },
          connect: { teacher: '“What’s one thing draining your focus today? ‘My focus is low today because ___.’ Share with a partner.”', student: 'Names a personal drain on focus using the sentence frame.', ifThen: 'If a student is quiet or anxious, then let them write it on a card and hand it to you instead.' },
          practice: { teacher: '“Now pick a tool. If you’re tired, stretch. If you’re restless, box breathe. If you’re stuck, break the task into one small step. Rehearse your pick.”', student: 'Chooses and rehearses a specific tool from their toolkit.', ifThen: 'If students go big or loud, then redo: “Tools are calm and controlled. Try again.”' },
          commit: { teacher: '“On your card, write: ‘Today I will own my next step by ___.’ Name one small, real win.”', student: 'Writes a specific, doable next-step commitment.', ifThen: 'If too general, then prompt: “Name the exact win—finish the first task? Commit to that.”' },
          transition: { teacher: '“Take your next step into the day. Stand on the one.”', student: 'Stands and transitions calmly and quietly on the cue.', ifThen: 'If students clump or chat, then a quiet hand cue. No power struggle—transition cleanly.' }
        }
      }
    }
  }
];
