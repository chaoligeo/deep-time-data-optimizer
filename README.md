# Deep-time Data Optimizer
## 深时科学数据检索优化器

This tool helps Earth scientists improve the discoverability, readability, and citability of their deep-time data.

It focuses on practical improvements used in real scientific workflows:

- Completeness assessment of essential metadata fields
- Standardization of geological age expressions and interval names
- Addition of structured, machine-readable fields
- Generation of clear natural-language summaries suitable for both human readers and AI systems
- Export of an optimized dataset ready for further use or deposition

The optimizer works on tabular data (CSV). It does not replace domain expertise; it highlights gaps and suggests concrete, standard-compliant improvements.

### Quick Start

```bash
git clone https://github.com/chaoligeo/deep-time-data-optimizer.git
cd deep-time-data-optimizer
pip install -r requirements.txt
streamlit run app.py
```

### What it checks and improves

- Presence of age information (numerical age and/or interval)
- Location information
- Lithology or rock type
- Taxonomic or stratigraphic unit names
- Reference or citation information
- Consistency of age units and formatting
- Suggestions for standard geological period/stage names where possible

### Design principles

- Uses terminology familiar to working Earth scientists (age in Ma, lithology, occurrence, stratigraphic unit, reference).
- Keeps the core schema simple and extensible.
- Produces outputs that are easier for both people and automated systems to parse and cite.

MIT License — see LICENSE.
