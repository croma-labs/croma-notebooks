# Croma notebooks

Análisis económicos con datos oficiales de gobierno, reproducibles de principio a fin con la [API de Croma](https://usecroma.com). Cada carpeta es un número del newsletter de Croma: el notebook con el análisis completo, los datos que usó y las gráficas.

*Economic analyses built on official government data, reproducible end to end with the Croma API. One folder per newsletter issue.*

## Números

| Fecha | Número | Fuentes |
|---|---|---|
| Octubre 2026 | [Tesla ya importa más que Toyota: qué está comprando Colombia en 2026](2026-10-importadores/analisis.ipynb) | DIAN (directorio de importadores), VUCE |

## Cómo correrlo

```bash
git clone https://github.com/croma-labs/croma-notebooks
cd croma-notebooks
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Sin API Key, cada notebook lee los CSV de su carpeta `data/`: la foto de los datos que usó el artículo. Con API Key, consulta la API y los actualiza:

```bash
export CROMA_API_KEY=...   # consíguela en https://usecroma.com
```

`croma.py` es un cliente mínimo: cada endpoint de Croma es un `POST` que responde `{"data": ...}`.

```python
import croma

croma.call("/co/vuce/tariff/v1", tariff_code="8703809000")
```

Todos los endpoints, parámetros y respuestas: [docs.usecroma.com](https://docs.usecroma.com).

## Sobre los datos

Todo sale de fuentes oficiales públicas; cada notebook dice cuáles y hasta qué fecha. Croma es un API | MCP que conecta más de 300 fuentes oficiales de gobierno en 9 países, para agentes, integraciones y soluciones a la medida.

¿Una pregunta que quieren ver respondida con datos? Abran un issue.

## Licencia

El código es MIT. Los datos son información pública de las entidades que los publican.
