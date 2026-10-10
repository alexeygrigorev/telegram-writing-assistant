import sys, json, re
sys.path.insert(0, "_internal/analysis")
from trends import load_by_date, DATES, seniority
from collections import Counter
by = load_by_date()
def skl(j, cat): return [s.lower() for s in ((j.get("position", {}).get("skills") or {}).get(cat) or [])]
def has(j, cat, *n): l = skl(j, cat); return any(x.lower() in l for x in n)
trainer = lambda j: has(j, "ml", "PyTorch", "TensorFlow", "scikit-learn", "CUDA", "RLHF") or has(j, "genai", "Fine-Tuning", "LoRA")
integ = lambda j: has(j, "genai", "RAG", "LangChain", "LangGraph", "CrewAI", "AutoGen", "MCP", "OpenAI API", "Anthropic API", "Function Calling", "AI Agents", "Agentic Workflows", "Multi-Agent Systems")
agents = lambda j: has(j, "genai", "AI Agents", "Agentic Workflows", "Multi-Agent Systems")
rag = lambda j: has(j, "genai", "RAG")
evals = lambda j: has(j, "genai", "LLM Evaluation")
fde = lambda j: bool(re.search(r"fde|forward.deploy", (j.get("position", {}).get("title") or ""), re.I))
out = {}
for d in DATES:
    js = by[d]; n = len(js)
    aif = [j for j in js if j.get("position", {}).get("ai_type", {}).get("type") == "ai-first"]
    loc = Counter()
    for j in js:
        l = (j.get("meta", {}).get("location") or "")
        loc["India" if re.search(r"IND|India", l) else "Other"] += 1
    sen = Counter(seniority(j.get("position", {}).get("title", "")) for j in js)
    out[d] = dict(n=n, india=loc["India"], fde=sum(map(fde, js)),
        trainer=100*sum(map(trainer, aif))/len(aif), integ=100*sum(map(integ, aif))/len(aif),
        agents=100*sum(map(agents, js))/n, evals=100*sum(map(evals, js))/n, rag=100*sum(map(rag, js))/n,
        junior=100*sen["Junior/Entry"]/n, sen={k: round(100*v/n,1) for k,v in sen.items()})
json.dump(out, open(sys.argv[1], "w"), indent=1)
for d,v in out.items(): print(d, v["n"], "india", v["india"], "fde", v["fde"], "tr %.1f in %.1f ag %.1f rag %.1f jr %.1f" % (v["trainer"], v["integ"], v["agents"], v["rag"], v["junior"]))
