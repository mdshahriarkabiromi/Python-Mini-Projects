
import random
import logo

pet_names = [
    "Buddy", "Max", "Bella", "Charlie", "Luna", "Rocky", "Lucy", "Cooper", "Daisy", "Milo",
    "Bailey", "Sadie", "Oliver", "Molly", "Tucker", "Sophie", "Bear", "Chloe", "Duke", "Zoey",
    "Jack", "Lily", "Finn", "Roxy", "Zeus", "Ruby", "Apollo", "Penny", "Thor", "Maggie",
    "Gizmo", "Nala", "Simba", "Coco", "Ranger", "Pepper", "Scout", "Willow", "Jasper", "Ginger",
    "Tank", "Hazel", "Ace", "Gracie", "Rex", "Stella", "Diesel","Mia", "Bruno", "Ellie","Simba"
]

ign_list = [
    "ShadowProwler", "EliteBane", "FrostByte", "Ravenous", "PhoenixRise", "IronClad", "MysticWarden", "LoneAssassin", "ViperStrike", "GhostRecon",
    "QuantumLeap", "NightHawk", "EchoVision", "BlazeInferno", "CrimsonFate", "VortexValor", "NeonSlayer", "OmegaReborn", "DarkNebula", "FinalCataclysm",
    "SavageSoul", "TerraNova", "ThunderStrike", "CosmicRanger", "AlphaGenesis", "BladeRunner", "RebelPhoenix", "StormSurge", "ElectroFury", "ChaosBlade",
    "WraithBringer", "DragonFire", "StealthTactic", "PixelPriest", "AquaReaver", "InfernoGaze", "TidalWave", "CelestialKnight", "ShadowMancer", "OblivionHawk",
    "CometStrike", "PhantomFury", "IronVanguard", "NexusBlade", "LightningRod", "DarkSpecter", "StarScream", "DreadKnight", "VoidWalker", "SkyRim"
]

print(logo.name_logo)
print("Welcome to the Name Generator.")
mode_choice = input("Would you like a name suggestion or to generate a name?\n"
                    "-----Press 1 for Name Suggestion\n"
                    "-----Press 2 to Generate a Name\n")
if mode_choice == "1":
    name_choice = input("What type of name suggestion do you need?\n"
                        "-----Enter 1 for Pet Name Suggestions\n"
                        "-----Enter 2 for In-Game Name Suggestions\n")
    if name_choice == "1":
        print(f"Consider naming your pet: {random.choice(pet_names)}")
    elif name_choice == "2":
        print(f"Consider using this IGN: {random.choice(ign_list)}")

elif mode_choice == "2":
    name_choice2 = input("What type of name would you like to generate?\n"
                         "-----Enter 1 to Generate a Music Band Name\n"
                         "-----Enter 2 to Generate a Startup Name\n")
    if name_choice2 == "1":
        genre = input("Enter the genre of your music (e.g., Rock, Pop, Jazz):\n ")
        mood = input("Enter the mood of your music (e.g., Happy, Sad, Energetic): \n")
        unique_feature = input("Enter a unique feature of your music (e.g., Acoustic, Electronic):\n ")
        music_name = genre + mood + unique_feature
        print(f"Your music name could be: {music_name}")
    elif name_choice2 == "2":
        niche = input("Enter the niche of your startup (e.g., Tech, Health, Finance):\n ")
        startup_type = input("Enter the type of your startup (e.g., App, Service, Solution): \n")
        unique_feature = input("Enter a unique feature of your startup (e.g., Smart, Secure): \n")
        startup_name = niche + unique_feature + startup_type
        print(f"Your startup name could be: {startup_name}")

