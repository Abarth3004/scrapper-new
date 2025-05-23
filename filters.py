def is_valid_job(text):
    text = text.lower()

    base_keywords = [
        "marketing",
        "communication",
        "digital",
        "digital media",
        "digital marketing",
        "social media",
        "advertising",
        "brand",
        "branding",
        "content",
        "strategy",
        "media",
        "comunicación",
        "medios digitales",
        "marketing digital",
        "redes sociales",
        "publicidad",
        "marca",
        "contenido",
        "estrategia",
        "medios"
    ]

    base_keywords = list(set(base_keywords))
    keywords = base_keywords + [f"junior {kw}" for kw in base_keywords]

    return any(kw in text for kw in keywords)
