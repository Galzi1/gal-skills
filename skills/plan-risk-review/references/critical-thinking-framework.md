# Critical Thinking Framework for Plan Risk Review

This reference document provides the analytical lenses to apply during the risk review. Each
lens is rooted in established critical thinking methodology and applies to any planning domain -
software, product, business, organizational. Examples below are drawn primarily from software
engineering; translate the pattern, not the literal example, when reviewing other document types.

## Table of Contents
1. [The Eight Elements of Reasoning](#1-the-eight-elements-of-reasoning)
2. [The Assumption Audit](#2-the-assumption-audit)
3. [Inference vs. Assumption Separation](#3-inference-vs-assumption-separation)
4. [Concept Examination](#4-concept-examination)
5. [The Ipcha Mistabra Doctrine](#5-the-ipcha-mistabra-doctrine)
6. [Three Thinking Modes](#6-three-thinking-modes)
7. [The Johari Risk Window](#7-the-johari-risk-window)
8. [Secrets vs. Mysteries](#8-secrets-vs-mysteries)
9. [Intellectual Standards Checklist](#9-intellectual-standards-checklist)
10. [Anti-Patterns to Watch For](#10-anti-patterns-to-watch-for)

---

## 1. The Eight Elements of Reasoning

Every plan is an act of reasoning. Examine each of these elements in the plan under review:

### Purpose
- What is the plan trying to achieve?
- Is the purpose clearly stated or must it be inferred?
- Is the purpose realistic and significant?
- Are there unstated secondary purposes (career advancement, technology preference, political maneuvering within the organization)?

### Question at Issue
- What problem is the plan solving?
- Is the problem clearly and precisely defined?
- Has the problem been decomposed into sub-problems?
- Is this the right problem to solve, or is the plan solving a symptom?
- Could the problem be framed differently, leading to a different solution?

### Assumptions
- What does the plan take for granted?
- Are these assumptions justified by evidence?
- Which assumptions, if wrong, would invalidate the plan?
- See the full Assumption Audit below.

### Point of View
- From whose perspective was this plan written?
- What perspectives are missing? (Operations, security, end users, downstream teams, finance)
- How would someone with a different point of view critique this plan?
- Is the plan author aware of their own biases?

### Information and Evidence
- What data supports the plan's claims?
- Is the data current, accurate, and relevant?
- What information is missing?
- Is the plan selectively citing favorable evidence while ignoring unfavorable evidence?
- Are there information sources the plan should have consulted but didn't?

### Concepts and Ideas
- What key technical concepts does the plan rely on? (e.g., "eventual consistency," "zero-downtime deployment," "backward compatibility")
- Are these concepts used precisely or loosely?
- Could alternative concepts reframe the solution space?
- Is the plan using buzzwords as substitutes for clear thinking?

### Inferences and Interpretations
- What conclusions does the plan draw from its evidence?
- Are these inferences logical and justified?
- Are there alternative inferences the same evidence could support?
- Does the plan conflate correlation with causation?

### Implications and Consequences
- What follows if the plan is implemented as proposed?
- What are the second-order and third-order effects?
- What are the negative implications the plan does not address?
- What are the consequences of *not* implementing this plan?

---

## 2. The Assumption Audit

Assumptions are the most common source of plan failure. They operate silently - we take them
for granted precisely because we don't question them.

### How to Surface Hidden Assumptions

1. **Read every declarative statement in the plan.** Behind each statement is at least one
   assumption. "We will deploy using blue-green deployment" assumes: the infrastructure
   supports it, the team knows how to do it, the state can be managed across two environments,
   the cost of running two environments is acceptable.

2. **Look for "will" statements.** "The API will handle 10k requests per second" - this is a
   prediction, not a fact. What assumption supports this prediction?

3. **Look for absent subjects.** "Testing will be completed by sprint 3" - who is doing the
   testing? With what resources? This assumes availability of testers and test environments.

4. **Look for implied "of course" assumptions.** These are things so obvious to the author that
   they don't mention them. "Of course our CI/CD pipeline can handle this." "Of course the
   team understands the legacy system." These are often the most dangerous.

5. **Check temporal assumptions.** Plans assume the world stays roughly the same between
   planning and execution. What could change? Departures, reorgs, dependency updates,
   security incidents, shifting priorities.

6. **Check dependency assumptions.** Every external dependency is an assumption about
   someone else's behavior, reliability, and priorities.

### Assumption Classification

For each assumption, classify it:

- **Foundational**: If this is wrong, the entire plan collapses. These need validation before
  proceeding.
- **Structural**: If this is wrong, the plan needs significant modification but is not dead.
  These should be monitored.
- **Peripheral**: If this is wrong, minor adjustments suffice. These can be accepted.

---

## 3. Inference vs. Assumption Separation

Plans frequently contain statements that blend assumptions (what is taken for granted) with
inferences (conclusions drawn from evidence). Separating them is critical because a sound
inference built on an unsound assumption produces a wrong conclusion that *feels* right.

### The Separation Exercise

For key plan decisions, decompose them:

**Example from a plan**: "We chose Kafka because our event volume will exceed what RabbitMQ
can handle."

- **Assumption 1**: Our event volume projections are accurate.
- **Assumption 2**: RabbitMQ has a hard ceiling at volume X.
- **Assumption 3**: Kafka does not have the same ceiling.
- **Inference**: Therefore Kafka is the right choice.

Now examine: Are the assumptions sound? Is the inference valid even if the assumptions hold?
(Maybe Kafka handles the volume but introduces operational complexity that exceeds the team's
capacity - a different assumption the inference ignores.)

### The Viewpoint Test

Different people make different inferences from the same facts because they hold different
assumptions. When reviewing a plan, ask: "What assumption would I need to hold for this
inference to seem obviously correct?" Then ask: "Is that assumption justified?"

---

## 4. Concept Examination

Plans use technical concepts as if they are self-evident. Often they are not. Examine key concepts:

### Concept Precision Check

- **Is the concept well-defined in context?** "Microservices" means different things to different
  teams. What does it mean in *this* plan?
- **Is the concept being used consistently?** Does "real-time" mean the same thing in section 1
  and section 4?
- **Is the concept load-bearing?** If the plan says "we'll use an event-driven architecture," the
  entire plan may rest on a particular interpretation of that concept. Pin it down.
- **Are there concept conflations?** Is the plan confusing "high availability" with "fault tolerance"?
  "Scalability" with "performance"? "Authentication" with "authorization"?

### Concept Alternatives

For each key concept, ask: What if we used a different concept to frame this?

- If the plan frames the problem as a "scaling" problem, what happens if you frame it as a
  "partitioning" problem?
- If the plan frames the solution as a "migration," what if it's framed as a "parallel run"?

Alternative concepts can reveal alternative solutions that the plan's framing has hidden.

---

## 5. The Ipcha Mistabra Doctrine

"Ipcha Mistabra" (איפכא מסתברא) is an Aramaic term meaning "the opposite is apparent" or
"the reverse stands to reason." In the Talmud, it signals that the obvious conclusion may be
wrong and the opposite deserves consideration.

After the intelligence failure of the 1973 Yom Kippur War, Israeli military intelligence
institutionalized this principle as a formal review mechanism - the Bikora (Review) department.
Its purpose: to challenge prevailing assessments and prevent "conception lock."

### Core Principles

1. **The right and obligation to think differently.** It is not enough to permit dissent - dissent
   must be actively sought and protected. A review that merely confirms the plan is worthless.

2. **Conception lock is the primary enemy.** When a team becomes convinced their plan is
   correct, confirming evidence is absorbed and disconfirming evidence is ignored or rationalized.
   The reviewer's job is to break through this.

3. **Humility as methodology.** The purpose of devil's advocacy is educational: to instill the
   habit of thinking "maybe I'm wrong" and checking oneself continuously. It is not about
   proving the plan wrong - it is about ensuring the authors have stress-tested their own
   thinking.

4. **The outsider's advantage.** Insiders are trapped in their context - their prior briefings,
   their team's conventions, their accumulated assumptions. An outsider (the "little boy from
   Copenhagen") can see what insiders cannot because they are not trapped in the prevailing
   conception. The reviewer should cultivate this outsider stance.

5. **The reviewer must take risks.** A reviewer who only makes safe, obvious observations
   from a comfortable distance is not doing their job. The reviewer should make concrete
   counter-assessments, even at the risk of being wrong. If the reviewer is never wrong,
   they are not being bold enough.

### Three Models of Review

These models can be combined:

- **The Inversion Model**: For each major plan assertion, construct the strongest case for
  the opposite. "This migration will reduce latency" → build the case that it will increase
  latency.

- **The Alternative Thinking Model**: Don't just critique - ask bigger questions that the plan
  doesn't address. "You're optimizing database queries, but have you considered whether the
  database is the right data store for this workload at all?"

- **The Real-Time Shadow Model**: Track the plan as it evolves and provide continuous
  challenge, not just a one-time review. Identify areas of disagreement and keep pushing on
  them.

### How to Argue the Inversion Without Strawmanning

1. Start from the plan's own evidence. Use the same data to construct the opposite conclusion.
2. Identify what the evidence does NOT say, not just what it says.
3. Seek out real-world examples where the opposite of the plan's prediction actually happened.
4. Do not invent implausible scenarios. The inversion must be credible - something a
   reasonable, informed person could believe.

---

## 6. Three Thinking Modes

Most plan authors think inductively - they gather data, identify patterns, and draw conclusions.
This is necessary but insufficient. Apply all three modes:

### Inductive (Bottom-Up)
- What does the available evidence tell us?
- Standard approach: collect data → identify patterns → form conclusion.
- Limitation: you are constrained by the data you have. If the data is incomplete (and it
  always is), your conclusions are incomplete.

### Deductive (Top-Down)
- Start from a hypothesis or principle and reason downward to what must be true.
- "If our system must serve users in 15 time zones with sub-100ms latency, what does that
  imply about our architecture?" - regardless of what the current codebase looks like.
- This is the Mendeleev approach: he deduced 30 unknown elements from the structure of
  the periodic table. Similarly, you can deduce missing components or risks from the
  structure of the plan.

### Systems Thinking (Lateral)
- No component exists in isolation. Every change ripples through the system.
- A developer optimizing a single service may not understand the economic constraints, the
  organizational politics, or the downstream effects on other teams.
- Zoom out: What is the broader system this plan is part of? What are the feedback loops?
  What are the emergent behaviors that could arise from the interaction of components?

---

## 7. The Johari Risk Window

Adapted from the Johari Window and intelligence analysis practice:

| | **We Know** | **We Don't Know** |
|---|---|---|
| **We Know We Know/Don't Know** | **Known Knowns**: Risks we understand and have mitigations for. Routine. | **Known Unknowns**: Risks we're aware of but can't yet quantify. Action: investigate, prototype, spike. |
| **We Don't Know We Know/Don't Know** | **Unknown Knowns**: Information buried in our own systems, docs, or team knowledge that we haven't connected to this plan. The answer exists - we just haven't asked the right question. Action: broaden consultation, search existing data. | **Unknown Unknowns**: Risks we haven't imagined. This is where failures of imagination live. Action: Ipcha Mistabra techniques, pre-mortems, scenario planning. |

The most dangerous quadrant is Unknown Unknowns, but the most actionable quadrant is often
Unknown Knowns - the answers that already exist in the organization but haven't been surfaced.

---

## 8. Secrets vs. Mysteries

This distinction, adapted from intelligence analysis, helps calibrate how to address each risk:

**A Secret** is something that has a definite answer, and that answer exists somewhere. Someone
knows it, or a test could reveal it.
- "Can our database handle 10M concurrent connections?" - run a load test.
- "Does the third-party API support pagination?" - read their docs or ask them.
- Secrets are resolved by investigation. Recommend specific investigations.

**A Mystery** is something that has no definite answer yet because it depends on future events,
human behavior, or complex system dynamics.
- "Will users adopt the new UI?" - nobody knows until it ships.
- "Will the competitor launch a similar feature first?" - unknowable.
- Mysteries are managed, not resolved. Recommend monitoring, flexibility, and fallback plans.

When the plan treats a mystery as if it were a secret (claiming certainty about an unknowable
outcome), flag it. When the plan treats a secret as if it were a mystery (throwing up its hands
about something that could be tested), also flag it.

---

## 9. Intellectual Standards Checklist

Apply these standards to the plan's reasoning:

- **Clarity**: Can a new team member understand this plan? Are terms defined?
- **Precision**: Are claims specific enough to be actionable and verifiable?
- **Accuracy**: Are the facts cited in the plan correct? Are the numbers real?
- **Relevance**: Does every section of the plan serve the stated purpose?
- **Depth**: Does the plan address the complexity of the problem, or does it oversimplify?
- **Breadth**: Does the plan consider alternative approaches and viewpoints?
- **Logic**: Do the conclusions follow from the evidence? Are there contradictions?
- **Fairness**: Does the plan fairly represent tradeoffs, or does it advocate for a predetermined
  conclusion?

---

## 10. Anti-Patterns to Watch For

These cognitive traps frequently appear in software plans:

### Conception Lock (Anchoring)
The team has been thinking about the problem one way for so long that alternatives feel
unthinkable. Look for plans that never seriously consider alternative approaches.

### Confirmation Bias in Evidence
The plan cites evidence that supports its proposal and omits evidence that doesn't.
"We benchmarked X and it performed well" - did you also benchmark Y and Z?

### The Streetlight Effect
Looking for risks only where it's easy to look. The plan thoroughly analyzes the new code but
ignores the deployment process, the monitoring gap, or the human workflow change.

### Optimism Bias in Timelines
Plans almost universally underestimate how long things take. If the plan says "2 weeks,"
ask what happens if it takes 6.

### Survivorship Bias
"Company X did this successfully" - how many companies tried and failed? You're only
hearing about the survivor.

### Sunk Cost Reasoning
"We've already invested 3 months in this approach" - irrelevant to whether the approach
is correct going forward.

### Complexity Denial
"It's just a simple migration" - migrations are never simple. Plans that describe complex
changes with words like "just," "simply," or "straightforward" deserve extra scrutiny.

### The Availability Heuristic
The plan over-indexes on risks from recent incidents and under-indexes on risks that haven't
happened recently (but could).

### Group Harmony Over Rigor
If the plan was produced by consensus, ask whether the consensus suppressed legitimate
dissent. Plans that say "the team agreed" may mean "nobody wanted to be the dissenter."
