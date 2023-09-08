from datetime import datetime, date

# Read the existing README
with open("README.md", "r") as f:
    lines = f.readlines()

# Find the line numbers for the countdown marker
start_line = lines.index("<!--COUNTDOWN_START-->\n") + 1
end_line = lines.index("<!--COUNTDOWN_END-->\n")

# Remove old countdown
del lines[start_line:end_line]

# Calculate the countdown

today = date.today()


# Add the new countdown
new_countdown = f"This profile has been updated on the: **{today}**\n"
lines.insert(start_line, new_countdown)

# Write the updated README back to file
with open("README.md", "w") as f:
    f.writelines(lines)
