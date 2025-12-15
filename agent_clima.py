def normalizar_texto(texto: str) -> str:
    return texto.strip().lower()


def obtener_clima_simulado(ciudad: str) -> dict | None:
    # Dataset simulado (puedes ampliarlo con más ciudades)
    clima_por_ciudad = {
        "lima": {"temp_c": 22, "condicion": "Soleado"},
        "arequipa": {"temp_c": 20, "condicion": "Despejado"},
        "cusco": {"temp_c": 14, "condicion": "Parcialmente nublado"},
        "trujillo": {"temp_c": 24, "condicion": "Soleado"},
        "piura": {"temp_c": 28, "condicion": "Caluroso"},
    }

    ciudad = normalizar_texto(ciudad)
    return clima_por_ciudad.get(ciudad)


def extraer_ciudad(pregunta: str) -> str:
    """
    Heurística simple:
    - Si el usuario escribe solo una palabra (ej. "Lima"), se asume que es la ciudad.
    - Si escribe una frase, se intenta tomar la última palabra como ciudad.
      (Ej. "Qué clima hay en Cusco" -> "Cusco")
    """
    texto = pregunta.strip()
    if not texto:
        return ""

    partes = texto.split()
    if len(partes) == 1:
        return partes[0]

    # Intento básico: última palabra
    return partes[-1]


def construir_respuesta(ciudad: str, clima: dict | None) -> str:
    if not ciudad:
        return "No identifiqué una ciudad. Escribe, por ejemplo: Lima, Cusco o Arequipa."

    if clima is None:
        return f"No tengo datos para '{ciudad}'. Prueba con: Lima, Arequipa, Cusco, Trujillo o Piura."

    return f"En {ciudad.title()}: {clima['temp_c']}°C, {clima['condicion']}."


def main() -> None:
    print("Agente de Clima (simulado)")
    print("Escribe una ciudad (ej. Lima) o una pregunta (ej. ¿Qué clima hay en Cusco?).")
    print("Para salir, escribe: salir\n")

    while True:
        entrada = input("Usuario: ").strip()
        if normalizar_texto(entrada) in {"salir", "exit", "quit"}:
            print("Agente: Listo. ¡Hasta luego!")
            break

        ciudad = extraer_ciudad(entrada)
        clima = obtener_clima_simulado(ciudad)
        respuesta = construir_respuesta(ciudad, clima)

        print(f"Agente: {respuesta}")

        continuar = input("Agente: ¿Deseas consultar otra ciudad? (si/no): ").strip()
        if normalizar_texto(continuar) not in {"si", "sí", "s", "yes", "y"}:
            print("Agente: Listo. ¡Hasta luego!")
            break

        print()  # línea en blanco para legibilidad


if __name__ == "__main__":
    main()
