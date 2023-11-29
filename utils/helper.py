def parseBool(input: any) -> bool:
    input = str(input).lower().strip()
    if input not in ["false", "0", "none", "null", ""]:
        return True
    return False
