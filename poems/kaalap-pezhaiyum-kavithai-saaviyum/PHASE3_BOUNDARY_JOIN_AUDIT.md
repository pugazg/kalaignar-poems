# Phase 3 boundary and page-join audit — காலப் பேழையும் கவிதைச் சாவியும்

## Scope

This audit follows completion of Phase 2 for all **306/306 physical scans** and completion of the Phase-3 physical-scan ↔ printed-page reconciliation.

For each of the **58 numbered items**, certify the opening boundary, every within-item physical-page join, the closing boundary, quotation/separator continuity, item metadata consistency, and contents/title-page witness differences. The controlling scan remains the highest authority. Source anomalies are preserved rather than silently repaired.

Canonical Tamil assembly remains blocked until all 58 items pass this audit.

## Iteration policy

Beginning with the current checkpoint, routine Phase-3 boundary/join work is processed in **25-physical-scan iterations**. An iteration may end inside an item; in that case the inspected joins are recorded durably but the item is not marked certified until its full physical range and closing boundary have been checked.

## Progress

- items certified: **13/58**
- last fully certified item: **13 — `காரவேலன் கண்டு நடுங்கிய கட்டுக்குலையாக் கூட்டணி!`**
- current partially audited item: **14 — `கனக விஜயர் கல் சுமந்த வரலாறு!`**, through scan **74 / printed page 73**
- current 25-scan iteration completed: **scans 50–74**
- unresolved structural joins: **none**
- source-level abrupt transitions preserved without normalization: **scan 31→32**
- next 25-scan iteration: **scans 75–99**

## Certified-item register

| Item | Title | Physical scans | Printed pages | Internal joins | Result |
|---:|---|---|---|---:|---|
| 1 | `பொது உலகம்` | 10–11 | 9–10 | 1/1 | PASS |
| 2 | `படிமுறை வளர்ச்சி` | 12–15 | 11–14 | 3/3 | PASS |
| 3 | `‘காந்தக்கல்’ கதையொன்று!` | 16–19 | 15–18 | 3/3 | PASS |
| 4 | `அன்றிருந்த கற்காலம் - இனி அமையாவிடின் நற்காலம்!` | 20–24 | 19–23 | 4/4 | PASS |
| 5 | `தங்க மனம் வேண்டும்; அது தந்திடும் அன்பு வேண்டும்!` | 25–28 | 24–27 | 3/3 | PASS |
| 6 | `கத்தி பகைவுடையது; இரத்தம் நாம் தருவது!` | 29–34 | 28–33 | 5/5 | PASS |
| 7 | `வரலாற்றுக் காலத்தின் கோலம்!` | 35–39 | 34–38 | 4/4 | PASS |
| 8 | `நெற்றி வியர்வை உதிர; நெஞ்செலும்பு ஒடிய!` | 40–43 | 39–42 | 3/3 | PASS |
| 9 | `உரையாடல் உணர்த்திடும் உண்மை என்ன?` | 44–49 | 43–48 | 5/5 | PASS |
| 10 | `பழந்தமிழர் பன்னாட்டுத் தொடர்பு!` | 50–53 | 49–52 | 3/3 | PASS |
| 11 | `ஆங்காங்கு அடையாள முத்திரைகள்!` | 54–57 | 53–56 | 3/3 | PASS |
| 12 | `வரலாற்றுப் பூங்காவில் வள்ளித் திருமணம்!` | 58–63 | 57–62 | 5/5 | PASS |
| 13 | `காரவேலன் கண்டு நடுங்கிய கட்டுக்குலையாக் கூட்டணி!` | 64–67 | 63–66 | 3/3 | PASS |

## Current 25-scan iteration — scans 50–74

### Item 10 — `பழந்தமிழர் பன்னாட்டுத் தொடர்பு!`

**Status: PASS — fully certified.**

- opening boundary 49→50: **PASS** — item 9 ends with `உறுதி! உறுதி! உறுதி!` and an ornament; scan 50 visibly begins item number 10 and the correct title;
- join 50→51: **PASS** — `உறுதி நல்கும் பெரு முயற்சி` continues as `பெருங்கடல் கலம் விடுத்து ; அது`;
- join 51→52: **PASS** — scan 51 closes `தெரிவித்து மகிழ்கின்றேன்.` and scan 52 starts the next paragraph `மற்றொரு செய்தியும் உண்டு ; நாம்`;
- join 52→53: **PASS** — `கடைச் சங்கத் தமிழ் இலக்கியங்கள்` continues directly as `கண்டறிந்து நவில்கின்றன என்றும் ; அந்த`;
- closing boundary 53→54: **PASS** — scan 53 ends after the `பாபிரசு` explanatory note and printed ornament; scan 54 begins item 11;
- title-witness difference: **none**;
- dropped/duplicated text: **none**.

### Item 11 — `ஆங்காங்கு அடையாள முத்திரைகள்!`

**Status: PASS — fully certified.**

- opening boundary 53→54: **PASS**;
- join 54→55: **PASS** — the source quotation on scan 54 closes completely; scan 55 explicitly resumes from the same `ஆபுத்திரன் நாட டைந்த காதை` evidence;
- join 55→56: **PASS** — `கவர்ச்சிமிகு ஓவியமொன்றை உரைநடையில் தீட்டியுள்ளார்.` is followed by `நானதில் பழைய வரலாறும் படித்து`;
- join 56→57: **PASS** — direct continuation `நாகரிகப் பண்பாட்டின் உறைவிடமாய்` → `இருந்தன என்பதற்கு எடுத்துக் காட்டாகத் தான்`;
- closing boundary 57→58: **PASS** — scan 57 closes with `பங்களிக்கும் பெரும் பொறுப்பும் நமக்கு உண்டு!` and ornament; scan 58 begins item 12;
- title-witness difference: **none**;
- dropped/duplicated text: **none**.

### Item 12 — `வரலாற்றுப் பூங்காவில் வள்ளித் திருமணம்!`

**Status: PASS — fully certified.**

- opening boundary 57→58: **PASS**;
- join 58→59: **PASS** — `அவ்வடிவ லிங்கம் அநாகரிகமெனக் கேலி புரிந்தோர் -` continues as `அடி முட்டாள்தனமென ஆத்திரமுற்றோர்`;
- join 59→60: **PASS** — `ஆரிய சுப்பிரமணியன் ஸ்கந்தன் எனப்` continues into `பழகிட வடமொழியில் பக்தி ரசப் / பயிற்சியளித்து விட்டார்.`;
- join 60→61: **PASS** — the தினைப்புனம் காவல் திட்டம் closes on scan 60 and its implementation begins on scan 61;
- join 61→62: **PASS** — `வனவேடன் ஒருவன் கன வேகமாய் ஓடிவந்து ;` is followed immediately by the hunter's dialogue;
- join 62→63: **PASS** — the quotation opened near the end of scan 62 continues with `ஆனைக்குக் கூட அஞ்சாமல்...` and closes on scan 63; no quotation mark is invented or dropped;
- closing boundary 63→64: **PASS** — glossary/citation material is complete and followed by an ornament before item 13 begins;
- title-witness difference: **none**;
- dropped/duplicated text: **none**.

#### Structural metadata correction discovered in item 12

Scan 58 already used the title-derived canonical section id `item-12-varalattrup-poongaavil-vallith-thirumanam`, while scans 59–63 still carried the older abbreviated id `item-12-valli-thirumanam`. This would split one source item at assembly time. The front-matter `section` field on scans **59–63** was aligned to the scan-58 canonical id. **No poem text, punctuation, source spelling or lineation was changed.**

Source-sensitive forms including `பெருளான்`, `அவர் ஆராய்`, `பூவைகாள்`, `புறவங்காள்`, `மயில்காள்`, `மணிக்கிளிகாள்`, `குயில்காள்`, `போன்றுவீழ்வது`, and `என் மகளாயின்` remain unchanged.

### Item 13 — `காரவேலன் கண்டு நடுங்கிய கட்டுக்குலையாக் கூட்டணி!`

**Status: PASS — fully certified.**

- opening boundary 63→64: **PASS**;
- join 64→65: **PASS** — `எடுத்தியம்புகின்றேன் –` continues as `இவற்றுக்கு ஆதாரமாகப் பன்மொழிப் புலவர்...`;
- join 65→66: **PASS** — the quoted historical passage ending scan 65 with `வட ஆரியர் படை கடந்து / தென் தமிழ்நாடு ஒருங்கு காணப்` continues on scan 66 and closes with `நெடுஞ்செழியன்”`;
- join 66→67: **PASS** — the preceding quotation/evidence closes before the next historical comparison begins;
- closing boundary 67→68: **PASS** — scan 67 closes with `செருப்பாழி = போர்க்களப் பாசறை.` and ornament; scan 68 begins item 14;
- title-witness difference: **none**;
- dropped/duplicated text: **none**.

Source-sensitive forms including `தொலைவடவர்`, `நேடியாட்சியாகவோ`, `ஒருசன்`, `புனரதீர்`, and `கைப்பா` remain unchanged.

### Item 14 — `கனக விஜயர் கல் சுமந்த வரலாறு!`

**Status: PARTIAL — scans 68–74 audited; item not yet certifiable.**

- opening boundary 67→68: **PASS** — scan 67 closes item 13 with an ornament and scan 68 visibly begins item number 14 with the contents-matching title;
- join 68→69: **PASS** — scan 68 closes its introductory historical framing; scan 69 continues into the Karikalan/Senguttuvan framing and `காட்சி 1` without a source gap;
- join 69→70: **PASS** — dialogue `உங்களில் ஒருவர்` continues directly as `ஜெயித்து விட்டால், அந்தப் பெண்ணை...`;
- join 70→71: **PASS** — the poet's `கண்டதே இல்லை.....` is answered by `கனகர் : அதையும் பார்த்து விடுவோம்.`;
- join 71→72: **PASS** — scene 1 closes with the repeated `சேரன் செங்குட்டுவன்!!`; scan 72 explicitly begins `காட்சி 2.`;
- join 72→73: **PASS** — the minister's `மட்டும் ஏன் மன்னவா?` is answered directly by `சேரன் : தமிழன் என்பதால்...`;
- join 73→74: **PASS** — `இகழ்ந்தார்கள்,` continues directly as `இகழ்ந்தவர்கள், இன்னும்`;
- scan 74 ends mid-sentence with `களத்திலே நமது தலைகள் / பறி போகலாம்! ஆனால் கனல்`;
- therefore item 14 remains **open**, with joins **6/9** audited so far. The next iteration must resume with boundary join **74→75**, then continue through the item closing boundary before certification.

Source-sensitive dialogue forms and physical line splits, including `மண்டூகே`, `அறிந்திலராகிச்`, `துவேன்`, `பொழிவும்`, `சிலதுகள்`, `தோரணங்கற்பட்டு`, and `கோட்டைகளிலுள்ள`, remain unchanged.

## Exact next activity

Process the next **25 physical scans: 75–99**. Resume item 14 with join **74→75**, finish and certify item 14 if its remaining joins and closing boundary pass, then continue consecutively through the batch. Do not begin canonical Tamil assembly yet.