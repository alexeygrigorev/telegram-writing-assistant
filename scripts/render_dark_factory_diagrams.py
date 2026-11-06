"""Render article diagrams: uv run --with resvg-py python scripts/render_dark_factory_diagrams.py."""
from pathlib import Path
from html import escape
import re
import textwrap
import resvg_py

BASE = Path(__file__).resolve().parents[1] / 'assets/images/dark-software-factories'
symbols = {}
for name in ['linear-to-pr', 'shapiro-levels', 'wilger-checks']:
    for symbol in re.findall(r'<symbol.*?</symbol>', (BASE / f'{name}.svg').read_text(encoding='utf-8'), re.S):
        symbols[re.search(r'id="([^"]+)"', symbol)[1]] = symbol
COLORS = {'blue': ('#2563eb', '#eff6ff'), 'purple': ('#7c3aed', '#f5f3ff'), 'amber': ('#c2410c', '#fff7ed'), 'green': ('#648900', '#f5fbe7'), 'gray': ('#737373', '#f5f5f5')}


class Diagram:
    def __init__(self, name, title, desc, height):
        self.name = name
        markers = ''.join(f'<marker id="arrow-{c}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 10 5 0 10Z" fill="{v[0]}"/></marker>' for c, v in COLORS.items())
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>', '<defs>'+markers+''.join(symbols.values())+'<filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.07"/></filter><style>text{font-family:"Segoe UI",Arial,sans-serif;fill:#171717}symbol [stroke]{vector-effect:non-scaling-stroke}</style></defs>', f'<rect width="1200" height="{height}" fill="white"/>']

    def text(self, x, y, text, color='gray', size=22, weight=500, anchor='middle'):
        self.parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" style="fill:{COLORS[color][0]}">{escape(text)}</text>')

    def card(self, x, y, title, detail, color='blue', icon='issue', w=320):
        stroke, fill = COLORS[color]
        titles = textwrap.wrap(title, width=int((w-32)/14.5))
        details = textwrap.wrap(detail, width=int((w-32)/11.1))
        assert len(titles) <= 2 and len(details) <= 2, (title, titles, details)
        self.parts.append(f'<g transform="translate({x} {y})" filter="url(#shadow)"><rect width="{w}" height="170" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2"/><use href="#icon-{icon}" x="{w/2-17}" y="12" width="34" height="34" color="{stroke}"/>')
        for i, line in enumerate(titles):
            self.parts.append(f'<text x="{w/2}" y="{76 if len(titles)==1 else 69+i*31}" text-anchor="middle" font-size="28" font-weight="600">{escape(line)}</text>')
        for i, line in enumerate(details):
            self.parts.append(f'<text x="{w/2}" y="{115+i*28 if len(titles)==1 else 129+i*27}" text-anchor="middle" font-size="22" style="fill:#525252">{escape(line)}</text>')
        self.parts.append('</g>')

    def arrow(self, path, color='gray'):
        self.parts.append(f'<path d="{path}" fill="none" stroke="{COLORS[color][0]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow-{color})"/>')

    def save(self):
        svg = '\n'.join(self.parts+['</svg>'])
        (BASE / f'{self.name}.svg').write_text(svg, encoding='utf-8')
        (BASE / f'{self.name}.png').write_bytes(resvg_py.svg_to_bytes(svg_string=svg))
        print(self.name)


d = Diagram('comprehension-debt-cycle', 'The comprehension debt cycle', 'Prompt, generate code, run it, discover problems, and prompt again: more code, less understanding.', 690)
for x,y,title,detail,color,icon in [
    (440,25,'Your prompt','Describe the next change','blue','document'),
    (850,255,'AI-generated code','Add or modify code','purple','robot'),
    (440,485,'Run the code','Try the application','green','terminal'),
    (30,255,'Bugs and edge cases','Customization and new needs','amber','issue')]:
    d.card(x,y,title,detail,color,icon)
d.arrow('M760 110H998Q1010 110 1010 122V255')
d.arrow('M1010 425V558Q1010 570 998 570H760')
d.arrow('M440 570H202Q190 570 190 558V425')
d.arrow('M190 255V122Q190 110 202 110H440')
d.text(600,315,'More code','amber',34,600)
d.text(600,360,'Less understanding','amber',34,600)
d.text(600,405,'With each iteration')
d.save()

d = Diagram('code-review-loop','The repeated code-review loop','Agent writes code, a human reviews it, the agent rewrites it, and the human reviews again.',350)
for x,title,detail,color,icon in [(40,'Agent writes code','Implementation and tests','purple','robot'),(440,'Human reviews code','Dictates review notes','amber','search'),(840,'Agent rewrites','Another round of changes','purple','robot')]:
    d.card(x,35,title,detail,color,icon)
d.arrow('M360 120H440'); d.arrow('M760 120H840')
d.arrow('M1000 205V258Q1000 270 988 270H612Q600 270 600 258V205','amber')
d.text(810,313,'Review again','amber')
d.save()

d = Diagram('product-direction-loop','Setting direction and checking the product','A human sets direction, agents build and verify, and human product checks inform better direction.',350)
for x,title,detail,color,icon in [(40,'Human sets direction','Specs and architecture','blue','document'),(440,'Agents build and verify','Implementation and tests','purple','robot'),(840,'Human checks product','Use it; inspect behavior','green','user')]:
    d.card(x,35,title,detail,color,icon)
d.arrow('M360 120H440'); d.arrow('M760 120H840')
d.arrow('M1000 205V258Q1000 270 988 270H212Q200 270 200 258V205','blue')
d.text(600,313,'Refine direction from product behavior','blue')
d.save()

d = Diagram('shapiro-levels',"Dan Shapiro's levels 0 through 5",'A descending staircase from writing code to running a factory without routine code review.',815)
nodes=[('Level 0: Write code','AI suggests occasionally','gray','terminal'),('Level 1: Delegate','Hand off small tasks','blue','issue'),('Level 2: Pair','Stay in implementation','blue','user'),('Level 3: Review','Read agent-written code','purple','search'),('Level 4: Specify','Set checks; agents work','amber','document'),('Level 5: Run factory','No routine code review','green','workflow')]
for i,(title,detail,color,icon) in enumerate(nodes):
    x,y=30+164*i,30+130*i
    stroke,fill=COLORS[color]
    d.parts.append(f'<g transform="translate({x} {y})" filter="url(#shadow)"><rect width="320" height="105" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2"/><use href="#icon-{icon}" x="18" y="19" width="28" height="28" color="{stroke}"/><text x="58" y="41" font-size="20" font-weight="600">{escape(title)}</text><text x="160" y="78" text-anchor="middle" font-size="18" style="fill:#525252">{escape(detail)}</text></g>')
    if i<5:
        d.arrow(f'M{x+320} {y+52.5}H{x+375}V{y+130}')
d.save()

def staircase(name, title, desc, nodes, loop=None):
    six = len(nodes) == 6
    width, height = (320, 140) if six else (402, 150)
    dx, dy = (164, 170) if six else (246, 190)
    d = Diagram(name, title, desc, 30 + dy*(len(nodes)-1) + height + 35)
    for i,(heading, detail, color, icon) in enumerate(nodes):
        x,y = 30+dx*i,30+dy*i
        stroke,fill=COLORS[color]
        size=24 if six else 26
        lines=textwrap.wrap(detail,width=int((width-36)/(10.1 if six else 11.1)))
        assert len(lines)<=2,(heading,lines)
        d.parts.append(f'<g transform="translate({x} {y})" filter="url(#shadow)"><rect width="{width}" height="{height}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="2"/><use href="#icon-{icon}" x="18" y="22" width="28" height="28" color="{stroke}"/><text x="58" y="45" font-size="{size}" font-weight="600">{escape(heading)}</text>')
        for j,line in enumerate(lines):
            d.parts.append(f'<text x="{width/2}" y="{86+j*28}" text-anchor="middle" font-size="{20 if six else 22}" style="fill:#525252">{escape(line)}</text>')
        d.parts.append('</g>')
        if i<len(nodes)-1:
            d.arrow(f'M{x+width} {y+height/2}H{x+width+55}V{y+dy}')
    if loop:
        review_index=3 if six else 2
        rx,ry=30+dx*review_index,30+dy*review_index
        # Return through the gap between steps, with its own card entry point.
        d.arrow(f'M{rx+80} {ry}V{ry-dy+height}','amber')
        d.text(rx-190,ry+35,loop[0],'amber')
        d.text(rx-190,ry+67,loop[1],'amber')
    d.save()

staircase('sandstorm-workflow-diagram','Sandstorm ticket-to-merge workflow','Prepare a ticket and workspace, implement and review, fix problems, then open a PR and merge.',[
    ('Ready ticket','Human refines the task','blue','issue'),
    ('Isolated workspace','Separate task environment','blue','terminal'),
    ('Implement','Write code; fix problems','purple','robot'),
    ('Review','Check work; report problems','purple','search'),
    ('Open PR','Submit for integration','amber','pull-request'),
    ('Merge','Resolve merge conflicts','green','check')],('Problems found:','fix and review again'))

staircase('wilger-checks',"John Wilger's checks",'Isolate the task, test current code, review in a fresh session, check the live URL. Code edits require new tests.',[
    ('Isolated task','Own worktree','blue','issue'),
    ('Test current code','Evidence for this change','amber','check'),
    ('Fresh review','Reviewer cannot edit','purple','search'),
    ('Check live URL','Confirm it responds','green','browser')],('Code edited:','test again'))

staircase('linear-to-pr','Linear-to-PR workflow','Ready story, agent session, pull request with preview, then release checks.',[
    ('Ready story','Picked up from Linear','blue','issue'),
    ('Agent session','Follows repo instructions','purple','robot'),
    ('PR and preview','Running change to inspect','amber','pull-request'),
    ('Release checks','End-to-end tests','green','check')])

d=Diagram('escalation-to-humans-diagram','Human escalation paths','Routine work continues; ambiguous, high-risk or blocked tasks go to a human, then are reassessed.',550)
d.card(30,45,'Agent task','Specs or verification','purple','robot')
d.card(440,45,'Escalation rules','Can the agent proceed?','blue','issue')
d.card(850,45,'Continue work','Follow required checks','green','check')
d.arrow('M350 130H440');d.arrow('M760 130H850','green')
d.text(1010,30,'No escalation needed','green')
d.card(440,345,'Human decision','Clarify, approve or unblock','amber','user')
d.arrow('M680 215V345','amber')
d.text(700,264,'Ambiguous, higher risk','amber',anchor='start')
d.text(700,296,'or required check blocked','amber',anchor='start')
d.arrow('M520 345V215','blue')
d.text(425,284,'Reassess','blue')
d.save()

d=Diagram('keeping-factory-useful-diagram','Keep the factory useful','Product feedback improves specifications; maintenance improves the factory.',610)
d.card(440,25,'Maintain the factory','Tune process; refactor or split projects','gray','workflow')
d.text(1010,95,'When work slows,')
d.text(1010,126,'investigate and improve')
d.arrow('M600 195V260')
for x,title,detail,color,icon in [(30,'Specify','Acceptance criteria','blue','document'),(440,'Build and verify','Agents implement and check','purple','robot'),(850,'Use the product','Notice surprises and gaps','green','user')]:
    d.card(x,260,title,detail,color,icon)
d.arrow('M350 345H440');d.arrow('M760 345H850')
d.arrow('M1010 430V498Q1010 510 998 510H202Q190 510 190 498V430','blue')
d.text(600,555,'Improve specifications from product experience','blue')
d.save()

d=Diagram('agent-roles-workflow','Product manager, engineer and QA','The product manager refines the task, the engineer implements it, and QA verifies acceptance criteria. Failures return to the engineer.',440)
for x,title,detail,color,icon in [(30,'Product manager','Refine issue and criteria','blue','document'),(440,'Engineer','Implement the feature','purple','robot'),(850,'QA','Check every criterion','green','check')]:
    d.card(x,45,title,detail,color,icon)
d.arrow('M350 130H440');d.arrow('M760 130H850')
d.arrow('M1010 215V288Q1010 300 998 300H612Q600 300 600 288V215','amber')
d.text(800,344,'Failed criterion: fix and check again','amber')
d.text(600,405,'QA reports observations and does not edit the code')
d.save()
