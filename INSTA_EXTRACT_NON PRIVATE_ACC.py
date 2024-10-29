import instaloader

def download_instagram_profile(profile_name):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Download the profile
        print(f"Downloading content from profile: {profile_name}")
        loader.download_profile(profile_name, profile_pic_only=False)
        print(f"Successfully downloaded all content from {profile_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the Instagram profile name from the user
    profile_name = input("Enter the Instagram profile name (without @): ")
    download_instagram_profile(profile_name)
