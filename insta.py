import json
import sys
import os
from datetime import date

FOLLOWERS_FILE = 'insta\\connections\\followers_and_following\\followers_1.json'
FOLLOWING_FILE = 'insta\\connections\\followers_and_following\\following.json'
OUTPUT_DIR = 'analysis_data'

def load_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    except json.JSONDecodeError:
        print(f"Error: Could not decode the JSON from '{filename}'.")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None

def extract_usernames(data, data_type):
    usernames = []
    data_list = [] # Initialize empty list

    if data_type == 'following':
        if 'relationships_following' in data:
            data_list = data['relationships_following'] 
        else:
            print("Error: Could not find 'relationships_following' key in following.json")
            return []
        

    elif data_type == 'followers':
        if isinstance(data, list):
            data_list = data 
        else:
            print("Error: Could not find list or 'relationships_followers' key in followers_1.json")
            return []

    for item in data_list:
        try:            
            if data_type == 'following':
                username = item['title']
            
            elif data_type == 'followers':
                username = item['string_list_data'][0]['value']
            
            if not username:
                raise ValueError("Extracted username is empty")
                
            usernames.append(username)

        except (KeyError, IndexError, TypeError, AttributeError, ValueError):
            print(f"Warning: Skipping an item with unexpected format in {data_type} data.")
            
    return usernames

def main():

    followers_data = load_json_file(FOLLOWERS_FILE)
    following_data = load_json_file(FOLLOWING_FILE)

    if followers_data is None or following_data is None:
        sys.exit(1)

    follower_usernames = extract_usernames(followers_data, 'followers')
    following_usernames = extract_usernames(following_data, 'following')

    if not follower_usernames or not following_usernames:
        print("Could not extract usernames. Exiting.")
        sys.exit(1)

    print(f"\nYou have {len(follower_usernames)} followers.")
    print(f"You are following {len(following_usernames)} accounts.\n")

    followers_set = set(follower_usernames)
    following_set = set(following_usernames)

    not_following_back = following_set - followers_set

    # you_dont_follow_back = followers_set - following_set

    if not_following_back:
        print(f"Accounts that do not follow you back ({len(not_following_back)}):")
        for username in sorted(list(not_following_back)):
            print(username)
    else:
        print("\nYou follow back everyone who follows you!")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    today_str = date.today().strftime('%Y-%m-%d')
    output_filename = os.path.join(OUTPUT_DIR, f'not_following_back_{today_str}.txt')
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            if not_following_back:
                f.write(f"Accounts that do not follow you back ({len(not_following_back)}):\n")
                f.write("--------------------------------------------------\n")
                for username in sorted(list(not_following_back)):
                    f.write(f"{username}\n")
            else:
                f.write("All accounts you follow also follow you back.")
    except Exception as e:
        print(f"\nError: Could not write results to file. {e}")

if __name__ == "__main__":
    main()

