export const unitMeta = {
  title: 'Bullying Prevention Unit',
  subtitle: 'Five Morning Meetings. One shared language for safety, action, and repair.',
  duration: '15 minutes',
  dates: 'August 11 and August 17–20, 2026',
  friday: 'Friday, August 21, 2026 · Friday Cypher application and celebration',
  sources: [
    {
      label: 'Indiana Department of Education · Student Safety/Bullying Reporting',
      url: 'https://www.in.gov/doe/students/school-safety-and-wellness/student-safetybullying-reporting/'
    },
    {
      label: 'StopBullying.gov · What Is Bullying',
      url: 'https://www.stopbullying.gov/bullying/what-is-bullying'
    },
    {
      label: 'StopBullying.gov · What Is Cyberbullying',
      url: 'https://www.stopbullying.gov/cyberbullying/what-is-it'
    }
  ]
};

export const bands = {
  k2: { label: 'Grades K–2', short: 'K–2', code: 'k2' },
  '35': { label: 'Grades 3–5', short: '3–5', code: '35' },
  '68': { label: 'Grades 6–8', short: '6–8', code: '68' }
};

const common = {
  disclosure: 'If a student shares a current concern, thank the student, protect privacy, do not investigate in front of peers, and follow the Matchbook Bullying Response Protocol the same day.',
  determination: 'Students report what they noticed; trained adults determine whether the facts meet the formal definition of bullying. A one-time harmful or dangerous act still matters and must be addressed.',
  repair: 'Never require the student who was harmed to accept an apology, meet with the other student, or participate in a repair conversation before safety and readiness are established.'
};

export const lessons = [
  {
    day: 1,
    date: 'Tuesday, August 11, 2026',
    weeklyMove: 'Pre-Unit Launch',
    focus: 'Name It',
    values: 'Safe',
    practiceMove: 'Notice the difference: accident, conflict, or possible bullying.',
    bands: {
      k2: {
        iCan: 'I can name what bullying may look like and know it is never okay.',
        vocabulary: ['accident', 'problem', 'bullying', 'on purpose', 'again and again', 'safe'],
        materials: ['Three scenario cards or puppets', 'Accident / Conflict / Possible Bullying signs', 'Class safety chart'],
        greeting: {
          name: 'Kindness Wave',
          student: 'Wave to a neighbor: “Good morning, [name]. I am glad you are here.”',
          teacher: 'Model first. Make sure every child is greeted by name; quietly pair anyone without a partner.'
        },
        sharing: {
          prompt: 'Show a face for kind. Show a face for unkind. What changes in your body?',
          frame: 'I feel ___ when someone is kind or unkind.',
          teacher: 'Accept a face, gesture, or one-word answer. Do not invite personal disclosures in the full group.'
        },
        teach: {
          title: 'Three clues adults listen for',
          cards: [
            ['Power', 'One person has more size, popularity, information, access, or control.'],
            ['Pattern', 'It happens again and again—or looks likely to keep happening.'],
            ['Harm', 'The behavior is unwanted and hurts, scares, humiliates, or excludes.']
          ]
        },
        activity: {
          directions: 'Hold up 1 for accident, 2 for conflict/problem, or 3 for possible bullying. Then name the clue you noticed.',
          scenarios: [
            { title: 'A bump', text: 'A classmate bumps your block tower by accident, says sorry, and helps rebuild it.', choices: ['Accident', 'Conflict', 'Possible bullying'], answer: 'Accident—the harm was not on purpose and the student repaired it.' },
            { title: 'One ball', text: 'Two classmates both want the same ball. They argue one time and both keep trying to get it.', choices: ['Accident', 'Conflict', 'Possible bullying'], answer: 'Conflict—both students have similar power and are part of the problem.' },
            { title: 'Every snack time', text: 'The same student takes another child’s snack every day, laughs, and will not stop when asked.', choices: ['Accident', 'Conflict', 'Possible bullying'], answer: 'Possible bullying—there is a pattern, harm, and possible unfair power. Tell an adult.' }
          ]
        },
        message: {
          statement: 'Bullying may be hurtful behavior with unfair power, a pattern, and harm. It is never okay.',
          commitment: 'If I am hurt, worried, or unsure, I will tell a trusted adult.',
          preview: 'Next: four ways bullying can happen.',
          teacher: 'Read once; students echo. Add the class commitment to the safety chart.'
        },
        guardrail: common.determination,
        lookFor: 'Students sort without naming real classmates and can say “tell an adult” when unsure.'
      },
      '35': {
        iCan: 'I can explain the difference between conflict and possible bullying.',
        vocabulary: ['bullying', 'conflict', 'power imbalance', 'pattern', 'unwanted', 'impact'],
        materials: ['Scenario cards', 'Accident / Conflict / Possible Bullying T-chart', 'Power + Pattern + Harm anchor chart'],
        greeting: {
          name: 'Name and Nod',
          student: 'Greet three classmates by name with a nod or another mutually comfortable greeting.',
          teacher: 'Name consent: a nod, wave, fist bump, or words all count. No forced touch.'
        },
        sharing: {
          prompt: 'What is one difference between a disagreement and bullying?',
          frame: 'A disagreement is ___. Possible bullying includes ___.',
          teacher: 'Invite two partner responses. Do not ask students to identify real peers.'
        },
        teach: {
          title: 'Power + Pattern + Harm',
          cards: [
            ['Power', 'A real or perceived advantage—strength, popularity, information, identity, group size, or access.'],
            ['Pattern', 'Repeated behavior or behavior likely to be repeated.'],
            ['Harm', 'Unwanted behavior that hurts, scares, humiliates, intimidates, or excludes.']
          ]
        },
        activity: {
          directions: 'Sort each situation. Defend the choice with evidence, not a label for a person.',
          scenarios: [
            { title: 'Group project', text: 'Two friends disagree once about who should present. Both interrupt and then ask the teacher for help.', choices: ['Conflict', 'Possible bullying', 'Need more information'], answer: 'Conflict—roughly equal power, one event, and both participate.' },
            { title: 'Lunch table', text: 'A popular group repeatedly tells one student the table is “full,” then posts jokes about the student in a group chat.', choices: ['Conflict', 'Possible bullying', 'Need more information'], answer: 'Possible bullying—social power, repeated exclusion, and harm are present.' },
            { title: 'Mean comment', text: 'A student insults a classmate once after losing a game.', choices: ['Conflict/misconduct', 'Possible bullying', 'Ignore it'], answer: 'It may not meet the bullying definition yet, but it is harmful behavior and still requires an adult response.' }
          ]
        },
        message: {
          statement: 'Bullying involves unfair power, a pattern or likely pattern, and unwanted harm.',
          commitment: 'I will report the facts when I see power, pattern, or harm—or when I am unsure.',
          preview: 'Next: physical, verbal, social, and cyberbullying.',
          teacher: 'Students read the definition together. Underline “possible”: adults investigate and determine.'
        },
        guardrail: common.determination,
        lookFor: 'Students cite evidence from the scenario and avoid treating every conflict as bullying.'
      },
      '68': {
        iCan: 'I can analyze power, pattern, and harm to distinguish conflict from possible bullying.',
        vocabulary: ['power imbalance', 'repetition', 'impact', 'unwanted aggression', 'relational', 'cyberbullying'],
        materials: ['Three realistic scenarios', 'Power + Pattern + Harm test', 'Individual response cards or paper'],
        greeting: {
          name: 'Status and Welcome',
          student: 'Greet a neighbor by name, then share a one-word status or pass.',
          teacher: 'Normalize “pass.” Keep the check-in moving; this is connection, not public processing.'
        },
        sharing: {
          prompt: 'Where is the line between drama, conflict, harassment, and possible bullying?',
          frame: 'The line changes when ___ because ___.',
          teacher: 'Take two brief responses. Say: “Labels are less useful than facts about power, pattern, and harm.”'
        },
        teach: {
          title: 'The three-test lens',
          cards: [
            ['Power', 'A real or perceived advantage: status, identity, numbers, strength, access, information, or technology.'],
            ['Pattern', 'Repeated—or likely to repeat because posts, shares, threats, or group dynamics keep the harm active.'],
            ['Harm', 'Unwanted aggression that intimidates, humiliates, isolates, controls, or causes physical or emotional harm.']
          ]
        },
        activity: {
          directions: 'Analyze privately first. Then discuss which facts are known, unknown, and important to report.',
          scenarios: [
            { title: '“Just jokes”', text: 'A student with social influence targets the same classmate’s accent each week. Others laugh. The classmate has asked them to stop.', choices: ['Conflict', 'Possible bullying', 'Need more information'], answer: 'Possible bullying—social power, pattern, unwanted harm, and identity-based targeting are present.' },
            { title: 'Private post, public impact', text: 'An embarrassing image is shared once in a group chat, then repeatedly screenshotted and reposted by others.', choices: ['One-time event only', 'Possible bullying', 'Not school-related'], answer: 'Possible cyberbullying—the repeated circulation can keep the harm active. Save evidence privately; do not reshare.' },
            { title: 'Argument', text: 'Two students with similar social power trade insults during one argument and both later stop.', choices: ['Conflict/misconduct', 'Possible bullying', 'Ignore it'], answer: 'Likely conflict or misconduct, not enough evidence of a power imbalance or pattern. It still needs repair and may need an adult response.' }
          ]
        },
        message: {
          statement: 'Impact and evidence matter more than “I was joking.” You do not need to prove the case before reporting it.',
          commitment: 'I will report facts about power, pattern, and harm and let adults investigate.',
          preview: 'Next: the four kinds of bullying and how they overlap.',
          teacher: 'Hold the line on dignity without publicly debating whether a named student is a bully.'
        },
        guardrail: common.determination + ' Watch closely for identity-based targeting and sexual harassment; route those concerns through the appropriate school protocol as well.',
        lookFor: 'Students distinguish facts from assumptions and understand that digital repetition can extend impact.'
      }
    }
  },
  {
    day: 2,
    date: 'Monday, August 17, 2026',
    weeklyMove: 'Launch',
    focus: 'Know It',
    values: 'Safe + Respectful',
    practiceMove: 'Name the behavior without labeling the person.',
    bands: {
      k2: {
        iCan: 'I can name four ways bullying may happen.',
        vocabulary: ['physical', 'verbal', 'social', 'online', 'safe'],
        materials: ['Four kinds cards', 'Picture scenario cards', 'Four-corner signs'],
        greeting: { name: 'Safe Hello', student: 'Say a classmate’s name and choose a wave, nod, or air high-five.', teacher: 'Model choice and consent. Every student receives a greeting.' },
        sharing: { prompt: 'Where can hurt show up—on a body, in feelings, in a friendship, or on a screen?', frame: 'Hurt can show up ___.', teacher: 'Students may point to one of four posted pictures instead of speaking.' },
        teach: { title: 'Four ways harm can happen', cards: [['Physical', 'Hitting, pushing, taking, or damaging things.'], ['Verbal', 'Threats, cruel names, or hurtful words.'], ['Social', 'Repeatedly leaving someone out or spreading rumors.'], ['Cyber', 'Harmful messages, pictures, posts, or game/chat behavior.']] },
        activity: { directions: 'Point to or move toward the kind that best matches. Some examples may fit more than one.', scenarios: [
          { title: 'On the playground', text: 'A student keeps pushing the same child away from the swings.', choices: ['Physical', 'Verbal', 'Social', 'Cyber'], answer: 'Physical, and possibly social if the pushing is used to exclude.' },
          { title: 'At lunch', text: 'A group repeatedly whispers that no one should sit with one child.', choices: ['Physical', 'Verbal', 'Social', 'Cyber'], answer: 'Social and verbal.' },
          { title: 'On a tablet', text: 'Someone sends the same scary message in a game chat every day.', choices: ['Physical', 'Verbal', 'Social', 'Cyber'], answer: 'Cyber and verbal.' }
        ] },
        message: { statement: 'Harm can happen to bodies, through words, inside friendships, or on screens.', commitment: 'I will name what happened and tell an adult.', preview: 'Tomorrow: safe ways to be an upstander.', teacher: 'Choral read; students show one finger for “name it” and two for “tell.”' },
        guardrail: common.disclosure,
        lookFor: 'Students can identify the four kinds and understand that one situation can overlap categories.'
      },
      '35': {
        iCan: 'I can identify physical, verbal, social, and cyberbullying and explain how they overlap.',
        vocabulary: ['physical', 'verbal', 'social/relational', 'cyber', 'exclusion', 'rumor'],
        materials: ['Four kinds poster', 'Scenario strips', 'Category cards'],
        greeting: { name: 'Four Greetings', student: 'Greet four classmates—one each with a wave, nod, kind word, or air high-five.', teacher: 'Keep movement calm and make all touch optional.' },
        sharing: { prompt: 'Which kinds of harm are easiest to see? Which are easier to hide?', frame: '___ is easier/harder to notice because ___.', teacher: 'Invite partners to compare responses; do not ask for personal examples.' },
        teach: { title: 'Four categories—not four separate boxes', cards: [['Physical', 'Actions against a body or property.'], ['Verbal', 'Spoken or written threats, insults, slurs, or cruel teasing.'], ['Social', 'Rumors, exclusion, humiliation, or damaging relationships/status.'], ['Cyber', 'Digital messages, posts, images, games, accounts, or group chats used to harm.']] },
        activity: { directions: 'Assign every category that fits. Then check for power, pattern, and harm.', scenarios: [
          { title: 'Fake account', text: 'Students make a fake account for a classmate and post embarrassing statements in the classmate’s name.', choices: ['Physical', 'Verbal', 'Social', 'Cyber'], answer: 'Cyber, social, and verbal can overlap.' },
          { title: 'Backpack', text: 'A larger student repeatedly grabs a smaller student’s backpack and dumps it out while others laugh.', choices: ['Physical', 'Verbal', 'Social', 'Cyber'], answer: 'Physical and social harm; the size and audience may add power.' },
          { title: 'Rumor chain', text: 'A rumor is whispered at school and then repeated in a group chat.', choices: ['Physical', 'Verbal', 'Social', 'Cyber'], answer: 'Verbal, social, and cyber.' }
        ] },
        message: { statement: 'The four kinds can overlap. Name the actions, then report the facts.', commitment: 'I will notice hidden social and online harm—not only physical harm.', preview: 'Tomorrow: move from bystander to upstander.', teacher: 'Ask the class to name one category and one fact from the final scenario.' },
        guardrail: common.disclosure,
        lookFor: 'Students explain overlap and use action words rather than calling a peer “a bully.”'
      },
      '68': {
        iCan: 'I can analyze physical, verbal, relational, and cyberbullying—including less visible overlap.',
        vocabulary: ['physical', 'verbal', 'relational', 'cyber', 'dogpiling', 'impersonation', 'exclusion'],
        materials: ['Four-category continuum', 'Scenario analysis cards', 'Private response slips'],
        greeting: { name: 'Connect by Choice', student: 'Greet two classmates by name using words or a non-contact signal.', teacher: 'Make the greeting brief and authentic; do not police eye contact.' },
        sharing: { prompt: 'Why can relational and cyber harm be harder for adults to notice?', frame: 'It can stay hidden when ___, so adults need ___.', teacher: 'Collect two responses that point toward evidence and reporting.' },
        teach: { title: 'Four forms can stack', cards: [['Physical', 'Force, restraint, threats of force, property damage, or repeated physical intimidation.'], ['Verbal', 'Threats, humiliation, slurs, degrading comments, or repeated targeted “jokes.”'], ['Relational', 'Exclusion, rumor campaigns, status manipulation, coercion, or group isolation.'], ['Cyber', 'Posts, DMs, images, group chats, gaming, impersonation, or repeated sharing that extends harm.']] },
        activity: { directions: 'Mark all forms present, then identify what evidence should be reported or saved privately.', scenarios: [
          { title: 'Dogpile', text: 'One student posts a humiliating clip. Several others add insults and tag more people to join.', choices: ['Verbal', 'Relational', 'Cyber', 'All three'], answer: 'All three. Reposting and tagging can extend the pattern. Save evidence; do not amplify it.' },
          { title: 'Access as power', text: 'A team captain threatens to exclude a classmate from practice unless the classmate shares homework answers.', choices: ['Physical', 'Verbal', 'Relational', 'Cyber'], answer: 'Verbal and relational; role-based access creates a power imbalance.' },
          { title: 'Hallway + group chat', text: 'A student is shoved at school, then mocked in the class group chat for reacting.', choices: ['Physical', 'Verbal', 'Relational', 'Cyber'], answer: 'All four may be present.' }
        ] },
        message: { statement: 'Visible and hidden harm both count. Save evidence privately; never repost it to prove a point.', commitment: 'I will name the behavior, protect the evidence, and report without amplifying the harm.', preview: 'Tomorrow: safe upstander moves.', teacher: 'Clarify that students should not put themselves in danger or record a dangerous confrontation.' },
        guardrail: common.disclosure + ' For explicit images or sexual content, do not ask students to forward the material; follow school safeguarding procedures immediately.',
        lookFor: 'Students recognize relational power and understand the difference between preserving evidence and resharing harm.'
      }
    }
  },
  {
    day: 3,
    date: 'Tuesday, August 18, 2026',
    weeklyMove: 'Practice',
    focus: 'Upstander, Not Bystander',
    values: 'Respectful + Responsible',
    practiceMove: 'Choose the safest helpful action: interrupt, support, or report.',
    bands: {
      k2: {
        iCan: 'I can help safely when someone is being hurt.',
        vocabulary: ['bystander', 'upstander', 'support', 'tell', 'safe'],
        materials: ['Stop / Support / Tell cards', 'Puppet or role-play cards'],
        greeting: { name: 'Help Is Here', student: 'Greet a classmate: “Good morning, [name]. You belong here.”', teacher: 'Model a warm voice; students may echo if the full sentence is difficult.' },
        sharing: { prompt: 'What helps a person feel less alone?', frame: 'I can help by ___.', teacher: 'Gather quick, safe ideas: stand nearby, invite, get an adult, use kind words.' },
        teach: { title: 'Three safe upstander moves', cards: [['Stop', 'If it feels safe, use a clear voice: “Stop. That is not okay.”'], ['Support', 'Stand with the person, invite them with you, or say something kind.'], ['Tell', 'Get a trusted adult right away. Keep telling until someone helps.']] },
        activity: { directions: 'Practice one safe move with a puppet. Students may say the words, point to a card, or ask an adult to act.', scenarios: [
          { title: 'No seat for you', text: 'A child is repeatedly told they cannot sit with the group.', choices: ['Stop', 'Support', 'Tell'], answer: 'Support by inviting the child; tell an adult about the repeated exclusion.' },
          { title: 'Pushing', text: 'A child is being pushed and looks scared.', choices: ['Step between them', 'Get an adult', 'Cheer'], answer: 'Get an adult. Do not put your body in danger.' },
          { title: 'Mean game chat', text: 'A classmate says someone keeps sending mean messages in a game.', choices: ['Send mean words back', 'Support and tell', 'Ignore'], answer: 'Support the classmate and tell a trusted adult.' }
        ] },
        message: { statement: 'An upstander helps without making the danger bigger.', commitment: 'I can stop safely, support the person, or tell an adult.', preview: 'Tomorrow: how to make a clear report.', teacher: 'Students show the Stop, Support, or Tell hand signal as they echo.' },
        guardrail: 'Never direct a child to physically intervene. Praise getting adult help as an active upstander move.',
        lookFor: 'Students choose adult help for physical danger and can name at least one support move.'
      },
      '35': {
        iCan: 'I can choose a safe upstander move when I witness possible bullying.',
        vocabulary: ['bystander', 'upstander', 'interrupt', 'redirect', 'support', 'report'],
        materials: ['Upstander choice card', 'Role-play scenarios', 'Observer feedback stems'],
        greeting: { name: 'You Belong', student: 'Greet a peer by name and finish: “I’m glad you are part of our class.”', teacher: 'Keep it sincere and quick; offer the shorter option “Good morning, [name].”' },
        sharing: { prompt: 'What can make it hard to help when other people are watching?', frame: 'It can be hard because ___. A safe first step is ___.', teacher: 'Normalize fear without excusing harm; pivot toward small, doable actions.' },
        teach: { title: 'The 3S upstander plan', cards: [['Speak or redirect', 'If safe: “That’s not okay.” Change the subject, interrupt the audience, or invite the person away.'], ['Support', 'Check in privately, sit beside the person, include them, and avoid blaming.'], ['Send for help', 'Report to a trusted adult. For danger, get help immediately instead of stepping in.']] },
        activity: { directions: 'Partners choose a move, role-play for 20 seconds, and receive feedback: safe, specific, helpful.', scenarios: [
          { title: 'Recess exclusion', text: 'A group repeatedly blocks one student from joining and laughs when the student asks why.', choices: ['Speak/redirect', 'Support', 'Send for help'], answer: 'Any safe combination can work: invite the student, name the exclusion, and report the pattern.' },
          { title: 'Threat', text: 'A student threatens to hit someone after school.', choices: ['Confront alone', 'Send for help now', 'Wait and see'], answer: 'Send for adult help immediately; do not confront alone.' },
          { title: 'Group chat', text: 'A humiliating meme about a classmate is being passed around.', choices: ['Add a laughing emoji', 'Save privately and report', 'Forward as proof'], answer: 'Do not react or forward. Preserve evidence privately if safe, support the classmate, and report.' }
        ] },
        message: { statement: 'Upstanders do not need to be heroes. They choose the safest helpful next step.', commitment: 'Today I will interrupt safely, support someone, or send for help.', preview: 'Tomorrow: reporting clearly and bravely.', teacher: 'Ask students to point to the move they are most ready to use.' },
        guardrail: 'Do not reward risky confrontation. Help-seeking, redirecting the audience, and private support are strong upstander actions.',
        lookFor: 'Students match the level of risk to the response and avoid resharing digital harm.'
      },
      '68': {
        iCan: 'I can select an upstander strategy that reduces harm without increasing risk.',
        vocabulary: ['upstander', 'de-escalate', 'redirect', 'document', 'amplify', 'retaliation'],
        materials: ['Strategy menu', 'Scenario cards', 'Safe/helpful feedback rubric'],
        greeting: { name: 'Belonging Signal', student: 'Greet a neighbor by name and offer a brief belonging statement or a simple “good morning.”', teacher: 'Model natural language; avoid making authenticity feel scripted.' },
        sharing: { prompt: 'Why might someone freeze, laugh along, or stay silent even when they know harm is happening?', frame: 'A bystander may ___. An upstander can start by ___.', teacher: 'Name audience pressure, fear, status, uncertainty, and digital permanence without shaming.' },
        teach: { title: 'Five options—choose for safety', cards: [['Interrupt', 'Name the behavior only if it is safe.'], ['Redirect', 'Change the audience, topic, or location.'], ['Support', 'Check in privately and restore connection.'], ['Document', 'Preserve evidence privately; never repost or solicit more harm.'], ['Report', 'Give facts to an adult and escalate urgent threats immediately.']] },
        activity: { directions: 'Teams choose the lowest-risk effective response. Explain what the move protects and what it avoids.', scenarios: [
          { title: 'Cafeteria audience', text: 'A socially influential student humiliates a classmate while a crowd watches and records.', choices: ['Public debate', 'Redirect/support/report', 'Record too'], answer: 'Reduce the audience, support the targeted student, and get adult help. Do not add another recording.' },
          { title: 'Anonymous account', text: 'An account posts identity-based insults about students and asks followers to submit names.', choices: ['Investigate alone', 'Report with evidence', 'Quote-post it'], answer: 'Preserve URLs/screenshots privately and report. Do not amplify or try to expose the operator yourself.' },
          { title: 'Immediate danger', text: 'A student says they are going to attack a classmate after dismissal.', choices: ['Wait for proof', 'Report immediately', 'Message the target only'], answer: 'Report immediately to an adult. Support the target only if doing so does not delay the urgent report.' }
        ] },
        message: { statement: 'Effective upstanders reduce the audience, increase support, preserve evidence, and bring in help.', commitment: 'I will choose a move that is both safe and helpful—even when no one applauds it.', preview: 'Tomorrow: the exact words for a clear report.', teacher: 'Close by naming that freezing is a stress response; the commitment is about the next available action.' },
        guardrail: 'Never instruct students to investigate, confront a group alone, or circulate harmful content. Urgent threats bypass role-play and go directly to an adult.',
        lookFor: 'Students justify strategy based on safety, audience, urgency, and likelihood of retaliation.'
      }
    }
  },
  {
    day: 4,
    date: 'Wednesday, August 19, 2026',
    weeklyMove: 'Notice',
    focus: 'Speak Up',
    values: 'Responsible + Safe',
    practiceMove: 'Notice facts and report: who, what, when, where, pattern, safety now.',
    bands: {
      k2: {
        iCan: 'I can tell a trusted adult what happened and what help I need.',
        vocabulary: ['report', 'trusted adult', 'brave', 'safe', 'again'],
        materials: ['Trusted adult hand card', 'Puppet scenarios', 'Reporting sentence strip'],
        greeting: { name: 'Trusted Adult Welcome', student: 'Greet the teacher: “Good morning. I know I can ask for help.”', teacher: 'Answer each student: “Yes. I will listen and help.”' },
        sharing: { prompt: 'Who are adults at school who can help keep you safe?', frame: 'I can tell ___.', teacher: 'Name roles available at Matchbook without promising one specific person will always be present.' },
        teach: { title: 'A clear report', cards: [['Who', 'Who was hurt? Who did it? Who saw it?'], ['What', 'What happened? Use action words.'], ['When + Where', 'When and where did it happen?'], ['Again + Safe', 'Has it happened before? Do you feel safe right now?']] },
        activity: { directions: 'Use the sentence strip with a puppet. It is okay to point, draw, or ask for a quiet place to talk.', scenarios: [
          { title: 'Practice report', text: 'A puppet says: “The same child takes my snack at lunch every day.”', choices: ['I need to report possible bullying.', 'It happened at lunch.', 'It keeps happening.', 'I need help staying safe.'], answer: 'Combine the facts: who, what, when/where, pattern, and safety need.' },
          { title: 'If the first adult is busy', text: 'You told one adult, but you still do not feel safe.', choices: ['Stop telling', 'Tell another trusted adult', 'Handle it alone'], answer: 'Tell another trusted adult and keep telling until someone helps.' }
        ] },
        message: { statement: 'Telling to keep someone safe is reporting. Reporting is brave.', commitment: 'I will say: “I need to report something. I need help staying safe.”', preview: 'Tomorrow: empathy, repair, and our class pledge.', teacher: 'Have students repeat the opening line once in a strong, calm voice.' },
        guardrail: common.disclosure + ' Never ask the child to tell the full story in front of classmates.',
        lookFor: 'Students can start the report and identify at least two trusted adults or roles.'
      },
      '35': {
        iCan: 'I can make a clear bullying report using facts and a safety need.',
        vocabulary: ['report', 'tattle', 'pattern', 'evidence', 'trusted adult', 'retaliation'],
        materials: ['Reporting card', 'Practice scenarios', 'Trusted adult map'],
        greeting: { name: 'Help Network', student: 'Greet a peer and name one school role students can ask for help.', teacher: 'Correct role names gently and add a backup option.' },
        sharing: { prompt: 'What makes reporting feel hard? What would help a student speak up?', frame: 'Reporting can feel hard when ___. It helps when adults ___.', teacher: 'Validate fear of being called a snitch; distinguish safety reporting from trying to cause trouble.' },
        teach: { title: 'Report the facts', cards: [['Start', '“I need to report possible bullying.”'], ['Who + What', 'Name people involved and the specific actions—not character labels.'], ['When + Where + Pattern', 'Say where, when, how often, and whether it may happen again.'], ['Safety + Evidence', 'Say what is needed now. Share evidence privately without forwarding it.']] },
        activity: { directions: 'Partner A reports. Partner B is the adult and asks only clarifying safety questions. Switch.', scenarios: [
          { title: 'Bus line', text: 'For three days, older students block a younger student from getting on the bus line and threaten to embarrass them online.', choices: ['Who/what', 'When/where', 'Pattern', 'Safety need'], answer: 'A strong report includes all four and asks for help before dismissal.' },
          { title: 'Group chat', text: 'A rumor is repeatedly posted about a classmate. You have a screenshot.', choices: ['Forward it widely', 'Show it privately to an adult', 'Delete and say nothing'], answer: 'Show the evidence privately to a trusted adult. Do not keep the rumor moving.' },
          { title: 'No response yet', text: 'You reported, but the behavior continues.', choices: ['Give up', 'Report again to another adult', 'Retaliate'], answer: 'Report again, name that it continues, and tell another trusted adult or administrator.' }
        ] },
        message: { statement: 'Tattling tries to create trouble. Reporting gives facts to get safety and help.', commitment: 'I will report who, what, when, where, the pattern, and what safety help is needed.', preview: 'Tomorrow: accountable repair and our pledge.', teacher: 'End with the whole class reading the six report elements.' },
        guardrail: common.disclosure,
        lookFor: 'Students use specific action words, state urgency, and understand they may tell another adult if harm continues.'
      },
      '68': {
        iCan: 'I can make a precise report that helps adults act without amplifying harm.',
        vocabulary: ['report', 'retaliation', 'documentation', 'confidentiality', 'pattern', 'immediate risk'],
        materials: ['Report framework', 'Scenario cards', 'Private written response option'],
        greeting: { name: 'Two-Adult Backup', student: 'Greet a neighbor, then silently identify one trusted adult and one backup adult.', teacher: 'Remind students that trusted adults are roles and relationships; no one has to announce names publicly.' },
        sharing: { prompt: 'What is the difference between spreading a story and reporting it?', frame: 'Reporting limits information to ___ so that ___.', teacher: 'Land on need-to-know adults, specific facts, safety, and no public reposting.' },
        teach: { title: 'The Matchbook report frame', cards: [['Open', '“I need to report possible bullying or harassment.”'], ['Facts', 'Who, what actions, when, where, witnesses—separate what you saw from what you heard.'], ['Pattern + Evidence', 'Frequency, prior reports, screenshots/links shown privately, and risk of repetition.'], ['Safety now', 'Immediate danger, retaliation concerns, and what support is needed today.']] },
        activity: { directions: 'Write a 30-second report. Partners check it for facts, pattern, evidence, and safety—not grammar.', scenarios: [
          { title: 'Identity-based targeting', text: 'A student receives repeated slurs in school and in DMs. Peers say it is “just their humor.”', choices: ['Facts', 'Pattern', 'Evidence', 'Safety/retaliation'], answer: 'Include all four. Identity-based harassment may require additional school civil-rights procedures.' },
          { title: 'Secondhand information', text: 'A friend tells you about threats you did not personally see.', choices: ['Pretend you saw it', 'Report what your friend said', 'Post for confirmation'], answer: 'Clearly distinguish secondhand information and report it; do not crowdsource proof.' },
          { title: 'Continued harm', text: 'A report was made, but the online targeting continues and students fear retaliation.', choices: ['Wait silently', 'Update another trusted adult/administrator', 'Retaliate anonymously'], answer: 'Update an adult promptly with new evidence and explicit retaliation concerns.' }
        ] },
        message: { statement: 'A strong report is specific, private, and clear about safety. Reporting is action—not gossip.', commitment: 'I will report facts, pattern, evidence, and immediate safety needs to an adult who can act.', preview: 'Tomorrow: repair, boundaries, and the class pledge.', teacher: 'Remind students: “You do not have to investigate or prove intent before you report.”' },
        guardrail: common.disclosure + ' Follow school protocols for identity-based harassment, sexual harassment, threats, or explicit content in addition to the bullying response pathway.',
        lookFor: 'Students separate firsthand/secondhand facts and state a clear safety or retaliation concern.'
      }
    }
  },
  {
    day: 5,
    date: 'Thursday, August 20, 2026',
    weeklyMove: 'Prepare',
    focus: 'Make It Right',
    values: 'Safe + Respectful + Responsible',
    practiceMove: 'Own harm, repair what can be repaired, change the pattern, and prepare evidence for the Cypher.',
    bands: {
      k2: {
        iCan: 'I can show care, make a repair, and help our class keep its promise.',
        vocabulary: ['empathy', 'repair', 'own it', 'change', 'promise'],
        materials: ['Repair steps cards', 'Class pledge chart', 'Markers or sticky notes'],
        greeting: { name: 'Appreciation Greeting', student: 'Greet a classmate: “Good morning, [name]. I noticed you ___.”', teacher: 'Offer concrete starters: helped, listened, shared, waited, included.' },
        sharing: { prompt: 'How can you tell when someone is ready to make things better?', frame: 'Repair sounds/looks like ___.', teacher: 'Accept actions as answers; clarify that “sorry” is a start, not the whole repair.' },
        teach: { title: 'Repair has four parts', cards: [['Stop', 'Stop the harmful behavior.'], ['Listen', 'Listen to the impact without arguing.'], ['Own + repair', 'Name what you did and fix what you can.'], ['Change', 'Show a different choice again and again.']] },
        activity: { directions: 'Help the puppet turn a weak apology into a real repair. The person harmed may ask for space.', scenarios: [
          { title: 'Weak apology', text: '“Sorry you got mad. Can we be friends now?”', choices: ['Own the action', 'Name the repair', 'Respect space'], answer: 'Better: “I took your things. That was wrong. I will return them and stop. You can have space.”' },
          { title: 'Class pledge', text: 'Choose one promise our class can keep every day.', choices: ['We include.', 'We speak up.', 'We get help.', 'We repair harm.'], answer: 'Combine student language into one short, observable class pledge.' }
        ] },
        message: { statement: 'Our class pledge: We notice harm. We speak up. We get help. We repair. Everyone belongs.', commitment: 'Today I will show our pledge by ___.', preview: 'Friday Cypher: celebrate evidence of Safe, Respectful, and Responsible choices.', teacher: 'Read the final pledge together and invite each child to add a thumbprint, mark, or initial.' },
        guardrail: common.repair,
        lookFor: 'Students can distinguish a repair from a demand for forgiveness and name one observable pledge action.'
      },
      '35': {
        iCan: 'I can describe accountable repair and help create a class pledge we can prove with actions.',
        vocabulary: ['empathy', 'accountability', 'impact', 'repair', 'boundary', 'commitment'],
        materials: ['Repair ladder', 'Class pledge builder', 'Cypher evidence slips'],
        greeting: { name: 'Evidence Appreciation', student: 'Greet a peer and name one Safe, Respectful, or Responsible action you actually observed.', teacher: 'Require observable evidence, not popularity words like “nice” or “cool.”' },
        sharing: { prompt: 'What makes an apology believable?', frame: 'An apology becomes believable when the person ___.', teacher: 'Listen for ownership, repair, changed behavior, and respect for boundaries.' },
        teach: { title: 'Accountable repair', cards: [['Name the action', 'Say exactly what you did without “if,” “but,” or blaming.'], ['Name the impact', 'Show you understand what became unsafe or disrespectful.'], ['Offer repair', 'Ask what can be repaired; restore property, truth, inclusion, or support.'], ['Change the pattern', 'Accept consequences and show different behavior over time.']] },
        activity: { directions: 'Revise the apology, then build one class pledge line that is specific enough to observe.', scenarios: [
          { title: 'Deflecting apology', text: '“I was only joking, but sorry if you were offended.”', choices: ['Name action', 'Name impact', 'Offer repair', 'Change behavior'], answer: 'Revision: “I repeated a hurtful joke after you asked me to stop. I embarrassed you. I will stop and correct the rumor with the people who heard it.”' },
          { title: 'Boundary', text: 'The student who was harmed says, “I do not want to talk with you right now.”', choices: ['Demand forgiveness', 'Respect the boundary', 'Ask peers to pressure them'], answer: 'Respect the boundary. Adults can plan repair without forced contact.' },
          { title: 'Pledge evidence', text: '“We will be kind” is hard to measure. Make it observable.', choices: ['Include someone', 'Report harm', 'Use names respectfully', 'All three'], answer: 'Use specific actions: “We include, report harm, and use names and identities respectfully.”' }
        ] },
        message: { statement: 'Our pledge: We notice harm, include others, report clearly, respect boundaries, and repair with changed actions.', commitment: 'I will create Cypher evidence by ___.', preview: 'Friday Cypher celebrates actions that prove the pledge.', teacher: 'Collect two or three student lines and finalize one class pledge. Prepare evidence-based nominations for Friday.' },
        guardrail: common.repair,
        lookFor: 'Students identify ownership and behavior change, protect boundaries, and write observable pledge language.'
      },
      '68': {
        iCan: 'I can distinguish accountability from image-management and build a pledge grounded in observable action.',
        vocabulary: ['accountability', 'impact', 'repair', 'boundary', 'restoration', 'changed pattern'],
        materials: ['Accountability test', 'Pledge builder', 'Cypher nomination slips'],
        greeting: { name: 'Evidence, Not Popularity', student: 'Greet a peer and cite one observed action connected to Safe, Respectful, or Responsible.', teacher: 'Keep recognition factual. Students may pass rather than invent evidence.' },
        sharing: { prompt: 'What is the difference between an apology that protects reputation and accountability that repairs harm?', frame: 'Image-management focuses on ___. Accountability focuses on ___.', teacher: 'Land on impact, action, consequence, repair, boundary, and changed behavior.' },
        teach: { title: 'The accountability test', cards: [['Specific ownership', 'Names the action without excuses, minimizing, or demanding agreement.'], ['Impact + boundary', 'Acknowledges harm and accepts the other person’s need for space or support.'], ['Repair + consequence', 'Offers appropriate repair and does not treat repair as a way to avoid consequences.'], ['Changed pattern', 'Shows different behavior over time and stops retaliation.']] },
        activity: { directions: 'Analyze each response for ownership, impact, boundary, repair, and changed pattern. Then draft one pledge line.', scenarios: [
          { title: 'Public apology, private retaliation', text: 'A student apologizes in front of adults, then tells friends to freeze out the reporting student.', choices: ['Accountability', 'Image-management', 'Complete repair'], answer: 'Image-management and retaliation. The harmful pattern continues.' },
          { title: 'No forced reconciliation', text: 'The targeted student does not want a face-to-face restorative conversation.', choices: ['Force the meeting', 'Respect the boundary', 'Cancel all accountability'], answer: 'Respect the boundary. Accountability, consequences, and other forms of repair can continue without forced contact.' },
          { title: 'Pledge test', text: '“No drama” could silence reporting. Revise it.', choices: ['Keep problems private', 'Report harm without spreading it', 'Ignore rumors'], answer: 'Use protective language: “We report harm privately to adults who can act, and we do not amplify it.”' }
        ] },
        message: { statement: 'Our pledge: We do not normalize harm. We report without amplifying, support without controlling, respect boundaries, and prove repair through changed behavior.', commitment: 'I will produce one observable piece of Cypher evidence today.', preview: 'Friday Cypher: recognize evidence, reinforce the pledge, and set the next practice focus.', teacher: 'Finalize the pledge, collect evidence-based nominations, and identify the class statement for Friday.' },
        guardrail: common.repair,
        lookFor: 'Students recognize retaliation and forced reconciliation as incompatible with repair, and draft precise pledge language.'
      }
    }
  }
];

export { common };
