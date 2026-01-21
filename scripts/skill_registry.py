#skill_registry
SKILL_REGISTRY = {} # Global dictionary to hold registered skills
def register_skill(skill_identity: dict):
    uid = skill_identity["skill_uid"]

    if uid in SKILL_REGISTRY:
        raise ValueError(f"Duplicate skill UID detected: {uid}")
    
    SKILL_REGISTRY[uid] = skill_identity