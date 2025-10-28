import random

EXCUSES = {
    "deadline": [
        "My code was compiling for three days.",
        "The API rate-limited my motivation.",
        "I accidentally scheduled my task for next week."
    ],
    "meeting": [
        "Zoom refused to unmute me.",
        "I got stuck in another meeting that could have been an email.",
        "My calendar app gaslit me about the time."
    ],
    "class": [
        "My virtual environment ate my homework.",
        "AI took credit for my assignment.",
        "My professor's email went straight to /dev/null."
    ],
    "techfail": [
        "Git refused to merge my brain branch.",
        "My laptop ran out of coffee.",
        "SyntaxError: life not defined."
    ],
    "general": [
        "The cloud was down.",
        "My Python became self-aware.",
        "A merge conflict broke my willpower."
    ]
}

import random

EXCUSES = {
    "deadline": [
        "My code was compiling for three days.",
        "The API rate-limited my motivation.",
        "I accidentally scheduled my task for next week."
    ],
    "meeting": [
        "Zoom refused to unmute me.",
        "I got stuck in another meeting that could have been an email.",
        "My calendar app lied about the time."
    ],
    "class": [
        "My virtual environment ate my homework.",
        "AI took credit for my assignment.",
        "My professor’s email went to spam."
    ],
    "general": [
        "The cloud was down.",
        "My laptop ran out of coffee.",
        "SyntaxError: life not defined."
    ]
}


def generate(category="general"):
    """
    Return randomly chosen excuse from the selected category.

    Args: category (str): type of excuse to return (deadline, meeting, class, or general)

    Raises ValueError if the category doesn't exist
    """
    category = category.lower()
    
    if category not in EXCUSES:
        raise ValueError("Invalid category. Try 'deadline', 'meeting', 'class', or 'general'.")
    
    return random.choice(EXCUSES[category])
