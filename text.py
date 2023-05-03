from typing import List, io


def format_(phrases: List[str]):
    structured_phrases = [f"    - {command}\n" for command in phrases]
    return structured_phrases


def write_content(path: str, phrases: List[str], phrases_name: str) -> io:
    formatted_commands = ''.join(format_(phrases))

    print(formatted_commands)
    text = (f"""
                    
        
- command:
    action: ahk
    exe_path: ah/{phrases_name}.bat
    exe_args:
  voice:
    sounds:
    - ok1
    - ok2
    - ok3
  phrases:
{formatted_commands}

    """)
    with open(path, "a+", encoding='utf-8') as file:
        file.write(text)
