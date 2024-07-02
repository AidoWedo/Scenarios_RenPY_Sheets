"""
This script is a Ren'Py visual novel project with integrated functionalities for Text-to-Speech (TTS) and image generation.
The script fetches story data, manages dialogues, and dynamically generates voice files and images when necessary.

Key functionalities:
1. Fetching and caching story data from an external source - json source generated from google sheets
2. Generating and playing Text-to-Speech (TTS) audio for dialogues.
3. Generating images based on prompts using an external service.
4. Handling dialogue choices and background images dynamically.
"""

init python:
    import json
    import urllib.request
    import time
    import os
    import ssl
    import sys

    print("Ren'Py version:", renpy.version())
    print("Python version:", sys.version)

    # SSL Workaround
    ssl._create_default_https_context = ssl._create_unverified_context

    # Cache settings
    CACHE_FILE = os.path.join("cache", "story_data.json")
    CACHE_DURATION = 3600  # Cache duration in seconds (1 hour)
    VOICE_DIR = os.path.join("audio", "voice")
    IMAGE_DIR = "images"

    print(f"Current working directory: {os.getcwd()}")
    print(f"Game directory: {config.gamedir}")

    # Set default volumes
    config.default_music_volume = 0.7
    config.default_voice_volume = 1.0

    def clear_cache():
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)
            print("Cache cleared.")
        else:
            print("No cache file found.")

    def fetch_story_data():
        print("Attempting to fetch story data...")
        try:
            url = "YOUR_GOOGLE_APPS_SCRIPT_URL"  # Replace with your actual URL from the google sheets App Script
            print(f"Fetching data from URL: {url}")
            
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
            
            with opener.open(url, timeout=10) as response:
                data = json.loads(response.read())

            print(f"Data fetched successfully. Keys in data: {', '.join(data.keys())}")

            # Save fetched data to cache
            os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
            with open(CACHE_FILE, 'w') as cache_file:
                json.dump(data, cache_file)

            return data

        except urllib.error.URLError as e:
            print(f"Network error: Unable to fetch story data. Error: {str(e)}")
            return fallback_story_data()
        except json.JSONDecodeError as e:
            print(f"Data error: Invalid JSON received. Error: {str(e)}")
            return fallback_story_data()
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return fallback_story_data()

    def fallback_story_data():
        # Use the provided raw data as fallback
        return {"scenes":[{"SceneID":"intro","Description":"Office","Background":"office","Characters":"consultant, client"},{"SceneID":"zcc_explanation","Description":"Zscaler Client Connector Demo","Background":"zcc_interface","Characters":"consultant, client"}],"dialogue":[{"SceneID":"intro","Character":"consultant","Text":"Welcome to our Zscaler Client Connector deployment call","VoiceFile":"consultant-intro.mp3"},{"SceneID":"intro","Character":"client","Text":"Thanks for the time. We're excited to get started","VoiceFile":"client-intro.mp3"}],"choices":[{"SceneID":"intro","ChoiceText":"Ask about ZCC","NextSceneID":"zcc_explanation"},{"SceneID":"intro","ChoiceText":"End call","NextSceneID":"end"}],"characters":[{"CharacterID":"consultant","Name":"Barbara"},{"CharacterID":"client","Name":"Barbara"}]}

    def get_scene(scene_id):
        try:
            return next(scene for scene in story_data['scenes'] if scene['SceneID'] == scene_id)
        except StopIteration:
            print(f"Error: Scene '{scene_id}' not found. Using default scene.")
            return {"SceneID": scene_id, "Description": "Default", "Background": "default", "Characters": ""}

    def get_dialogue(scene_id):
        return [d for d in story_data.get('dialogue', []) if d['SceneID'] == scene_id]

    def get_choices(scene_id):
        choices = [c for c in story_data.get('choices', []) if c['SceneID'] == scene_id]
        if not choices:
            print(f"Warning: No choices found for scene '{scene_id}'. Adding default choice.")
            return [{"ChoiceText": "Continue", "NextSceneID": "end"}]
        return choices

    def get_characters():
        return {c['CharacterID']: c for c in story_data.get('characters', [])}

    def get_background(scene):
        bg = scene.get('Background', 'default_background')
        for ext in ['.png', '.jpg', '.jpeg']:
            full_path = os.path.join(config.gamedir, IMAGE_DIR, bg + ext)
            print(f"Checking for background image: {full_path}")
            if os.path.exists(full_path):
                print(f"Background image found: {full_path}")
                return bg
        print(f"Warning: No background image found for {bg}")
        return 'black'  # Fallback to a black background

    def play_voice(voice_file):
        # Play the voice file using the music channel
        print(f"Attempting to play voice file: {voice_file}")
        renpy.music.play(voice_file)
        print("Playback command issued successfully.")
        return True

    def file_exists(filepath):
        return os.path.isfile(filepath)

# TODO: Implement TTS generation using the chosen service/library
# def generate_tts(text, filename):
    # This function should generate TTS audio for the given text and save it as the specified filename
#    pass

# TODO: Check if the voice file already exists and generate TTS if it does not
# def play_voice_or_generate(text, voice_file):
    # This function should check for the existence of the voice file and generate it using TTS if necessary, then play the voice file
#    pass

# Main game label
label start:
    $ clear_cache()
    $ story_data = fetch_story_data()
    $ print("Loaded story data:", json.dumps(story_data, indent=2))
    $ characters = get_characters()
    $ define_characters = {char_id: Character(char['Name']) for char_id, char in characters.items()}
    
    # Debug information
    $ print(f"Current working directory: {os.getcwd()}")
    $ print(f"Game directory: {config.gamedir}")
    $ print(f"Base directory: {config.basedir}")
    $ print(f"Audio directory: {VOICE_DIR}")
    $ print(f"illurock.opus exists: {file_exists(os.path.join(config.gamedir, VOICE_DIR, 'illurock.opus'))}")
    
    # Test voice playback
    # Comment this out after you complete (testing only)
    $ print("Testing voice playback...") # Comment this out after you complete (testing only)
    $ success = play_voice("illurock.opus") # Comment this out after you complete (testing only)
    if success: # Comment this out after you complete (testing only)
        "This is a test of voice playback. You should hear a voice now." # Comment this out after you complete (testing only)
    else: # Comment this out after you complete (testing only)
        "Voice playback failed. Check the console for more information." # Comment this out after you complete (testing only)
    $ renpy.pause(5) # Comment this out after you complete (testing only)
    stop music # Comment this out after you complete (testing only)
    "Sound playback stopped." # Comment this out after you complete (testing only)

    # Set volumes at the start of the game
    $ renpy.music.set_volume(0.7, channel="music")
    $ renpy.music.set_volume(1.0, channel="voice")

    $ current_scene = "intro"
    
    while True:
        $ print("\n--- New Scene ---")
        $ print(f"Current scene: {current_scene}")
        
        $ scene = get_scene(current_scene)
        $ dialogue = get_dialogue(current_scene)
        $ choices = get_choices(current_scene)

        $ print(f"Scene data: {scene}")
        $ print(f"Dialogue: {dialogue}")
        $ print(f"Choices: {choices}")

        $ background = get_background(scene)
        $ print(f"Using background: {background}")
        scene expression background

        python:
            for d in dialogue:
                character = define_characters.get(d['Character'].lower(), narrator)
                voice_file = d.get('VoiceFile')
                
                print(f"Character: {d['Character']}, Text: {d['Text']}, Voice File: {voice_file}")
                
                if voice_file:
                    play_voice(voice_file)
                    
                renpy.say(character, d['Text'])
                renpy.sound.stop(channel="voice")

        $ choice_list = [(c['ChoiceText'], c['NextSceneID']) for c in choices]

        python:
            print("Choices:")
            for choice, next_scene in choice_list:
                print(f"  - {choice} -> {next_scene}")

        $ current_scene = renpy.display_menu(choice_list)

        if current_scene == "end":
            return