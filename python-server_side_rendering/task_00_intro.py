import os
""" fdasdafsdf  fsad """


def generate_invitations(template, attendees):
    """
    sfdadfsafdfsd
    sdfsadfsd
    """

    # ---------------------------
    # 1. Validate input types
    # ---------------------------
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # ---------------------------
    # 2. Handle empty inputs
    # ---------------------------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---------------------------
    # 3. Process each attendee
    # ---------------------------
    for index, attendee in enumerate(attendees, start=1):

        # Get values or replace missing ones with "N/A"
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Fill template
        processed_template = template.replace("{name}", name)
        processed_template = processed_template.replace("{event_title}", event_title)
        processed_template = processed_template.replace("{event_date}", event_date)
        processed_template = processed_template.replace("{event_location}", event_location)

        # Output file name
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as outfile:
                outfile.write(processed_template)

        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue
