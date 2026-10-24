# Weekly build: Morning Meeting unit + Morning Spark + Ember

This workflow comes from the last three uploads: Morning Meeting Weeks 9, 10, and 11 and Spark/Ember Weeks 1, 2, and 3.
AGENTS.md sets the rules. This file sets the order of work. `check_week.py` enforces what a script can check.

Each school week ships two packages and changes the hub in four places:

| Package | Folder | Bands | Days |
|---|---|---|---|
| Morning Meeting unit (MM Week N) | `resources/week-N-slug/` | K–2, 3–5, 6–8 | Mon–Thu lessons. Friday is the Friday Cypher. In a short week the Cypher moves to the last school day (Week 10). |
| Spark/Ember week (SE Week M) | `resources/spark-ember/week-M-slug/` | K–1, 2–3, 4–5, 6–8 | Every school day. Spark Friday Wonder and Ember Friday only when Friday is a school day. |

The two numbers are counted separately. October 19–23, 2026 was MM Week 11 and SE Week 3. **October 26–30 is MM Week 12, SE Week 4, and IXL Week 9.**

## Who does what

| Step | Owner |
|---|---|
| 1. Intake: school days, focus titles, priorities, operational changes (list below) | Marlitha |
| 2. Confirm the week numbers, IXL week, and folder slugs, and list any missing inputs | Claude |
| 3. Draft the MM unit: four lessons × three bands, teacher guide, printables, media page, unit hub | Claude |
| 4. Draft Spark: four band decks (Do Now, reveal, and hand-off for each day), student pages PDF, IXL pin | Claude |
| 5. Draft Ember: four band boards (one new video and reflection per day), reflection slips PDF | Claude |
| 6. Package page, teacher guide (HTML + PDF), `media-sources.json`, `ixl-week-K-source.json`, then the ZIP **last** | Claude |
| 7. Add the hub sections (four places, below) on a branch. Run `check_week.py`. Render and look at everything | Claude |
| 8. Review the drafts and the previews | Marlitha |
| 9. Revise, rebuild the ZIP, re-run the checks, open the PR | Claude |
| 10. Merge, then check the live tabs and projected decks | Marlitha + Claude |

Lock the focus title in step 1, before naming the folder. Week 11 changed its title after the folder was made, so
`week-11-back-on-the-one` now holds "Back from Break. Ready to Learn."

## 1. Intake (needed before drafting)

- **School calendar for the week.** Which days have school, whether Friday is a school day, and any early release or event days.
  Leave out every non-school day. Never guess this from earlier weeks.
- **MM focus** (the theme and four daily lesson titles) and any admin or culture priorities.
- **Spark/Ember focus title** (it can connect to the MM theme, as "Back Together" did with "Back from Break").
- **IXL:** the current source is `https://marlithaw.github.io/Matchbook_Learning_IXL/ixl-data.json`. The IXL week is the number of
  calendar weeks since Monday, August 31, 2026, counting break weeks: Oct 5 = 6, Oct 19 = 8, Oct 26 = 9.
- **Operational changes.** Dismissal groups, times, release order, Chromebook procedure, hallway procedures. If none are
  supplied, the Ember rail and pack-up text stay exactly as they were last week.

If anything is missing, list it in the draft notes and in the PR. Do not make up IXL codes, dates, or procedures.

## 2. Morning Meeting unit (`resources/week-N-slug/`)

Copy the structure of the newest unit (Week 11). **Do not copy its content forward.** Week 11 first shipped with
Week 10's lesson text (fixed in 121b4b7).

```
index.html                 unit hub: theme, six-phase line, visible "Weekly Videos & Do Now – First 5" section,
                           Monday–Thursday lesson cards (each with K–2 / 3–5 / 6–8 + Relax · Excite + Relax · Excite),
                           three "Keep the learning visible" toolkit cards, Prepare for Monday
lesson-D-{k2,35,68}.html   D = 1..4; <title>Week N · <band-specific title> · <band></title>
teacher-guide.html         anchors #day-D-{k2,35,68}
printables-{k2,35,68}.html anchors #day-D
media.html                 topic clips (these add to the recurring videos, never replace them)
assets/  shared/           SVG scenes and icons; site.css, toolkit.css, Matchbook fonts, flame
```

Lesson standard (Weeks 10 and 11): a Welcome ready screen, then six phases totaling 15 minutes:
Regulate 2 · Orient 2 · Connect 3 (See It 2 + Name It 1) · Practice 3 · Commit 3 · Transition 2. Use the Week 11
screen eyebrow `Week N · <Day Month D> · <Phase> · <time>`. Every screen has presenter notes: script, model or worked
response, look for, access supports. Each deck links back to the unit hub, its teacher-guide anchor, and its printable,
and it carries the Do Now – First 5 link.

## 3. Spark/Ember package (`resources/spark-ember/week-M-slug/`)

```
morning-spark-{k1,23,45,68}.html              one deck per band for the whole week: slide do / reveal / handoff per day,
                                              day buttons (data-go) for exactly the school days, #mon..#fri and #week hashes
morning-spark-{band}-student-pages.pdf        one dated page per day (Monday is the private check-in slip)
ember-{band}.html                             board; weekly content lives in the `const EMBER={...}` block:
                                              videos[], prompts[] (EN, ES, frame EN, frame ES), bridges[]
ember-{band}-reflection-slips.pdf
index.html                                    package page with #teacher-guide and #photo-credits
teacher-guide.html / teacher-guide.pdf        dated, day by day per band: task, reveal/key, look for
media-sources.json                            videos {key: [youtubeId, title, channel]}, daily_sequence per band,
                                              photo_credits [title, author, url, license, license url], review_note
ixl-week-K-source.json                        snapshot of the IXL source used for the pin
assets/  shared/                              photos (CC licensed and credited), fonts
spark-ember-week-M-all-files.zip              built last, from the finished folder
```

**Morning Spark day formats:** Monday Check-In, Tuesday Picture of the Day, Wednesday Zoom In, Thursday Would You Rather,
and Friday Wonder (only on a school-day Friday). Each band gets its own prompt, not one prompt reworded:
K–1 pictures first, 2–3 frames and one sentence, 4–5 claim and evidence, 6–8 argue both sides (the Week 2 rebuild,
37562fd). Read-aloud text is bilingual. K–1 reads a book after the Do Now. Grades 2–8 get IXL codes on the Do Now
slide, pinned with `var w = K` and an embedded snapshot that includes week K. Update the comment above the pin too:
Week 3 still says "Week 6 for October 5-8."

**Ember:** one new video per band per school day, matched to that day's reflection, with the channel credited.
Videos play from YouTube, and the breathing circle is the fallback when YouTube is blocked. Content that never changes
unless Marlitha supplies a change: seated pack-up text, Chromebook return to its numbered cart slot, the "No lining up"
rule, release rail groups, times, and order, Practice mode, the 2:05 auto start.

## 4. Hub (`index.html`), four places

1. **Morning Spark tab:** a new `<section aria-labelledby="spark-weekM-title">` directly under the teacher-guide
   card and above last week's section. Copy last week's section markup and change only the content. Include:
   the eyebrow `Week M · Four grade bands · <n> formats · <dates>, 2026`, the title, a yellow how-to bar, a row with the
   guide, guide PDF, and ZIP buttons, the line `Weekly Videos: Relax · Excite · Do Now – First 5: Relax · Excite`,
   four band cards (present, download, preview week, student pages), and a Week at a glance table with a direct link
   for each band and day.
2. **Ember tab:** `ember-weekM-title`, the same pattern (`Dismissal · Week M · <dates> · Four grade bands · <n> days`),
   four board and slip cards, and a "This week's videos" table: video link, channel, reflection, and an "Open dated board"
   link in every cell.
3. **Instructional Units tab:** update the intro paragraph to MM Week N, then add `week{N}-title` above last week's unit:
   a header with an "Open Week N toolkit" button, a menu table (Date, Lesson, K–2, 3–5, 6–8, Videos, Do Now – First 5,
   Teacher Guide), a Teacher scripts card, and three Print toolkit cards.
4. Leave every earlier section in place. Nothing is deleted or replaced.

**Use the table classes from last week's section.** The Ember table was restyled once to match (1cf029f). The approved
Week 3 publish then switched both Week 3 tables to `revision-week-table`, a class with no CSS rule anywhere.

## 5. Checks before publishing

```
python3 _build/weekly/check_week.py              # newest MM unit + newest Spark/Ember week
python3 _build/weekly/check_week.py --mm 12 --se 4 --quiet
```

It checks: recurring links in every menu row, unit hub, and weekly section; hub order and archives; band cards;
the six phases; weekday names against dates; band and day links in the glance tables; day buttons that match the school
days; the IXL pin against the date; Ember video count and unchanged dismissal text and rail; the ZIP byte for byte against
the folder; text carried over from last week; table classes that match last week; and every local link and anchor.
Fix every FAIL. Read every WARN and either fix it or say why it stays.

The script cannot check what the page looks like. You still need to:

- Render every PDF page to an image and look at it (overflow, crops, wrapping, dates).
- Step through every Spark deck day, including the reveal and hand-off and the IXL chip, and every Ember board day,
  including a Practice run, at projector size (1920×1080) and laptop size.
- Look at the three hub tabs on a desktop and a phone. Compare the new section with last week's section on screen.
- After the merge, hard refresh the live site and repeat the tab check. Test one YouTube video on a classroom computer.

Cloud sessions cannot reach `cdn.tailwindcss.com` or the live site, so they cannot render the hub with its styles.
Do the visual check where those load, and say plainly when a visual check has not been done.

## 6. Publish

Work on a branch. Commit drafts as "draft, not published". Open a PR that lists the inputs used, the missing inputs,
and the WARN lines that remain. After approval: one "Publish approved Week N / Week M ..." commit, rebuild the ZIP,
re-run the checks, merge, then do the live check.
