# Phase 3 boundary and page-join audit — காலப் பேழையும் கவிதைச் சாவியும்

## Scope

This audit follows completion of Phase 2 for all **306/306 physical scans** and completion of the Phase-3 physical-scan ↔ printed-page reconciliation.

For each of the **58 numbered items**, certify the opening boundary, every within-item physical-page join, the closing boundary, quotation/separator continuity, item metadata consistency, and contents/title-page witness differences. The controlling scan remains the highest authority. Source anomalies are preserved rather than silently repaired.

Canonical Tamil assembly remains blocked until all 58 items pass this audit.

## Iteration policy

Routine Phase-3 boundary/join work is processed in **25-physical-scan iterations**. An iteration may end inside an item; in that case the inspected joins are recorded durably but the item is not marked certified until its full physical range and closing boundary have been checked.

## Progress

- items fully certified: **30/58**
- last fully certified item: **30 — `ஆற்றலின் அளவுகோல்; அவன் செங்கோல்!`**
- current partial item: **31 — contents `மாண்பு நிறை தாயும், மாசற்ற மகனும்!`; title scan `மாண்பு நிறை தாயும் மாசற்ற மகனும்!`**, audited through scan **149 / printed page 148**
- latest 25-scan iteration completed: **scans 125–149**
- unresolved structural joins: **none**
- Tamil transcription changes in this iteration: **none**
- structural metadata changes in this iteration: **none**
- next 25-scan iteration: **scans 150–174**, beginning with join **149→150**

## Certified-item register

| Item | Title / contents witness | Physical scans | Printed pages | Internal joins | Result |
|---:|---|---|---|---:|---|
| 1–17 | see earlier repository history / page map | 10–95 | 9–94 | all | PASS |
| 18 | `தேய்ந்ததுபோக மிச்சத்தைத் தேடுகின்றோம்!` | 96–98 | 95–97 | 2/2 | PASS; title witness differs |
| 19 | `வருந்தத்தக்க வரலாற்று நிகழ்ச்சி!` | 99–102 | 98–101 | 3/3 | PASS |
| 20 | `வீழினும் அவன் வெற்றித் திருமகனே!` | 103–106 | 102–105 | 3/3 | PASS |
| 21 | `பண்பாட்டுக்கு ஊனம் எனில் பார்க்கவும் விரும்பார்!` | 107–111 | 106–110 | 4/4 | PASS |
| 22 | `பிறகேன் வினா? என்பதே என் வினா!` | 112–116 | 111–115 | 4/4 | PASS; title witness differs |
| 23 | `பெண்ணியத்தின் திண்மை கூறும் குண்டலகேசி!` | 117–119 | 116–118 | 2/2 | PASS |
| 24 | `ஈராயிரம் ஆண்டின் முன்னே இந்தத் தமிழ் நிலம்!` | 120–123 | 119–122 | 3/3 | PASS |
| 25 | `கலாச்சாரத்தின்மீது கண்ணகி காட்டிய அழுத்தம்!` | 124–127 | 123–126 | 3/3 | PASS; title witness differs |
| 26 | `விழித்தெழுக; இதோ, செம்மொழி விடியல்!` | 128–131 | 127–130 | 3/3 | PASS; title witness differs |
| 27 | `வழிகாட்டும் வண்ணம்; திறக்கப்படுவது திண்ணம்!` | 132–135 | 131–134 | 3/3 | PASS |
| 28 | `பார் முழுதும் பரவிய பழம்பெரும் நாகரிகம்!` | 136–139 | 135–138 | 3/3 | PASS |
| 29 | `தாயே, தந்திடு எமக்கு தன்மானச் செல்வங்களை ஈன்று!` | 140–144 | 139–143 | 4/4 | PASS; title witness differs |
| 30 | `ஆற்றலின் அளவுகோல்; அவன் செங்கோல்!` | 145–147 | 144–146 | 2/2 | PASS |

## Durable structural notes

- **scan 31→32:** the abrupt rhetorical/narrative transition is source-level; continuous pagination and intact page edges show no missing physical scan. It remains unrepaired.
- **item 12 metadata:** scans 59–63 were previously aligned to the title-scan section id `item-12-varalattrup-poongaavil-vallith-thirumanam`; no Tamil text changed.
- title witnesses remain separate and unreconciled. Reached discrepancies now include items **18, 22, 25, 26, 29 and 31**.

## 25-scan iteration — scans 125–149

### Item 25 — contents `கலாச்சாரத்தின்மீது கண்ணகி காட்டிய அழுத்தம்!`

**Status: PASS — fully certified.**

- opening boundary **123→124: PASS** was established in the preceding iteration;
- join **124→125: PASS** — scan 124 closes with `எஞ்சியதுண்டோ கணப் பொழுதேனும் கண்ணகிக்கென்று ;`; scan 125 continues the same discussion with the `சம்பூர்ணத் தேவன்` passage;
- join **125→126: PASS** — continuous argument; no separator, duplicate or source gap;
- join **126→127: PASS** — `கண்ணகி நிலை கேள்வியுற்று ;` continues into `அவள் தோழி பெயருத்தி ஆரிய மாது - ... தேவந்தி ஆறுதல் கூறிட வருகிறாள்.`;
- closing boundary **127→128: PASS** — scan 127 completes the item and source/citation note material; scan 128 begins item 26;
- title witnesses remain distinct: contents has final `!`, title scan 124 does not;
- dropped/duplicated text: **none**.

### Item 26 — contents `விழித்தெழுக; இதோ, செம்மொழி விடியல்!`

**Status: PASS — fully certified.**

- opening boundary **127→128: PASS**;
- title scan 128 visibly reads `விழித்தெழுக; இதோ செம்மொழி விடியல்!`, omitting the contents comma after `இதோ`;
- join **128→129: PASS** — the rhetorical question sequence continues directly from the `ஈக்களுக்குப் பல் இல்லை...` example into the next comparison;
- join **129→130: PASS** — source-contiguous continuation with no missing or repeated lines;
- join **130→131: PASS** — the discussion leads directly into the name/list sequence and item conclusion;
- closing boundary **131→132: PASS** — scan 131 ends with `இதோ ‘செம்மொழி’ விடியல்!` and ornament; scan 132 begins item 27;
- dropped/duplicated text: **none**.

### Item 27 — `வழிகாட்டும் வண்ணம்; திறக்கப்படுவது திண்ணம்!`

**Status: PASS — fully certified.**

- opening boundary **131→132: PASS**;
- joins **132→133, 133→134, 134→135: 3/3 PASS**;
- the argument around `கோட்டைகளும்` continues into `வானைத் தொடும் மதில் அரண்களும்...`, and scan 134's `உலகு உள்ளிட்ட கோள்களின் / உலாவில் இருந்தே தொடங்கி` proceeds into the conclusion on scan 135;
- closing boundary **135→136: PASS** — `கவிதைச் சாவி கொண்டு / திறக்கப்படுவது திண்ணம்!` and ornament close the item before item 28 begins;
- title-witness difference: **none**;
- dropped/duplicated text: **none**.

### Item 28 — `பார் முழுதும் பரவிய பழம்பெரும் நாகரிகம்!`

**Status: PASS — fully certified.**

- opening boundary **135→136: PASS**;
- join **136→137: PASS** — the English quotation ending scan 136 is followed by its `G. Zograf / Soviet Indologist...` attribution on scan 137;
- join **137→138: PASS** — `திராவிடர்க்கும்` continues into the same argument on scan 138;
- join **138→139: PASS** — `அப்போதே இரையாகிப் போனது -` continues as `அதன் பின்னரும் அங்கிருந்த திராவிடப் பண்பாட்டு இனம் ;`;
- closing boundary **139→140: PASS** — ornament followed by item 29 title;
- title-witness difference: **none**;
- dropped/duplicated text: **none**.

### Item 29 — contents `தாயே, தந்திடு எமக்கு தன்மானச் செல்வங்களை ஈன்று!`

**Status: PASS — fully certified.**

- opening boundary **139→140: PASS**;
- title scan 140 visibly reads `தாயே தந்திடு எமக்கு தன்மானச் செல்வங்களை ஈன்று!`, omitting the comma after `தாயே`;
- join **140→141: PASS** — the quotation/open construction at the foot of scan 140 continues directly on scan 141;
- joins **141→142, 142→143, 143→144: PASS**;
- closing boundary **144→145: PASS** — scan 144 closes with `தாயே ; தந்திடு எமக்கு அத்தகு / தன்மானச் செல்வங்களை ஈன்று!` and ornament; scan 145 begins item 30;
- dropped/duplicated text: **none**.

### Item 30 — `ஆற்றலின் அளவுகோல்; அவன் செங்கோல்!`

**Status: PASS — fully certified.**

- opening boundary **144→145: PASS**;
- join **145→146: PASS**;
- join **146→147: PASS** — the question concerning Karikalan's Lanka expedition is answered/continued directly on scan 147;
- closing boundary **147→148: PASS** — scan 147 closes with `துடைத்துக் கொள்வோம் ; / முழுமை வரலாறில்லா சோகம்!` and ornament; scan 148 begins item 31;
- title-witness difference: **none**;
- dropped/duplicated text: **none**.

### Item 31 — contents `மாண்பு நிறை தாயும், மாசற்ற மகனும்!`

**Status: PARTIAL — audited through scan 149.**

- opening boundary **147→148: PASS**;
- title scan 148 visibly reads `மாண்பு நிறை தாயும் மாசற்ற மகனும்!`, omitting the comma after `தாயும்` found in the contents witness;
- join **148→149: PASS** — `அத்தனை அழகுகளும் அணி வகுத்துப் / படைத்த பெண்ணுருவே தான் ;` continues as `பைங்கிளி மாதவி என்கிற போது ; ...`;
- scan 149 ends mid-continuation at `நேரிலே கோரிக்கை வைக்கத்தான்” என்றும்,`;
- item 31 therefore remains open. Join **149→150** is the first check of the next 25-scan iteration;
- internal joins audited so far: **1/3 PASS**;
- dropped/duplicated text detected so far: **none**.

## Source-sensitive readings preserved

No Phase-2 source reading was normalized in this pass. Among the forms retained are `வாணியது`, `தூமப்பணிகளாக`, `தமிழ்ச்சியர்`, `பத்தரை மாற்றுப் பொன்னெனத்`, `நல் வெள்ளியார்`, `ஊண்பித்தையார்`, `அஷ்டமாசித்தி`, `கலாம் விளைக்கும்`, `சாகிரப்`, `குருக்கர்`, `ஆரப்பா`, `மொகஞ்சதாரோ`, `அசுரா`, `காந்திரதோவ்`, `ஒனசு`, `எரிது`, `அய்வரும்`, `அழுந்தார்`, `வணங்கி பேற்றிட`, `எடுத்தனன்`, `முரசமொன்று`, `தணித்துக் கொள்வோம்`, `வாணிக்க`, and `இதயமா`.

## Exact next activity

Process **physical scans 150–174** as the next 25-page Phase-3 iteration, beginning with item 31's pending join **149→150**. Do not begin canonical Tamil assembly yet.