# F18 — Gravedad emergente de fractones

> Copia publicada del atlas canónico de `qca-causal-cones` (commit `0a4606c`). Las referencias a informes, teoría, scripts, debates y estado del repositorio de investigación, que es privado, aparecen como texto sin enlace.

[Atlas](../FAMILY_BIBLE.md)

## 1. Identidad

Fuente primaria: *Emergent gravity of fractons*, `biblioteca/arXiv-1702.07613.pdf`.

## 2. Cuantificadores congelados

| Campo | Alcance |
|---|---|
| Variables | Fractones y campo gauge tensorial de rango 2 (pp.1-4) |
| Restricción | Conservación de centro de masa y movilidad restringida (pp.1-3) |
| Excitación | Gravitón emergente en el modelo de juguete (pp.1-5) |
| Dinámica | Modelo de campo/lattice; no QCA unitaria CJWW (pp.8-12) |
| Test CJWW | No ejecutado |

## 3. Resultado

**`FRACTON_TENSOR_GRAVITY_PRIOR_ART / DIRECT_CJWW_QCA_BRIDGE_ABSENT`.**

El resultado relevante es la arquitectura de conservación y movilidad
subdimensional, no una certificación de métrica CJWW.

## Flujo visual

```mermaid
flowchart LR
 A["Conservación de centro de masa"] --> B["Fractones"] --> C["Gauge rank-2"] --> D["Gravitón emergente"]
 D -.-> E["Regla CJWW: ausente"]
```
