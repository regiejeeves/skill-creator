---
name: new-skills
description: |
  Create new AgentSkills for OpenClaw and iteratively improve them. Use when users want to create a skill from scratch, update or optimize an existing skill, or improve a skill's triggering description.
  OpenClaw skills are simpler than Claude Code plugins - they're primarily a SKILL.md file with optional scripts/ and references/ folders.
---

# Skill Creator

Create and improve OpenClaw AgentSkills.

OpenClaw skills are simpler than Claude Code plugins:
- Primary file: `SKILL.md` with YAML frontmatter (name, description)
- Optional: `scripts/`, `references/`, `assets/` folders

## Workflow

### 1. Understand the User's Intent

Ask clarifying questions:
- What should the skill do?
- When should it trigger? (user phrases/contexts)
- Expected output format?
- Test cases needed?

### 2. Research

- Check existing skills in `~/.openclaw/workspace/skills/` for reference
- Research best practices for the skill domain

### 3. Write SKILL.md

Structure:
```yaml
---
name: skill-name
description: |
  What the skill does. Include when to trigger - specific contexts,
  user phrases, and use cases. This is the primary triggering mechanism.
---

# Skill Name

Detailed instructions...
```

**Key elements:**
- **name**: Skill identifier (kebab-case)
- **description**: When to trigger + what it does (make it "pushy" to improve triggering)
- **body**: Detailed instructions, patterns, examples

### 4. Test the Skill

Test with realistic prompts. For skills with testable outputs:
- Create test cases in `evals/evals.json`
- Run the skill on test prompts
- Evaluate results

### 5. Iterate Based on Feedback

Improve based on test results:
- Generalize from specific failures
- Keep prompts lean
- Explain the "why" behind instructions

## Skill Structure Reference

```
skill-name/
├── SKILL.md              # Required - name, description, instructions
├── scripts/             # Optional - executable scripts
├── references/          # Optional - docs loaded as needed
├── assets/              # Optional - templates, icons
└── evals/               # Optional - test cases
    └── evals.json
```

## Description Optimization

The description field determines triggering. To optimize:

1. Create 20 eval queries (8-10 should-trigger, 8-10 should-not-trigger)
2. Test current description trigger rate
3. Improve based on failures
4. Validate on held-out test set

Use realistic, specific queries - not abstract requests.

## Useful Commands

- List skills: `ls ~/.openclaw/workspace/skills/`
- Test skill loading: Check available_skills in conversation
