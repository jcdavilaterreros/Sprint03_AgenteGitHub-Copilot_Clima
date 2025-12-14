# Sprint03_AgenteGitHub-Copilot_Clima
Repositorio para Sprint03 de Agente en GitHub Copilot para función Clima
# Agente de Clima (Sprint 3) — Primer agente inteligente

## Propósito
Este proyecto implementa un agente simple que responde consultas básicas sobre el clima (temperatura y condición) para distintas ciudades.  
El objetivo es dar los primeros pasos en la creación de un agente, entendiendo cómo se estructura un flujo de interacción y reforzando fundamentos de programación.

> Nota conceptual: un LLM puede actuar como “cerebro” del agente, interpretando instrucciones, razonando y decidiendo acciones; el agente además puede combinar herramientas externas y memoria. (En este sprint usamos datos simulados para mantenerlo simple.) :contentReference[oaicite:0]{index=0}

## Herramientas utilizadas
- GitHub (repositorio y control de versiones). :contentReference[oaicite:1]{index=1}
- GitHub Copilot (asistencia para generar/editar código).
- Python 3 (script simple y legible; ideal para principiantes). :contentReference[oaicite:2]{index=2}

## Flujo lógico de interacción del agente
1. El usuario escribe una pregunta o una ciudad (ej. “Lima” o “¿Qué clima hay en Cusco?”).
2. El agente extrae la ciudad objetivo (heurística simple).
3. El agente consulta un “dataset” simulado (diccionario) con temperaturas/condición.
4. El agente responde con un mensaje en lenguaje natural.
5. El agente pregunta si se desea realizar otra consulta (loop).

Este flujo usa el patrón percepción → procesamiento → acción:
- **Percepción:** lectura de texto del usuario (entrada).
- **Procesamiento:** normaliza, decide la ciudad, busca datos.
- **Acción:** responde con el clima y continúa o termina.

## Fundamentos de programación presentes (explicación en lenguaje natural)
Estos conceptos son los “bloques” del ejemplo:

- **Variables (contenedores de información):** guardan datos como la ciudad solicitada, la temperatura o la decisión de continuar. :contentReference[oaicite:3]{index=3}  
  Ejemplo mental: “cajas con etiquetas” que contienen valores (ciudad = “Lima”).

- **Condicionales (if/else):** permiten tomar decisiones.  
  Ejemplo: “si la ciudad existe en el dataset, devuelvo clima; si no existe, aviso que no la tengo registrada”. :contentReference[oaicite:4]{index=4}

- **Bucles (repetición hasta condición):** el agente puede seguir preguntando y respondiendo hasta que el usuario diga “salir”. :contentReference[oaicite:5]{index=5}

- **Funciones (recetas reutilizables):** agrupan pasos para no repetirlos.  
  Ejemplo: una función que obtiene el clima y otra que construye la respuesta final. :contentReference[oaicite:6]{index=6}

## Cómo ejecutar
Requisitos:
- Python 3 instalado.

Ejecutar:
```bash
python agent_clima.py
