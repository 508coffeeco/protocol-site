"""Build the three industry pages from the commercial page's shell.
Run from the repo root:  python3 _build/build_industry.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from industry_shared import *  # noqa

HEAD, PRE, FOOT = split_template()

# ======================================================================
# MED SPA — calm, soft, the treatment room you can tap around
# ======================================================================
MS_SPOTS = [
    ("bed", 51, 62, "Treatment bed & stool",
     "Bed surface, frame, base and controls disinfected, rolling stool wiped top to casters. Paper or linens changed out the way you set it up.", "Every visit"),
    ("counter", 85, 60, "Counters & sink",
     "Cleared, disinfected and dried. Faucet and backsplash polished with no water spots. Product bottles wiped and put back exactly where they were.", "Every visit"),
    ("mirror", 85, 34, "Mirror & glass",
     "Streak-free mirrors, glass doors and display cases, checked at an angle in your lighting, the way a client sees them from the bed.", "Every visit"),
    ("shelf", 41, 30, "Product shelves & retail",
     "Dusted shelf by shelf, products lifted and wiped underneath, labels turned out. Your retail wall is part of the experience.", "Weekly detail · nightly touch-up"),
    ("door", 19, 60, "Door handles & switches",
     "Every handle, light switch and push plate disinfected. The small surfaces every client and provider touches.", "Every visit"),
    ("floor", 47, 92, "Floors & baseboards",
     "Vacuumed and mopped edge to edge, under the bed and stool. Baseboards wiped so nothing shows up in your photos.", "Every visit"),
    ("trash", 27, 86, "Trash",
     "Trash removed and liners replaced. Sharps and regulated medical waste stay with your licensed vendor. We never handle them.", "Every visit"),
]

MS_ROOM_SVG = """<svg class="ms-room-svg" viewBox="0 0 800 500" role="img" aria-label="Illustration of a med spa treatment room">
  <rect width="800" height="500" fill="#f4fafa"/>
  <rect y="420" width="800" height="80" fill="#e3eeef"/>
  <rect y="414" width="800" height="8" fill="#d2e3e5"/>
  <!-- door -->
  <rect x="48" y="150" width="130" height="266" rx="4" fill="#fff" stroke="#b9d3d6" stroke-width="3"/>
  <rect x="64" y="170" width="98" height="96" rx="3" fill="none" stroke="#d6e6e7" stroke-width="2"/>
  <rect x="64" y="290" width="98" height="108" rx="3" fill="none" stroke="#d6e6e7" stroke-width="2"/>
  <circle cx="156" cy="298" r="7" fill="#2e6d76"/>
  <rect x="192" y="240" width="18" height="28" rx="3" fill="#fff" stroke="#b9d3d6" stroke-width="2"/>
  <!-- shelves -->
  <rect x="244" y="150" width="200" height="8" rx="2" fill="#b9d3d6"/>
  <rect x="244" y="212" width="200" height="8" rx="2" fill="#b9d3d6"/>
  <g fill="#2e6d76"><rect x="258" y="118" width="16" height="32" rx="4"/><rect x="282" y="126" width="14" height="24" rx="4" opacity=".55"/><rect x="304" y="112" width="18" height="38" rx="5"/><rect x="332" y="124" width="14" height="26" rx="4" opacity=".55"/><rect x="356" y="118" width="16" height="32" rx="4"/><rect x="384" y="128" width="40" height="22" rx="5" fill="#b2dddf"/></g>
  <g fill="#2e6d76"><rect x="262" y="182" width="22" height="30" rx="5" opacity=".55"/><rect x="292" y="176" width="16" height="36" rx="4"/><rect x="318" y="186" width="30" height="26" rx="5" fill="#b2dddf"/><rect x="358" y="180" width="16" height="32" rx="4"/><rect x="384" y="184" width="16" height="28" rx="4" opacity=".55"/></g>
  <!-- bed -->
  <rect x="262" y="350" width="16" height="66" fill="#9fbfc3"/><rect x="530" y="350" width="16" height="66" fill="#9fbfc3"/>
  <rect x="282" y="368" width="246" height="12" rx="3" fill="#b9d3d6"/>
  <rect x="246" y="306" width="318" height="46" rx="16" fill="#2e6d76"/>
  <rect x="254" y="300" width="300" height="20" rx="10" fill="#fff" opacity=".9"/>
  <rect x="490" y="288" width="64" height="22" rx="11" fill="#e8f4f5"/>
  <!-- stool -->
  <ellipse cx="216" cy="380" rx="24" ry="8" fill="#2e6d76"/><rect x="212" y="386" width="8" height="24" fill="#9fbfc3"/><rect x="196" y="408" width="40" height="5" rx="2" fill="#9fbfc3"/>
  <!-- trash -->
  <path d="M200 432 h36 l-4 50 h-28 z" fill="#fff" stroke="#9fbfc3" stroke-width="3"/>
  <!-- mirror -->
  <rect x="616" y="96" width="144" height="150" rx="72" fill="#e8f4f5" stroke="#b9d3d6" stroke-width="4"/>
  <path d="M650 130 l30 -14 M650 150 l50 -24" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
  <!-- counter -->
  <rect x="600" y="296" width="190" height="14" rx="3" fill="#b9d3d6"/>
  <rect x="606" y="310" width="178" height="106" rx="4" fill="#fff" stroke="#d6e6e7" stroke-width="3"/>
  <line x1="695" y1="316" x2="695" y2="410" stroke="#e3eeef" stroke-width="3"/>
  <circle cx="680" cy="362" r="4" fill="#b9d3d6"/><circle cx="710" cy="362" r="4" fill="#b9d3d6"/>
  <ellipse cx="740" cy="296" rx="30" ry="6" fill="#d6e6e7"/>
  <path d="M740 296 v-24 h-14" fill="none" stroke="#2e6d76" stroke-width="5" stroke-linecap="round"/>
  <rect x="622" y="274" width="12" height="22" rx="3" fill="#2e6d76"/><rect x="640" y="280" width="20" height="16" rx="4" fill="#b2dddf"/>
</svg>"""

ms_buttons = "\n".join(
    f'<button type="button" class="ms-spot" style="left:{x}%;top:{y}%" data-spot="{k}" aria-label="{t}" aria-pressed="{"true" if i == 0 else "false"}"><span>{i+1}</span></button>'
    for i, (k, x, y, t, d, f) in enumerate(MS_SPOTS))
ms_data = json.dumps({k: {"t": t, "d": d, "f": f, "n": i + 1} for i, (k, x, y, t, d, f) in enumerate(MS_SPOTS)})
ms_list = "\n".join(
    f'<li><button type="button" data-spot="{k}" aria-pressed="{"true" if i == 0 else "false"}"><b>{i+1}</b>{t}</button></li>'
    for i, (k, x, y, t, d, f) in enumerate(MS_SPOTS))
k0, _, _, t0, d0, f0 = MS_SPOTS[0]

MS_CSS = """
<style>
.ms{--ms-blush:#f3ece6}
.ms-hero{background:linear-gradient(180deg,#f4fafa 0%,#fff 100%);position:relative;overflow:hidden}
.ms-hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center;padding-top:90px;padding-bottom:90px}
@media(max-width:900px){.ms-hero .wrap{grid-template-columns:1fr;gap:36px;padding-top:56px;padding-bottom:60px}}
.ms-hero h1{font-weight:500;font-size:clamp(42px,6vw,72px)}
.ms-hero h1 em{font-style:italic;color:var(--teal-dk)}
.ms-hero .orb-a{position:absolute;width:520px;height:520px;border-radius:50%;background:var(--sky);opacity:.25;right:-180px;top:-160px;filter:blur(10px)}
.ms-tonight{background:#fff;border-radius:28px;padding:28px 28px 22px;box-shadow:0 30px 70px rgba(31,81,89,.14);position:relative;z-index:1}
.ms-tonight .k{font-family:var(--sub);font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--grey);font-weight:700}
.ms-tonight h3{font-weight:500;margin:6px 0 16px;font-size:26px}
.ms-tonight ul{list-style:none;margin:0;padding:0}
.ms-tonight li{display:flex;align-items:center;gap:12px;padding:11px 0;border-top:1px solid #edf3f3;font-size:15px;opacity:.35;transition:opacity .5s}
.ms-tonight li i{width:22px;height:22px;border-radius:50%;border:1.5px solid var(--sky);flex:none;display:grid;place-items:center;transition:background .4s,border-color .4s}
.ms-tonight li i::after{content:"";width:8px;height:4px;border-left:2px solid #fff;border-bottom:2px solid #fff;transform:rotate(-45deg) translate(1px,-1px);opacity:0;transition:opacity .3s}
.ms-tonight li.done{opacity:1}
.ms-tonight li.done i{background:var(--teal);border-color:var(--teal)}
.ms-tonight li.done i::after{opacity:1}
.ms-tonight .foot{font-size:12px;color:var(--grey);margin-top:10px}

.ms-roomsec{padding:96px 0;background:#fff}
.ms-roomgrid{display:grid;grid-template-columns:1.35fr .65fr;gap:36px;align-items:stretch;margin-top:34px}
@media(max-width:980px){.ms-roomgrid{grid-template-columns:1fr}}
.ms-room{position:relative;border-radius:28px;overflow:hidden;box-shadow:inset 0 0 0 1px #e3eeef;align-self:start;aspect-ratio:8/5}
.ms-room-svg{position:absolute;inset:0;width:100%;height:100%}
.ms-room-svg{display:block;width:100%;height:auto}
.ms-spot{position:absolute;transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;border:0;cursor:pointer;background:transparent;padding:0}
.ms-spot span{position:absolute;inset:7px;border-radius:50%;background:#fff;color:var(--teal);font:700 14px/30px var(--sub);box-shadow:0 0 0 2px var(--teal),0 6px 16px rgba(31,81,89,.25);transition:background .2s,color .2s,transform .2s}
.ms-spot::before{content:"";position:absolute;inset:0;border-radius:50%;background:var(--sky);opacity:.55;animation:msPulse 2.4s ease-out infinite}
.ms-spot[aria-pressed="true"] span{background:var(--teal);color:#fff;transform:scale(1.12)}
.ms-spot:focus-visible span{outline:3px solid var(--charcoal);outline-offset:3px}
@keyframes msPulse{0%{transform:scale(.6);opacity:.6}100%{transform:scale(1.5);opacity:0}}
@media(prefers-reduced-motion:reduce){.ms-spot::before{animation:none;opacity:.25}}
.ms-panel{background:var(--mist);border-radius:28px;padding:30px;display:flex;flex-direction:column}
.ms-panel .num{font-family:var(--serif);font-size:56px;line-height:1;color:var(--sky)}
.ms-panel h3{font-weight:500;margin:8px 0 10px}
.ms-panel p{margin:0 0 16px;font-size:16px}
.ms-panel .freq{align-self:flex-start;font-family:var(--sub);font-weight:700;font-size:12px;letter-spacing:.14em;text-transform:uppercase;background:#fff;color:var(--teal);padding:8px 12px;border-radius:999px}
.ms-panel ol{list-style:none;margin:auto 0 0;padding:22px 0 0;border-top:1px solid #d3e7e9;display:grid;gap:4px}
.ms-panel ol button{width:100%;text-align:left;background:none;border:0;font:500 14px/1.3 var(--body);color:var(--charcoal);padding:8px 6px;border-radius:8px;cursor:pointer;display:flex;gap:10px;align-items:center;min-height:40px}
.ms-panel ol button b{font-family:var(--sub);width:22px;height:22px;border-radius:50%;background:#fff;color:var(--teal);display:grid;place-items:center;font-size:11px;flex:none}
.ms-panel ol button[aria-pressed="true"]{background:#fff}
.ms-panel ol button[aria-pressed="true"] b{background:var(--teal);color:#fff}
.ms-fade{animation:msFade .35s ease}
@keyframes msFade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}

.ms-notice{padding:90px 0;background:var(--ms-blush)}
.ms-notice-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:34px}
@media(max-width:900px){.ms-notice-grid{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.ms-notice-grid{grid-template-columns:1fr}}
.ms-n{background:#fff;border-radius:22px;padding:26px 22px}
.ms-n .ix{font-family:var(--serif);font-style:italic;color:var(--teal);font-size:15px}
.ms-n h4{font-weight:500;margin:8px 0 8px}
.ms-n p{font-size:15px;margin:0;color:var(--grey)}

.ms .sp-wrap{padding:96px 0;background:#fff}
.ms .ind-faq{padding:20px 0 96px;background:#fff}
""" + SCOPE_CSS + FAQ_CSS + "</style>"

MS_MAIN = f"""
<main class="ms">
<section class="ms-hero">
  <div class="orb-a" aria-hidden="true"></div>
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Med Spa Cleaning · Tampa Bay</span>
      <h1>Treatment rooms, <em>reset every night.</em></h1>
      <p class="lede">Your clients notice every surface they touch. We write a cleaning protocol around those surfaces, then follow it the same way every visit.</p>
      <div class="btn-row">
        <a class="btn primary" href="#scope">Build your scope</a>
        <a class="btn outline" href="{TEL}">{PHONE_ICON}{PHONE}</a>
      </div>
    </div>
    <div class="ms-tonight reveal d1" aria-label="Sample nightly checklist">
      <span class="k">Sample protocol · Treatment room 2</span>
      <h3>Tonight's reset</h3>
      <ul id="msTonight">
        <li><i></i>Bed, stool &amp; controls disinfected</li>
        <li><i></i>Counter and sink cleared and dried</li>
        <li><i></i>Mirror and glass, streak-free</li>
        <li><i></i>Handles and switches wiped</li>
        <li><i></i>Floor edge to edge, under the bed</li>
      </ul>
      <p class="foot">Every room gets its own written checklist.</p>
    </div>
  </div>
</section>

<section class="ms-roomsec">
  <div class="wrap">
    <div class="reveal" style="max-width:640px">
      <span class="eyebrow">Inside the protocol</span>
      <h2>Tap around the room.</h2>
      <p class="lede">Each number is a surface on your treatment room checklist. Tap one to see exactly what we do there.</p>
    </div>
    <div class="ms-roomgrid reveal d1">
      <div class="ms-room">
        {MS_ROOM_SVG}
        {ms_buttons}
      </div>
      <div class="ms-panel" aria-live="polite">
        <div id="msDetail">
          <div class="num">01</div>
          <h3>{t0}</h3>
          <p>{d0}</p>
          <span class="freq">{f0}</span>
        </div>
        <ol aria-label="All surfaces">{ms_list}</ol>
      </div>
    </div>
  </div>
</section>

<section class="ms-notice">
  <div class="wrap">
    <div class="reveal" style="max-width:640px">
      <span class="eyebrow">What clients notice first</span>
      <h2>The details they never mention, but always see.</h2>
    </div>
    <div class="ms-notice-grid reveal d1">
      <div class="ms-n"><span class="ix">At check-in</span><h4>The front desk</h4><p>Fingerprints on glass, dust on the product display, a smudged card reader.</p></div>
      <div class="ms-n"><span class="ix">Before the appointment</span><h4>The restroom</h4><p>Dry counters, stocked dispensers, a mirror without spots.</p></div>
      <div class="ms-n"><span class="ix">The moment they walk in</span><h4>The air</h4><p>Clean should smell like nothing. We skip heavy fragrances unless you ask for them.</p></div>
      <div class="ms-n"><span class="ix">Lying on the bed</span><h4>The ceiling and vents</h4><p>Clients look up. Vents, light fixtures and corners go on a detail schedule.</p></div>
    </div>
  </div>
</section>

{scope_section(page_key="ms", eyebrow="Build your scope", title="Tell us what your spa needs.",
   intro="Tap the areas you want covered and how often. Your walkthrough request goes out with your choices, so we arrive with a plan.",
   areas=["Treatment rooms", "Injection & procedure rooms", "Reception & lobby", "Retail displays", "Restrooms", "Glass & mirrors", "Staff room", "Floors & baseboards"],
   facility="Med spa")}

<section class="ind-faq">
  <div class="wrap" style="max-width:860px">
    <span class="eyebrow">Questions</span>
    <h2 style="margin-bottom:10px">Before you book.</h2>
    {faq([
      ("When do you clean?", "After your last appointment or before you open, whichever keeps rooms free for clients. Your times go into the written protocol so it never changes on you."),
      ("Do you handle sharps or medical waste?", "No. Sharps and regulated medical waste stay with your licensed disposal vendor. We clean everything around them and never open those containers."),
      ("What products do you use around clients?", "Disinfectants used according to the label, including the contact time, on every touch point, and low-scent products everywhere else. If you have products you prefer, we'll use yours."),
      ("How does the free trial clean work?", "After a free walkthrough, new recurring accounts get one trial clean at no charge. You see the protocol in action before you sign anything."),
    ])}
  </div>
</section>
</main>
"""

MS_JS = """
<script>
(function(){
  var D=""" + ms_data + """;
  var detail=document.getElementById('msDetail');
  function pick(k){
    var s=D[k];if(!s)return;
    document.querySelectorAll('.ms [data-spot]').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.spot===k?'true':'false');});
    detail.innerHTML='<div class="num">'+String(s.n).padStart(2,'0')+'</div><h3>'+s.t+'</h3><p>'+s.d+'</p><span class="freq">'+s.f+'</span>';
    detail.classList.remove('ms-fade');void detail.offsetWidth;detail.classList.add('ms-fade');
  }
  document.querySelectorAll('.ms [data-spot]').forEach(function(b){b.addEventListener('click',function(){pick(b.dataset.spot);});});
  // hero checklist ticks itself off once
  var items=document.querySelectorAll('#msTonight li'),i=0,still=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(still){items.forEach(function(li){li.classList.add('done');});}
  else{(function tick(){if(i<items.length){items[i++].classList.add('done');setTimeout(tick,700);}})();}
})();
</script>"""

# ======================================================================
# MEDICAL & DENTAL — structured, clinical grid, zone tabs + timeline
# ======================================================================
MD_ZONES = [
    ("waiting", "Waiting Room", [
        ("Chair arms, seats and side tables disinfected", True),
        ("Check-in pens, clipboards and kiosk screen wiped", True),
        ("Door handles and push plates", True),
        ("Coffee and water station cleaned and restocked", False),
        ("Entry glass and windows, streak-free", False),
        ("Floors vacuumed and mopped edge to edge", False),
        ("Trash and recycling out, liners replaced", False)]),
    ("desk", "Front Desk", [
        ("Counter and check-in window", True),
        ("Card readers and shared phones", True),
        ("Drawer pulls and chair arms", True),
        ("Keyboards and screens with a dry-safe method", False),
        ("Under-desk floor and cords area", False),
        ("Trash and shred bins emptied (shred stays sealed)", False)]),
    ("exam", "Exam Rooms & Operatories", [
        ("Counters, sinks and backsplashes disinfected", True),
        ("Cabinet pulls, light switches and door handles", True),
        ("Soap, towel and glove dispensers refilled", False),
        ("Exterior surfaces of non-clinical furniture", False),
        ("Floors with a mop used only in clinical rooms", False),
        ("General trash only. No regulated waste", False)]),
    ("rest", "Restrooms", [
        ("Toilets, sinks and fixtures disinfected", True),
        ("Partitions, locks and flush handles", True),
        ("Dispensers refilled", False),
        ("Mirrors and chrome polished", False),
        ("Floors and drains, mopped last", False),
        ("Baby changing station", True)]),
    ("staff", "Staff Areas", [
        ("Break room counters and sink", True),
        ("Microwave and fridge handles and exteriors", True),
        ("Tables and chairs", False),
        ("Floors and trash", False)]),
]
md_tabs = "\n".join(
    f'<button type="button" role="tab" id="md-t-{k}" aria-controls="md-p-{k}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}"><span>{i+1:02d}</span>{n}</button>'
    for i, (k, n, items) in enumerate(MD_ZONES))
def _md_items(items):
    return "\n".join(
        f'<li><i aria-hidden="true"></i><span>{html.escape(t)}</span>{"<em>High-touch</em>" if ht else ""}</li>' for t, ht in items)
md_panels = "\n".join(
    f'<div role="tabpanel" id="md-p-{k}" aria-labelledby="md-t-{k}" class="md-panel"{"" if i == 0 else " hidden"}><ul>{_md_items(items)}</ul></div>'
    for i, (k, n, items) in enumerate(MD_ZONES))

MD_STEPS = [
    ("6:00 PM", "Check in", "Last patient is out. The crew lead signs in, walks the practice and confirms the night's checklist."),
    ("6:10 PM", "Exam rooms first", "Top to bottom in every room: high surfaces, counters and sinks, touch points, then dispensers."),
    ("7:00 PM", "Restrooms", "Fixtures, partitions and touch points disinfected with restroom-only cloths and mops."),
    ("7:30 PM", "Front desk & waiting room", "Chairs, counters, card readers and entry glass. The first things a patient sees tomorrow."),
    ("8:00 PM", "Floors last", "Every floor, back of the practice to the front door, so nothing gets tracked over."),
    ("8:30 PM", "Sign off & lock up", "Checklist completed and signed, lights off, doors locked, alarm set."),
]
md_steps = "\n".join(
    f'<li><button type="button" data-step="{i}" aria-pressed="{"true" if i == 0 else "false"}"><time>{t}</time><b>{h}</b></button></li>'
    for i, (t, h, d) in enumerate(MD_STEPS))
md_step_data = json.dumps([{"t": t, "h": h, "d": d} for t, h, d in MD_STEPS])

MD_CSS = """
<style>
.md{--md-grid:rgba(46,109,118,.07)}
.md-hero{background:#fff;background-image:linear-gradient(var(--md-grid) 1px,transparent 1px),linear-gradient(90deg,var(--md-grid) 1px,transparent 1px);background-size:40px 40px;border-bottom:1px solid #dfe9ea}
.md-hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:56px;align-items:center;padding-top:88px;padding-bottom:88px}
@media(max-width:900px){.md-hero .wrap{grid-template-columns:1fr;gap:36px;padding-top:56px;padding-bottom:56px}}
.md-board{background:#fff;border:1px solid #cfdfe1;border-radius:6px;box-shadow:0 20px 50px rgba(31,81,89,.10);font-size:14px}
.md-board header{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:1px solid #e3ecec;background:var(--teal);color:#fff;border-radius:6px 6px 0 0}
.md-board header b{font-family:var(--sub);letter-spacing:.16em;text-transform:uppercase;font-size:11px}
.md-board header span{font-size:12px;opacity:.85}
.md-board .row{display:grid;grid-template-columns:1fr auto auto;gap:14px;align-items:center;padding:13px 18px;border-bottom:1px solid #eef3f3}
.md-board .row:last-child{border-bottom:0}
.md-board .row small{color:var(--grey);font-variant-numeric:tabular-nums}
.md-board .ok{font-family:var(--sub);font-weight:700;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--teal);background:var(--mist);padding:5px 9px;border-radius:4px}
.md-note{font-size:12px;color:var(--grey);padding:10px 18px 14px}

.md-zones{padding:96px 0;background:var(--soft)}
.md-zgrid{display:grid;grid-template-columns:280px 1fr;gap:0;margin-top:34px;background:#fff;border:1px solid #dbe6e7;border-radius:6px;overflow:hidden}
@media(max-width:860px){.md-zgrid{grid-template-columns:1fr}}
.md-tabs{display:flex;flex-direction:column;border-right:1px solid #dbe6e7;background:#fbfdfd}
@media(max-width:860px){.md-tabs{flex-direction:row;overflow-x:auto;border-right:0;border-bottom:1px solid #dbe6e7;scrollbar-width:none}.md-tabs::-webkit-scrollbar{display:none}}
.md-tabs button{all:unset;cursor:pointer;display:flex;align-items:center;gap:12px;padding:18px 22px;font:600 15px/1.3 var(--body);color:var(--charcoal);border-bottom:1px solid #eef3f3;border-left:3px solid transparent;min-height:24px;white-space:nowrap}
@media(max-width:860px){.md-tabs button{border-bottom:3px solid transparent;border-left:0;padding:16px 18px}}
.md-tabs button span{font-family:var(--sub);font-size:11px;font-weight:700;color:var(--grey);letter-spacing:.1em}
.md-tabs button[aria-selected="true"]{background:#fff;border-left-color:var(--teal);color:var(--teal)}
@media(max-width:860px){.md-tabs button[aria-selected="true"]{border-bottom-color:var(--teal)}}
.md-tabs button:focus-visible{outline:3px solid var(--sky);outline-offset:-3px}
.md-panel{padding:26px 30px}
.md-panel ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:0 28px}
@media(max-width:640px){.md-panel{padding:18px}.md-panel ul{grid-template-columns:1fr}}
.md-panel li{display:flex;align-items:flex-start;gap:12px;padding:14px 0;border-bottom:1px solid #eef3f3;font-size:15.5px;line-height:1.45}
.md-panel li i{width:18px;height:18px;border:1.5px solid var(--teal);border-radius:3px;flex:none;margin-top:2px;position:relative}
.md-panel li i::after{content:"";position:absolute;left:4px;top:1px;width:5px;height:9px;border-right:2px solid var(--teal);border-bottom:2px solid var(--teal);transform:rotate(45deg)}
.md-panel li span{flex:1}
.md-panel li em{font-style:normal;font-family:var(--sub);font-weight:700;font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:var(--teal);padding:4px 7px;border-radius:3px;white-space:nowrap;margin-top:1px}
.md-split{margin-top:22px;display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #dbe6e7;border-left:4px solid var(--teal);border-radius:6px;padding:18px 20px;font-size:15px}
.md-split b{color:var(--teal)}

.md-night{padding:96px 0;background:#fff}
.md-tl{display:grid;grid-template-columns:.9fr 1.1fr;gap:48px;margin-top:34px;align-items:start}
@media(max-width:900px){.md-tl{grid-template-columns:1fr;gap:24px}}
.md-tl ol{list-style:none;margin:0;padding:0;position:relative}
.md-tl ol::before{content:"";position:absolute;left:11px;top:18px;bottom:18px;width:2px;background:#dbe6e7}
.md-tl ol button{all:unset;cursor:pointer;display:grid;grid-template-columns:24px 82px 1fr;gap:14px;align-items:center;width:100%;padding:12px 0;box-sizing:border-box;min-height:24px}
.md-tl ol button::before{content:"";width:14px;height:14px;border-radius:50%;background:#fff;border:2px solid #b9d3d6;margin-left:3px;position:relative;z-index:1;transition:all .2s}
.md-tl ol button time{font:600 13px var(--body);color:var(--grey);font-variant-numeric:tabular-nums}
.md-tl ol button b{font:600 16px var(--body);color:var(--charcoal)}
.md-tl ol button[aria-pressed="true"]::before{background:var(--teal);border-color:var(--teal);box-shadow:0 0 0 5px var(--mist)}
.md-tl ol button[aria-pressed="true"] b{color:var(--teal)}
.md-tl ol button.past::before{background:var(--sky);border-color:var(--sky)}
.md-tl ol button:focus-visible{outline:3px solid var(--sky);outline-offset:2px;border-radius:6px}
.md-stage{background:var(--teal);color:#fff;border-radius:6px;padding:36px;min-height:280px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.md-stage::after{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);background-size:32px 32px;pointer-events:none}
.md-stage time{font-family:var(--serif);font-size:clamp(44px,6vw,64px);line-height:1;position:relative}
.md-stage h3{color:#fff;margin:14px 0 8px;position:relative}
.md-stage p{margin:0;font-size:16.5px;opacity:.92;max-width:460px;position:relative}
.md-stage .bar{margin-top:auto;padding-top:26px;display:flex;gap:6px;position:relative}
.md-stage .bar i{flex:1;height:4px;border-radius:2px;background:rgba(255,255,255,.25)}
.md-stage .bar i.on{background:var(--sky)}
.md-stage .nav{display:flex;gap:10px;margin-top:18px;position:relative}
.md-stage .nav button{background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.3);border-radius:6px;padding:10px 16px;font:600 14px var(--body);cursor:pointer;min-height:44px}
.md-stage .nav button:disabled{opacity:.35;cursor:default}
.md-fade{animation:mdFade .3s ease}
@keyframes mdFade{from{opacity:0}to{opacity:1}}

.md-why{padding:0 0 96px;background:#fff}
.md-why-grid{display:grid;grid-template-columns:repeat(3,1fr);border:1px solid #dbe6e7;border-radius:6px}
@media(max-width:860px){.md-why-grid{grid-template-columns:1fr}}
.md-why-grid>div{padding:28px;border-right:1px solid #dbe6e7}
.md-why-grid>div:last-child{border-right:0}
@media(max-width:860px){.md-why-grid>div{border-right:0;border-bottom:1px solid #dbe6e7}.md-why-grid>div:last-child{border-bottom:0}}
.md-why-grid .n{font-family:var(--sub);font-weight:700;font-size:12px;letter-spacing:.16em;color:var(--grey)}
.md-why-grid h4{margin:10px 0 8px}
.md-why-grid p{margin:0;font-size:15px;color:var(--grey)}
.md-sw{display:flex;gap:6px;margin-top:14px}
.md-sw span{font:700 10px var(--sub);letter-spacing:.1em;text-transform:uppercase;padding:5px 8px;border-radius:3px;color:#fff}

.md .sp-wrap{padding:96px 0;background:var(--soft);border-top:1px solid #dfe9ea}
.md .sp-chip{border-radius:6px}
.md .sp-card{border-radius:6px}
.md .ind-faq{padding:80px 0 96px;background:#fff}
""" + SCOPE_CSS + FAQ_CSS + "</style>"

MD_MAIN = f"""
<main class="md">
<section class="md-hero">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">Medical &amp; Dental Office Cleaning · Tampa Bay</span>
      <h1>Inspection-ready, every night.</h1>
      <p class="lede">Patients judge your practice by the waiting room before they meet you. We clean after hours from a written checklist for every zone, and leave a signed record of what was done.</p>
      <div class="btn-row">
        <a class="btn primary" href="#scope">Build your scope</a>
        <a class="btn outline" href="{TEL}">{PHONE_ICON}{PHONE}</a>
      </div>
    </div>
    <div class="md-board reveal d1" aria-label="Sample nightly log">
      <header><b>Nightly log</b><span>Sample · 6-room practice</span></header>
      <div class="row"><span>Exam rooms 1–4</span><small>6:58 PM</small><span class="ok">Done</span></div>
      <div class="row"><span>Operatories A–B</span><small>7:12 PM</small><span class="ok">Done</span></div>
      <div class="row"><span>Restrooms</span><small>7:29 PM</small><span class="ok">Done</span></div>
      <div class="row"><span>Front desk &amp; waiting room</span><small>7:58 PM</small><span class="ok">Done</span></div>
      <div class="row"><span>Floors, back to front</span><small>8:24 PM</small><span class="ok">Done</span></div>
      <p class="md-note">Signed by the crew lead before lockup, every visit.</p>
    </div>
  </div>
</section>

<section class="md-zones">
  <div class="wrap">
    <div class="reveal" style="max-width:660px">
      <span class="eyebrow">The checklist</span>
      <h2>Every zone has its own protocol.</h2>
      <p class="lede">Pick a zone to see what's on the list. High-touch points are disinfected every visit.</p>
    </div>
    <div class="md-zgrid reveal d1">
      <div class="md-tabs" role="tablist" aria-label="Practice zones">
{md_tabs}
      </div>
      <div>
{md_panels}
      </div>
    </div>
    <div class="md-split reveal"><span><b>Clear lines.</b> Your clinical team keeps responsibility for clinical equipment, sterilization and regulated waste. We handle everything around them, so nothing falls between the two.</span></div>
  </div>
</section>

<section class="md-night">
  <div class="wrap">
    <div class="reveal" style="max-width:660px">
      <span class="eyebrow">Tonight's protocol</span>
      <h2>What happens after you lock up.</h2>
      <p class="lede">A sample night at a six-room practice. Your schedule is built around your hours.</p>
    </div>
    <div class="md-tl reveal d1">
      <ol aria-label="Timeline">
{md_steps}
      </ol>
      <div class="md-stage" aria-live="polite">
        <div id="mdStage"><time>{MD_STEPS[0][0]}</time><h3>{MD_STEPS[0][1]}</h3><p>{MD_STEPS[0][2]}</p></div>
        <div class="bar" aria-hidden="true">{''.join('<i class="on"></i>' if i == 0 else '<i></i>' for i in range(len(MD_STEPS)))}</div>
        <div class="nav"><button type="button" id="mdPrev" disabled>Previous</button><button type="button" id="mdNext">Next step</button></div>
      </div>
    </div>
  </div>
</section>

<section class="md-why">
  <div class="wrap">
    <div class="md-why-grid reveal">
      <div><span class="n">01</span><h4>Written, not remembered</h4><p>A checklist for every zone, signed each visit. If something slips, you have something specific to point to.</p></div>
      <div><span class="n">02</span><h4>Color-coded cloths</h4><p>Restroom cloths never touch an exam room. Separate colors for each area keep cross-contamination out.</p>
        <div class="md-sw" aria-hidden="true"><span style="background:#b94a48">Restroom</span><span style="background:#2e6d76">Clinical</span><span style="background:#4a7fb0">Glass</span><span style="background:#5e8f5b">General</span></div></div>
      <div><span class="n">03</span><h4>A direct line to the owner</h4><p>No call center. If your office manager has a question at 7 AM, she texts the owner and gets an answer.</p></div>
    </div>
  </div>
</section>

{scope_section(page_key="md", eyebrow="Build your scope", title="Map out your practice.",
   intro="Tap the zones you need and how often. Your walkthrough request goes out with your choices, so we arrive with a plan.",
   areas=["Waiting room", "Front desk", "Exam rooms", "Dental operatories", "Restrooms", "Staff break room", "Hallways", "Entry glass"],
   facility="Medical / dental office")}

<section class="ind-faq">
  <div class="wrap" style="max-width:860px">
    <span class="eyebrow">Questions</span>
    <h2 style="margin-bottom:10px">Before you book.</h2>
    {faq([
      ("Do you clean clinical equipment?", "No. Clinical equipment, instruments and sterilization stay with your staff and their infection-control procedures. We clean the room around them: counters, sinks, touch points, dispensers and floors."),
      ("Do you handle sharps or biohazard waste?", "No. Those stay sealed for your licensed medical waste vendor. We remove general trash and recycling only."),
      ("Can you work around evening hours or Saturday clinics?", "Yes. We start after your last patient leaves and build the schedule around your hours, including late nights and weekend clinics."),
      ("How does the free trial clean work?", "After a free walkthrough, new recurring accounts get one trial clean at no charge. You see the checklist and the signed log before you commit."),
    ])}
  </div>
</section>
</main>
"""

MD_JS = """
<script>
(function(){
  // zone tabs (arrow keys move between tabs)
  var tabs=[].slice.call(document.querySelectorAll('.md-tabs [role=tab]'));
  function sel(t,focus){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;
    document.getElementById(x.getAttribute('aria-controls')).hidden=!on;});if(focus)t.focus();}
  tabs.forEach(function(t,i){t.addEventListener('click',function(){sel(t);});
    t.addEventListener('keydown',function(e){var d=e.key==='ArrowRight'||e.key==='ArrowDown'?1:e.key==='ArrowLeft'||e.key==='ArrowUp'?-1:0;
      if(d){e.preventDefault();sel(tabs[(i+d+tabs.length)%tabs.length],true);}});});
  // timeline stepper
  var S=""" + md_step_data + """,cur=0,stage=document.getElementById('mdStage'),
      btns=[].slice.call(document.querySelectorAll('.md-tl [data-step]')),bars=document.querySelectorAll('.md-stage .bar i'),
      prev=document.getElementById('mdPrev'),next=document.getElementById('mdNext');
  function go(n){cur=Math.max(0,Math.min(S.length-1,n));var s=S[cur];
    stage.innerHTML='<time>'+s.t+'</time><h3>'+s.h+'</h3><p>'+s.d+'</p>';stage.classList.remove('md-fade');void stage.offsetWidth;stage.classList.add('md-fade');
    btns.forEach(function(b,i){b.setAttribute('aria-pressed',i===cur);b.classList.toggle('past',i<cur);});
    bars.forEach(function(b,i){b.classList.toggle('on',i<=cur);});
    prev.disabled=cur===0;next.disabled=cur===S.length-1;}
  btns.forEach(function(b){b.addEventListener('click',function(){go(+b.dataset.step);});});
  prev.addEventListener('click',function(){go(cur-1);});next.addEventListener('click',function(){go(cur+1);});
})();
</script>"""

# ======================================================================
# RESTAURANT — dark, after-close story you scroll + inspection self-check
# ======================================================================
RS_STEPS = [
    ("11:30", "PM", "Doors lock. We walk in.", "Your closers head home. Our crew signs in and walks the room with tonight's checklist."),
    ("11:40", "PM", "Restrooms first", "Partitions, locks and fixtures disinfected. Floors and drains scrubbed, not just mopped. Dispensers refilled for the morning."),
    ("12:30", "AM", "The dining room", "Tables, chairs and the legs nobody looks at. Under the booths, high chairs, condiment stations and menus."),
    ("1:30", "AM", "The bar", "Bar top and rail, the mats lifted and cleaned, floor drains cleared of buildup, cooler doors and glass polished."),
    ("2:30", "AM", "Entry & host stand", "Front doors, windows and the host stand: the first thing your guests touch and the first thing an inspector sees."),
    ("3:00", "AM", "Floors last", "Back of the room to the front door, so nothing gets tracked across a clean floor."),
    ("6:00", "AM", "Ready to open", "The signed checklist is waiting at the host stand. Your opener walks into a room that's already done."),
]
rs_steps = "\n".join(
    f'<li class="rs-step" data-t="{t}" data-ap="{ap}" data-i="{i}"><span class="rs-mt">{t} {ap}</span><h3>{h}</h3><p>{d}</p></li>'
    for i, (t, ap, h, d) in enumerate(RS_STEPS))

RS_Q = [
    "Are restroom partitions, fixtures and floor drains detailed every night, not just wiped down?",
    "Is the floor under booths, tables and the bar cleaned nightly, not just the open floor?",
    "Are bar mats lifted and cleaned, and the floor drains free of buildup?",
    "Are high-dust spots (vents, light fixtures, ledges) on a regular schedule?",
    "Could you show an inspector a written cleaning schedule for the front of house today?",
]
rs_q = "\n".join(
    f'<div class="rs-q" data-q="{i}"{"" if i == 0 else " hidden"}><span class="rs-qn">Question {i+1} of {len(RS_Q)}</span><h3>{html.escape(q)}</h3>'
    f'<div class="rs-yn"><button type="button" data-a="1">Yes</button><button type="button" data-a="0">Not really</button></div></div>'
    for i, q in enumerate(RS_Q))

RS_CSS = """
<style>
.rs{--night:#0f2b30;--night2:#163a40;--glow:#b2dddf;background:var(--night);color:#e9f3f4}
.rs h1,.rs h2,.rs h3{color:#fff}
.rs .eyebrow{color:var(--glow)}
.rs .eyebrow::before{background:var(--glow)}
.rs .lede{color:#cfe2e4}
.rs-hero{position:relative;min-height:min(86vh,760px);display:flex;align-items:flex-end;overflow:hidden}
.rs-hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.rs-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,43,48,.35) 0%,rgba(15,43,48,.75) 55%,var(--night) 100%)}
.rs-hero .wrap{position:relative;z-index:1;padding-top:140px;padding-bottom:80px;width:100%}
.rs-hero h1{max-width:760px;font-size:clamp(44px,7vw,82px)}
.rs-hero .lede{max-width:620px}
.rs .btn.outline{color:#fff;border-color:rgba(255,255,255,.6)}
.rs .btn.outline:hover{background:#fff;color:var(--teal-dk)}
.rs-moon{position:absolute;right:8%;top:22%;z-index:1;width:84px;height:84px;border-radius:50%;box-shadow:-18px 10px 0 0 #f4f1e6;transform:rotate(-20deg);opacity:.85}
@media(max-width:700px){.rs-moon{width:56px;height:56px;right:10%;top:18%}}

.rs-story{padding:80px 0 40px}
.rs-sgrid{display:grid;grid-template-columns:.85fr 1.15fr;gap:60px;margin-top:20px}
@media(max-width:900px){.rs-sgrid{grid-template-columns:1fr;gap:0}}
.rs-clock{position:sticky;top:110px;align-self:start;padding:30px 0}
@media(max-width:900px){.rs-clock{top:78px;z-index:5;background:linear-gradient(var(--night) 80%,rgba(15,43,48,0));padding:14px 0 22px;margin:0 -4px}}
.rs-time{font-family:var(--serif);font-size:clamp(64px,10vw,128px);line-height:.95;color:#fff;font-variant-numeric:tabular-nums;display:flex;align-items:baseline;gap:12px}
.rs-time small{font-family:var(--sub);font-weight:700;font-size:16px;letter-spacing:.2em;color:var(--glow)}
@media(max-width:900px){.rs-time{font-size:52px}}
.rs-track{margin-top:20px;height:4px;background:rgba(255,255,255,.12);border-radius:2px;overflow:hidden}
.rs-track i{display:block;height:100%;width:0;background:var(--glow);transition:width .4s ease}
.rs-cap{margin-top:12px;font-size:13px;color:#9fbfc3}
@media(max-width:900px){.rs-cap{display:none}}
.rs-steps{list-style:none;margin:0;padding:0}
.rs-step{padding:12vh 0;border-top:1px solid rgba(255,255,255,.08);opacity:.32;transition:opacity .4s}
.rs-step:first-child{border-top:0;padding-top:30px}
.rs-step.on{opacity:1}
.rs-step h3{font-size:clamp(28px,3.4vw,40px);margin:6px 0 10px}
.rs-step p{font-size:18px;max-width:520px;margin:0;color:#cfe2e4}
.rs-mt{display:none;font-family:var(--sub);font-weight:700;font-size:12px;letter-spacing:.18em;color:var(--glow)}
@media(max-width:900px){.rs-step{padding:9vh 0}}
@media(prefers-reduced-motion:reduce){.rs-step{opacity:1}}

.rs-check{background:var(--night2);padding:96px 0}
.rs-cgrid{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
@media(max-width:900px){.rs-cgrid{grid-template-columns:1fr}}
.rs-photo{border-radius:20px;overflow:hidden;aspect-ratio:4/3}
.rs-photo img{width:100%;height:100%;object-fit:cover}
.rs-quiz{background:#fff;color:var(--charcoal);border-radius:20px;padding:32px;min-height:330px;display:flex;flex-direction:column}
.rs-quiz h3{color:var(--teal-dk);font-size:24px;line-height:1.3;margin:10px 0 22px}
.rs-qn{font-family:var(--sub);font-weight:700;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey)}
.rs-dots{display:flex;gap:6px;margin-bottom:18px}
.rs-dots i{flex:1;height:4px;border-radius:2px;background:#e3eeef}
.rs-dots i.on{background:var(--teal)}
.rs-yn{display:flex;gap:12px;flex-wrap:wrap}
.rs-yn button{flex:1;min-width:130px;padding:14px 18px;border-radius:12px;border:1.5px solid #cfe3e5;background:#fff;font:600 16px var(--body);color:var(--charcoal);cursor:pointer;min-height:48px}
.rs-yn button:hover{border-color:var(--teal);color:var(--teal)}
.rs-yn button:focus-visible{outline:3px solid var(--sky);outline-offset:2px}
.rs-res .score{font-family:var(--serif);font-size:64px;line-height:1;color:var(--teal)}
.rs-res .score small{font-size:24px;color:var(--grey)}
.rs-res p{margin:12px 0 20px}
.rs-res .again{background:none;border:0;color:var(--grey);text-decoration:underline;cursor:pointer;font:500 14px var(--body);margin-top:12px;padding:8px 0}
.rs-fine{font-size:12px;color:#9fbfc3;margin-top:14px}

.rs .sp-wrap.sp-dark{padding:96px 0;background:var(--night);--sp-line:rgba(255,255,255,.28);--sp-chip-bg:transparent;--sp-ink:#e9f3f4}
.rs .sp-dark .sp-freq input:checked+span{background:#fff;color:var(--night);border-color:#fff}
.rs .sp-dark .sp-chip[aria-pressed="true"]{background:var(--glow);border-color:var(--glow);color:var(--night)}
.rs .sp-dark .sp-chip[aria-pressed="true"]::before{background:var(--night);box-shadow:inset 0 0 0 3px var(--glow)}
.rs .sp-card h3{color:var(--teal-dk)}
.rs .ind-faq{padding:20px 0 96px;background:var(--night);--faq-line:rgba(255,255,255,.12);--faq-ink:#fff;--faq-body:#cfe2e4}
""" + SCOPE_CSS + FAQ_CSS + "</style>"

RS_MAIN = f"""
<main class="rs">
<section class="rs-hero">
  <img src="/images/commercial-restaurant.jpg" alt="" aria-hidden="true">
  <div class="rs-moon" aria-hidden="true"></div>
  <div class="wrap">
    <span class="eyebrow">Restaurant Cleaning · Tampa Bay</span>
    <h1>After close, we take the night shift.</h1>
    <p class="lede">Your team closes late and does what it can. We come in after them and reset the dining room, bar and restrooms, so you open to a room that's ready for guests and inspectors.</p>
    <div class="btn-row">
      <a class="btn primary" href="#scope">Build your scope</a>
      <a class="btn outline" href="{TEL}">{PHONE_ICON}{PHONE}</a>
    </div>
  </div>
</section>

<section class="rs-story" aria-label="A night with Protocol">
  <div class="wrap">
    <span class="eyebrow">One night, start to finish</span>
    <h2 style="max-width:640px">Scroll through a night with us.</h2>
    <div class="rs-sgrid">
      <div class="rs-clock" aria-hidden="true">
        <div class="rs-time"><span id="rsT">{RS_STEPS[0][0]}</span><small id="rsAp">{RS_STEPS[0][1]}</small></div>
        <div class="rs-track"><i id="rsBar"></i></div>
        <p class="rs-cap">A sample night. Your schedule is built around your close.</p>
      </div>
      <ol class="rs-steps">
{rs_steps}
      </ol>
    </div>
  </div>
</section>

<section class="rs-check">
  <div class="wrap rs-cgrid">
    <div class="reveal">
      <span class="eyebrow">Self-check</span>
      <h2>Are you inspection-ready?</h2>
      <p class="lede">Five quick questions about your front of house. Answer honestly, it's just for you.</p>
      <div class="rs-photo" style="margin-top:28px"><img src="/video/commercial-cleaning-poster-v2.jpg" alt="Cleaner wiping down a restaurant booth partition after close" loading="lazy"></div>
    </div>
    <div class="reveal d1">
      <div class="rs-quiz" id="rsQuiz" aria-live="polite">
        <div class="rs-dots" aria-hidden="true">{''.join('<i></i>' for _ in RS_Q)}</div>
{rs_q}
        <div class="rs-res" hidden></div>
      </div>
      <p class="rs-fine">A quick self-check, not an official health inspection.</p>
    </div>
  </div>
</section>

{scope_section(page_key="rs", eyebrow="Build your scope", title="Set up your night shift.",
   intro="Tap the areas you want covered and how often. Your walkthrough request goes out with your choices, so we arrive with a plan.",
   areas=["Dining room", "Bar", "Restrooms", "Entry & host stand", "Patio", "Private dining", "Windows & glass", "Back-of-house floors"],
   facility="Restaurant / bar", dark=True)}

<section class="ind-faq">
  <div class="wrap" style="max-width:860px">
    <span class="eyebrow">Questions</span>
    <h2 style="margin-bottom:10px">Before you book.</h2>
    {faq([
      ("Do you clean kitchen hoods or grease traps?", "No. Hoods and grease traps are specialty services with their own certifications. We focus on front of house, the bar, restrooms and entry. Back-of-house floors can be added at your walkthrough."),
      ("What time do you come in?", "After your last closer leaves, and we're done before your opener arrives. The exact window goes into your written protocol."),
      ("How do you get in after hours?", "During onboarding you give us a key or code and your alarm steps. Access details stay with the crew lead, and we lock up and arm the alarm on the way out."),
      ("How does the free trial clean work?", "After a free walkthrough, new recurring accounts get one trial clean at no charge. You open the next morning to the result before you sign anything."),
    ])}
  </div>
</section>
</main>
"""

RS_JS = """
<script>
(function(){
  // scroll story: the clock follows the step in view
  var steps=[].slice.call(document.querySelectorAll('.rs-step')),T=document.getElementById('rsT'),AP=document.getElementById('rsAp'),bar=document.getElementById('rsBar');
  function set(el){steps.forEach(function(s){s.classList.toggle('on',s===el);});T.textContent=el.dataset.t;AP.textContent=el.dataset.ap;
    bar.style.width=((+el.dataset.i+1)/steps.length*100)+'%';}
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)set(e.target);});},{rootMargin:'-45% 0px -45% 0px'});
    steps.forEach(function(s){io.observe(s);});}
  set(steps[0]);
  // self-check quiz
  var quiz=document.getElementById('rsQuiz'),qs=[].slice.call(quiz.querySelectorAll('.rs-q')),dots=quiz.querySelectorAll('.rs-dots i'),res=quiz.querySelector('.rs-res'),yes=0,at=0;
  function show(i){qs.forEach(function(q,n){q.hidden=n!==i;});dots.forEach(function(d,n){d.classList.toggle('on',n<i);});}
  function done(){qs.forEach(function(q){q.hidden=true;});dots.forEach(function(d){d.classList.add('on');});
    var msg=yes===5?'You\\'re in good shape. A written protocol keeps it that way when staff changes and busy weeks hit.'
      :yes>=3?'A few gaps. Those are usually the spots an inspector or a sharp-eyed guest finds first.'
      :'An inspector would likely notice. The good news: every one of these is on our nightly checklist.';
    res.innerHTML='<span class="rs-qn">Your result</span><div class="score">'+yes+'<small>/5</small></div><p>'+msg+'</p><a class="btn primary" href="#scope">Book a free walkthrough</a><br><button type="button" class="again">Start over</button>';
    res.hidden=false;res.querySelector('.again').addEventListener('click',function(){yes=0;at=0;res.hidden=true;show(0);});}
  qs.forEach(function(q,i){q.querySelectorAll('[data-a]').forEach(function(b){b.addEventListener('click',function(){yes+=+b.dataset.a;at=i+1;
    if(at<qs.length){show(at);var nb=qs[at].querySelector('button');if(nb)nb.focus();}else done();});});});
  show(0);
})();
</script>"""


def page(slug, head_kw, css, main, js):
    head = set_head(HEAD, slug=slug, **head_kw)
    out = head + css + PRE + main + FOOT
    out = out.replace("</body>", SCOPE_JS + js + "\n</body>", 1)
    open(f"{slug}.html", "w", encoding="utf-8").write(out)
    print("wrote", slug + ".html", len(out))


page("med-spa-cleaning",
     dict(title="Med Spa Cleaning in Tampa, FL | Protocol Facility Services",
          desc="Nightly treatment room resets for Tampa Bay med spas: a written cleaning protocol for every room, followed every visit. Free walkthrough and trial clean.",
          service_name="Med spa cleaning", service_type="Med spa cleaning"),
     MS_CSS, MS_MAIN, MS_JS)
page("medical-dental-office-cleaning",
     dict(title="Medical & Dental Office Cleaning in Tampa, FL | Protocol Facility Services",
          desc="After-hours cleaning for Tampa Bay medical and dental practices: a written checklist for every zone and a signed nightly log. Free walkthrough.",
          service_name="Medical and dental office cleaning", service_type="Medical office cleaning"),
     MD_CSS, MD_MAIN, MD_JS)
page("restaurant-cleaning",
     dict(title="Restaurant Cleaning in Tampa, FL | Protocol Facility Services",
          desc="Overnight restaurant cleaning in Tampa Bay: dining room, bar and restrooms reset after close so you open guest-ready and inspection-ready. Free walkthrough.",
          service_name="Restaurant cleaning", service_type="Restaurant cleaning"),
     RS_CSS, RS_MAIN, RS_JS)
