def validate_input(request: dict) -> bool:
    if "id" and "is_main" and "text" and "title" and "version" in request.keys():
        return True
