"""Shared pieces for the industry pages (med spa, medical & dental, restaurant).

Each page = the commercial page's head, header, base CSS, footer and popup,
with its own <main> content in between. Run build_industry.py to regenerate.
"""
import json, re, html

SITE = "https://www.protocolcommercialcleaning.com"
PHONE = "(508) 205-8810"
TEL = "tel:5082058810"


def split_template(path="commercial.html"):
    s = open(path, encoding="utf-8").read()
    head_end = s.index("</head>")
    head = s[:head_end]
    start = s.index('<section class="com-hero">')
    pre_body = s[head_end:start]           # </head><body>, banner, header, helper JS, base CSS
    foot = s[s.index("<footer>"):]          # footer, trial popup, scripts
    return head, pre_body, foot


def set_head(head, *, title, desc, slug, service_name, service_type):
    url = f"{SITE}/{slug}"
    head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)}</title>", head, count=1)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + html.escape(desc), head, count=1)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + html.escape(title), head, count=1)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + html.escape(desc), head, count=1)
    head = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', head, count=1)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + url, head, count=1)
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "name": service_name, "serviceType": service_type,
             "provider": {"@id": f"{SITE}/#business"},
             "areaServed": [{"@type": "City", "name": c} for c in ["Tampa, FL", "St. Petersburg, FL", "Clearwater, FL"]],
             "url": url},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": service_name, "item": url}]},
        ],
    }
    head = re.sub(r'<script type="application/ld\+json">.*?</script>',
                  lambda m: '<script type="application/ld+json">' + json.dumps(schema) + "</script>", head, count=1, flags=re.S)
    return head


# ---------- shared component: scope picker + walkthrough request ----------
SCOPE_CSS = """
.sp{display:grid;gap:40px;grid-template-columns:1.1fr .9fr;align-items:start}
@media(max-width:900px){.sp{grid-template-columns:1fr;gap:28px}}
.sp-chips{display:flex;flex-wrap:wrap;gap:10px;margin:18px 0 26px}
.sp-chip{font-family:var(--body);font-size:15px;line-height:1.2;padding:12px 16px;border-radius:999px;border:1.5px solid var(--sp-line,#cfe3e5);
  background:var(--sp-chip-bg,#fff);color:var(--sp-ink,var(--charcoal));cursor:pointer;display:inline-flex;align-items:center;gap:8px;min-height:44px;transition:background .15s,border-color .15s,color .15s}
.sp-chip::before{content:"";width:16px;height:16px;border-radius:50%;border:1.5px solid currentColor;opacity:.55;flex:none;box-sizing:border-box}
.sp-chip[aria-pressed="true"]{background:var(--teal);border-color:var(--teal);color:#fff}
.sp-chip[aria-pressed="true"]::before{opacity:1;background:#fff;box-shadow:inset 0 0 0 3px var(--teal)}
.sp-chip:focus-visible{outline:3px solid var(--sky);outline-offset:2px}
.sp-freq{display:flex;flex-wrap:wrap;gap:8px}
.sp-freq label{cursor:pointer}
.sp-freq input{position:absolute;opacity:0;pointer-events:none}
.sp-freq span{display:inline-block;padding:10px 16px;border-radius:10px;border:1.5px solid var(--sp-line,#cfe3e5);font-size:14px;min-height:44px;line-height:22px;background:var(--sp-chip-bg,#fff);color:var(--sp-ink,var(--charcoal))}
.sp-freq input:checked+span{background:var(--charcoal);border-color:var(--charcoal);color:#fff}
.sp-freq input:focus-visible+span{outline:3px solid var(--sky);outline-offset:2px}
.sp-card{background:#fff;border-radius:var(--r);padding:30px;box-shadow:0 18px 50px rgba(31,81,89,.12);color:var(--charcoal)}
.sp-card h3{margin-bottom:6px}
.sp-sum{font-size:14px;color:var(--grey);background:var(--mist);border-radius:10px;padding:12px 14px;margin:14px 0 18px;min-height:46px}
.sp-sum b{color:var(--teal-dk)}
.sp-label{font-family:var(--sub);font-weight:700;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--sp-ink,var(--teal));display:block;margin-bottom:4px}
"""


def scope_section(*, page_key, eyebrow, title, intro, areas, facility, dark=False):
    chips = "\n".join(
        f'<button type="button" class="sp-chip" aria-pressed="false" data-area="{html.escape(a)}">{html.escape(a)}</button>'
        for a in areas)
    freqs = ["Nightly", "3x a week", "2x a week", "Weekly", "Not sure yet"]
    freq = "\n".join(
        f'<label><input type="radio" name="{page_key}-freq" value="{f}"{" checked" if i == 0 else ""}><span>{f}</span></label>'
        for i, f in enumerate(freqs))
    return f"""
<section class="sp-wrap {'sp-dark' if dark else ''}" id="scope">
  <div class="wrap sp">
    <div class="reveal">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{title}</h2>
      <p class="lede">{intro}</p>
      <span class="sp-label" id="{page_key}-areas-l">Areas you need covered</span>
      <div class="sp-chips" role="group" aria-labelledby="{page_key}-areas-l">
{chips}
      </div>
      <span class="sp-label" id="{page_key}-freq-l">How often</span>
      <div class="sp-freq" role="radiogroup" aria-labelledby="{page_key}-freq-l">
{freq}
      </div>
    </div>
    <div class="sp-card reveal d1">
      <h3>Request your walkthrough</h3>
      <p style="font-size:15px;color:var(--grey);margin:0">We reply within 24 hours. New recurring accounts get a free trial clean after the walkthrough.</p>
      <form id="{page_key}Form" onsubmit="return false">
        <div class="sp-sum" aria-live="polite" data-sum>Tap the areas you need and they'll show up here.</div>
        <input type="hidden" id="{page_key}-areas" data-areas>
        <label for="{page_key}-areas" hidden>Areas needed</label>
        <input type="hidden" id="{page_key}-often" data-often>
        <label for="{page_key}-often" hidden>Frequency</label>
        <input type="hidden" id="{page_key}-type" value="{html.escape(facility)}">
        <label for="{page_key}-type" hidden>Facility type</label>
        <div class="fld"><label for="{page_key}-biz">Business name</label><input id="{page_key}-biz" type="text" autocomplete="organization" placeholder="Your business"></div>
        <div class="form-row">
          <div class="fld"><label for="{page_key}-phone">Phone</label><input id="{page_key}-phone" type="tel" required autocomplete="tel" placeholder="(813) 555-0123"></div>
          <div class="fld"><label for="{page_key}-email">Email</label><input id="{page_key}-email" type="email" required autocomplete="email" placeholder="you@business.com"></div>
        </div>
        <button type="button" class="btn primary" style="width:100%" data-send="{html.escape(facility)} walkthrough request">Request my walkthrough</button>
        <p class="form-fine" style="margin-top:10px">No prices until we've seen your space. No obligation.</p>
      </form>
    </div>
  </div>
</section>"""


SCOPE_JS = """
<script>
(function(){
  document.querySelectorAll('.sp-wrap').forEach(function(sec){
    var form=sec.querySelector('form'),sum=sec.querySelector('[data-sum]'),
        areas=sec.querySelector('[data-areas]'),often=sec.querySelector('[data-often]');
    function update(){
      var on=[].map.call(sec.querySelectorAll('.sp-chip[aria-pressed="true"]'),function(c){return c.dataset.area;});
      var f=sec.querySelector('.sp-freq input:checked');
      areas.value=on.join(', ');often.value=f?f.value:'';
      sum.innerHTML=on.length?('<b>'+on.length+' area'+(on.length>1?'s':'')+'</b>, '+(f?f.value.toLowerCase():'')+': '+on.join(', ')):'Tap the areas you need and they\\'ll show up here.';
    }
    sec.querySelectorAll('.sp-chip').forEach(function(c){c.addEventListener('click',function(){
      c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')==='true'?'false':'true');update();});});
    sec.querySelectorAll('.sp-freq input').forEach(function(r){r.addEventListener('change',update);});
    var btn=sec.querySelector('[data-send]');
    btn.addEventListener('click',function(){if(!tcsValid(form))return;update();tcsSend(form,btn.dataset.send);});
    update();
  });
})();
</script>"""

FAQ_CSS = """
.ind-faq details{border-bottom:1px solid var(--faq-line,#dfe9ea);padding:6px 0}
.ind-faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:16px;
  font-family:var(--sub);font-weight:700;font-size:17px;color:var(--faq-ink,var(--teal));padding:16px 0;min-height:44px}
.ind-faq summary::-webkit-details-marker{display:none}
.ind-faq summary::after{content:"+";font-family:var(--body);font-weight:300;font-size:26px;line-height:1;transition:transform .2s}
.ind-faq details[open] summary::after{transform:rotate(45deg)}
.ind-faq details p{margin:0 0 18px;max-width:680px;color:var(--faq-body,var(--charcoal))}
"""


def faq(items):
    return "\n".join(
        f"<details><summary>{html.escape(q)}</summary><p>{a}</p></details>" for q, a in items)


PHONE_ICON = '<svg class="icn" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.37 1.9.72 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.35 1.85.59 2.81.72A2 2 0 0 1 22 16.92z"></path></svg>'
