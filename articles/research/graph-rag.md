---
title: "Graph RAG"
created: 2026-02-18
updated: 2026-02-18
tags: [research, rag, graph-rag, agents, knowledge-graphs, neo4j, incident-response]
status: draft
---

# Graph RAG

Research on Graph RAG - using knowledge graphs to enhance retrieval-augmented generation for AI agents, particularly for production engineering and incident response.

## Resources

### Designing a Production Engineer Agent with GraphRAG

Source: https://www.decodingai.com/p/designing-production-engineer-agent-graphrag

Author: Anca Muscalagiu (Decoding AI newsletter). Published: 2026-01-20.

Overview: A detailed architecture walkthrough for building a Production Engineer agent that uses GraphRAG as its memory layer. When an alert fires, the agent identifies affected services and teams, understands how failures propagate through the system, and surfaces the context engineers need to act quickly. The article covers the full system design from alert ingestion to incident report generation.

Key Ideas:
- The core problem is not fixing production incidents but reconstructing context. Engineers spend most of their time stitching together information from dashboards, Slack threads, old postmortems, and workarounds buried in Confluence
- Traditional RAG retrieves semantically similar text chunks. GraphRAG retrieves connected knowledge by traversing relationships in a graph. This distinction matters because production questions are coverage and synthesis questions, not similarity questions
- GraphRAG works in two phases: graph generation (turning raw organizational knowledge into a structured, navigable graph) and query answering (using that structure to retrieve complete, connected context)
- The agent's real superpower is not reasoning but its structured memory. The knowledge graph encodes how on-call engineers already think: services, dependencies, ownership, incidents, and the artifacts that explain them

Key Insights:
- Enterprise systems decay not through broken code but through forgotten understanding. The system is held together by the accumulated memory of production engineers, which fails when someone is asleep, leaves, or the system grows beyond what one mind can hold
- GraphRAG is a set of RAG patterns where retrieval is guided by graph structure, not just similarity scores. A similarity-based retriever might return relevant chunks but still miss entire systems, related incidents, or differently worded documentation
- Community detection (hierarchical Leiden clustering) creates natural operational boundaries in the graph. These communities align with platform areas, interdependent service groups, or recurring incident classes, and they emerge from the data rather than being manually defined
- Community summaries become the primary unit of retrieval. When a query is issued, the system identifies relevant communities, generates intermediate answers from each, and merges them into a single global response
- The retrieval step becomes structural reasoning over the organization itself. You are no longer pulling relevant documents - you are reconstructing a slice of the system: which services are involved, how far the blast radius extends, who owns what, and which operational knowledge applies

Actionable Patterns:
- Separate graph memory from real-time data. The graph holds structure and history (populated daily from documentation sources). MCP servers provide current state (metrics, deployments, active discussions). Encode priority in the system prompt: MCP data takes precedence for the current incident, graph provides historical patterns
- Use a two-phase retrieval strategy: semantic search over node embeddings to find entry points, then graph traversal to expand through dependencies and ownership until you have the full dependency radius
- Build the graph once from existing documentation (Confluence, runbooks, postmortems, architecture docs), then update daily via scheduled batch jobs. Production topology changes slowly enough that daily syncs suffice
- Keep the agent loop explicit rather than using framework abstractions. The controller decides when to retrieve context, when to call tools, when to invoke the model, and when to stop. Retries and limits are owned by the application, making behavior predictable
- Flag discrepancies between graph knowledge and real-time MCP data explicitly in reports: "The graph shows no dependency between service A and B, but recent deployments suggest otherwise"

Technical Details:
- Architecture has five components: Alerting System (Prometheus/Alertmanager webhook to FastAPI), Agent Component (FastAPI server with Agent Controller, MCP Client, LLM Gateway), GraphRAG Component (Neo4j graph database with Graph Query Engine and offline Graph Extractor), MCP Servers (Confluence, GitHub, Slack, Prometheus via global MCP router), and Observability (Opik for prompt monitoring and trace logging)
- Graph schema (ontology) for production engineering:
  - Nodes: Service (name, domain, tier, repo, tags, embedding), Team (name, oncall channel, owners, embedding), Incident (id, timestamp, severity, summary, embedding), Runbook (url, title, steps summary, embedding), Doc (source, url, title, embedding), Release/PR (id, timestamp, author, summary, embedding)
  - Relationships: DEPENDS_ON (Service to Service), OWNED_BY (Service to Team), AFFECTED (Incident to Service), RESPONDED_BY (Incident to Team), HAS_RUNBOOK (Service to Runbook), DOCUMENTED_IN (Service/Incident to Doc), RELATED_TO (Incident to Incident), INTRODUCED_BY (Incident/Service to Release/PR)
- Embeddings are created from LLM-generated summaries of each node, not from raw documents. A Service node is embedded from its service summary, an Incident from its description, a Runbook from its condensed operational steps
- Graph generation pipeline: chunk source documents, extract elements (entities and relationships) via LLM, generate summaries for each element, convert elements to graph objects (nodes and edges), cluster into communities using hierarchical Leiden, generate community summaries
- Cypher query example for dependency expansion:
```
MATCH (s:Service {name: "payments-api"})
OPTIONAL MATCH (s)-[:DEPENDS_ON]->(dep:Service)
OPTIONAL MATCH (s)-[:OWNED_BY]->(t:Team)
OPTIONAL MATCH (s)-[:HAS_RUNBOOK]->(r:Runbook)
RETURN s, collect(dep) AS dependencies, t AS owner, collect(r) AS runbooks
```
- Bounded hop expansion to prevent subgraph explosion:
```
MATCH (s:Service {name: "payments-api"})-[:DEPENDS_ON*1..2]->(dep:Service)
RETURN s, collect(DISTINCT dep) AS deps_2_hops
```
- Implementation recommendation: LlamaIndex PropertyGraph for agentic GraphRAG queries, with reference implementation at https://developers.llamaindex.ai/python/examples/property_graph/agentic_graph_rag_vertex/
- Agent framework choice: custom Agent Controller over LangChain/LangGraph. Frameworks hide execution order and error handling behind abstractions that become liabilities in production
- System prompt priority encoding for MCP vs graph data:
```
When assembling incident context, treat information sources in this order:
1. MCP servers provide current state (deployments, metrics, discussions)
2. Graph provides historical patterns and documented structure
3. If they conflict, use MCP data and note the discrepancy in your report
```

Data Flow:
1. Prometheus detects threshold breach, fires webhook to Alerting Manager
2. Alerting Manager routes to FastAPI server, which hands off to Agent Controller
3. Agent Controller queries GraphRAG - Graph Query Engine does semantic search for closest communities and fetches them with dependencies
4. Agent Controller sends plan to LLM specifying which MCP servers to call
5. LLM returns required tools, Agent Controller invokes Global MCP Server
6. Each MCP server is called: GitHub for recent changes, Slack for discussions, Confluence for documentation, Prometheus for current metrics
7. All context (graph + MCP) sent to LLM for synthesis
8. LLM produces structured incident report with impact summary, pattern recognition, recent changes, current state, recommended actions
9. Report posted to affected team channels via Slack MCP Server
10. Steps 6-9 can loop if the LLM requests additional tool calls

Quotes:
- "GraphRAG is a set of RAG patterns where retrieval is guided by graph structure, not just similarity scores"
- "We are no longer pulling relevant documents. We are reconstructing a slice of the system: which services are involved, how far the blast radius extends, who owns what, and which operational knowledge applies"
- "The retrieval step becomes an act of structural reasoning over the organization itself"
- "Most production incidents are not slowed down by the lack of a fix. They are slowed down by the lack of clarity"
- "Each component should solve one problem well and expose a stable boundary to the rest of the system"
- "The embeddings tell the system where to start. The graph tells it what else matters"
- "Frameworks like LangChain or LangGraph are useful for prototyping, but they often hide execution order and error handling behind abstractions that become liabilities in production"

References cited in the article:
- Zilliz Learn: GraphRAG Explained - https://medium.com/@zilliz_learn/graphrag-explained-enhancing-rag-with-knowledge-graphs-3312065f99e1
- LlamaIndex: Agentic GraphRAG with Property Graphs - https://developers.llamaindex.ai/python/examples/property_graph/agentic_graph_rag_vertex/
- JingleMind: Mastering Advanced RAG Methods with Neo4j - https://medium.com/@jinglemind.dev/mastering-advanced-rag-methods-graphrag-with-neo4j-implementation-with-langchain-42b8f1d05246

## Notes

This article connects directly to the agentic memory research. The key differentiator of GraphRAG over traditional RAG is the shift from similarity-based retrieval to structural reasoning. Traditional vector search answers "what text is similar to my query?" while GraphRAG answers "what is connected to the thing I found?"

The production engineer use case is compelling because it demonstrates a domain where flat document retrieval genuinely fails. An incident involving payments-api requires understanding not just what payments-api is, but what it depends on (auth-service, ledger-service), who owns it (Payments Platform team), what runbooks exist, and whether similar incidents have occurred before. No amount of embedding similarity captures this multi-hop relational structure.

The ontology design is a critical decision. The article uses a relatively simple schema (6 node types, 8 relationship types) that maps to how engineers already think about production systems. This aligns with the Fixed Entity Architecture insight from the agentic memory research - when you know your domain, a curated ontology outperforms LLM-extracted entity graphs.

The MCP integration pattern is worth noting: static knowledge lives in the graph (updated daily), while dynamic knowledge flows through MCP servers in real time. This separation of concerns avoids the freshness problem that plagues many RAG systems. The system prompt explicitly encodes priority: MCP data wins over graph data for the current incident, with discrepancies flagged rather than silently resolved.

The explicit agent controller pattern (no LangChain/LangGraph) reflects a growing consensus in production AI systems: framework abstractions that simplify prototyping become debugging nightmares in production. When your agent is responding to a 2am incident, you need predictable, inspectable execution flow.

For our own work, the most transferable patterns are: (1) the two-phase retrieval strategy (embeddings for entry points, graph traversal for context expansion), (2) the ontology-first approach to knowledge graph design, (3) the separation of static graph knowledge from real-time tool access, and (4) community-based summarization as a retrieval unit rather than individual documents.

## Sources

[^1]: [20260218_143953_AlexeyDTC_msg1947.md](../../inbox/used/20260218_143953_AlexeyDTC_msg1947.md)
[^2]: https://www.decodingai.com/p/designing-production-engineer-agent-graphrag
[^3]: Related LinkedIn post: https://www.linkedin.com/feed/update/urn:li:activity:7424806464000651264
