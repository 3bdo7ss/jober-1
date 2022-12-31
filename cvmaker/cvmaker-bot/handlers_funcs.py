from db_manager import *
from markups import *
from initialize import bot
from app import *
import os

###################----------VARIABLES-----------###################
last = insert_lastmsg
welcome_new = '''مرحبا بك عزيزي المستخدم 
                انا جوبر صانع CV يعتمد على الذكاء الاصطناعي
                '''
###################----------VARIABLES-----------###################


###################----------WELCOME MESSAGE-----------###################
def welcome_message(msg):
    id = int(msg.from_user.id)
    bot.reply_to(msg, last(id,welcome_new), reply_markup = yes_no())
###################----------WELCOME MESSAGE-----------###################


##################----------JOB SENDER-----------###################
def job_sender(msg):
    user_id = int(msg.from_user.id)
    exsisting = does_exist(user_id, False)
    if exsisting :
        bot.send_message(msg.chat.id, last(user_id,"مرحبا بك في واجهة التوظيف"), reply_markup = jober_markup())
    else:
        bot.reply_to(msg, last(user_id,'انت لا تمتلك الصلاحية لهذا الامر \n تواصل مع \n @abdo_hss'))    
##################----------JOB SENDER-----------###################


###################----------EXAMPLE MESSAGE-----------###################
def example_messages(call):
    user_id = int(call.from_user.id)
    bot.edit_message_text(call.message.text, call.from_user.id, call.message.id)

    if call.message.text == 'ما هو اسمك ؟':
        bot.send_message(call.from_user.id, "محمد مهدي")
    
    elif call.message.text == 'الان كم عمرك ؟':
        bot.send_message(call.from_user.id, "30")
    
    elif call.message.text == 'ما هو رقم هاتفك':
        bot.send_message(call.from_user.id,  "+964770123456789 \n او \n 0770123456789")
    
    elif call.message.text == 'ماهو بريدك الالكتروني؟':
        bot.send_message(call.from_user.id, "name@example.com")
    
    elif call.message.text == 'اخبرنا عن نفسك قليلا':
        bot.send_message(call.from_user.id, "")
    
    elif call.message.text == "اين عملت ؟":
        bot.send_message(call.from_user.id, 
        """
        شركة التمثال للمثال
        """)
    
    elif call.message.text == "ماكان دورك في العمل ؟":
        bot.send_message(call.from_user.id,
        """
        مطور برامجيات
        """)
    
    elif call.message.text == "متى باشرت بالعمل ؟":
        bot.send_message(call.from_user.id,
        """
        2017
        """)
    
    elif call.message.text == "متى انتهيت من العمل هناك ؟":              
        bot.send_message(call.from_user.id,
        """
        2020
        """)
    
    elif call.message.text == 'ما اسم المؤسسة التي درست بها ؟':
        bot.send_message(call.from_user.id,
        """
        جامعة التمثال للمثال
        """)
    
    elif call.message.text == 'متى باشرت بالدراسة؟':
        bot.send_message(call.from_user.id,
        """
        2017
        """)
    
    elif call.message.text == "متى انهيت/ستنهي دراستك؟":
        bot.send_message(call.from_user.id,
        """
        2021
        """)
    
    elif call.message.text == 'ما الذي درسته/تدرسه؟':              
        bot.send_message(call.from_user.id,
        """
        بكلوريوس هندسة برامجيات
        """)
    
    elif call.message.text == 'ماهي مهاراتك ؟ اكتبها جميعا':
        bot.send_message(call.from_user.id,
        """
        البرمجة
        التصميم
        التصوير
        """)
###################----------EXAMPLE MESSAGE-----------###################


###################----------CHOICES-----------###################
def user_chocies(call):
    
    user_id = int(call.from_user.id)
#        bot.send_message(message.chat.id, last(user_id,f"مبروك ! لقد انتهينا من جمع معلوماتك \n انتظرنا قليلاً ريثما نكمل انشاءها \n سيتأخر الامر بضع ثواني"))
    if call.data in ["cb_search", "cb_upload"]:
        bot.answer_callback_query(call.id, "هذه الميزة غير متوفرة حالياً ):")

    elif call.data in ["cb_a", "cb_b", "cb_c", 'cb_d']:
        update(user_id, 16, call.data[-1])
        bot.edit_message_text(last(user_id,"ارسل الينا افضل صورة رسمية لديك"),
        call.from_user.id, call.message.id)

    elif call.data == 'cb_nuser':
        bot.answer_callback_query(call.id, "لنصنع الـCV")
        bot.edit_message_text('القسم الاول المعلومات الشخصية \n (معلومات الاتصال):', call.from_user.id, call.message.id)
        insert_user(user_id)
        bot.send_message(call.from_user.id, last(user_id,'ما هو اسمك ؟')  , reply_markup=example_markup())

    elif call.data == 'cb_oldcv':
        user_id = int(call.from_user.id)
        bot.edit_message_text(f"سأرسل لك سيرتك الذاتية في الحال، ولكن لدي طلب واحد", user_id, call.message.id)
        bot.answer_callback_query(call.id, "تم تأكيد المستخدم")
        bot.send_message(user_id, """
        ارسل افضل صورة لديك.. نحن نطلبها اكثر من مرة لأننا لا نحتفظ بصور مستخدمينا
        """)
        last(user_id, call.data)
    elif call.data == 'cb_edit':
        bot.answer_callback_query(call.id, "هذه الميزة غير متوفرة حالياً")
            #bot.edit_message_text(f"اخبرني مالذي اخطأت به اذا", user_id, call.message.id, reply_markup=edit_markup(user_id))
        
    elif call.data == 'cb_ouser':
        if does_exist(user_id, False):
            bot.edit_message_text(f"ها انت ذا مجددا تسعدني رؤيتك، كيف تود ان اساعدك ؟", user_id, call.message.id, reply_markup= old_markup())
        else:
            bot.answer_callback_query(call.id, "انت لست بمستخدم قديم")
    elif call.data in sec_cb :
        sec_index = sec_cb.index(str(call.data))
        update(user_id, 14, sec_list[sec_index])
        bot.edit_message_text("الان اختر عنوانك الوظيفي", call.from_user.id, call.message.id, reply_markup=speciality_markup(sec_index))

    elif (call.data[:-2] in sec_cb and len(call.data) == 8) or (call.data[:-1] in sec_cb and len(call.data) == 7):
        if len(call.data) == 8:
            i = int(call.data[-2:])
            cb = call.data[:-2]
        else:
            i = int(call.data[-1:])
            cb = call.data[:-1]
        sec_index = sec_cb.index(str(cb))
        if (len(all_list[sec_index]) - 1) != i:
            update(user_id, 15, all_list[sec_index][i])
            bot.edit_message_text(last(user_id, "هل عملت من قبل ؟"),call.from_user.id, call.message.id, reply_markup = work_markup())
            
        else:
            bot.edit_message_text(last(user_id, "اكتب عنوانك الوظيفي"),call.from_user.id, call.message.id)

        
    elif call.data == 'cb_ywork':
        bot.delete_message(call.from_user.id, call.message.id)
        bot.send_message(call.from_user.id, "القسم الثاني الخبرات العملية : ")
        bot.send_message(call.from_user.id, "اجب عن المعلومات التالية بمعلومات اول الخبرات التي تود اضافتها في الـCV")
        bot.send_message(call.from_user.id, last(user_id,"اين عملت ؟"), reply_markup = example_markup())

    elif call.data == 'cb_nwork':
        bot.delete_message(call.from_user.id,  
                    call.message.id)
        bot.send_message(call.from_user.id, "القسم الثالث الدراسة : ")
        bot.send_message(call.from_user.id, "اجب عن المعلومات التالية بمعلومات اول شهادة تود اضافتها في الـCV")
        bot.send_message(call.from_user.id, last(user_id,"ما اسم المؤسسة التي درست بها ؟"), reply_markup = example_markup())

    elif call.data == 'cb_male':
        user_id = int(call.from_user.id)
        sex = "Male"
        
        update(user_id, 13, sex)

        bot.delete_message(user_id, call.message.id)
        bot.send_message(user_id, last(user_id,"الان كم عمرك ؟"), reply_markup=example_markup())
        bot.send_message(user_id, "رجاء اكتب العمر كرقم فقط بدون كتابة اي شيء معه")

    elif call.data == 'cb_female':
        user_id = int(call.from_user.id)
        sex = "Female"
        update(user_id, 13, sex)
        bot.delete_message(user_id, call.message.id)        
        bot.send_message(user_id, last(user_id,"الان كم عمرك ؟"), reply_markup=example_markup())
        bot.send_message(user_id, "رجاء اكتب العمر كرقم فقط بدون كتابة اي شيء معه")

    elif call.data == 'cb_yemail':
        bot.delete_message(call.from_user.id,  
                    call.message.id)
        bot.send_message(call.from_user.id, last(user_id,"ماهو بريدك الالكتروني؟"), reply_markup = example_markup())

    elif call.data == 'cb_nemail':
        bot.delete_message(call.from_user.id,  
                    call.message.id)
        bot.send_message(call.from_user.id, last(user_id,"اخبرنا عن نفسك قليلا"), reply_markup=example_markup())
                    
    elif call.data == 'cb_jober':
        bot.answer_callback_query(call.id, "هذه الميزة غير متوفرة حالياً")
        # user_id = int(call.from_user.id)
        # exsisting = None
        # #  user_id)
        # if exsisting:
        #     name = None
        #     name = name[0]
        #     bot.edit_message_text(f"اهلا بك مجددا يا {name}", user_id, call.message.id)
        #     bot.answer_callback_query(call.id, "تم تأكيد المستخدم")
        #     bot.send_message(user_id, last(user_id,"""تذكر ان لديك الاوامر التالية :
        #     /send_job ---> اعلان وظيفة
        #                                     """))
        # else:
        #     bot.answer_callback_query(call.id, "انت لم تسجل بحساب توظيف")
    
    elif call.data == 'cb_yc':
        bot.send_message(call.from_user.id, last(user_id ,"ماهو اكبر عمر مسموح ؟"), reply_markup = example_markup())
    
    elif call.data == 'cb_nc':
        user_id = int(call.from_user.id)
        users = None
        for user in users:
            bot.copy_message()
    
    elif call.data == "cb_add":
        if call.message.text == "هل تود اضافة شهادة اخرى ؟":
            bot.edit_message_text(last(user_id, "ما اسم المؤسسة التي درست بها ؟"), call.from_user.id, call.message.id,reply_markup=example_markup())
        else:
            bot.send_message(call.from_user.id, last(user_id,"اين عملت ؟"), reply_markup = example_markup())
    elif call.data == "cb_skip":
        if call.message.text == "هل تود اضافة شهادة اخرى ؟":
            bot.delete_message(call.from_user.id,  
                        call.message.id)
            bot.send_message(call.from_user.id, "القسم الرابع المهارات و المواهب : ")                
            bot.send_message(call.from_user.id, last(user_id,"ماهي مهاراتك ؟ اكتبها جميعا \n احرص على ان تكون كل مهارة بسطر"), reply_markup=example_markup())
        else:
            bot.send_message(call.from_user.id, "القسم الثالث الدراسة : ")
            bot.send_message(call.from_user.id, "اجب عن المعلومات التالية بمعلومات اول شهادة تود اضافتها في الـCV")
            bot.send_message(call.from_user.id, last(user_id,"ما اسم المؤسسة التي درست بها ؟"), reply_markup=example_markup())

    elif call.data == 'cb_user':
        bot.edit_message_text(last(user_id,'هل انت مستخدم قديم ام جديد'), call.from_user.id, call.message.id, reply_markup = old_new())
###################----------CHOICES-----------###################


###################----------GET INFO-----------###################
def get_info(message):
    user_id = int(message.from_user.id)
    last_message = lastmsg(user_id)
    #  JOBER
    if last_message == "ارسل رسالة بالمنشور الذي تود ارساله للمستخدمين":
        pass

    elif last_message ==  "ماهو اكبر عمر مسموح ؟":
        pass

    elif last_message ==  "ماهو اصغر عمر مسموح ؟":
        pass
    # USER
    if last_message == 'ما هو اسمك ؟':
        fullname = message.text
        update(user_id, 17, fullname)
        bot.send_message(message.chat.id, last(user_id,"هل انت ذكر ام انثى ؟"), reply_markup=gender_markup())

    elif last_message == 'الان كم عمرك ؟':
        age = int(message.text)
        update(user_id, 0, age)
        bot.send_message(message.chat.id, last(user_id,"ما هو رقم هاتفك"), reply_markup=example_markup())

    elif last_message == 'ما هو رقم هاتفك':
        context = message.text
        update(user_id, 1, context)
        bot.send_message(message.chat.id, last(user_id,"هل لديك بريد الكتروني؟"), reply_markup= email_markup())

    elif last_message == 'ماهو بريدك الالكتروني؟':
        context = message.text
        update(user_id, 2, context)
        bot.send_message(message.chat.id, last(user_id,"اخبرنا عن نفسك قليلا"), reply_markup=example_markup())

    elif last_message == 'اخبرنا عن نفسك قليلا':
        context = message.text
        update(user_id, 3, context)
        bot.send_message(message.chat.id, last(user_id,"في اي قطاع تعمل ؟"), reply_markup=sector_markup())
    elif last_message == 'اكتب عنوانك الوظيفي':
        context = message.text
        update(user_id, 15, context)
        bot.send_message(message.chat.id, last(user_id,"هل عملت من قبل ؟"), reply_markup=work_markup())

    elif last_message == "اين عملت ؟":
        context = message.text
        update(user_id, 4, context)
        bot.send_message(message.chat.id, last(user_id," ماكان دورك في العمل ؟"), reply_markup=example_markup())
    
    elif last_message == " ماكان دورك في العمل ؟":
        context = message.text
        update(user_id, 5, context)
        bot.send_message(message.chat.id, last(user_id,"متى باشرت بالعمل ؟"), reply_markup=example_markup())

    elif last_message == "متى باشرت بالعمل ؟":
        context = message.text
        update(user_id, 6, context)
        bot.send_message(message.chat.id, last(user_id,"متى انتهيت من العمل هناك ؟"),
                            reply_markup=example_markup())
        bot.send_message(message.chat.id, "ارسل علامة النجمة (*) ان لم تنهي عملك هذا بعد")

    elif last_message == "متى انتهيت من العمل هناك ؟":
        context = message.text
        update(user_id, 7, context)
        bot.send_message(message.chat.id, last(user_id,"هل تود اضافة خبرات اخرى ؟"), reply_markup=add_skip())


    elif last_message == 'ما اسم المؤسسة التي درست بها ؟':
        context = message.text
        x = selector(user_id, 8)
        if x != None:
            context = f"{context}\n{x}"
        update(user_id, 8, context)
        bot.send_message(message.chat.id, last(user_id,"متى باشرت بالدراسة؟"), reply_markup=example_markup())

    elif last_message == 'متى باشرت بالدراسة؟':
        context = message.text
        x = selector(user_id, 9)
        if x != None:
            context = f"{context}\n{x}"
        update(user_id, 9, context)
        bot.send_message(message.chat.id, last(user_id,"متى انهيت دراستك؟"),
                            reply_markup=example_markup())
        bot.send_message(message.chat.id, "ارسل علامة النجمة (*) ان لم تنهي دراستك هذه بعد")

    elif last_message == "متى انهيت دراستك؟":
        context = message.text
        x = selector(user_id, 10)
        if x != None:
            context = f"{context}\n{x}"
        update(user_id, 10, context)
        bot.send_message(message.chat.id, last(user_id,"ما الذي درسته/تدرسه؟"), reply_markup=example_markup())
 
    elif last_message == 'ما الذي درسته/تدرسه؟':
        context = message.text
        x = selector(user_id, 11)
        if x != None:
            context = f"{context}\n{x}"
        update(user_id, 11, context)
        bot.send_message(message.chat.id, last(user_id,"هل تود اضافة شهادة اخرى ؟"), reply_markup=add_skip())
    elif last_message == 'ماهي مهاراتك ؟ اكتبها جميعا \n احرص على ان تكون كل مهارة بسطر':
        context = message.text
        update(user_id, 12, context)
        bot.send_message(message.chat.id, "كيف تود استلام اشعارات الوظائف ؟", reply_markup = recive_markup())
    
    
###################----------GET INFO-----------###################

###################----------GET PHOTO-----------###################
def photo(message):
    user_id = int(message.from_user.id)
    if does_exist(user_id, False) and (lastmsg(user_id) == "cb_oldcv" or lastmsg(user_id) == "ارسل الينا افضل صورة رسمية لديك"):
        bot.send_message(message.chat.id, "نقوم الان بمزج بياناتك مع قليل من الابداع والحب لننتج اليك سيرة ذاتية ترضي خاطرك ستستغرق هذه العملي بضع ثواني")
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        if str(user_id) not in list(os.listdir("users_data")):
            os.makedirs(f"users_data/{str(user_id)}")
            bot.send_message(message.chat.id, "step 4")
        with open(f"users_data/{user_id}/{user_id}.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        user_data = id2dict(message.from_user.id)

        cv_maker(user_data)
        bot.send_message(message.chat.id, "step 7")
        bot.send_document(user_id, document=open(f'users_data/{user_id}/{user_id}.pdf', 'rb'), caption = f'{user_data["name"]}')
        bot.send_message(message.chat.id, "step 8")

    else:
        bot.send_message(message.chat.id, "يبدو انك قد ارسلت هذه الصورة بالخطأ \n لاتخف لن نتمكن من تخزينها")
###################----------GET PHOTO-----------###################

###################----------EDIT INFO-----------###################
edit_calls = [
    'cb_name', 'cb_age', 'cb_phone',
    'cb_email', 'cb_about', 'cb_spec',
    'cb_sector', 'cb_edu', 'cb_exp', 'cb_skills']
def edit_info(call):
    pass
###################----------EDIT INFO-----------###################