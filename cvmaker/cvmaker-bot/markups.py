from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from markups_lists import *

def add_skip():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("اضافة", callback_data="cb_add"), 
    InlineKeyboardButton("تخطي", callback_data="cb_skip"))
    return markup    

def jober_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("نشر اعلان وظيفة", callback_data="cb_post"), 
    InlineKeyboardButton("حالة الحساب", callback_data="cb_status"))
    return markup    

def old_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("تعديل المعلومات", callback_data="cb_edit"), 
    InlineKeyboardButton("ارسال السيرة الذاتية", callback_data="cb_oldcv"))
    return markup

def edit_markup(id):
    info = id2dict(id)
    edu = info["education"]
    x = ""
    for i in edu:
        y = f"""1.\n *الجامعة/المدرسة : {i['university']} \n *تاريخ المباشرة و الانتهاء : ({i['end']} - {i['start']})\n *الدراسة : {i['degree']}"""
        x = (x,'\n\n', y)

    exp = info["experience"]
    a = ""
    for h in exp:
        b = f"""1.\n *الشركة : {h['company']} \n *تاريخ المباشرة و الانتهاء : ({h['end']} - {h['start']})\n *الدور : {h['role']}"""
        a = (a,'\n\n', b)
    skills = ""
    for skill in info["skills"]:
        skills = (skills, "\n", skill)
    edit_dict = {
    "cb_name":[f"ارسل الينا الاسم الجديد، اسمك كان \n({info['name']})","الاسم", 17],
    "cb_age":[f"ارسل الينا العمر الجديد، عمرك كان \n({info['age']})", "العمر",0],
    "cb_phone":[f"ارسل الينا رقم الهاتف الجديد، رقم هاتفك كان \n({info['phone_number']})", "رقم الهاتف",1],
    "cb_email":[f"ارسل الينا البريد الاكتروني الجديد، بريدك الالكتروني كان \n({info['email']})", "البريد الالكتروني",2],
    "cb_about":[f"ارسل الينا نبذتك الشخصية الجديدة، نبذتك الشخصية كانت \n({info['about']})", "نبذة عني",3],
    "cb_spec":[f"ارسل تخصصك الجديدة، تخصصك كان \n({info['role']})", "الاختصاص",15],
    "cb_sector":[f"ارسل قطاعك الجديدة، قطاعك كان \n({info['sector']})", "القطاع",14],
    "cb_edu":["ميزة تعديل الدراسة تحت التطوير، هذا ما ادخلته عن دراستك \n{x}", "الدراسة"],
    "cb_exp":["ميزة تعديل الخبرات تحت التطوير، هذا ما ادخلته عن خبراتك \n{a}", "الخبرة"],
    "cb_skills":[f"ارسل مهاراتك الجديدة، مهاراتك كانت \n{skills}", "المهارات",12],
    "cb_back":["","رجوع"]
    }
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for i in list(edit_dict.keys()):
        markup.add(InlineKeyboardButton(edit_dict[i][1], callback_data=i))
    return markup

def sector_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    for i, h in zip(sec_list, sec_cb):
        markup.add(InlineKeyboardButton(i, callback_data=h))
    return markup

def speciality_markup(i):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    spec_list = all_list[i]
    sec_list
    for h in range(len(spec_list)):
        markup.add(InlineKeyboardButton(spec_list[h], callback_data=f"{sec_cb[i]}{h}"))
    return markup

def example_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("مثال", callback_data="cb_example"))
    return markup 

def old_new():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("مستخدم قديم", callback_data="cb_ouser"), 
    InlineKeyboardButton("مستخدم جديد", callback_data="cb_nuser"))
    return markup

def recive_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("استلام جميع انواع الوظائف الممكنة", callback_data="cb_a"), 
    InlineKeyboardButton("استلام الوظائف من نفس القطاع فقط", callback_data="cb_b"),
    InlineKeyboardButton("استلام الوظائف من نفس العنوان الوظيفي فقط", callback_data="cb_c"),
    InlineKeyboardButton("عدم استلام اي وظائف", callback_data="cb_d"))
    return markup

def yes_no():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("نشر وظيفة", callback_data="cb_jober"), 
    InlineKeyboardButton("انشاء سيرة ذاتية", callback_data="cb_user"),
    InlineKeyboardButton("البحث عن عمل حر (بدون شهادة)", callback_data="cb_search"),
    InlineKeyboardButton("رفع سيرة ذاتية", callback_data="cb_upload"))
    return markup

def criteria_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("نعم لدي معايير", callback_data="cb_yc"), 
    InlineKeyboardButton("لا ليس لدي اي معايير", callback_data="cb_nc"))
    return markup

def email_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("نعم", callback_data="cb_yemail"),
    InlineKeyboardButton("كلا", callback_data="cb_nemail"))
    return markup

def gender_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("ذكر", callback_data="cb_male"),
    InlineKeyboardButton("انثى", callback_data="cb_female"))
    return markup

def work_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("نعم", callback_data="cb_ywork"),
    InlineKeyboardButton("كلا", callback_data="cb_nwork"))
    return markup