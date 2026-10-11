# K-2 SEL Toolkit: building one topic

Each topic ships the same bundle: 7-slide student deck (HTML + PDF), poster (letter + 11x17), center kit
(sort, sequence, act it out, desk strips, coloring), Tier 2 mini book, teacher guide (Word + PDF),
family half-sheets (EN/ES/KR), a captioned song video, a topic web page, and an offline ZIP.

## Who does what

| Step | Owner |
|---|---|
| 1. Draft the topic file `topics/NN-slug.py` (story, script, notes, cards, mini book, family text, guide) | Claude |
| 2. Map art: reuse `assets/img` first; list the gaps | Claude |
| 3. Review the content draft | Marlitha |
| 4. Flow image prompts for the gaps; generate in Flow (personal Gmail only, never the Matchbook account); she picks | Claude + Marlitha |
| 5. Build the draft bundle and check every page | Claude |
| 6. Lyrics: shared intro + "I can choose" chorus (music/SHARED.md) word for word, new topic hook, verses, outro; she makes it in Suno and uploads it | Claude + Marlitha |
| 7. Flow video clips (Frames mode, 8s, no ages in prompts, never animate the unsafe act); cut the captioned video | Claude |
| 8. Publish on a branch, open a PR; she merges; check the live site | Claude + Marlitha |

## Commands

See README.md, "How to build a topic". In short:

```
cd _build/k2-toolkit
python3 build.py topics/02-calm-corner.py                 # draft into out/02-calm-corner (includes the topic page)
python3 build.py topics/02-calm-corner.py --only deck     # rebuild one part
python3 builder/lineart.py c_breathe color_calm.png       # trace a white-background image into a coloring page
python3 music/build_mv.py 02-calm-corner --clips <folder> # captioned song video (needs music/02-calm-corner/mv.py)
python3 build.py topics/02-calm-corner.py --publish       # copy into resources/k2-behavior-toolkit and refresh the toolkit home
```

## Content rules

- Lee and Tee never do the unsafe behavior. Unsafe moments rotate across the classmates (Kiara, Diego, Nadege, Malik, Sofia).
- Never cast a real student. The teacher guide is only for the teacher delivering the lesson.
- Calm choices are calm-corner tools only (no fidgets).
- Every caption line has Spanish and Haitian Creole.
- No em dashes in teacher, student, or family text.
- Same seven Morning Meeting phases: Title & Promise (R2), Get Calm First (R1), Orient (R2, R3), Connect (R3, R4),
  Practice "Watch Me, Then Show Me" (R3, R4, R5), Commit (R2, R5), Transition (R1, R4, R5).
- Presenter notes per slide: script, look for, if it breaks, support adult, language support, engagement move
  (equity sticks / LiveSchool), optional aside.
- Every published page keeps the Weekly Videos and Do Now – First 5 links (see AGENTS.md) and the credit line:
  Lee & Tee characters © AH-HA Coaching and Consulting, used with permission.
- The tracker spreadsheet never goes on the site.

## Checks before publishing

Render every PDF page to an image and look at it (crops, overflow, wrapping, 2-line titles). Open the deck and step
through all 7 slides with notes. Check every local link on the topic page. After the merge, hard refresh the live
site and check the hub button, toolkit menu, topic page, video, and deck song button.

Picture crops: Flow art is 16:9, but most frames are narrower (slide 4's big picture is about 1.2:1, so a third of
the width is cut). Flow scenes usually put the main character in the left or right third, so a "center" crop pushes
the character the slide asks about to the edge. For every cover-cropped picture, set the horizontal part of `pos`
to where that character stands, not "center". On slide 4, if the character is in the outer third, add `zoom`
(1.15 to 1.25) with `pos` near 0% or 100%. Then check that the named character's face sits near the middle of the
frame on the rendered slide, not just that the slide looks fine overall.
Mini book pages are portrait (about 0.85:1), so a 16:9 scene loses more than half its width there. For any classroom
or hallway scene in the mini book, set `fit='wide'` on the page (and `cover_wide=True` for a scene cover): it uses a
4:3 frame and centers the page. Keep the portrait frame for white-background step pictures (`fit='contain'`).
Scenes that teach a spatial idea ("stand close") must show it: generate them with the characters grouped near the
middle and give the left-to-right order in the prompt, or every narrow crop loses someone.
