from backend.repositories.profile_repositories import ProfileRepository
from backend.services.example_extractor import extract_examples


def load_profile(
    db,
    user_id: int
):
    """
    Load the user's writing profile and extract representative
    writing examples from the latest uploaded document.
    """

    # Load writing profile
    profile = ProfileRepository.get_style_profile(
        db=db,
        user_id=user_id
    )

    # Load latest uploaded document
    reference = ProfileRepository.get_reference_text(
        db=db,
        user_id=user_id
    )

    # Extract representative examples
    examples = extract_examples(reference)

    return profile, examples