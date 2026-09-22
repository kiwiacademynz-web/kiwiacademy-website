#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import page, page_hero, icon, SITE_NAME  # noqa

# ============================================================ TRAIL SVG (home hero)
TRAIL_SVG = """
<svg viewBox="0 0 480 660" role="img" aria-labelledby="trailTitle trailDesc">
  <title id="trailTitle">The route to nursing registration in New Zealand</title>
  <desc id="trailDesc">A trail from where you are now, through OET or IELTS, IQN theory training and OSCE clinical training, to becoming a registered nurse in New Zealand.</desc>
  <path class="trail__path-bg" pathLength="1" d="M64,58 Q210,34 340,150 Q252,214 128,296 Q300,342 372,438 Q300,520 150,576" />
  <path class="trail__path" pathLength="1" d="M64,58 Q210,34 340,150 Q252,214 128,296 Q300,342 372,438 Q300,520 150,576" />

  <g class="trail__node trail__node--you" style="animation-delay:.5s">
    <circle cx="64" cy="58" r="23" />
    <text class="n" x="64" y="64">1</text>
  </g>
  <text class="trail__label" x="64" y="112" text-anchor="middle">You, today</text>
  <text class="trail__sub" x="64" y="132" text-anchor="middle">Kerala &middot; RN/RM</text>

  <g class="trail__node trail__node--kna" style="animation-delay:1s">
    <circle cx="340" cy="150" r="23" />
    <text class="n" x="340" y="156">2</text>
  </g>
  <text class="trail__label" x="422" y="130" text-anchor="middle">OET / IELTS</text>
  <text class="trail__sub" x="422" y="150" text-anchor="middle">NCNZ band score</text>

  <g class="trail__node trail__node--kna" style="animation-delay:1.5s">
    <circle cx="128" cy="296" r="23" />
    <text class="n" x="128" y="302">3</text>
  </g>
  <text class="trail__label" x="128" y="352" text-anchor="middle">IQN theory exam</text>
  <text class="trail__sub" x="128" y="372" text-anchor="middle">Pearson VUE</text>

  <g class="trail__node trail__node--kna" style="animation-delay:2s">
    <circle cx="372" cy="438" r="23" />
    <text class="n" x="372" y="444">4</text>
  </g>
  <text class="trail__label" x="372" y="398" text-anchor="middle">OSCE</text>
  <text class="trail__sub" x="372" y="490" text-anchor="middle">Christchurch, in person</text>

  <g class="trail__node trail__node--kna" style="animation-delay:2.5s">
    <circle cx="150" cy="576" r="25" />
    <text class="n" x="150" y="582">5</text>
  </g>
  <text class="trail__label" x="150" y="626" text-anchor="middle">Registered nurse, NZ</text>
</svg>
"""

HOME_HERO = """<div class="topo hero">
  <div class="wrap hero__grid">
    <div>
      <h1>The route from Kerala to a registered-nurse role in New Zealand.</h1>
      <p class="lead">Kiwi Nurse Academy trains internationally qualified nurses for the three exams the Nursing Council of New Zealand actually asks for: OET or IELTS, the IQN theoretical exam, and the OSCE. One centre, one plan, no guesswork about what comes next.</p>
      <ul class="hero__proof">
        <li>{c1} Coaching built around NCNZ's current three-step competence pathway, not the old paperwork-only process</li>
        <li>{c2} OSCE simulation practice on the same station format used at Nurse Maude, Christchurch</li>
        <li>{c3} Small batches, so every candidate gets corrected speaking and writing practice, not just recordings</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--kowhai" data-wa href="#">{wa} Talk to a counsellor</a>
        <a class="btn btn--ghost" href="courses/index.html">See all courses</a>
      </div>
    </div>
    <div class="trail" aria-hidden="false">
      {trail}
      <div class="trail__legend">
        <span><i class="k"></i> Trained at Kiwi Nurse Academy</span>
        <span><i></i> Milestone you reach</span>
      </div>
    </div>
  </div>
</div>""".format(c1=icon("check-circle"), c2=icon("check-circle"), c3=icon("check-circle"), wa=icon("whatsapp"), trail=TRAIL_SVG)

HOME_ROUTES = """<div class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Three exams. One route to registration.</h2>
      <p>NCNZ only registers you once you've cleared all three. Most candidates lose months by preparing for them in the wrong order, or under-preparing for the one that feels "easiest." We plan your route first, then train you for it.</p>
    </div>
    <ol class="routes">
      <li class="route route--oet">
        <div>
          <h3>OET Preparation</h3>
          <p class="route__for">For nurses who haven't yet met NCNZ's English-language requirement.</p>
        </div>
        <div>
          <p>NCNZ requires a minimum OET score of 350 in reading, listening and speaking, and 300 in writing &mdash; or 7.0/7.0/7.0/6.5 on IELTS Academic. We drill each sub-test against the healthcare-specific format so your score reflects your real clinical English, not just test technique.</p>
          <ul class="route__facts">
            <li>All 4 sub-tests covered</li>
            <li>Speaking role-plays with feedback</li>
            <li>Score can be built across sittings within 12 months</li>
          </ul>
        </div>
        <a class="btn btn--line btn--small" href="courses/oet-preparation.html">OET details</a>
      </li>
      <li class="route route--iqn">
        <div>
          <h3>IQN Training</h3>
          <p class="route__for">For nurses ready to sit NCNZ's online theoretical examination.</p>
        </div>
        <div>
          <p>The IQN theoretical exam is taken at a Pearson VUE centre and covers medication safety and nursing knowledge against New Zealand's clinical standards and scope of practice &mdash; not your home country's. We rebuild your theory around that difference.</p>
          <ul class="route__facts">
            <li>Part A: medication safety</li>
            <li>Part B: nursing knowledge</li>
            <li>Timed mock exams, Pearson VUE format</li>
          </ul>
        </div>
        <a class="btn btn--line btn--small" href="courses/iqn-training.html">IQN details</a>
      </li>
      <li class="route route--osce">
        <div>
          <h3>OSCE Training</h3>
          <p class="route__for">For nurses invited to the clinical competence assessment.</p>
        </div>
        <div>
          <p>The clinical competence assessment is a 2-day orientation and preparation course followed by an OSCE at Nurse Maude, Christchurch &mdash; both taken in person. We run the same station structure in our simulation lab so the real thing feels like a repeat, not a surprise.</p>
          <ul class="route__facts">
            <li>Station-by-station simulation drills</li>
            <li>Cultural-safety &amp; tikanga orientation</li>
            <li>Communication &amp; escalation practice</li>
          </ul>
        </div>
        <a class="btn btn--line btn--small" href="courses/osce-training.html">OSCE details</a>
      </li>
    </ol>
  </div>
</div>"""

CHOOSER_DATA = {
    "start": {
        "kicker": "Start here",
        "title": "Let's find your next step",
        "body": "Answer the question on the left and we'll point you to the exact stage of the pathway you should train for next.",
        "links": [{"href": "contact.html", "label": "Or just book a free call"}],
    },
    "no-english": {
        "kicker": "Next step: OET or IELTS",
        "title": "Sit your English test first",
        "body": "NCNZ won't progress your file without a passing OET or IELTS Academic score. Start here so the rest of your pathway isn't held up later.",
        "links": [{"href": "courses/oet-preparation.html", "label": "See OET Preparation"}],
    },
    "has-english": {
        "kicker": "Next step: IQN Theory",
        "title": "Prepare for the theoretical exam",
        "body": "With English sorted, the online theoretical exam at Pearson VUE is next. It tests New Zealand medication safety and nursing knowledge specifically.",
        "links": [{"href": "courses/iqn-training.html", "label": "See IQN Training"}],
    },
    "invited-osce": {
        "kicker": "Next step: OSCE",
        "title": "Train for your clinical exam",
        "body": "You've been invited to the clinical competence assessment. This is a 2-day orientation plus a 3-hour OSCE in Christchurch, taken in person — simulation practice matters most now.",
        "links": [{"href": "courses/osce-training.html", "label": "See OSCE Training"}],
    },
    "unsure": {
        "kicker": "Not sure yet — that's fine",
        "title": "Get a free pathway assessment",
        "body": "Send us your qualification, registration and English-test status and we'll map your exact route, in writing, before you commit to anything.",
        "links": [{"href": "contact.html", "label": "Book a free pathway call"}],
    },
}

HOME_CHOOSER = """<div class="section section--mist">
  <div class="wrap">
    <div class="chooser" data-chooser='{data}'>
      <div class="chooser__q">
        <h2>Where are you on the pathway right now?</h2>
        <div class="chooser__opts" role="group" aria-label="Choose your current stage">
          <button class="chooser__opt" type="button" data-key="no-english" aria-pressed="false">I haven't passed OET or IELTS yet</button>
          <button class="chooser__opt" type="button" data-key="has-english" aria-pressed="false">I've passed English, need IQN theory</button>
          <button class="chooser__opt" type="button" data-key="invited-osce" aria-pressed="false">I've been invited to sit the OSCE</button>
          <button class="chooser__opt" type="button" data-key="unsure" aria-pressed="false">I'm honestly not sure</button>
        </div>
      </div>
      <div class="chooser__out" data-chooser-out>
        <p class="kicker">Start here</p>
        <h3>Let's find your next step</h3>
        <p>Answer the question on the left and we'll point you to the exact stage of the pathway you should train for next.</p>
      </div>
    </div>
  </div>
</div>""".format(data=json.dumps(CHOOSER_DATA).replace("'", "&#39;"))

HOME_METHOD = """<div class="topo section section--fiord">
  <div class="wrap">
    <div class="section-head">
      <h2>How we teach, station by station</h2>
      <p>Nursing exams in New Zealand test judgement under pressure, not memorised answers. Our method is built around that.</p>
    </div>
    <dl class="defs">
      <div>
        <dt>Diagnostic first</dt>
        <dd>Before you join a batch, we assess your current OET/IELTS band, theory gaps and clinical communication style, so your study plan targets what's actually missing.</dd>
      </div>
      <div>
        <dt>Small live batches</dt>
        <dd>Classes stay small enough that every speaking task and every OSCE station gets individual, recorded feedback &mdash; not a group correction at the end.</dd>
      </div>
      <div>
        <dt>New Zealand context, not generic nursing</dt>
        <dd>Medication safety, escalation language, cultural safety and tikanga are taught the way NCNZ examines them, using their own published handbooks as the baseline.</dd>
      </div>
      <div>
        <dt>Full-length mock exams</dt>
        <dd>Timed IQN mocks in the Pearson VUE format and full OSCE station walkthroughs in our simulation lab, so exam day is the least stressful part of the journey.</dd>
      </div>
    </dl>
  </div>
</div>"""

HOME_STORIES = """<div class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>What candidates say</h2>
      <p>Real stories from our students are being collected as the first batches complete their exams &mdash; check back soon, or ask us to connect you directly with a recent graduate.</p>
    </div>
    <div class="stories">
      <div class="story">
        <blockquote>&ldquo;Add your first testimonial here once a candidate agrees to be featured &mdash; keep it specific: which exam, what score, what changed.&rdquo;</blockquote>
        <div class="story__who"><span class="avatar">?</span><span><b>Candidate name</b>IQN &middot; batch month/year</span></div>
      </div>
      <div class="story">
        <blockquote>&ldquo;A second testimonial slot &mdash; OSCE candidates responding well to simulation-lab practice is a strong story to capture early.&rdquo;</blockquote>
        <div class="story__who"><span class="avatar">?</span><span><b>Candidate name</b>OSCE &middot; batch month/year</span></div>
      </div>
      <div class="story">
        <blockquote>&ldquo;A third slot for an OET success story &mdash; a before/after band score is the most persuasive detail you can include.&rdquo;</blockquote>
        <div class="story__who"><span class="avatar">?</span><span><b>Candidate name</b>OET &middot; batch month/year</span></div>
      </div>
    </div>
  </div>
</div>"""

HOME_BODY = HOME_HERO + HOME_ROUTES + HOME_CHOOSER + HOME_METHOD + HOME_STORIES

page(
    "index.html",
    "Kiwi Nurse Academy — IQN, OSCE & OET Training for New Zealand Registration",
    "IQN theory, OSCE clinical and OET/IELTS training for internationally qualified nurses moving to New Zealand. Kerala-based classroom and simulation training.",
    "index.html", "",
    HOME_BODY,
)
print("home done")

# ============================================================ SHARED FAQ ACCORDION HELPER
def accordion(qas, group_title=None):
    rows = []
    for q, a in qas:
        rows.append('<details><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>'.format(q=q, a=a))
    body = '<div class="accordion">' + "".join(rows) + '</div>'
    if group_title:
        return '<div class="faq-group"><h2>{t}</h2>{b}</div>'.format(t=group_title, b=body)
    return body


# ============================================================ COURSES INDEX
COURSES_HERO = page_hero(
    '<a href="../index.html">Home</a><span>/</span>Courses',
    "Three courses, mapped to NCNZ's own three-step pathway.",
    "We don't teach generic nursing English or generic exam tips. Each course targets the exact exam the Nursing Council of New Zealand sets, in the order most candidates need it.",
)

COURSES_COMPARE = """<div class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Compare the three courses</h2>
      <p>Not sure which one you need right now? The table below shows what each course covers and who it's for. You can also use the pathway chooser on the home page.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Course</th><th>Tests</th><th>Who it's for</th><th>Format</th><th></th></tr>
        </thead>
        <tbody>
          <tr>
            <th><span class="pill pill--oet">OET Preparation</span></th>
            <td>OET (all 4 sub-tests) or IELTS Academic</td>
            <td>Nurses who haven't yet met NCNZ's English-language requirement</td>
            <td>Live online + in-centre speaking practice</td>
            <td><a class="btn btn--line btn--small" href="oet-preparation.html">View course</a></td>
          </tr>
          <tr>
            <th><span class="pill pill--iqn">IQN Training</span></th>
            <td>IQN theoretical exam (Pearson VUE)</td>
            <td>Nurses ready to sit the online theory exam</td>
            <td>Live online classes + timed mock exams</td>
            <td><a class="btn btn--line btn--small" href="iqn-training.html">View course</a></td>
          </tr>
          <tr>
            <th><span class="pill pill--osce">OSCE Training</span></th>
            <td>Orientation &amp; preparation course + OSCE</td>
            <td>Nurses invited to the clinical competence assessment</td>
            <td>In-centre simulation lab, hands-on stations</td>
            <td><a class="btn btn--line btn--small" href="osce-training.html">View course</a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>"""

COURSES_ORDER = """<div class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <h2>Which order should you take them in?</h2>
      <p>NCNZ's process is sequential, and skipping ahead usually backfires. Here's the order that works for most candidates.</p>
    </div>
    <ol class="timeline">
      <li class="is-kna"><span class="tag tag--kna">Step 1</span><h3>English language test</h3><p>Sit OET or IELTS Academic before anything else. NCNZ's minimums are fixed &mdash; OET 350/350/350/300, or IELTS 7.0/7.0/7.0/6.5 &mdash; and you can combine scores across sittings within 12 months. Getting this out of the way early means it never becomes the thing holding up your file.</p></li>
      <li><span class="tag tag--you">Your side</span><h3>Submit your NCNZ application</h3><p>Apply to the Nursing Council with your qualification documents, registration history and English evidence. NCNZ will tell you whether you're directed to complete a competence assessment.</p></li>
      <li class="is-kna"><span class="tag tag--kna">Step 2</span><h3>IQN theoretical exam</h3><p>If directed, you'll sit the online theory exam at an accredited Pearson VUE centre, covering medication safety and nursing knowledge against New Zealand's clinical standards.</p></li>
      <li class="is-kna"><span class="tag tag--kna">Step 3</span><h3>Orientation, preparation &amp; OSCE</h3><p>Once you pass the theory exam, you'll be invited to a 2-day orientation and preparation course followed by the OSCE &mdash; both held in person in Christchurch.</p></li>
      <li><span class="tag tag--you">Your side</span><h3>Registration &amp; move</h3><p>Once every step is passed, NCNZ processes your registration. From there it's visa, travel and settling into your first New Zealand role.</p></li>
    </ol>
  </div>
</div>"""

page(
    "courses/index.html",
    "Courses — IQN, OSCE & OET Training | Kiwi Nurse Academy",
    "Compare Kiwi Nurse Academy's IQN theory, OSCE clinical and OET/IELTS preparation courses, and see the order most nurses take them in on the way to NZ registration.",
    "courses/index.html", "../",
    COURSES_HERO + COURSES_COMPARE + COURSES_ORDER,
)

# ============================================================ IQN TRAINING PAGE
IQN_HERO = page_hero(
    '<a href="../index.html">Home</a><span>/</span><a href="index.html">Courses</a><span>/</span>IQN Training',
    "IQN Training",
    "Prepare for the Nursing Council of New Zealand's online theoretical examination &mdash; the test of your medication safety and nursing knowledge against New Zealand's own clinical standards.",
    ["Pearson VUE format", "Part A + Part B covered", "Live classes + timed mocks"],
)

IQN_INTRO = """<div class="section">
  <div class="wrap split split--wide-left">
    <div class="stack">
      <h2>What the IQN theoretical exam actually tests</h2>
      <p>Since 2023, NCNZ assesses internationally qualified nurses by direct testing rather than relying only on paperwork. If you're directed to a competence assessment, the first stage is an online theoretical exam sat at an accredited Pearson VUE centre, either overseas or in New Zealand.</p>
      <p>The exam has two parts, and both are based on New Zealand's own domestic State Final Examination standard &mdash; not a generic international nursing syllabus:</p>
      <ul class="tick-list">
        <li><strong>Part A &mdash; Medication safety.</strong> Calculation, administration and safety-checking questions set against New Zealand medicines and protocols.</li>
        <li><strong>Part B &mdash; Nursing knowledge.</strong> Scenario-based questions on assessment, clinical reasoning, prioritisation and scope of practice as defined in Aotearoa.</li>
      </ul>
      <p>Most candidates who don't prepare specifically for this exam lose marks not because their nursing is weak, but because the expected answer follows a New Zealand protocol that differs from what they trained under. That's the gap our course closes.</p>
    </div>
    <aside class="note note--jade">
      <p><strong>Good to know</strong></p>
      <p>Not every IQN is directed to sit a competence assessment &mdash; NCNZ assesses this after your application. If you're not sure whether you'll need this exam, we can review your qualification and registration history on a free call.</p>
    </aside>
  </div>
</div>"""

IQN_SYLLABUS = """<div class="section section--mist">
  <div class="wrap">
    <div class="section-head">
      <h2>What's covered in the course</h2>
    </div>
    <dl class="facts">
      <div><dt>Format</dt><dd>Live online classes, 3 sessions a week, plus recorded sessions for revision.</dd></div>
      <div><dt>Duration</dt><dd>Typically 6&ndash;8 weeks, depending on your starting point &mdash; confirmed after your diagnostic assessment.</dd></div>
      <div><dt>Part A focus</dt><dd>Drug calculations, medication administration rights, high-alert medicines, and documentation standards used in New Zealand practice.</dd></div>
      <div><dt>Part B focus</dt><dd>Clinical scenarios covering adult, maternal, mental health and paediatric nursing, escalation of care, and New Zealand's scope-of-practice framework.</dd></div>
      <div><dt>Practice exams</dt><dd>Full-length, timed mock exams that mirror the Pearson VUE interface, with a detailed score breakdown after each attempt.</dd></div>
      <div><dt>Support</dt><dd>Doubt-clearing sessions and a study group so you're never preparing alone.</dd></div>
    </dl>
  </div>
</div>"""

IQN_FAQ = accordion([
    ("Where do I sit the actual exam?", "The IQN theoretical exam is delivered through Pearson VUE's accredited test centres, which operate both in New Zealand and internationally, including in India. We'll help you book a centre near you once you're ready."),
    ("Do I need to pass Part A and Part B together?", "Check your specific requirement with NCNZ when they issue your competence assessment direction &mdash; our course prepares you for both parts fully regardless, so you're ready either way."),
    ("What happens if I don't pass?", "NCNZ allows re-sits. We offer a revision-focused top-up track for candidates who need to re-sit, targeted at the specific part and topics you were short on."),
    ("Can I start IQN training before I've passed OET or IELTS?", "You can start building your theory knowledge in parallel, but NCNZ will need your English-language evidence as part of your application. We usually recommend clearing English first so nothing holds up your file."),
], "IQN Training FAQs")

page(
    "courses/iqn-training.html",
    "IQN Training — NCNZ Theoretical Exam Preparation | Kiwi Nurse Academy",
    "Prepare for the Nursing Council of New Zealand's IQN theoretical exam (Pearson VUE) covering medication safety and nursing knowledge. Live classes and timed mock exams.",
    "courses/iqn-training.html", "../",
    IQN_HERO + IQN_INTRO + IQN_SYLLABUS + '<div class="section"><div class="wrap">' + IQN_FAQ + '</div></div>',
)

# ============================================================ OSCE TRAINING PAGE
OSCE_HERO = page_hero(
    '<a href="../index.html">Home</a><span>/</span><a href="index.html">Courses</a><span>/</span>OSCE Training',
    "OSCE Training",
    "Simulation-lab preparation for the clinical competence assessment: the 2-day orientation and preparation course, and the objective structured clinical examination held in Christchurch.",
    ["2-day OPC + 3-hour OSCE", "Nurse Maude station format", "In-person simulation lab"],
)

OSCE_INTRO = """<div class="section">
  <div class="wrap split split--wide-left">
    <div class="stack">
      <h2>What the clinical competence assessment involves</h2>
      <p>Once you pass the IQN theoretical exam, NCNZ invites you to the clinical competence assessment. This has two parts, both taken in person in Christchurch:</p>
      <ul class="tick-list">
        <li><strong>Two-day orientation and preparation course (OPC).</strong> Covers cultural safety, whānau-centred care and tikanga, an overview of the New Zealand health system, communication and escalation skills, and hands-on familiarisation with the clinical equipment and OSCE format.</li>
        <li><strong>Objective structured clinical examination (OSCE).</strong> A roughly three-hour exam held at an accredited simulation and assessment centre in Christchurch, made up of timed stations that each test a specific clinical skill in a simulated setting.</li>
      </ul>
      <p>The OSCE format has been used internationally &mdash; including in Australia, Canada and the UK &mdash; for decades, so it's well understood. What trips candidates up isn't the format, it's the New Zealand-specific detail inside each station: the exact phrasing expected when escalating a concern, the equipment layout, and the cultural-safety framing examiners are listening for.</p>
    </div>
    <aside class="note note--warn">
      <p><strong>This exam is taken in person, no exceptions</strong></p>
      <p>Both the orientation course and the OSCE must be attended in New Zealand &mdash; there's no remote or online sitting for the clinical stage. Our job is to make sure the trip is a formality, not a gamble.</p>
    </aside>
  </div>
</div>"""

OSCE_STATIONS = """<div class="section section--fiord topo">
  <div class="wrap">
    <div class="section-head">
      <h2>How we train for it</h2>
      <p>Our simulation lab is set up to mirror the station structure candidates report from the real OSCE, so the exam day itself becomes familiar ground.</p>
    </div>
    <dl class="defs">
      <div><dt>Station walkthroughs</dt><dd>Full run-throughs of common station types &mdash; medication administration, wound care, patient assessment, and escalation scenarios &mdash; with a marker's-eye view of what's being scored.</dd></div>
      <div><dt>Communication drills</dt><dd>Structured practice on handover language, SBAR-style escalation, and culturally safe communication with patients and whānau.</dd></div>
      <div><dt>Equipment familiarisation</dt><dd>Hands-on time with the manikins, monitors and documentation formats used in New Zealand simulation and assessment centres.</dd></div>
      <div><dt>Timed mock OSCEs</dt><dd>Full mock exams under real time pressure, with individual video-reviewed feedback after every station, not just a group debrief.</dd></div>
    </dl>
  </div>
</div>"""

OSCE_TIMELINE = """<div class="section">
  <div class="wrap">
    <div class="section-head"><h2>Your OSCE week, station by station</h2></div>
    <ol class="timeline">
      <li class="is-kna"><span class="tag tag--kna">With us</span><h3>Weeks before: simulation practice</h3><p>Station drills, mock OSCEs and communication coaching at our Kerala centre, building both clinical accuracy and exam-day composure.</p></li>
      <li><span class="tag tag--you">In NZ</span><h3>Day 1&ndash;2: Orientation &amp; preparation course</h3><p>In-person at an accredited centre &mdash; cultural safety, the NZ health system, escalation skills, and hands-on time with the exact equipment you'll be assessed on.</p></li>
      <li><span class="tag tag--you">In NZ</span><h3>OSCE day</h3><p>The roughly three-hour clinical exam at the simulation and assessment centre in Christchurch, moving station to station against the clock.</p></li>
      <li><span class="tag tag--you">After</span><h3>Results &amp; registration</h3><p>NCNZ notifies you of your result. A pass completes your competence assessment, clearing the way to registration.</p></li>
    </ol>
  </div>
</div>"""

OSCE_FAQ = accordion([
    ("Can I do the OSCE training itself online?", "The orientation course and OSCE exam must be attended in person in New Zealand. Our preparation training beforehand is delivered in our Kerala simulation lab, with an online option for the theory and communication components."),
    ("What if I don't pass the OSCE?", "NCNZ allows candidates to re-sit. We run a focused re-sit track targeting the specific stations you were marked down on, rather than repeating the whole course."),
    ("Do you help with travel, accommodation or visas for the NZ trip?", "We can point you to trusted local contacts and give you a checklist for the trip, though visa advice itself should come from a licensed immigration adviser. Ask us on a call and we'll be upfront about what we can and can't help with directly."),
], "OSCE Training FAQs")

page(
    "courses/osce-training.html",
    "OSCE Training — Clinical Simulation Preparation | Kiwi Nurse Academy",
    "Simulation-lab OSCE preparation for NCNZ's clinical competence assessment: orientation course content, station drills, and mock OSCEs before your Christchurch exam.",
    "courses/osce-training.html", "../",
    OSCE_HERO + OSCE_INTRO + OSCE_STATIONS + OSCE_TIMELINE + '<div class="section"><div class="wrap">' + OSCE_FAQ + '</div></div>',
)

# ============================================================ OET PREPARATION PAGE
OET_HERO = page_hero(
    '<a href="../index.html">Home</a><span>/</span><a href="index.html">Courses</a><span>/</span>OET Preparation',
    "OET Preparation",
    "Reach NCNZ's English-language requirement with healthcare-specific OET (or IELTS Academic) coaching across all four sub-tests.",
    ["OET or IELTS Academic", "All 4 sub-tests", "Scores can be combined within 12 months"],
)

OET_INTRO = """<div class="section">
  <div class="wrap split split--wide-left">
    <div class="stack">
      <h2>NCNZ's English-language requirement</h2>
      <p>Every internationally qualified nurse must demonstrate English-language competence before registration. NCNZ accepts two tests, each with its own minimum bands:</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Test</th><th>Reading</th><th>Listening</th><th>Speaking</th><th>Writing</th></tr></thead>
          <tbody>
            <tr><th>OET</th><td>350</td><td>350</td><td>350</td><td>300</td></tr>
            <tr><th>IELTS Academic</th><td>7.0</td><td>7.0</td><td>7.0</td><td>6.5</td></tr>
          </tbody>
        </table>
      </div>
      <p>You can reach these minimums across more than one sitting &mdash; often called "clubbing" &mdash; as long as every required score is achieved within 12 months of your first sitting. We help you pick the test, and the sitting strategy, that gets you there fastest.</p>
    </div>
    <aside class="note">
      <p><strong>OET or IELTS &mdash; which should you sit?</strong></p>
      <p>OET's material is drawn entirely from healthcare contexts, which suits candidates who find general-topic IELTS material harder to relate to. IELTS Academic is more widely available and familiar to many candidates. We'll help you choose based on a quick diagnostic, not a one-size-fits-all answer.</p>
    </aside>
  </div>
</div>"""

OET_TOOL = """<div class="section section--mist">
  <div class="wrap wrap--narrow">
    <div class="section-head">
      <h2>Check your score against NCNZ's minimum</h2>
      <p>Enter a recent OET or IELTS result to see exactly which bands already meet NCNZ's requirement, and which ones need work.</p>
    </div>
    <form class="tool" id="score-checker">
      <div class="field">
        <label for="test">Which test?</label>
        <select id="test" name="test">
          <option value="OET">OET</option>
          <option value="IELTS">IELTS Academic</option>
        </select>
      </div>
      <div class="tool__grid">
        <div class="tool__field"><label for="reading">Reading</label><input id="reading" name="reading" type="number" step="0.5" inputmode="decimal" placeholder="e.g. 350"></div>
        <div class="tool__field"><label for="listening">Listening</label><input id="listening" name="listening" type="number" step="0.5" inputmode="decimal" placeholder="e.g. 350"></div>
        <div class="tool__field"><label for="speaking">Speaking</label><input id="speaking" name="speaking" type="number" step="0.5" inputmode="decimal" placeholder="e.g. 350"></div>
        <div class="tool__field"><label for="writing">Writing</label><input id="writing" name="writing" type="number" step="0.5" inputmode="decimal" placeholder="e.g. 300"></div>
      </div>
      <button class="btn btn--jade" type="submit">Check my score</button>
      <div data-result hidden style="margin-top:1.25rem"></div>
    </form>
    <p class="muted" style="margin-top:1rem;font-size:.9rem">This is a quick self-check against NCNZ's published minimums, not an official assessment. Always confirm your result directly with the Nursing Council.</p>
  </div>
</div>"""

OET_SYLLABUS = """<div class="section">
  <div class="wrap">
    <div class="section-head"><h2>What's covered in the course</h2></div>
    <dl class="facts">
      <div><dt>Listening</dt><dd>Consultation extracts and case-note style tasks drawn from real clinical situations, with active-listening strategy coaching.</dd></div>
      <div><dt>Reading</dt><dd>Time-boxed practice on healthcare texts, matching, gap-fill and detailed comprehension tasks in the exact OET format.</dd></div>
      <div><dt>Writing</dt><dd>Referral-letter writing practice with structured feedback on organisation, clinical accuracy and register.</dd></div>
      <div><dt>Speaking</dt><dd>Role-play consultations with recorded, examiner-style feedback on fluency, clinical communication and rapport.</dd></div>
      <div><dt>Mock tests</dt><dd>Full-length timed mock exams, marked against the same criteria OET and IELTS examiners use.</dd></div>
    </dl>
  </div>
</div>"""

OET_FAQ = accordion([
    ("How long does it take to reach the required score?", "It depends on your starting band and how much spoken/written English practice you're getting day to day. Most candidates need 4&ndash;10 weeks of focused coaching &mdash; we'll give you a realistic estimate after a diagnostic test."),
    ("Can I combine scores from different sittings?", "Yes. NCNZ allows you to meet each band's minimum across more than one sitting, as long as every required score is achieved within 12 months of your first sitting, and all sittings are completed within three years of starting your application."),
    ("Does NCNZ accept the online, at-home version of these tests?", "Check the current NCNZ policy directly before booking, as accepted test formats and centres can change. We'll flag this during your enrolment call so you don't book the wrong sitting."),
], "OET / IELTS FAQs")

page(
    "courses/oet-preparation.html",
    "OET & IELTS Preparation for Nurses | Kiwi Nurse Academy",
    "OET and IELTS Academic coaching for internationally qualified nurses, targeting NCNZ's minimum bands across reading, listening, writing and speaking. Includes a free score checker.",
    "courses/oet-preparation.html", "../",
    OET_HERO + OET_INTRO + OET_TOOL + OET_SYLLABUS + '<div class="section"><div class="wrap">' + OET_FAQ + '</div></div>',
)

# ============================================================ ABOUT PAGE
ABOUT_HERO = page_hero(
    '<a href="index.html">Home</a><span>/</span>About Us',
    "Built by people who know the route firsthand.",
    "Kiwi Nurse Academy exists because the gap between passing a nursing exam in Kerala and passing one written for New Zealand's health system is bigger than most training centres admit.",
)

ABOUT_STORY = """<div class="section">
  <div class="wrap split split--wide-left">
    <div class="stack">
      <h2>Why we started here</h2>
      <p>Add your founding story here: who started Kiwi Nurse Academy, what gap you saw in the market, and why Kerala-to-New-Zealand specifically. A specific, honest story (a candidate who struggled, a training gap you noticed) will do more work than a generic mission statement.</p>
      <p>Since December 2023, NCNZ has assessed internationally qualified nurses through direct testing &mdash; an IQN theory exam, then an orientation course and OSCE &mdash; rather than mostly paperwork. That shift is exactly what this academy is built around: not general nursing coaching, but training mapped to NCNZ's current process, station by station.</p>
    </div>
    <aside class="note note--jade">
      <p><strong>Replace this box</strong></p>
      <p>Add a short, credible detail here &mdash; years the founder(s) spent nursing in NZ, a registration body membership, or the number of the first batch you trained. Specifics build more trust than adjectives.</p>
    </aside>
  </div>
</div>"""

ABOUT_VALUES = """<div class="topo section section--fiord">
  <div class="wrap">
    <div class="section-head"><h2>What we won't compromise on</h2></div>
    <dl class="defs">
      <div><dt>Honest pathway advice</dt><dd>If you're not ready for a course, or NCNZ's requirements have changed, we'll tell you before we take your fee &mdash; not after.</dd></div>
      <div><dt>Small batches</dt><dd>Every OSCE station and every OET speaking task gets individual feedback. We cap batch sizes to make that possible.</dd></div>
      <div><dt>Current information</dt><dd>NCNZ's process has changed significantly since 2023. We update our syllabus against their published handbooks, not last year's notes.</dd></div>
      <div><dt>No visa overreach</dt><dd>We're a training provider, not a licensed migration or immigration adviser. We'll always point you to a licensed adviser for visa-specific advice.</dd></div>
    </dl>
  </div>
</div>"""

ABOUT_TEAM = """<div class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Meet the team</h2>
      <p>Add real names, photos and one-line credentials once your team profiles are ready. Specific registration numbers or years of NZ clinical experience are strong trust signals here.</p>
    </div>
    <ul class="team">
      <li><span class="avatar">?</span><h3>Founder / Director name</h3><p>One line on their nursing/NZ background</p></li>
      <li><span class="avatar">?</span><h3>Lead OSCE trainer</h3><p>Simulation &amp; clinical training lead</p></li>
      <li><span class="avatar">?</span><h3>OET/IELTS coach</h3><p>English-language training lead</p></li>
      <li><span class="avatar">?</span><h3>Student counsellor</h3><p>Enrolment &amp; pathway guidance</p></li>
    </ul>
  </div>
</div>"""

page(
    "about.html",
    "About Us | Kiwi Nurse Academy",
    "Kiwi Nurse Academy trains internationally qualified nurses in Kerala for NCNZ's IQN, OSCE and OET/IELTS pathway to registration in New Zealand.",
    "about.html", "",
    ABOUT_HERO + ABOUT_STORY + ABOUT_VALUES + ABOUT_TEAM,
)

# ============================================================ CAREER PAGE
CAREER_HERO = page_hero(
    '<a href="index.html">Home</a><span>/</span>Career',
    "Help nurses reach New Zealand.",
    "We're building the team for our first full year of batches. If you can teach, coach or mentor toward these exams, we'd like to hear from you.",
)

CAREER_ROLES = """<div class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Current openings</h2>
      <p>Replace the placeholders below with real openings as they come up. Leaving this page live with "no openings right now, but tell us about yourself" is far better than deleting it.</p>
    </div>
    <div class="accordion">
      <details open>
        <summary>OSCE / Clinical Simulation Trainer</summary>
        <div class="answer">
          <p>Registered nurse with New Zealand clinical or OSCE examiner experience, able to run hands-on simulation sessions and give individual station feedback. Add exact requirements, location and salary band here.</p>
          <a class="btn btn--line btn--small" data-wa href="#">Apply on WhatsApp</a>
        </div>
      </details>
      <details>
        <summary>OET / IELTS Coach</summary>
        <div class="answer">
          <p>Experience teaching healthcare-specific English, ideally with OET or IELTS examiner or coaching background. Add exact requirements, location and salary band here.</p>
          <a class="btn btn--line btn--small" data-wa href="#">Apply on WhatsApp</a>
        </div>
      </details>
      <details>
        <summary>Student Counsellor / Admissions</summary>
        <div class="answer">
          <p>First point of contact for enquiries, running diagnostic calls and guiding candidates to the right course. Add exact requirements, location and salary band here.</p>
          <a class="btn btn--line btn--small" data-wa href="#">Apply on WhatsApp</a>
        </div>
      </details>
    </div>
  </div>
</div>"""

CAREER_WHY = """<div class="section section--mist">
  <div class="wrap">
    <div class="section-head"><h2>Why work with us</h2></div>
    <dl class="facts">
      <div><dt>Direct impact</dt><dd>You're working on the specific exam that decides whether a nurse's move to New Zealand happens on schedule.</dd></div>
      <div><dt>Small, hands-on team</dt><dd>Add detail on team size, culture and how decisions get made once you have it &mdash; specifics beat "fast-paced environment."</dd></div>
      <div><dt>Growing with the batch numbers</dt><dd>Early team members shape how courses are taught as we scale from our first batches onward.</dd></div>
    </dl>
  </div>
</div>"""

CAREER_APPLY = """<div class="section">
  <div class="wrap wrap--narrow">
    <div class="section-head"><h2>Don't see the right role?</h2><p>Send your CV and a line about what you'd want to teach or run &mdash; we keep every application on file for the next batch we open hiring for.</p></div>
    <form class="form" data-enquiry>
      <div class="form__grid">
        <div class="field"><label for="c-name">Full name</label><input id="c-name" name="name" required></div>
        <div class="field"><label for="c-phone">Phone / WhatsApp</label><input id="c-phone" name="phone" type="tel" required></div>
        <div class="field form__full"><label for="c-role">Role you're interested in</label><input id="c-role" name="course" placeholder="e.g. OSCE Trainer"></div>
        <div class="field form__full"><label for="c-msg">Tell us about your experience</label><textarea id="c-msg" name="message"></textarea></div>
      </div>
      <div class="form__foot">
        <button class="btn btn--jade" type="submit">Send application</button>
        <a class="btn btn--kowhai" data-wa data-wa-submit hidden href="#">Continue on WhatsApp</a>
        <p>We'll get back to you within a few working days.</p>
      </div>
      <p class="form__status" aria-live="polite"></p>
    </form>
  </div>
</div>"""

page(
    "career.html",
    "Careers | Kiwi Nurse Academy",
    "Join Kiwi Nurse Academy as an OSCE trainer, OET/IELTS coach or student counsellor, training internationally qualified nurses for New Zealand registration.",
    "career.html", "",
    CAREER_HERO + CAREER_ROLES + CAREER_WHY + CAREER_APPLY,
)

# ============================================================ FAQ PAGE
FAQ_HERO = page_hero(
    '<a href="index.html">Home</a><span>/</span>FAQ',
    "Frequently asked questions",
    "Straight answers about the pathway, our courses, and what to expect. Can't find yours? Ask us directly on WhatsApp.",
)

FAQ_GENERAL = accordion([
    ("What is NCNZ's current process for internationally qualified nurses?", "Since December 2023, the Nursing Council of New Zealand directly assesses competence rather than relying mainly on paperwork. If you're directed to a competence assessment, you'll need to pass an online theoretical exam, then a 2-day orientation and preparation course followed by an OSCE, both taken in person in New Zealand."),
    ("Do all internationally qualified nurses need to sit these exams?", "Not necessarily &mdash; NCNZ decides whether you're directed to a competence assessment after reviewing your application. We can help you understand what's likely in your case on a free call."),
    ("How long does the whole pathway usually take?", "It varies a lot by starting point, but most candidates move from enrolling with us to sitting their OSCE within 6&ndash;12 months, assuming steady study and no major delays on the NCNZ side."),
], "General pathway")

FAQ_OET = accordion([
    ("What's the minimum score I need?", "OET: 350 in reading, listening and speaking, and 300 in writing. IELTS Academic: 7.0 in reading, listening and speaking, and 6.5 in writing."),
    ("Can I combine results from different sittings?", "Yes, as long as every required minimum is met within 12 months of your first sitting, and all sittings are completed within three years of starting your application."),
    ("OET or IELTS — which is right for me?", "It depends on your comfort with healthcare-specific material versus general topics, and test availability near you. We help you decide after a short diagnostic."),
], "OET / IELTS")

FAQ_IQN = accordion([
    ("Where is the IQN theoretical exam held?", "At an accredited Pearson VUE test centre, either in New Zealand or internationally, including centres in India."),
    ("What does the exam cover?", "Part A covers medication safety; Part B covers nursing knowledge, both benchmarked against New Zealand's clinical standards."),
    ("What if I don't pass?", "NCNZ allows re-sits. We run a focused revision track for candidates re-sitting a specific part."),
], "IQN Theory Exam")

FAQ_OSCE = accordion([
    ("Where is the OSCE held?", "At an accredited clinical simulation and assessment centre in Christchurch, following a 2-day orientation and preparation course held nearby."),
    ("Can I prepare for the OSCE without travelling to New Zealand first?", "Yes — all our simulation-lab preparation happens at our Kerala centre. The orientation course and OSCE itself must be attended in New Zealand in person."),
    ("How long is the actual OSCE exam?", "Around three hours, made up of multiple timed clinical stations."),
], "OSCE Training")

FAQ_FEES = accordion([
    ("What do your courses cost?", "Add your current fee structure here, ideally broken down per course (OET / IQN / OSCE) and any bundle pricing."),
    ("Do you offer payment plans?", "Add your instalment policy here if you offer one — this is a common question and answering it up front reduces hesitation."),
    ("Do fees include the official exam fees (Pearson VUE, OET, OSCE)?", "Clarify here whether NCNZ, Pearson VUE, OET/IELTS and OSCE exam fees are separate from your course fee — candidates need this distinction to budget correctly."),
], "Fees &amp; logistics")

page(
    "faq.html",
    "FAQ | Kiwi Nurse Academy",
    "Answers to common questions about NCNZ's IQN, OSCE and OET/IELTS pathway, and about Kiwi Nurse Academy's courses, fees and logistics.",
    "faq.html", "",
    FAQ_HERO + '<div class="section"><div class="wrap wrap--narrow">' + FAQ_GENERAL + FAQ_OET + FAQ_IQN + FAQ_OSCE + FAQ_FEES + '</div></div>',
)

# ============================================================ CONTACT PAGE
CONTACT_HERO = page_hero(
    '<a href="index.html">Home</a><span>/</span>Contact',
    "Let's map your pathway.",
    "Send your details or message us on WhatsApp — most enquiries get a same-day response.",
)

CONTACT_BODY = """<div class="section">
  <div class="wrap split split--wide-right">
    <div>
      <h2>Get in touch</h2>
      <ul class="contact-list">
        <li><span class="ic">{phone}</span><div><b>Call or WhatsApp</b><a data-tel data-tel-text href="#">+91 00000 00000</a></div></li>
        <li><span class="ic">{mail}</span><div><b>Email</b><a data-email data-email-text href="#">info@kiwinurseacademy.com</a></div></li>
        <li><span class="ic">{pin}</span><div><b>India centre</b><span data-addr-india>Add your India centre address, City, Kerala</span></div></li>
        <li><span class="ic">{pin}</span><div><b>New Zealand</b><span data-addr-nz>Add your New Zealand address (optional)</span></div></li>
        <li><span class="ic">{clock}</span><div><b>Hours</b><span data-hours>Mon &ndash; Sat, 9:00 am &ndash; 6:00 pm IST</span></div></li>
      </ul>
      <div class="social" style="margin-top:2rem">
        <a data-social="instagram" href="#" aria-label="Instagram">{insta}</a>
        <a data-social="facebook" href="#" aria-label="Facebook">{fb}</a>
        <a data-social="youtube" href="#" aria-label="YouTube">{yt}</a>
        <a data-social="linkedin" href="#" aria-label="LinkedIn">{li}</a>
      </div>
    </div>
    <form class="form" data-enquiry>
      <div class="form__grid">
        <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" required></div>
        <div class="field"><label for="f-phone">Phone / WhatsApp</label><input id="f-phone" name="phone" type="tel" required></div>
        <div class="field form__full"><label for="f-email">Email <span class="opt">(optional)</span></label><input id="f-email" name="email" type="email"></div>
        <div class="field form__full">
          <label for="f-course">Which course are you asking about?</label>
          <select id="f-course" name="course">
            <option>OET / IELTS Preparation</option>
            <option>IQN Training</option>
            <option>OSCE Training</option>
            <option>Not sure — need guidance</option>
          </select>
        </div>
        <div class="field form__full"><label for="f-msg">Message <span class="opt">(optional)</span></label><textarea id="f-msg" name="message" placeholder="Tell us where you're at — e.g. exam status, target intake"></textarea></div>
      </div>
      <div class="form__foot">
        <button class="btn btn--jade" type="submit">Send enquiry</button>
        <a class="btn btn--kowhai" data-wa data-wa-submit hidden href="#">Continue on WhatsApp</a>
        <p>We'll respond the same working day wherever possible.</p>
      </div>
      <p class="form__status" aria-live="polite"></p>
    </form>
  </div>
</div>""".format(phone=icon("phone"), mail=icon("mail"), pin=icon("pin"), clock=icon("clock"),
                  insta=icon("insta"), fb=icon("fb"), yt=icon("yt"), li=icon("linkedin"))

page(
    "contact.html",
    "Contact Us | Kiwi Nurse Academy",
    "Get in touch with Kiwi Nurse Academy for IQN, OSCE and OET/IELTS training enquiries. Call, WhatsApp or send an enquiry form.",
    "contact.html", "",
    CONTACT_HERO + CONTACT_BODY,
)

# ============================================================ BLOG POSTS (content)
POSTS = [
    {
        "slug": "ncnz-competence-pathway-explained",
        "accent": "pounamu",
        "meta": "Pathway &middot; 6 min read",
        "title": "NCNZ's competence pathway, explained step by step",
        "desc": "How the Nursing Council of New Zealand assesses internationally qualified nurses since its 2023 changes: the IQN theory exam, the orientation course, and the OSCE.",
        "excerpt": "Since December 2023, NCNZ tests competence directly instead of relying mainly on paperwork. Here's exactly what that means for your application.",
        "body": """
<p>If you qualified as a nurse outside New Zealand, the route to registration changed in a meaningful way from 4 December 2023. Where the Nursing Council of New Zealand (NCNZ) previously leaned heavily on document review and Competence Assessment Programmes, it now directly tests a nurse's competence to practise &mdash; an approach already used in Australia, the UK and Canada.</p>
<h2>The two-part competence assessment</h2>
<p>If NCNZ directs you to complete a competence assessment, you'll need to pass both of the following:</p>
<ul>
  <li><strong>An online theoretical examination</strong> &mdash; sat at an accredited Pearson VUE test centre, overseas or in New Zealand. It's based on the same State Final Examination standard used for domestically trained nurses, and covers medication safety and general nursing knowledge.</li>
  <li><strong>A clinical competence assessment</strong> &mdash; a two-day orientation and preparation course (OPC), followed by an objective structured clinical examination (OSCE). Both are taken in person in New Zealand, with the OSCE held at an accredited simulation and assessment centre in Christchurch.</li>
</ul>
<h2>What the orientation course covers</h2>
<p>The two-day OPC isn't a formality &mdash; it's designed to introduce nurses to the specific and unique aspects of practising in Aotearoa New Zealand: cultural safety, relational and whānau-centred care, and tikanga, alongside an overview of the health system, legal requirements, and how to communicate and escalate issues the way New Zealand teams expect. It also gives candidates hands-on time with the clinical equipment and OSCE format before the real exam.</p>
<h2>Why the order matters</h2>
<p>Because the theory exam and the clinical assessment are sequential &mdash; you're only invited to the OPC and OSCE after passing the theoretical exam &mdash; candidates who prepare for both in parallel from day one often spread their effort too thin. We generally recommend locking in your English-language score first, since that's a prerequisite for your NCNZ application regardless of when you sit the other two exams.</p>
<h2>What hasn't changed</h2>
<p>NCNZ still requires standard supporting evidence &mdash; verified qualifications, registration history, and English-language competence &mdash; alongside the new assessment steps. Requirements are reviewed periodically, so always check the current position on NCNZ's own site before relying on any date or score here.</p>
""",
    },
    {
        "slug": "oet-vs-ielts-for-nurses",
        "accent": "sky",
        "meta": "OET / IELTS &middot; 5 min read",
        "title": "OET vs IELTS for nurses: which should you sit?",
        "desc": "A practical comparison of OET and IELTS Academic against NCNZ's English-language requirement for internationally qualified nurses.",
        "excerpt": "NCNZ accepts both OET and IELTS Academic, with different minimum bands. Here's how to decide which one suits you.",
        "body": """
<p>Every internationally qualified nurse applying to NCNZ has to clear an English-language requirement, and there are two approved routes: the Occupational English Test (OET) and IELTS Academic. Both are rigorous, but they suit different candidates.</p>
<h2>NCNZ's minimum scores</h2>
<div class="table-wrap">
<table>
<thead><tr><th>Test</th><th>Reading</th><th>Listening</th><th>Speaking</th><th>Writing</th></tr></thead>
<tbody>
<tr><th>OET</th><td>350</td><td>350</td><td>350</td><td>300</td></tr>
<tr><th>IELTS Academic</th><td>7.0</td><td>7.0</td><td>7.0</td><td>6.5</td></tr>
</tbody>
</table>
</div>
<p>Both tests let you combine scores across sittings &mdash; as long as every required minimum is reached within 12 months of your first attempt, and all sittings fall within three years of starting your NCNZ application.</p>
<h2>Where OET tends to help</h2>
<p>OET's material is entirely healthcare-based &mdash; consultations, referral letters, clinical case notes. If you find general-topic IELTS material (economics, environment, culture) harder to engage with than clinical scenarios, OET's format often plays to your strengths, and its writing task specifically practises the kind of referral-letter writing nurses actually do.</p>
<h2>Where IELTS tends to help</h2>
<p>IELTS Academic is more widely available, with more test centres and dates, and its format is broadly familiar to anyone who's prepared for a general English exam before. If flexibility of test dates and locations matters more to you than subject-matter familiarity, IELTS can be the more practical choice.</p>
<h2>Our take</h2>
<p>There's no universally "easier" option &mdash; the right test depends on your existing strengths. A short diagnostic against both formats, which we run as part of enrolment, usually settles the question in one session rather than weeks of guessing.</p>
""",
    },
    {
        "slug": "what-happens-at-the-osce",
        "accent": "pohutukawa",
        "meta": "OSCE &middot; 6 min read",
        "title": "What actually happens at the orientation course and OSCE",
        "desc": "A walkthrough of NCNZ's two-day orientation and preparation course and the OSCE clinical exam held in Christchurch.",
        "excerpt": "The clinical competence assessment is the stage candidates worry about most. Here's what the two days actually involve.",
        "body": """
<p>Once you pass the IQN theoretical exam, NCNZ invites you to the clinical competence assessment &mdash; the stage most candidates feel the least certain about, mostly because it's the one you have to attend in person, thousands of kilometres from home. Here's what it actually looks like.</p>
<h2>Day one and two: the orientation and preparation course</h2>
<p>The OPC is designed to build the New Zealand-specific context that a purely clinical exam can't test on its own. Over two days, it covers:</p>
<ul>
  <li>Cultural safety, relational and whānau-centred care, and tikanga &mdash; introduced as a starting point for your ongoing cultural learning, not a full training in itself.</li>
  <li>An overview of the New Zealand health system and the legal requirements of practising here.</li>
  <li>Communicating and escalating nursing concerns the way New Zealand teams expect.</li>
  <li>Hands-on familiarisation with the clinical equipment and the OSCE's station format, so exam day isn't the first time you've seen the setup.</li>
</ul>
<h2>The OSCE itself</h2>
<p>The objective structured clinical examination takes around three hours and is held at an accredited simulation and assessment centre in Christchurch. It's built from a series of timed stations, each simulating a specific clinical scenario and testing a particular skill &mdash; a format used internationally for assessing nurses and doctors since the 1970s, including in Australia, Canada and the UK.</p>
<p>What examiners are scoring isn't just clinical accuracy. Communication, escalation, and culturally safe practice are assessed alongside your hands-on skills at each station.</p>
<h2>How to prepare before you fly</h2>
<p>Because the OPC and OSCE both happen in New Zealand, the highest-value preparation happens before you leave home: station-by-station simulation drills, structured communication practice, and full mock OSCEs under time pressure. Done well, the two days in New Zealand should feel like a repeat of something you've already rehearsed, not a first attempt.</p>
""",
    },
]

POST_CARDS = "".join(
    '<article class="post" style="--c:var(--{acc})"><p class="post__meta">{meta}</p><h3><a href="blog/{slug}.html">{title}</a></h3><p>{excerpt}</p><a class="btn btn--line btn--small" href="blog/{slug}.html">Read more</a></article>'.format(**p, acc=p["accent"])
    for p in POSTS
)

BLOG_HERO = page_hero(
    '<a href="index.html">Home</a><span>/</span>Blog',
    "Notes on the pathway",
    "Plain explanations of NCNZ's process, the exams, and what to expect at each stage &mdash; written from our own coaching notes, not copied from anywhere else.",
)

page(
    "blog.html",
    "Blog | Kiwi Nurse Academy",
    "Articles on NCNZ's IQN, OSCE and OET/IELTS pathway for internationally qualified nurses moving to New Zealand.",
    "blog.html", "",
    BLOG_HERO + '<div class="section"><div class="wrap"><div class="posts">' + POST_CARDS + '</div></div></div>',
)

for p in POSTS:
    crumbs = '<a href="../index.html">Home</a><span>/</span><a href="../blog.html">Blog</a><span>/</span>' + p["title"]
    hero = page_hero(crumbs, p["title"], p["desc"], [p["meta"]])
    body = hero + '<div class="section"><div class="wrap wrap--narrow prose">' + p["body"] + """
    <div class="note note--jade" style="margin-top:2.5rem">
      <p><strong>Ready to start this stage?</strong></p>
      <p>Talk to us on a free call and we'll tell you honestly where you stand on the pathway.</p>
      <a class="btn btn--jade btn--small" data-wa href="#" style="margin-top:.75rem">Chat on WhatsApp</a>
    </div>
    </div></div>"""
    page(
        "blog/" + p["slug"] + ".html",
        p["title"] + " | Kiwi Nurse Academy Blog",
        p["desc"],
        "blog.html", "../",
        body,
    )

print("ALL PAGES BUILT")
