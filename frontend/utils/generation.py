_generated_text_id = None


def save_generated_text_id(text_id: int):
    global _generated_text_id
    _generated_text_id = text_id


def get_generated_text_id():
    return _generated_text_id