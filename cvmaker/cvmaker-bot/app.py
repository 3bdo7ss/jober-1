from html2image import Html2Image
import img2pdf
from data_prep import prep
import os


# bot_funcs\cv_builder
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# * NOTE: Before running the code below
# There MUST be a folder created and has the user_id as a name
# + it MUST contain a profile picture name f"{user_id}.png"
def cv_maker(data):
    skills, experience, education = prep(data)
    my_html1 = rf"""
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style1.css">
        <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
        <script src="script.js" defer></script>
        <title>Creat your resume</title>
    </head>
    <body>
        <div class="resume">
            <div class="topdiv"> </div>
            <div class="heading">
                <img src="{ROOT_DIR}\users_data\{data['user_id']}\{data['user_id']}.jpg" alt="My photo">
                <div class="aps-head"  dir='rtl'>
                    <h1 class="name">{data['name']}</h1>
                    <p class="role">{data['role']}</p>
                    <p class="age">{data['age']} سنة</p>
                </div>
            </div>
            <div class="grid" dir='rtl'>
                <section>
                    <h2 class="topic">نبذة عني</h2>
                    <p id="about">{data['about']}</p>
                </section>
                <section>
                    <h2 class="topic">المهارات</h2>
                    <ul id="skillList">
                        {skills}
                    </ul>
                </section>
                <section>
                    <h2 class="topic">التعليم</h2>
                    <ol id="edu">
                        {education}
                    </ol>
                </section>
                {experience}            
                <section>
                    <h2 class="topic">معلومات الاتصال</h2>
                    <p id="contact">{data['email']} <br> {data['phone_number']}</p>
                </section>
            </div>
            <footer></footer>
        </div>
    </body>
    </html>
    """

    # Just for simplicity
    user_id = f"{data['user_id']}"  # id = 12345, (remove this comment after you modify the dictionary)

    # convert html_str to HTML file, use (wb) because we use arabic language
    with open(f"users_data/{user_id}/{user_id}.html", "wb") as f:
        # since we used (wb) above, we should use .encode()
        f.write(my_html1.encode())

    # convert HTML to PNG
    hti = Html2Image(output_path=f"users_data/{user_id}/")
    hti.screenshot(
        html_file=f"users_data/{user_id}/{user_id}.html",
        css_file=f'style1.css',
        size=(595, 842),       # these 2 nums are the dimensions of html file, should be updated after fixing html to A4
        save_as=f'{user_id}.png'
    )

    # convert PNG to PDF
    with open(f"users_data/{user_id}/{user_id}.pdf", "wb") as f:
        f.write(img2pdf.convert(f'users_data/{user_id}/{user_id}.png'))


# just call it

