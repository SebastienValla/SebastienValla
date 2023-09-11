from datetime import date

# Read the existing README
with open("README.md", "r") as f:
    lines = f.readlines()

try:
    # Find the line numbers for the countdown marker
    start_line = (
        next(
            i
            for i, line in enumerate(lines)
            if line.strip() == "<!--COUNTDOWN_START-->"
        )
        + 1
    )
    end_line = next(
        i for i, line in enumerate(lines) if line.strip() == "<!--COUNTDOWN_END-->"
    )

    # Remove old countdown
    del lines[start_line:end_line]
except StopIteration:
    print("Markers not found. Exiting.")
    exit(1)

# Calculate the countdown
today = date.today()

# Add the new countdown
new_countdown = f"This profile has been updated on the: **{today}**\n"
lines.insert(start_line, new_countdown)

# Write the updated README back to file
with open("README.md", "w") as f:
    f.writelines(lines)
