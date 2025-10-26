import os


DIR_NAME = 'backup'

print(f"Ensuring directory '{DIR_NAME}' exists...")  # Announce the action

try:
    os.makedirs(DIR_NAME, exist_ok=True)

    if os.path.isdir(DIR_NAME):
        print(f"✅ Directory '{DIR_NAME}' successfully ensured.")

    else:
        print(f"❌ Error: Failed to create directory '{DIR_NAME}'.")

except PermissionError as e:
    print(
        f"❌ Permission Error: Cannot create directory '{DIR_NAME}'. Details: {e}")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
