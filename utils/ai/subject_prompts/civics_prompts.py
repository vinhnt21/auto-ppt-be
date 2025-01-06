# utils/ai/subject_prompts/civics_prompts.py

CIVICS_PROMPTS = {
    'outline': """Create an educational outline for the following civics content:
{content}""",

    'content': """Generate detailed slide content based on this civics outline:
{outline}""",

    'illustration': """Suggest appropriate illustrations for this civics slide content:
Slide Content: {slide_content}
Original Content: {content}"""
}