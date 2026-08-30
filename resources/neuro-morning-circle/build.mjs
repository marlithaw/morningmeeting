import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { bands, common, lessons, unitMeta, imageCredit } from './unit-data.mjs';

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

// Six-phase framework, shared across all bands and lessons.
const PHASES = [
  { key: 'regulate', name: 'Regulate', minutes: '2 minutes', tone: 'Calm the nervous system', frame: 'Breathe with me' },
  { key: 'orient', name: 'Orient', minutes: '2 minutes', tone: 'Name today’s value', frame: 'Our value today' },
  { key: 'connect', name: 'Connect', minutes: '3 minutes', tone: 'Share · relational capital', frame: 'Share · sentence frame' },
  { key: 'practice', name: 'Practice', minutes: '3 minutes', tone: 'Rehearse the move', frame: 'Practice the move' },
  { key: 'commit', name: 'Commit', minutes: '3 minutes', tone: 'Own a specific intention', frame: 'My commitment' },
  { key: 'transition', name: 'Transition', minutes: '2 minutes', tone: 'Stand on the one', frame: 'Transition cue' }
];
const SLIDE_COLOR = { regulate: 'white', orient: 'yellow', connect: 'dark', practice: 'paper', commit: 'red', transition: 'white' };

const figuresHtml = (imgs) => !imgs || !imgs.length ? '' : `<div class="figures">${imgs.map((image) => `<figure class="figure"><img src="${esc(image.src)}" alt="${esc(image.label)}" loading="lazy" width="160" height="160"><figcaption>${esc(image.label)}</figcaption></figure>`).join('')}</div>`;

const footer = (lesson, band, slideNo) => `<div class="footer"><span class="brand"><img src="../shared/matchbook-flame.png" alt=""> Neuro-Regulated Circle · ${esc(lesson.step)}</span><span>${esc(bands[band].short)} · ${String(slideNo).padStart(2, '0')}</span></div>`;
const noteAttr = (html) => `data-note="${esc(html)}"`;

function buildDeck(lesson, band) {
  const data = lesson.bands[band];
  const titleNote = `<strong>0:00 setup</strong> Open in full screen. The 15-minute arc is Regulate (2) · Orient (2) · Connect (3) · Practice (3) · Commit (3) · Transition (2).<br><strong>Core somatic goal:</strong> ${data.somaticGoal}<br><strong>Somatic set-up:</strong> ${data.somatic}<br><strong>I can:</strong> ${data.iCan}`;

  const phaseSlides = PHASES.map((phase, i) => {
    const p = data.phases[phase.key];
    const color = SLIDE_COLOR[phase.key];
    const somaticNote = phase.key === 'regulate' ? `<strong>Somatic set-up:</strong> ${data.somatic}<br>` : '';
    const note = `<strong>${phase.name} · ${phase.minutes}</strong><br>${somaticNote}<strong>Teacher script &amp; action:</strong> ${p.teacher}<br><strong>Student action:</strong> ${p.student}<br><strong>If / Then coaching:</strong> ${p.ifThen}`;
    const figures = figuresHtml(p.img);
    const bodyClass = figures ? 'body with-figures' : 'body';
    return `  <section class="slide ${color}" ${noteAttr(note)}>
    <div class="topline"><span>${phase.name} · ${phase.minutes}</span><span class="phase">${esc(phase.key === 'orient' ? lesson.value : phase.tone)}</span></div>
    <div class="${bodyClass}"><h2>${esc(phase.name)}</h2><div class="prompt"><span class="frame-label">${esc(phase.frame)}</span>${esc(p.teacher)}</div>${figures}${phase.key === 'regulate' && !figures ? `<p class="note"><strong>Somatic move:</strong> ${esc(data.somatic)}</p>` : ''}</div>
    ${footer(lesson, band, i + 2)}
  </section>`;
  }).join('\n');

  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(data.focus)} · ${esc(bands[band].label)} | Neuro-Regulated Morning Circle</title>
<link rel="stylesheet" href="../shared/deck.css"></head><body>
<div class="hud"><button id="previous" aria-label="Previous slide">←</button><button id="next" aria-label="Next slide">→</button><button id="toggle-notes">Notes (N)</button><span id="count"></span></div>
<div class="deck">
  <section class="slide red active" ${noteAttr(titleNote)}>
    <div class="topline"><span>Neuro-Regulated Circle · Lesson ${lesson.day}</span><span class="phase">${esc(lesson.step)}</span></div>
    <div class="body hero"><div><h1>${esc(data.focus)}</h1><p class="lede">${esc(data.somaticGoal)}</p><div class="objective"><strong>I can:</strong> ${esc(data.iCan)}</div></div><div class="hero-mark">${lesson.day}</div></div>
    ${footer(lesson, band, 1)}
  </section>
${phaseSlides}
</div><div class="notes" id="notes" aria-live="polite"></div><script src="../shared/deck.js"></script></body></html>`;
}

function head(title, description = '') {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(title)}</title><meta name="description" content="${esc(description)}"><link rel="stylesheet" href="./shared/site.css"></head><body>`;
}

const bandCards = (lesson) => bandOrder.map((band) => `<a class="btn small" href="./decks/${slug(lesson, band)}" target="_blank">${bands[band].short} slides</a>`).join('');

function buildIndex() {
  const scheduleRows = lessons.map((lesson) => `<tr><td><strong>Lesson ${lesson.day}</strong></td><td>${esc(lesson.date)}</td><td>${esc(lesson.step)}</td><td>${esc(lesson.summary)}</td><td>${esc(lesson.value)}</td></tr>`).join('');
  const dayCards = lessons.map((lesson) => `<article class="card"><div class="meta">Lesson ${lesson.day} · ${esc(lesson.step)}</div><h3>${esc(lesson.bands.k2.focus)}</h3><p>${esc(lesson.date)}</p><p>${esc(lesson.summary)}</p><div class="actions">${bandCards(lesson)}</div></article>`).join('');
  const pathwayCards = bandOrder.map((band) => `<article class="card"><div class="meta">${esc(bands[band].engine)}</div><h3>${esc(bands[band].label)}</h3><p>${esc(bands[band].focusSystem)} focus.</p></article>`).join('');
  return `${head(unitMeta.title, unitMeta.subtitle)}
<header class="hero"><div class="shell"><div class="brand"><img src="./shared/matchbook-flame.png" alt=""> Matchbook Learning · Morning Meeting</div><div class="kicker">Instructional Unit · Student-Facing</div><h1>${esc(unitMeta.title)}</h1><p>${esc(unitMeta.subtitle)} Every 15-minute lesson runs the same six-step arc: Regulate, Orient, Connect, Practice, Commit, and Transition.</p><div class="actions"><a class="btn" href="./teacher-guide.html">Teacher guide + scripts</a><a class="btn light" href="#slides">Open student slides</a><a class="btn yellow" href="./neuro-morning-circle-offline.zip" download>Download offline ZIP</a></div></div></header>
<main><div class="shell">
  <section class="section"><div class="notice yellow"><strong>Four lessons this week.</strong> Lesson 1 launches Monday, August 31, 2026. Lessons 2–4 follow Tuesday–Thursday, September 1–3. ${esc(unitMeta.friday)}</div></section>
  <section class="section"><h2>Design pathway</h2><p class="section-intro">Quarter 1 is mapped to physiological regulation and expanding the Window of Tolerance. Each grade band regulates a different part of the nervous system.</p><div class="grid three">${pathwayCards}</div></section>
  <section class="section"><h2>Weekly-cycle alignment</h2><div class="cycle">${lessons.map((lesson) => `<div><strong>${esc(lesson.step)}</strong><div class="date">${esc(lesson.date)}</div><h3>${esc(lesson.bands.k2.focus)}</h3><p>${esc(lesson.summary)}</p></div>`).join('')}</div></section>
  <section class="section"><h2>Unit at a glance</h2><div class="table-wrap"><table><thead><tr><th>Lesson</th><th>Date</th><th>Daily step</th><th>Focus + regulation</th><th>Value</th></tr></thead><tbody>${scheduleRows}</tbody></table></div></section>
  <section id="slides" class="section"><h2>Student slides</h2><p class="section-intro">Each deck includes seven student-facing screens and a private teacher-notes drawer. Use the arrow keys to advance and press N to show or hide notes. K–2 decks add student-friendly picture supports on every screen.</p><div class="grid three">${dayCards}</div></section>
  <section class="section"><h2>Teacher + print resources</h2><div class="grid three"><article class="card dark"><div class="meta">Complete delivery guide</div><h3>Teacher scripts</h3><p>Exact six-phase timing, grade-band language, somatic set-ups, student actions, and If/Then Warm Demander coaching.</p><div class="actions"><a class="btn small" href="./teacher-guide.html">Open guide</a></div></article>${bandOrder.map((band) => `<article class="card"><div class="meta">Print toolkit</div><h3>${bands[band].label}</h3><p>Somatic set-ups, the six-phase student checklist, sentence frames, and daily commitment cards.</p><div class="actions"><a class="btn small" href="./printables-${band}.html">Open printables</a></div></article>`).join('')}</div></section>
  <section class="section"><h2>Regulation guardrails</h2><div class="notice"><strong>Regulate before you reason.</strong> ${esc(common.warmDemander)} ${esc(common.disclosure)}</div></section>
  <section class="section"><p class="section-intro" style="margin:0">${esc(imageCredit)}</p></section>
</div></main></body></html>`;
}

function buildTeacherGuide() {
  const nav = lessons.map((lesson) => `<a class="btn small dark" href="#lesson-${lesson.day}">Lesson ${lesson.day}: ${esc(lesson.step)}</a>`).join('');
  const lessonBlocks = lessons.map((lesson) => `<section class="day-block" id="lesson-${lesson.day}"><div class="day-head"><div><div class="meta">Lesson ${lesson.day} · ${esc(lesson.step)} · Value: ${esc(lesson.value)}</div><h2>${esc(lesson.summary)}</h2></div><div>${esc(lesson.date)}</div></div>${bandOrder.map((band) => {
    const info = bands[band];
    const data = lesson.bands[band];
    const rows = PHASES.map((phase) => {
      const p = data.phases[phase.key];
      return `<tr><td><strong>${phase.name}</strong><br>${phase.minutes}</td><td>${esc(p.teacher)}</td><td>${esc(p.student)}</td><td>${esc(p.ifThen)}</td></tr>`;
    }).join('');
    return `<article class="band-block" id="lesson-${lesson.day}-${band}"><div class="band-title"><div><div class="meta">${info.label} · ${esc(info.engine)}</div><h3>${esc(data.focus)}</h3></div><div class="resource-links"><a class="btn small" href="./decks/${slug(lesson, band)}" target="_blank">Open slides</a><a class="btn small yellow" href="./printables-${band}.html">Print toolkit</a></div></div>
      <div class="chips"><span class="chip">${esc(lesson.step)}</span><span class="chip">Value: ${esc(lesson.value)}</span><span class="chip">${esc(info.focusSystem)}</span></div>
      <p><strong>I can:</strong> ${esc(data.iCan)}</p>
      <p><strong>Core somatic goal:</strong> ${esc(data.somaticGoal)}</p>
      <p><strong>Somatic set-up:</strong> ${esc(data.somatic)}</p>
      <div class="table-wrap"><table><thead><tr><th>Phase</th><th>Teacher script &amp; action</th><th>Student action</th><th>If / Then coaching scenario</th></tr></thead><tbody>${rows}</tbody></table></div>
      <div class="guardrail"><strong>Warm Demander guardrail:</strong> ${esc(common.warmDemander)}</div>
    </article>`;
  }).join('')}</section>`).join('');

  const scenarioBank = `<section class="section"><h2>Restorative coaching &amp; Warm Demander scenario bank</h2>
  <div class="notice"><p>In a trauma-responsive school, behavioral issues are read not as willful compliance failures but as biometric signals of dysregulation (Porges, 2011). When a student is pushed outside the Window of Tolerance, de-escalate the biology before addressing accountability.</p></div>
  <div class="table-wrap"><table><thead><tr><th>Trigger / behavior</th><th>Recommended track</th><th>Somatic fix</th></tr></thead><tbody>
    <tr><td>Regulatory rupture / behavioral crisis (fight / flight / freeze)</td><td><strong>Quarter 1 · Physiological Regulation</strong></td><td>Prioritize brainstem stabilization with somatic breathing, body scans, and sensory grounding. Higher-order reasoning is biologically offline until arousal settles.</td></tr>
    <tr><td>Relational conflict / social harm (excluding, mocking peers)</td><td><strong>Quarter 2 · Interpersonal Harm Repair</strong></td><td>Target limbic needs for co-regulation. Restore relational safety through perspective-taking, kindness sways, and active-listening frames.</td></tr>
    <tr><td>Rigor gap / task avoidance (slamming books, head on desk)</td><td><strong>Quarter 3 · Executive Function Blueprint</strong></td><td>Address lost prefrontal focus from allostatic load. Normalize the struggle, reframe mistakes as data, break tasks into checked wins.</td></tr>
    <tr><td>Disengagement / systemic frustration (defiant head down)</td><td><strong>Quarter 4 · Student-Led Power Sharing</strong></td><td>Restore agency and counter learned helplessness by transferring managing roles (Speaker, Listener) to students.</td></tr>
  </tbody></table></div>
  <div class="grid three" style="margin-top:22px">
    <article class="card"><div class="meta">Scenario 1 · The shut-down student</div><h3>Head dropped on folded arms</h3><p><strong>What backfires:</strong> Standing over the desk, pointing, demanding “Head up. Get to work.” This violates space and pushes a freezing student toward fight-or-flight.</p><p><strong>What lands:</strong> Quietly place a sticky note: “Start task 1 when you can. I am right here.” Walk away, let the freeze thaw, and return in 10 minutes. If started, whisper “I see you working, thank you.” If still frozen, “I’ll check in during our transition. Let’s take a breath.” Follow up privately with Regulate–Relate–Reason.</p></article>
    <article class="card"><div class="meta">Scenario 2 · The physical outburst</div><h3>Knocking over a desk in frustration</h3><p><strong>What backfires:</strong> Yelling “Get out! That’s a detention! Go to the office!” This escalates public shame and feeds “the world is not safe.”</p><p><strong>What lands:</strong> Approach calmly, supportive but firm: “Are you okay? [Pause.] Knocking over furniture breaks our safety rule, so that is a detention. I’ll write the pass, you take a deep breath, and we’ll talk at lunch about repairing our classroom.” Apply the boundary neutrally, pivot to regulation, and schedule the restorative repair.</p></article>
    <article class="card dark"><div class="meta">Same-day response</div><h3>Protect safety first</h3><p>${esc(common.disclosure)}</p></article>
  </div></section>`;

  const sourceLinks = unitMeta.sources.map((source) => `<li><a href="${esc(source.url)}">${esc(source.label)}</a></li>`).join('');
  return `${head('Teacher Guide · Neuro-Regulated Morning Circle', 'Four complete 15-minute Morning Circle scripts for grades K–2, 3–5, and 6–8.')}
<div class="back"><div class="shell"><a href="./index.html">← Neuro-Regulated Morning Circle</a></div></div><header class="hero"><div class="shell"><div class="brand"><img src="./shared/matchbook-flame.png" alt=""> Matchbook Learning · Morning Meeting</div><div class="kicker">Teacher Edition · Complete Scripts</div><h1>Neuro-Regulated Circle Teacher Guide</h1><p>Four 15-minute lessons, three calibrated grade bands, one six-phase regulation arc.</p><div class="actions">${nav}</div></div></header>
<main><div class="shell"><section class="section"><div class="notice yellow"><strong>Timing:</strong> Regulate 2 · Orient 2 · Connect 3 · Practice 3 · Commit 3 · Transition 2 = 15 minutes. Run the same arc every morning so the routine itself becomes predictable and safe.</div></section>
<section class="section"><h2>The non-negotiable sequence</h2><div class="grid three"><div class="card"><div class="meta">1 · Regulate the biology</div><h3>“De-escalate before you educate.”</h3><p>Somatic co-regulation opens the Window of Tolerance so the prefrontal cortex can access learning.</p></div><div class="card"><div class="meta">2 · Relate with warmth</div><h3>“Every child welcomed and seen.”</h3><p>Unconditional positive regard first — connection is the intervention, not the reward.</p></div><div class="card"><div class="meta">3 · Reason as a Warm Demander</div><h3>“Absolute, neutral accountability.”</h3><p>Apply boundaries calmly as procedures, never as personal attacks or public shame.</p></div></div></section>
${lessonBlocks}
${scenarioBank}
<section class="section"><h2>Sources and implementation notes</h2><div class="notice"><p>This universal Tier 1 block is grounded in Lori Desautels’ brain-aligned, trauma-responsive practices and Stephen Porges’ Polyvagal Theory, and it maps to Matchbook’s ROAR values — Safe, Respectful, Responsible. Quarter 1 protects psychological safety through predictable, sensory-motor co-regulation before instructional pressure begins.</p><ul class="sources">${sourceLinks}</ul></div></section>
<section class="section"><p class="section-intro" style="margin:0">${esc(imageCredit)}</p></section>
</div></main></body></html>`;
}

function buildPrintables(band) {
  const info = bands[band];
  const lessonSections = lessons.map((lesson) => {
    const data = lesson.bands[band];
    const checklist = PHASES.map((phase) => `<div class="card"><div class="meta">${phase.name} · ${phase.minutes}</div><h3>${esc(phase.tone)}</h3><p>${esc(data.phases[phase.key].student)}</p></div>`).join('');
    return `<section class="section print-page" id="print-lesson-${lesson.day}"><div class="meta">Lesson ${lesson.day} · ${esc(lesson.step)} · ${esc(info.label)}</div><h2>${esc(data.focus)}</h2>
      <div class="notice"><strong>I can:</strong> ${esc(data.iCan)}<br><strong>Somatic set-up:</strong> ${esc(data.somatic)}</div>
      <h3 style="margin-top:24px">The six-phase circle</h3><div class="grid three">${checklist}</div>
      <div class="notice yellow" style="margin-top:22px"><strong>Value of the day:</strong> ${esc(lesson.value)}<br><strong>My commitment:</strong> ${esc(data.phases.commit.teacher)}</div></section>`;
  }).join('');
  return `${head(`${info.label} Printables · Neuro-Regulated Morning Circle`, 'Printable somatic set-ups and six-phase circle checklists for grades ' + info.short + '.')}
<div class="back"><div class="shell"><a href="./index.html">← Neuro-Regulated Morning Circle</a></div></div><header class="hero"><div class="shell"><div class="brand"><img src="./shared/matchbook-flame.png" alt=""> Matchbook Learning · Morning Meeting</div><div class="kicker">Print Toolkit · ${info.label}</div><h1>Morning Circle Materials</h1><p>Print the full set or use your browser’s page range to select the lesson you need.</p><div class="actions"><button class="btn" onclick="window.print()">Print / Save PDF</button></div></div></header><main><div class="shell">${lessonSections}</div></main></body></html>`;
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
