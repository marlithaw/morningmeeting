import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { bands, common, lessons, unitMeta } from './unit-data.mjs';

const root = dirname(fileURLToPath(import.meta.url));
const decksDir = join(root, 'decks');
const bandOrder = ['k2', '35', '68'];
await mkdir(decksDir, { recursive: true });

const esc = (value = '') => String(value)
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;');

const slug = (lesson, band) => `lesson-${lesson.day}-${band}-student-deck.html`;
const cardGrid = (cards, cols = cards.length) => `<div class="cards" style="--cols:${Math.min(cols, 4)}">${cards.map(([head, body], index) => `
  <div class="card"><div class="num">${String(index + 1).padStart(2, '0')}</div><h3>${esc(head)}</h3><p>${esc(body)}</p></div>`).join('')}</div>`;

const footer = (lesson, band, slideNo) => `<div class="footer"><span class="brand"><img src="../shared/matchbook-flame.png" alt=""> Matchbook Morning Meeting · ${esc(lesson.focus)}</span><span>${esc(bands[band].short)} · ${String(slideNo).padStart(2, '0')}</span></div>`;
const noteAttr = (html) => `data-note="${esc(html)}"`;

function scenarioCard(scenario) {
  return `<div class="card"><h3>${esc(scenario.title)}</h3><p>${esc(scenario.text)}</p><div class="choices">${scenario.choices.map((choice) => `<div class="choice">${esc(choice)}</div>`).join('')}</div></div>`;
}

function buildDeck(lesson, band) {
  const data = lesson.bands[band];
  const firstScenarios = data.activity.scenarios.slice(0, 2);
  const finalScenarios = data.activity.scenarios.slice(2);
  const slide6Scenarios = finalScenarios.length ? finalScenarios : data.activity.scenarios.slice(-1);
  const titleNote = `<strong>0:00 setup</strong> Open in full screen. The four-part rhythm is Greeting (2), Sharing (3), Activity (7), Message (3).<br><strong>Teacher:</strong> ${data.iCan}`;
  const greetingNote = `<strong>Greeting · 0:00–2:00</strong><br>${data.greeting.teacher}<br><strong>Look for:</strong> Every student is welcomed by name.`;
  const sharingNote = `<strong>Sharing · 2:00–5:00</strong><br>${data.sharing.teacher}<br><strong>Frame:</strong> ${data.sharing.frame}`;
  const teachNote = `<strong>Activity · 5:00–8:00</strong><br>Teach the language briefly, then move into student analysis. ${data.guardrail}`;
  const activityNote = `<strong>Activity · 8:00–12:00</strong><br>${data.activity.directions}<br><strong>Answers:</strong><br>${firstScenarios.map((item) => `${item.title}: ${item.answer}`).join('<br>')}`;
  const debriefNote = `<strong>Activity debrief · by 12:00</strong><br>${slide6Scenarios.map((item) => `${item.title}: ${item.answer}`).join('<br>')}<br><strong>Look for:</strong> ${data.lookFor}`;
  const messageNote = `<strong>Message · 12:00–15:00</strong><br>${data.message.teacher}<br><strong>Commitment:</strong> ${data.message.commitment}<br><strong>Same-day response:</strong> ${common.disclosure}`;

  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(lesson.focus)} · ${esc(bands[band].label)} | Matchbook Morning Meeting</title>
<link rel="stylesheet" href="../shared/deck.css"></head><body>
<div class="hud"><button id="previous" aria-label="Previous slide">←</button><button id="next" aria-label="Next slide">→</button><button id="toggle-notes">Notes (N)</button><span id="count"></span></div>
<div class="deck">
  <section class="slide red active" ${noteAttr(titleNote)}>
    <div class="topline"><span>Bullying Prevention · Lesson ${lesson.day}</span><span class="phase">${esc(lesson.weeklyMove)}</span></div>
    <div class="body hero"><div><h1>${esc(lesson.focus)}</h1><p class="lede">${esc(lesson.practiceMove)}</p><div class="objective"><strong>I can:</strong> ${esc(data.iCan)}</div></div><div class="hero-mark">${lesson.day}</div></div>
    ${footer(lesson, band, 1)}
  </section>
  <section class="slide white" ${noteAttr(greetingNote)}>
    <div class="topline"><span>Greeting · 2 minutes</span><span class="phase">Every student welcomed by name</span></div>
    <div class="body"><h2>${esc(data.greeting.name)}</h2><div class="prompt"><span class="frame-label">Do this</span>${esc(data.greeting.student)}</div><p class="note"><strong>Choice counts:</strong> Words, a wave, or another mutually comfortable greeting can all communicate belonging.</p></div>
    ${footer(lesson, band, 2)}
  </section>
  <section class="slide yellow" ${noteAttr(sharingNote)}>
    <div class="topline"><span>Sharing · 3 minutes</span><span class="phase">Think · Pair · Brief share</span></div>
    <div class="body"><h2>${esc(data.sharing.prompt)}</h2><div class="prompt"><span class="frame-label">Sentence frame</span>${esc(data.sharing.frame)}</div></div>
    ${footer(lesson, band, 3)}
  </section>
  <section class="slide dark" ${noteAttr(teachNote)}>
    <div class="topline"><span>Activity · Learn the move</span><span class="phase">${esc(lesson.values)}</span></div>
    <div class="body"><h2>${esc(data.teach.title)}</h2>${cardGrid(data.teach.cards)}</div>
    ${footer(lesson, band, 4)}
  </section>
  <section class="slide paper" ${noteAttr(activityNote)}>
    <div class="topline"><span>Activity · Practice</span><span class="phase">Use evidence, not labels</span></div>
    <div class="body"><h2>What is the safest, most accurate response?</h2><div class="cards" style="--cols:${firstScenarios.length}">${firstScenarios.map(scenarioCard).join('')}</div></div>
    ${footer(lesson, band, 5)}
  </section>
  <section class="slide white" ${noteAttr(debriefNote)}>
    <div class="topline"><span>Activity · Debrief</span><span class="phase">Explain the why</span></div>
    <div class="body"><h2>Use the shared language</h2><div class="cards" style="--cols:${slide6Scenarios.length}">${slide6Scenarios.map(scenarioCard).join('')}</div><p class="note"><strong>Remember:</strong> When you are unsure, report the facts to a trusted adult.</p></div>
    ${footer(lesson, band, 6)}
  </section>
  <section class="slide red" ${noteAttr(messageNote)}>
    <div class="topline"><span>Message · 3 minutes</span><span class="phase">Commit and carry it into the day</span></div>
    <div class="body"><h2>${esc(data.message.statement)}</h2><div class="prompt"><span class="frame-label">My commitment</span>${esc(data.message.commitment)}</div><p class="lede">${esc(data.message.preview)}</p></div>
    ${footer(lesson, band, 7)}
  </section>
</div><div class="notes" id="notes" aria-live="polite"></div><script src="../shared/deck.js"></script></body></html>`;
}

function head(title, description = '') {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(title)}</title><meta name="description" content="${esc(description)}"><link rel="stylesheet" href="./shared/site.css"></head><body>`;
}

const bandCards = (lesson) => bandOrder.map((band) => `<a class="btn small" href="./decks/${slug(lesson, band)}" target="_blank">${bands[band].short} slides</a>`).join('');

function buildIndex() {
  const scheduleRows = lessons.map((lesson) => `<tr><td><strong>Lesson ${lesson.day}</strong></td><td>${esc(lesson.date)}</td><td>${esc(lesson.weeklyMove)}</td><td><strong>${esc(lesson.focus)}</strong><br>${esc(lesson.practiceMove)}</td><td>${esc(lesson.values)}</td></tr>`).join('');
  const dayCards = lessons.map((lesson) => `<article class="card"><div class="meta">Lesson ${lesson.day} · ${esc(lesson.weeklyMove)}</div><h3>${esc(lesson.focus)}</h3><p>${esc(lesson.date)}</p><p>${esc(lesson.practiceMove)}</p><div class="actions">${bandCards(lesson)}</div></article>`).join('');
  return `${head(unitMeta.title, unitMeta.subtitle)}
<header class="hero"><div class="shell"><div class="brand"><img src="./shared/matchbook-flame.png" alt=""> Matchbook Learning · Morning Meeting</div><div class="kicker">Instructional Unit · Student-Facing</div><h1>${esc(unitMeta.title)}</h1><p>${esc(unitMeta.subtitle)} The unit uses Greeting, Sharing, Activity, and Message in every 15-minute lesson.</p><div class="actions"><a class="btn" href="./teacher-guide.html">Teacher guide + scripts</a><a class="btn light" href="#slides">Open student slides</a><a class="btn yellow" href="./bullying-prevention-offline.zip" download>Download offline ZIP</a></div></div></header>
<main><div class="shell">
  <section class="section"><div class="notice yellow"><strong>Five lessons—not six.</strong> Lesson 1 launches on Tuesday, August 11. Lessons 2–5 follow the four instructional days of the weekly cycle on August 17–20. Friday, August 21 is the Friday Cypher application and celebration; it is not another lesson.</div></section>
  <section class="section"><h2>Weekly-cycle alignment</h2><div class="cycle">${lessons.slice(1).map((lesson) => `<div><strong>${esc(lesson.weeklyMove)}</strong><div class="date">${esc(lesson.date)}</div><h3>${esc(lesson.focus)}</h3><p>${esc(lesson.practiceMove)}</p></div>`).join('')}</div></section>
  <section class="section"><h2>Unit at a glance</h2><div class="table-wrap"><table><thead><tr><th>Lesson</th><th>Date</th><th>Cycle move</th><th>Focus + practice</th><th>Value</th></tr></thead><tbody>${scheduleRows}</tbody></table></div></section>
  <section id="slides" class="section"><h2>Student slides</h2><p class="section-intro">Each deck includes seven student-facing screens and a private teacher-notes drawer. Use the arrow keys to advance and press N to show or hide notes.</p><div class="grid five">${dayCards}</div></section>
  <section class="section"><h2>Teacher + print resources</h2><div class="grid three"><article class="card dark"><div class="meta">Complete delivery guide</div><h3>Teacher scripts</h3><p>Exact four-part timing, grade-band language, materials, answers, look-fors, and disclosure guardrails.</p><div class="actions"><a class="btn small" href="./teacher-guide.html">Open guide</a></div></article>${bandOrder.map((band) => `<article class="card"><div class="meta">Print toolkit</div><h3>${bands[band].label}</h3><p>Scenario cards, four-kinds poster, upstander menu, report card, repair guide, and pledge builder.</p><div class="actions"><a class="btn small" href="./printables-${band}.html">Open printables</a></div></article>`).join('')}</div></section>
  <section class="section"><h2>Definition and response guardrails</h2><div class="notice"><strong>Power + pattern + harm is a student analysis lens, not a student verdict.</strong> Students report facts and safety needs. Trained adults determine whether the incident meets the formal bullying definition. A one-time harmful act, threat, harassment concern, or dangerous behavior still requires an adult response.</div></section>
</div></main></body></html>`;
}

function buildTeacherGuide() {
  const nav = lessons.map((lesson) => `<a class="btn small dark" href="#lesson-${lesson.day}">Lesson ${lesson.day}: ${esc(lesson.focus)}</a>`).join('');
  const lessonBlocks = lessons.map((lesson) => `<section class="day-block" id="lesson-${lesson.day}"><div class="day-head"><div><div class="meta">Lesson ${lesson.day} · ${esc(lesson.weeklyMove)} · ${esc(lesson.values)}</div><h2>${esc(lesson.focus)}</h2></div><div>${esc(lesson.date)}</div></div>${bandOrder.map((band) => {
    const info = bands[band];
    const data = lesson.bands[band];
    const answers = data.activity.scenarios.map((item) => `<li><strong>${esc(item.title)}:</strong> ${esc(item.answer)}</li>`).join('');
    return `<article class="band-block" id="lesson-${lesson.day}-${band}"><div class="band-title"><div><div class="meta">${info.label}</div><h3>${esc(data.iCan)}</h3></div><div class="resource-links"><a class="btn small" href="./decks/${slug(lesson, band)}" target="_blank">Open slides</a><a class="btn small yellow" href="./printables-${band}.html">Print toolkit</a></div></div>
      <div class="chips">${data.vocabulary.map((word) => `<span class="chip">${esc(word)}</span>`).join('')}</div>
      <p><strong>Materials:</strong> ${data.materials.map(esc).join(' · ')}</p>
      <div class="table-wrap"><table><thead><tr><th>Time</th><th>Part</th><th>Teacher script + move</th><th>Student action</th></tr></thead><tbody>
        <tr><td>0:00–2:00</td><td><strong>Greeting</strong><br>${esc(data.greeting.name)}</td><td>${esc(data.greeting.teacher)}</td><td>${esc(data.greeting.student)}</td></tr>
        <tr><td>2:00–5:00</td><td><strong>Sharing</strong></td><td>${esc(data.sharing.teacher)}<br><em>Prompt:</em> ${esc(data.sharing.prompt)}</td><td>${esc(data.sharing.frame)}</td></tr>
        <tr><td>5:00–12:00</td><td><strong>Activity</strong><br>${esc(data.teach.title)}</td><td>Teach: ${data.teach.cards.map(([head, body]) => `<strong>${esc(head)}:</strong> ${esc(body)}`).join(' · ')}<br><br>${esc(data.activity.directions)}</td><td>Analyze, sort, or role-play using the shared language.<ul>${answers}</ul></td></tr>
        <tr><td>12:00–15:00</td><td><strong>Message</strong></td><td>${esc(data.message.teacher)}<br><strong>Class message:</strong> ${esc(data.message.statement)}</td><td><strong>Commit:</strong> ${esc(data.message.commitment)}<br><strong>Preview:</strong> ${esc(data.message.preview)}</td></tr>
      </tbody></table></div>
      <div class="guardrail"><strong>Teacher guardrail:</strong> ${esc(data.guardrail)}<br><strong>Look for:</strong> ${esc(data.lookFor)}</div>
    </article>`;
  }).join('')}</section>`).join('');
  const sourceLinks = unitMeta.sources.map((source) => `<li><a href="${esc(source.url)}">${esc(source.label)}</a></li>`).join('');
  return `${head('Teacher Guide · Bullying Prevention Unit', 'Five complete Morning Meeting scripts for grades K–2, 3–5, and 6–8.')}
<div class="back"><div class="shell"><a href="./index.html">← Bullying Prevention Unit</a></div></div><header class="hero"><div class="shell"><div class="brand"><img src="./shared/matchbook-flame.png" alt=""> Matchbook Learning · Morning Meeting</div><div class="kicker">Teacher Edition · Complete Scripts</div><h1>Bullying Prevention Teacher Guide</h1><p>Five 15-minute lessons, three calibrated grade bands, one shared response language.</p><div class="actions">${nav}</div></div></header>
<main><div class="shell"><section class="section"><div class="notice yellow"><strong>Timing:</strong> Greeting 2 minutes · Sharing 3 minutes · Activity 7 minutes · Message 3 minutes. The activity includes one minute for directions/reset and six minutes of core practice.</div></section>
<section class="section"><h2>Non-negotiable response language</h2><div class="grid three"><div class="card"><div class="meta">Student report opening</div><h3>“I need to report possible bullying or harassment.”</h3><p>Who · what actions · when · where · pattern · evidence · safety now.</p></div><div class="card"><div class="meta">Teacher response</div><h3>“Thank you for telling me. I am going to help.”</h3><p>Protect privacy. Do not promise secrecy. Follow the Matchbook Bullying Response Protocol the same day.</p></div><div class="card"><div class="meta">If harm continues</div><h3>Tell again—and tell another trusted adult.</h3><p>Students are not responsible for proving the case or managing retaliation alone.</p></div></div></section>
${lessonBlocks}
<section class="section"><h2>Sources and implementation notes</h2><div class="notice"><p>This unit uses the federal definition elements of unwanted aggressive behavior, real or perceived power imbalance, and repetition or likelihood of repetition. Indiana requires age-appropriate bullying-prevention instruction and local reporting procedures. Matchbook’s internal Bullying Response Protocol remains the controlling procedure for staff response, documentation, notification, and investigation.</p><ul class="sources">${sourceLinks}</ul></div></section>
</div></main></body></html>`;
}

function buildPrintables(band) {
  const info = bands[band];
  const lessonSections = lessons.map((lesson) => {
    const data = lesson.bands[band];
    const coreCards = cardGrid(data.teach.cards);
    const scenarios = data.activity.scenarios.map((item) => `<div class="card"><div class="meta">Cut card · Lesson ${lesson.day}</div><h3>${esc(item.title)}</h3><p>${esc(item.text)}</p><p><strong>Teacher key:</strong> ${esc(item.answer)}</p></div>`).join('');
    return `<section class="section print-page" id="print-lesson-${lesson.day}"><div class="meta">Lesson ${lesson.day} · ${esc(lesson.focus)} · ${esc(info.label)}</div><h2>${esc(data.teach.title)}</h2>${coreCards}<h3 style="margin-top:28px">Scenario cards</h3><div class="grid three">${scenarios}</div><div class="notice yellow" style="margin-top:22px"><strong>Message/pledge:</strong> ${esc(data.message.statement)}<br><strong>Student commitment:</strong> ${esc(data.message.commitment)}</div></section>`;
  }).join('');
  return `${head(`${info.label} Printables · Bullying Prevention`, 'Printable activity materials for the five-lesson bullying prevention unit.')}
<div class="back"><div class="shell"><a href="./index.html">← Bullying Prevention Unit</a></div></div><header class="hero"><div class="shell"><div class="brand"><img src="./shared/matchbook-flame.png" alt=""> Matchbook Learning · Morning Meeting</div><div class="kicker">Print Toolkit · ${info.label}</div><h1>Bullying Prevention Materials</h1><p>Print the full set or use your browser’s page range to select the lesson you need.</p><div class="actions"><button class="btn" onclick="window.print()">Print / Save PDF</button></div></div></header><main><div class="shell">${lessonSections}</div></main></body></html>`;
}

for (const lesson of lessons) {
  for (const band of bandOrder) {
    await writeFile(join(decksDir, slug(lesson, band)), buildDeck(lesson, band));
  }
}
await writeFile(join(root, 'index.html'), buildIndex());
await writeFile(join(root, 'teacher-guide.html'), buildTeacherGuide());
for (const band of bandOrder) await writeFile(join(root, `printables-${band}.html`), buildPrintables(band));

console.log(`Built ${lessons.length * bandOrder.length} decks, teacher guide, unit index, and ${bandOrder.length} printable toolkits.`);
