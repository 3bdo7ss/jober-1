from my_dictionary import data


def prep(data):
    # SKILLS #
    skills = ""
    for skill in data['skills']:
        skills += f"<li>{skill}</li>"

    # EDUCATION #
    education = ""
    for edu in data['education']:
        if edu['end'] == '':
            education += f"""
    <li><strong>{edu['start']} - الحاضر  </strong><br>
    <strong>{edu['university']}</strong><br>{edu['degree']}</li>\n
            """
        else:
            education += f"""
    <li><strong>{edu['start']} - {edu['end']}</strong><br>
    <strong>{edu['university']}</strong><br>{edu['degree']}</li>\n
            """

    # EXPERIENCE #
    experience = ""
    if data['experience'] != "":

        # EXPERIENCE LIST aka <li> #
        experience_block = """

        """
        for job in data['experience']:
            if job['end'] == '':
                experience_block += f"""
    <li><strong>{job['start']} - الحاضر  </strong><br>
    <strong>{job['company']}</strong><br>{job['role']}</li>\n
            """
            else:
                experience_block += f"""
    <li><strong>{job['start']} - {job['end']}</strong><br>
    <strong>{job['company']}</strong><br>{job['role']}</li>\n
            """

        # EXPERIENCE CONTAINER #
        experience = f"""
    <section id="exp">
    <h2 class="topic" id="expHeader">الخبرات</h2>
    <ol id="expSection">
    {experience_block}
    </ol>
    </section>
        """
    return skills, experience, education


skills, experience, education = prep(data)
