---
name: plan-risk-review
description: >
  Perform a rigorous risk review of any plan, proposal, or design document - including PRDs, product
  roadmaps, project/team roadmaps, system and feature designs, technical architectures, RFCs, ADRs,
  migration plans, rollout strategies, and business or organizational proposals - using structured
  risk analysis combined with advanced critical thinking techniques: devil's advocacy (Ipcha Mistabra),
  assumption surfacing, inference auditing, and failure-of-imagination checks.
  Trigger whenever a user asks to review, critique, challenge, stress-test, red-team, or assess risks
  in any plan or proposal. Also trigger for: "play devil's advocate," "find blind spots," "pre-mortem,"
  "what could go wrong," or simply "review this plan" or "review this doc" - those are risk review
  requests regardless of domain.
---

# Plan Risk Review - Critical Thinking Applied to Plans

## Purpose

This skill guides the agent through a structured, multi-layered risk review of any plan, design,
or proposal. It goes beyond surface-level checklists by applying intelligence-analysis and
critical-thinking techniques to uncover hidden assumptions, challenge prevailing conceptions, and
imagine failure modes the plan's authors may not have considered.

The review produces a written risk assessment document that is both actionable and intellectually
honest about uncertainty. The process applies equally to software architectures, product roadmaps,
team initiatives, business proposals, and any other structured plan.

## Before You Begin

Read `references/critical-thinking-framework.md` in this skill's directory. It contains the detailed
analytical lenses you must apply during the review. Do not skip this step - the framework is the
core intellectual engine of the review.

## Inputs

The agent needs at least one of the following:
- A plan, design document, RFC, ADR, or proposal (text, file, or pasted content)
- A verbal description of what is being planned

If the input is vague, ask the user to clarify scope, goals, and constraints before proceeding.
If a file was uploaded, read it fully before starting.

## Review Process

Work through these five phases in order. Each phase builds on the previous one. Write your
analysis as you go - do not defer writing until the end.

---

### Phase 1: Comprehension - Understand Before You Challenge

Before critiquing anything, make sure you genuinely understand the plan. Misunderstanding
the plan and then critiquing your misunderstanding is worse than no review at all.

1. **Restate the plan's purpose** in one sentence. Confirm with the user if unsure.
2. **Map the key components**: What stakeholders, teams, systems, processes, dependencies,
   or external actors does the plan involve?
3. **Identify the plan's own stated assumptions** - things it explicitly takes for granted.
4. **Identify the plan's theory of success** - what has to go right for this to work?

Output a brief "Plan Summary" section capturing the above.

---

### Phase 2: Assumption Surfacing - What Is Being Taken for Granted?

This is the most important phase. Plans fail far more often because of flawed assumptions than
because of flawed logic. Apply the framework from `references/critical-thinking-framework.md`,
specifically the Assumption Audit.

For each assumption you surface, assess:
- **Is this assumption explicit or implicit?** Implicit ones are more dangerous.
- **Is this assumption justified?** What evidence supports it? Is the evidence current?
- **What happens if this assumption is wrong?** Trace the downstream consequences.
- **Is there a way to test this assumption before committing to the plan?**

Common categories of hidden assumptions (adapt examples to the document's domain):
- **Capacity/scale assumptions**: "Our system/team/process can handle 10x the current load" - based on what evidence?
- **Capability assumptions**: "The team has the skills and bandwidth to execute this" - have they done comparable work before?
- **Dependency assumptions**: "This team, vendor, or system will deliver on time and reliably" - who owns it, what's their track record?
- **Timeline assumptions**: "This will take N weeks/sprints" - does that include review, iteration, testing, and contingency?
- **Adoption/behavioral assumptions**: "Users/stakeholders will embrace this change" - what's the evidence, and what's the adoption plan?
- **Organizational assumptions**: "Leadership will approve this, fund it, and stay aligned through execution" - explicitly confirmed?
- **Compatibility/continuity assumptions**: "This is non-breaking and backward-compatible" - verified how, and for whom?
- **Resource assumptions**: "We have the budget, tooling, and headcount this requires" - allocated or assumed?
- **Market/context assumptions** (PRDs, roadmaps): "The problem, competitive landscape, and user needs will remain stable through delivery" - what's the plan if they shift?

Output an "Assumptions & Evidence" section listing each assumption, its justification status, and
its blast radius if wrong.

---

### Phase 3: Ipcha Mistabra - The Opposite Is More Likely

This is the devil's advocacy phase, named after the Aramaic Talmudic term meaning "the opposite
is apparent." The technique was institutionalized by Israeli military intelligence after the 1973
failure and is designed to break through "conception lock" - the state where a team becomes so
convinced of their plan's correctness that disconfirming evidence is ignored or rationalized away.

Apply these three techniques:

#### 3a. The Inversion Test
For each major claim or prediction in the plan, construct the strongest possible argument for
the opposite conclusion. Do not strawman - argue the inversion as if you genuinely believe it.

Example: If the plan says "Migrating to microservices will improve deployment velocity,"
argue the case that it will decrease deployment velocity (coordination overhead, distributed
debugging, contract management, CI/CD complexity).

The goal is not to prove the plan wrong, but to stress-test whether the authors have considered
the strongest counterarguments. If the inversion is easy to dismiss, the plan is probably sound
on that point. If the inversion is uncomfortably compelling, that is a risk.

#### 3b. The Little Boy from Copenhagen
(Named after the child in Hans Christian Andersen's "The Emperor's New Clothes" - the outsider
who sees what insiders cannot because he is not trapped in the prevailing conception.)

Ask: What would someone from outside this team, this company, or this domain see that the
authors might miss? Consider perspectives relevant to the document type:
- A new team member joining next month - does this plan stand on its own, or does it rely on tribal knowledge?
- An end user or customer who doesn't read release notes - how will they experience this change?
- The person responsible for operations or support after launch - can they handle what goes wrong?
- A finance or budget owner - does the cost math hold under realistic conditions?
- A competitor - could this plan inadvertently create an opening or signal strategic intent?
- A regulator, auditor, or legal reviewer - does this plan create compliance or liability exposure?

#### 3c. Failure of Imagination Check
The most dangerous risks are those the team never considered - not the ones they considered
and dismissed. This is the "unknown unknowns" quadrant.

Ask yourself:
- What scenario, if it occurred, would make this plan catastrophically wrong - and that the
  plan does not address at all?
- What has happened in similar migrations/rollouts/changes at other companies that surprised
  everyone?
- Is there a failure mode that the team would consider "impossible" or "not worth thinking
  about"? Examine that one especially.
- Are there second-order effects - things that happen as a consequence of the plan succeeding?

Output an "Ipcha Mistabra" section containing the inversions, outsider perspectives, and
imagination-stretching scenarios. Be specific and concrete, not vague.

---

### Phase 4: Structured Risk Register

Now synthesize everything from Phases 2 and 3 into a structured risk register. For each risk:

| Field | Description |
|-------|-------------|
| **Risk ID** | Sequential identifier (R1, R2, ...) |
| **Category** | Use categories relevant to the document's domain. Common ones: Technical, Security, Scalability, Performance, Schedule, Budgetary, Operational, Market/Competitive, Adoption/Behavioral, Contractual/Legal, Organizational, Strategic |
| **Description** | Clear statement of what could go wrong |
| **Trigger** | What conditions or events would cause this risk to materialize |
| **Probability** | Low / Medium / High - with reasoning |
| **Severity** | Low / Medium / High / Critical - with reasoning |
| **Priority** | Probability × Severity (use the higher of the two when in doubt) |
| **Detection** | How would we know this risk is materializing? What signals to watch? |
| **Mitigation** | What can be done to reduce probability or severity? |
| **Contingency** | If the risk materializes despite mitigation, what is the fallback? |
| **Assumption link** | Which assumption from Phase 2 does this risk relate to? |

Prioritize the register: address Critical and High priority risks first.

Distinguish between:
- **Known Knowns**: Risks that are well-understood and have established mitigations
- **Known Unknowns**: Risks we are aware of but cannot yet quantify
- **Unknown Unknowns**: Risks surfaced by the Ipcha Mistabra phase that were not in the
  original plan at all - flag these prominently

---

### Phase 5: Verdict & Recommendations

Close the review with an honest overall assessment.

**Do not sugarcoat.** If the plan has serious problems, say so clearly. If it is sound, say that too.
Intellectual honesty means being tentative where evidence is thin, and confident where evidence
is strong.

Structure:
1. **Overall Risk Level**: Low / Moderate / High / Critical - for the plan as a whole
2. **Top 3 Risks**: The risks that most deserve attention before proceeding
3. **Recommended Actions**: Concrete next steps appropriate to the document type, such as:
   - Assumptions to validate before proceeding (and how to validate them)
   - Experiments, prototypes, spikes, or pilots to run
   - Stakeholders or domain experts to consult
   - Fallback or rollback plans to define
   - Metrics, signals, or checkpoints to establish for early detection
   - Phased or incremental delivery strategies to reduce blast radius
4. **Open Questions**: Things the reviewer could not assess - be explicit about what you
   don't know. Saying "I don't know" is a strength, not a weakness.
5. **What the plan does well**: Acknowledge strengths. A good risk review is fair-minded, not
   adversarial.

---

## Output Format

Present the full review as a single, readable document with these sections:
1. Plan Summary (Phase 1)
2. Assumptions & Evidence (Phase 2)
3. Ipcha Mistabra - Devil's Advocacy (Phase 3)
4. Risk Register (Phase 4)
5. Verdict & Recommendations (Phase 5)

Use clear prose. Use tables for the risk register. Avoid unnecessary bullet nesting.

If the review is long, offer to save it as a markdown file.

## Calibration Notes

- **Be specific, not generic.** Vague risks are useless. Name the exact component, assumption,
  or condition that creates the risk. Bad: "There could be adoption issues." Good (PRD): "The
  plan assumes power users will voluntarily migrate to the new workflow, but there is no
  migration incentive and the old workflow remains available indefinitely." Good (technical): "The
  plan assumes the Postgres query planner will choose an index scan on `orders` at 10M rows,
  but the compound index on (user_id, created_at) may not cover the new filter clause."
- **Scale depth to plan size.** A two-paragraph plan gets a focused review. A 20-page RFC gets
  a thorough one. Don't produce a 3000-word review of a 200-word plan.
- **Maintain intellectual humility.** You are reviewing from the outside. The authors may have
  context you lack. Frame uncertainties as questions, not accusations.
- **Distinguish secrets from mysteries.** Some risks have knowable answers (a load test could
  resolve them) - those are "secrets." Others are genuinely unknowable (how users will behave
  after launch) - those are "mysteries." Recommend different approaches for each.
