# QCA/QW Atlas — student edition

This folder is an independent pedagogical edition of the QCA/QW family atlas.
It is intended for physics students: it introduces the ideas through examples,
diagrams, and a guided reading path before the technical details.

The canonical atlas and the project's scientific status remain in the source
repository:

- [Canonical family atlas](https://github.com/nacho09021973/qca-causal-cones/blob/research/gravitational-normalization-gate/docs/family_atlas/FAMILY_BIBLE.md)
- [Current project state](https://github.com/nacho09021973/qca-causal-cones/blob/research/gravitational-normalization-gate/state/CURRENT_STATE.md)

This copy does not replace those documents or extend their claims.

This is the introductory version of the [canonical family atlas](https://github.com/nacho09021973/qca-causal-cones/blob/research/gravitational-normalization-gate/docs/family_atlas/FAMILY_BIBLE.md).
It assumes basic quantum mechanics and some linear algebra.

The pedagogical edition explains intuitions and examples. The canonical atlas
remains authoritative for status, quantifiers, sources, and claim ceilings.
When details differ, the canonical atlas and [`CURRENT_STATE.md`](https://github.com/nacho09021973/qca-causal-cones/blob/research/gravitational-normalization-gate/state/CURRENT_STATE.md) prevail.

## Recommended path

1. [The physical question](00_the_question.md)
2. [QCA, quantum walks, and causal cones](01_qca_and_quantum_walks.md)
3. [A Weyl example on a lattice](02_weyl_bcc_example.md)
4. [How to read a family](03_how_to_read_a_family.md)
5. [Families and relations](04_families_and_relations.md)
6. [Failures and obstructions](05_failures_and_obstructions.md)

## An important warning

This project uses terms such as “emergent gravity,” “gauge,” and “Lorentz.”
They do not always mean the same thing. A local rule can produce an equation
resembling Weyl's equation in the infrared without producing a dynamical
metric, a gravitational source, or a microscopic gauge symmetry.

The question accompanying every result is:

> What exactly has been shown, under which assumptions, and what does it not
> allow us to conclude?

## Figures

The editable diagrams are in [`figures/`](figures/). They are Mermaid source
files, not decorative images: every arrow should be explainable by an atlas
card or report.
