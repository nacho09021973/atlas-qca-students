# F15 — Derivación informacional de Weyl y Dirac como QCA

> Copia publicada del atlas canónico de `qca-causal-cones` (commit `0a4606c`). Las referencias a informes, teoría, scripts, debates y estado del repositorio de investigación, que es privado, aparecen como texto sin enlace.

[Atlas](../FAMILY_BIBLE.md)

## 1. Identidad

Alta documental: 2026-10-01. Fuente primaria: D’Ariano y Perinotti,
*Derivation of the Dirac Equation from Principles of Information Processing*,
`biblioteca/Derivation of the Dirac Equation from Principles of Information
Processing.pdf`, arXiv:1306.1934v2.

La familia deriva una QCA Weyl mínima y su acoplamiento Dirac a partir de
linealidad, unitaridad, localidad, homogeneidad e isotropía discreta. Es
distinta de F14: allí se clasifica el walk isotrópico de coin 2; aquí se da la
construcción de QCA, la emergencia del grafo/espacio y el acoplamiento Weyl–Dirac.

## 2. Cuantificadores congelados

| Campo | Alcance de la fuente |
|---|---|
| Sistemas | Conjunto numerable de sistemas fermiónicos con `s_g` componentes (pp.1-2, Ecs.1-3) |
| Principios | Linealidad, unitaridad, localidad, homogeneidad e isotropía (p.2) |
| Regla | `A = sum_h T_h tensor A_h` sobre un grafo de Cayley (pp.2-3, Ec.4) |
| Espacio | Grupos infinitos cuasi-isométricamente embebibles en `R^d`; análisis principal en `Z^d` (pp.3-4) |
| Caso 3D | BCC, cuatro soluciones Weyl `A^±, B^±` módulo simetrías (pp.4-5) |
| Acoplamiento | Dos autómatas Weyl acoplados localmente para obtener Dirac (pp.2, 5-6) |
| Límite | Bajo momento y masa pequeña; correcciones dispersivas a escala de red (pp.1, 7-8) |
| Test CJWW | No ejecutado; no hay cuatro especies ni controles métricos del proyecto |

## 3. Qué es geometría

La ficha cuenta como estructura geométrica el grafo de Cayley definido por los
generadores y relatores, su palabra-métrica y la embedding cuasi-isométrica
usada para recuperar una noción de espacio (pp.2-3, Ecs.7-9). La BCC aparece
como la presentación 3D que admite la QCA Weyl bajo las condiciones declaradas.

## 4. Qué no se cuenta como geometría

La cuasi-isometría, la isotropía del grafo y la dispersión Weyl/Dirac no
constituyen por sí mismas una métrica dinámica, una tetrada variable o un
campo gravitatorio. La distorsión ultrarrelativista tampoco fija una escala
física universal ni una respuesta a controles CJWW.

## 5. Regla microscópica

La evolución lineal de los campos fermiónicos es
`psi_g(t+1) = sum_{g'} A_{gg'} psi_{g'}(t)` (p.2, Ec.3). Homogeneidad y
localidad permiten escribirla con matrices `A_h` sobre el grafo de Cayley
(pp.2-3, Ec.4). En `Z^3`, el caso BCC usa cuatro generadores con relator
`h_1+h_2+h_3+h_4=0`; las soluciones Weyl aparecen en la resolución de las
condiciones de unitaridad (pp.4-5, Ecs.17-22). El acoplamiento de dos copias
Weyl produce el sector Dirac bajo las hipótesis del artículo (pp.5-6).

## 6. Kill tests

1. Localidad, homogeneidad y unitaridad: PASS documental bajo los principios
   fijados, pp.1-3.
2. Emergencia del grafo de Cayley y embedding cuasi-isométrico: PASS como
   construcción de la fuente, pp.2-4; no es un certificado de métrica física.
3. Soluciones Weyl 3D en BCC: PASS documental, pp.4-7.
4. Acoplamiento local Weyl–Dirac: PASS documental bajo la regla publicada,
   pp.5-6.
5. Puente directo a métrica CJWW variable y respuesta común: ABSENT.
6. Test de las cuatro especies: NOT_EXECUTED.

## 7. Resultado

**`INFORMATION_AXIOM_DERIVED_WEYL_DIRAC_QCA_PRIOR_ART /
DIRECT_CJWW_METRIC_BRIDGE_ABSENT`.**

Evidencia: lectura primaria acotada; no hay revisión independiente de la
ficha ni certificado algebraico nuevo. Informe: preflight F15.

## 8. Modo de fallo

El límite de transferencia es de alcance: los principios derivan una QCA
Weyl/Dirac concreta, pero no una teoría de controles métricos, backreaction o
universalidad de especies CJWW.

## 9. Qué deja vivo

Deja una arquitectura informacional para comparar con las condiciones de
homogeneidad/isotropía de F14 y con la QCA BCC de F12. Cualquier puente CJWW
requiere congelar un observable métrico y demostrar recuperación plana exacta.

## 10. Qué queda prohibido después

No presentar la derivación informacional como prueba de gravedad emergente ni
como derivación de la métrica CJWW. No interpretar las correcciones
ultrarrelativistas o la embedding cuasi-isométrica como escala física absoluta.

## Flujo visual

```mermaid
flowchart LR
  A["Principios informacionales"] --> B["Grafo de Cayley / BCC"]
  B --> C["QCA Weyl"]
  C --> D["Dos Weyl acoplados"]
  D --> E["Dirac a bajo k"]
  E -.-> F["Métrica CJWW variable: ausente"]
  F -.-> G["Cuatro especies: no ejecutado"]
```
