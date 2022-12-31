from data_prep import skills, experience, education
from my_dictionary import data
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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
            <img src="{data['user_id']}.jpg" alt="My photo">
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
            <section id="exp">
            {experience}
                </ol>
            </section>
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

