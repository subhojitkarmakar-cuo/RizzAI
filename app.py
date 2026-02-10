def get_rizz_response(api_key, text_input, image_input=None):
    genai.configure(api_key=api_key)
    
    # এরর এড়াতে মডেলের নাম সংশোধন
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    system_role = (
        "You are the world's best relationship coach and Rizz expert. Your task is to analyze "
        "chat screenshots or text messages provided by the user. Understand the emotional context, "
        "tone, and subtext. Detect the language of the input (Bengali, Hindi, English, etc.) "
        "and generate the replies in that SAME language and script automatically."
    )

    content = [system_role]
    if text_input:
        content.append(f"User Message: {text_input}")
    if image_input:
        img = Image.open(image_input)
        content.append(img)

    response = model.generate_content(content)
    return response.text
