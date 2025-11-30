STRUCTURAL_MAP = {
    "PUNCTUATION_MAP": {
        "។": [".", "", "៕"],             # Khmer full stop → English period, missing, or ៕
        "៕": ["។", ".", ""],             # Literary full stop → confused with others or omitted
        "៖": [":", ";", ""],             # Khmer colon → English colon, semicolon, or missing
        "ៗ": ["2", ""],                  # Repetition sign → mistyped as numeral 2 or dropped
        "“": ['"', "'"],                 # Curly opening quote → replaced with ASCII
        "”": ['"', "'"],                 # Curly closing quote → replaced with ASCII
        "‘": ["'", "`"],                 # Single opening quote → ASCII alternatives
        "’": ["'", "`"],                 # Single closing quote → ASCII alternatives
        "«": ['"', "'", "“"],            # Guillemet opening → replaced with western or curly
        "»": ['"', "'", "”"]             # Guillemet closing → replaced with western or curly
    },

    # Khmer informal writing tends to include extra spaces more often than deleting necessary ones.
    "SPACE_DELETE_RATE": 0.15,
    "SPACE_INSERT_RATE": 0.25
}
