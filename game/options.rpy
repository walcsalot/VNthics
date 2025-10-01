## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("VNEthics")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "VNEthics"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "VNEthics-1756905156"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Custom Autosave System ####################################################
##
## Disable default autosave and create custom autosave for educational tracking

# Disable default autosave
define config.has_autosave = False

# Custom autosave functions with Supabase integration
init python:
    # Import Supabase modules
    try:
        from supabase_config import init_supabase
        from supabase_auth import supabase_auth
        from supabase_saves import supabase_saves
        from supabase_progress import supabase_progress
        
        # Initialize Supabase connection
        supabase_available = init_supabase()
        if supabase_available:
            print("Supabase integration loaded successfully")
        else:
            print("Supabase integration loaded in offline mode")
    except Exception as e:
        print(f"Supabase integration failed to load: {e}")
        supabase_available = False
    
    def custom_autosave_scenario_start(scenario_id, scenario_name):
        """Autosave when starting a new scenario with Supabase tracking"""
        # Traditional Ren'Py save
        renpy.save("auto-scenario-{}-start".format(scenario_id), "Autosave: Started {}".format(scenario_name))
        print("Autosaved: Started scenario {}".format(scenario_id))
        
        # Supabase progress tracking
        if supabase_available:
            try:
                result = supabase_progress.track_scenario_start(scenario_id, scenario_name)
                if result["success"]:
                    print("Progress tracked: Started scenario {}".format(scenario_id))
            except Exception as e:
                print(f"Progress tracking error: {e}")
    
    def custom_autosave_choice(scenario_id, choice_number, choice_text):
        """Autosave when reaching a choice with Supabase tracking"""
        # Traditional Ren'Py save
        save_name = "auto-scenario-{}-choice-{}".format(scenario_id, choice_number)
        save_description = "Autosave: Choice {} in {}".format(choice_number, scenario_id)
        renpy.save(save_name, save_description)
        print("Autosaved: Choice {} in scenario {}".format(choice_number, scenario_id))
        
        # Supabase progress tracking
        if supabase_available:
            try:
                # Extract moral impact from choice (this would need to be passed as parameter)
                moral_impact = 0  # Default, should be calculated based on choice
                result = supabase_progress.track_choice(scenario_id, choice_number, choice_text, "", moral_impact)
                if result["success"]:
                    print("Progress tracked: Choice {} in scenario {}".format(choice_number, scenario_id))
            except Exception as e:
                print(f"Progress tracking error: {e}")
    
    def custom_autosave_ending(scenario_id, ending_type, moral_score):
        """Autosave when reaching an ending with Supabase tracking"""
        # Traditional Ren'Py save
        save_name = "auto-scenario-{}-ending-{}".format(scenario_id, ending_type)
        save_description = "Autosave: {} ending (Score: {})".format(ending_type.title(), moral_score)
        renpy.save(save_name, save_description)
        print("Autosaved: {} ending in scenario {} with score {}".format(ending_type, scenario_id, moral_score))
        
        # Supabase progress tracking
        if supabase_available:
            try:
                result = supabase_progress.track_scenario_end(scenario_id, ending_type, moral_score)
                if result["success"]:
                    print("Progress tracked: {} ending in scenario {}".format(ending_type, scenario_id))
            except Exception as e:
                print(f"Progress tracking error: {e}")
    
    def authenticate_user():
        """Authenticate user login with Supabase integration"""
        global username, password, is_authenticated, login_attempts, max_login_attempts, registered_users
        
        # Try Supabase authentication first
        if supabase_available:
            try:
                result = supabase_auth.login_user(username, password)
                if result["success"]:
                    is_authenticated = True
                    login_attempts = 0
                    user_data = result.get("user", {})
                    renpy.notify("Login successful! Welcome to VNEthics.")
                    renpy.restart_interaction()
                    return
                else:
                    renpy.notify(result["message"])
                    username = ""
                    password = ""
                    login_attempts += 1
                    if login_attempts >= max_login_attempts:
                        renpy.notify("Too many failed attempts. Please restart the game.")
                        renpy.quit()
                    renpy.restart_interaction()
                    return
            except Exception as e:
                print(f"Supabase login error: {e}")
                # Fall back to local authentication
        
        # Fallback to local authentication
        if username in registered_users and registered_users[username]["password"] == password:
            is_authenticated = True
            login_attempts = 0
            renpy.notify("Login successful! Welcome to VNEthics.")
            renpy.restart_interaction()
        # Fallback to default credentials for backward compatibility
        elif username == default_username and password == default_password:
            is_authenticated = True
            login_attempts = 0
            renpy.notify("Login successful! Welcome to VNEthics.")
            renpy.restart_interaction()
        else:
            login_attempts += 1
            if login_attempts >= max_login_attempts:
                renpy.notify("Too many failed attempts. Please restart the game.")
                renpy.quit()
            else:
                renpy.notify("Invalid credentials. Please try again.")
                username = ""
                password = ""
                renpy.restart_interaction()
    
    def logout_user():
        """Logout user and return to login screen"""
        global is_authenticated, username, password, login_attempts
        
        # Logout from Supabase if available
        if supabase_available:
            try:
                supabase_auth.logout_user()
            except Exception as e:
                print(f"Supabase logout error: {e}")
        
        # Clear local session
        is_authenticated = False
        username = ""
        password = ""
        login_attempts = 0
        renpy.notify("Logged out successfully.")
        renpy.restart_interaction()
    
    def register_user():
        """Register a new user with Supabase integration"""
        global reg_username, reg_password, reg_confirm_password, reg_email, reg_full_name, registered_users
        
        # Validation checks
        if not reg_username or len(reg_username) < 3:
            renpy.notify("Username must be at least 3 characters long.")
            renpy.restart_interaction()
            return
        
        if not reg_password or len(reg_password) < 4:
            renpy.notify("Password must be at least 4 characters long.")
            renpy.restart_interaction()
            return
        
        if reg_password != reg_confirm_password:
            renpy.notify("Passwords do not match. Please try again.")
            renpy.restart_interaction()
            return
        
        if not reg_email or "@" not in reg_email:
            renpy.notify("Please enter a valid email address.")
            renpy.restart_interaction()
            return
        
        if not reg_full_name or len(reg_full_name) < 2:
            renpy.notify("Please enter your full name.")
            renpy.restart_interaction()
            return
        
        # Try Supabase registration first
        if supabase_available:
            try:
                result = supabase_auth.register_user(reg_email, reg_password, reg_full_name, reg_username)
                if result["success"]:
                    # Clear registration form
                    reg_username = ""
                    reg_password = ""
                    reg_confirm_password = ""
                    reg_email = ""
                    reg_full_name = ""
                    
                    renpy.notify(result["message"])
                    renpy.restart_interaction()
                    return
                else:
                    renpy.notify(result["message"])
                    renpy.restart_interaction()
                    return
            except Exception as e:
                print(f"Supabase registration error: {e}")
                # Fall back to local registration
        
        # Fallback to local registration
        if reg_username in registered_users:
            renpy.notify("Username already exists. Please choose a different one.")
            renpy.restart_interaction()
            return
        
        # Create new user locally
        import datetime
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        registered_users[reg_username] = {
            "password": reg_password,
            "email": reg_email,
            "full_name": reg_full_name,
            "created_date": current_date
        }
        
        # Clear registration form
        reg_username = ""
        reg_password = ""
        reg_confirm_password = ""
        reg_email = ""
        reg_full_name = ""
        
        renpy.notify("Registration successful! You can now login with your new account.")
        renpy.restart_interaction()
    
    def show_registration_screen():
        """Show registration screen"""
        global show_registration
        show_registration = True
        renpy.restart_interaction()

    def hide_registration_screen():
        """Hide registration screen and return to login"""
        global show_registration, reg_username, reg_password, reg_confirm_password, reg_email, reg_full_name
        show_registration = False
        # Clear registration form
        reg_username = ""
        reg_password = ""
        reg_confirm_password = ""
        reg_email = ""
        reg_full_name = ""
        renpy.restart_interaction()

    def clear_input_focus():
        """Clear focus from all input fields"""
        renpy.restart_interaction()

    def focus_input(input_id):
        """Focus on a specific input field"""
        renpy.restart_interaction()
    
    # Enhanced save/load functions with Supabase integration
    def cloud_save_game(save_name, description=""):
        """Save game to cloud with current state"""
        if supabase_available:
            try:
                # Get current game state
                current_scenario = getattr(renpy.store, 'current_scenario', 'unknown')
                current_moral_score = getattr(renpy.store, 'moral_score', 0)
                
                # Create save data
                save_data = {
                    "scenario": current_scenario,
                    "moral_score": current_moral_score,
                    "timestamp": datetime.now().isoformat()
                }
                
                result = supabase_saves.save_game(
                    save_name, 
                    save_data, 
                    current_scenario, 
                    current_moral_score, 
                    description
                )
                
                if result["success"]:
                    renpy.notify(f"Game saved to cloud: {result['message']}")
                else:
                    renpy.notify(f"Save failed: {result['message']}")
                    
            except Exception as e:
                print(f"Cloud save error: {e}")
                renpy.notify("Cloud save failed, saved locally instead")
                renpy.save(save_name, description)
        else:
            # Fallback to local save
            renpy.save(save_name, description)
            renpy.notify("Game saved locally")
    
    def cloud_load_game(save_name):
        """Load game from cloud"""
        if supabase_available:
            try:
                result = supabase_saves.load_game(save_name)
                if result["success"]:
                    # Restore game state
                    if "moral_score" in result["save_data"]:
                        renpy.store.moral_score = result["save_data"]["moral_score"]
                    if "scenario" in result["save_data"]:
                        renpy.store.current_scenario = result["save_data"]["scenario"]
                    
                    renpy.notify(f"Game loaded from {result['source']}")
                    return True
                else:
                    renpy.notify(f"Load failed: {result['message']}")
                    return False
                    
            except Exception as e:
                print(f"Cloud load error: {e}")
                renpy.notify("Cloud load failed, trying local save")
        
        # Fallback to local load
        if renpy.can_load(save_name):
            renpy.load(save_name)
            renpy.notify("Game loaded from local storage")
            return True
        else:
            renpy.notify("Save file not found")
            return False
    
    def list_cloud_saves():
        """List all available saves (cloud and local)"""
        if supabase_available:
            try:
                result = supabase_saves.list_saves()
                if result["success"]:
                    return result["saves"]
            except Exception as e:
                print(f"List saves error: {e}")
        
        # Fallback to local saves
        local_saves = []
        for i in range(1, 10):
            if renpy.can_load(str(i)):
                local_saves.append({
                    "name": str(i),
                    "description": f"Local Save {i}",
                    "source": "local"
                })
        return local_saves
    
    def track_moral_choice(scenario_id, choice_number, choice_text, choice_result, moral_impact):
        """Track a moral choice with proper impact"""
        if supabase_available:
            try:
                result = supabase_progress.track_choice(
                    scenario_id, choice_number, choice_text, choice_result, moral_impact
                )
                if result["success"]:
                    print(f"Choice tracked: {choice_text} (impact: {moral_impact})")
            except Exception as e:
                print(f"Choice tracking error: {e}")



## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
