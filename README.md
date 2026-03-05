# Skill Creator

Create and package AgentSkills for OpenClaw.

## What This Skill Does

The skill-creator provides guidance for building AgentSkills—modular packages that extend OpenClaw's capabilities with specialized knowledge, workflows, and tools.

Skills can provide:
- **Specialized workflows** - Multi-step procedures for specific domains
- **Tool integrations** - Instructions for working with file formats or APIs
- **Domain expertise** - Company-specific knowledge, schemas, business logic
- **Bundled resources** - Scripts, references, and assets for complex tasks

## When to Use This Skill

Use this skill when you need to:
- Create a new skill from scratch
- Update or iterate on an existing skill
- Package a skill for distribution
- Understand skill anatomy and best practices

## Quick Start

### 1. Initialize a New Skill

```bash
cd ~/.openclaw/workspace/skills
python3 scripts/init_skill.py <skill-name> --path . [--resources scripts,references,assets] [--examples]
```

Examples:
```bash
python3 scripts/init_skill.py pdf-editor --path . --resources scripts,references
python3 scripts/init_skill.py brand-assets --path . --resources assets --examples
```

### 2. Edit the Skill

1. Customize `SKILL.md` with:
   - YAML frontmatter (`name` and `description`)
   - Markdown body with instructions

2. Add bundled resources:
   - `scripts/` - Executable code (Python, Bash, etc.)
   - `references/` - Documentation to load as needed
   - `assets/` - Files for output (templates, icons, etc.)

3. Test your scripts by running them directly.

### 3. Package the Skill

```bash
python3 scripts/package_skill.py <path/to/skill-folder>
```

This validates the skill and creates a `.skill` file (zip) for distribution.

## Skill Anatomy

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
├── scripts/ (optional)
│   └── Executable code
├── references/ (optional)
│   └── Documentation
└── assets/ (optional)
    └── Output files
```

## Key Principles

- **Keep it concise** - Only add context OpenClaw doesn't already have
- **Use progressive disclosure** - Load detailed references only when needed
- **Match degrees of freedom** - Be specific where tasks are fragile, flexible where they're not

## File Structure Requirements

- `SKILL.md` is required for every skill
- YAML frontmatter must have `name` and `description` fields
- Skill name: lowercase, digits, hyphens only
- No extraneous documentation files (README.md, CHANGELOG.md, etc.)

## Scripts

The skill-creator includes helper scripts:

- `init_skill.py` - Generate a new skill template
- `package_skill.py` - Validate and package a skill

## See Also

- [SKILL.md](./SKILL.md) - Full technical documentation
