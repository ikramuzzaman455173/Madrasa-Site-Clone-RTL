import reflex as rx
from datetime import datetime


class Translation(rx.Base):
    """Type definition for translation dictionary values"""

    en: str
    bn: str
    ar: str


class BaseState(rx.State):
    """The base state for the application handling language and global settings."""

    current_lang: str = "bn"
    is_mobile_menu_open: bool = False

    @rx.var
    def is_rtl(self) -> bool:
        return self.current_lang == "ar"

    @rx.var
    def current_date_display(self) -> str:
        """Returns the current date formatted based on locale approximation."""
        now = datetime.now()
        if self.current_lang == "bn":
            return now.strftime("%d-%m-%Y")
        elif self.current_lang == "ar":
            return now.strftime("%Y-%m-%d")
        return now.strftime("%A, %d %B %Y")

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    @rx.event
    def set_language(self, lang: str):
        self.current_lang = lang

    @rx.event
    def t(self, key: str) -> str:
        """Helper to get translation by key"""
        return ""

    @rx.var
    def strings(self) -> dict[str, str]:
        """Returns the dictionary of strings for the current language."""
        data = {
            "en": {
                "institute_name": "Bangladesh Science and Technology Madrasah",
                "institute_slogan": "A Unique Institution for Modern and Islamic Education",
                "home": "Home",
                "about": "About Us",
                "about_institute": "About Institute",
                "mission_vision": "Mission & Vision",
                "academic": "Academic",
                "class_routine": "Class Routine",
                "syllabus": "Syllabus",
                "admission": "Admission",
                "admission_circular": "Admission Circular",
                "apply_online": "Apply Online",
                "results": "Results",
                "internal_result": "Internal Results",
                "public_result": "Board Results",
                "gallery": "Gallery",
                "photo_gallery": "Photo Gallery",
                "video_gallery": "Video Gallery",
                "notice": "Notice",
                "contact": "Contact",
                "login": "Login",
                "student_login": "Student Login",
                "teacher_login": "Teacher Login",
                "webmail": "Webmail",
                "latest_news": "Latest News",
                "read_more": "Read More",
                "principal_message": "Principal's Message",
                "important_links": "Important Links",
            },
            "bn": {
                "institute_name": "বাংলাদেশ বিজ্ঞান ও প্রযুক্তি মাদ্রাসা",
                "institute_slogan": "আধুনিক ও ইসলামী শিক্ষার অনন্য সমন্বয়",
                "home": "প্রথম পাতা",
                "about": "আমাদের কথা",
                "about_institute": "প্রতিষ্ঠান সম্পর্কে",
                "mission_vision": "লক্ষ্য ও উদ্দেশ্য",
                "academic": "একাডেমিক",
                "class_routine": "ক্লাস রুটিন",
                "syllabus": "সিলেবাস",
                "admission": "ভর্তি",
                "admission_circular": "ভর্তি বিজ্ঞপ্তি",
                "apply_online": "অনলাইনে আবেদন",
                "results": "ফলাফল",
                "internal_result": "অভ্যন্তরীণ ফলাফল",
                "public_result": "বোর্ড ফলাফল",
                "gallery": "গ্যালারি",
                "photo_gallery": "ফটো গ্যালারি",
                "video_gallery": "ভিডিও গ্যালারি",
                "notice": "নোটিশ",
                "contact": "যোগাযোগ",
                "login": "লগইন",
                "student_login": "শিক্ষার্থী লগইন",
                "teacher_login": "শিক্ষক লগইন",
                "webmail": "ওয়েবমেইল",
                "latest_news": "সর্বশেষ সংবাদ",
                "read_more": "আরও পড়ুন",
                "principal_message": "অধ্যক্ষের বাণী",
                "important_links": "গুরুত্বপূর্ণ লিঙ্ক",
            },
            "ar": {
                "institute_name": "المدرسة البنغلاديشية للعلوم والتكنولوجيا",
                "institute_slogan": "مؤسسة فريدة للتعليم الحديث والإسلامي",
                "home": "الرئيسية",
                "about": "من نحن",
                "about_institute": "عن المعهد",
                "mission_vision": "الرسالة والرؤية",
                "academic": "الأكاديمي",
                "class_routine": "روتين الفصل",
                "syllabus": "المنهج",
                "admission": "القبول",
                "admission_circular": "إشعار القبول",
                "apply_online": "التقديم عبر الإنترنت",
                "results": "النتائج",
                "internal_result": "النتائج الداخلية",
                "public_result": "نتائج المجلس",
                "gallery": "المعرض",
                "photo_gallery": "معرض الصور",
                "video_gallery": "معرض الفيديو",
                "notice": "إشعار",
                "contact": "اتصل بنا",
                "login": "تسجيل الدخول",
                "student_login": "دخول الطالب",
                "teacher_login": "دخول المعلم",
                "webmail": "البريد الإلكتروني",
                "latest_news": "آخر الأخبار",
                "read_more": "اقرأ المزيد",
                "principal_message": "رسالة المدير",
                "important_links": "روابط مهمة",
                "welcome_title": "مرحبا بكم في المدرسة البنغلاديشية للعلوم والتكنولوجيا",
                "welcome_content": "المدرسة البنغلاديشية للعلوم والتكنولوجيا هي مؤسسة تعليمية رائدة مكرسة لتعزيز التميز الأكاديمي والقيم الأخلاقية. يوفر حرمنا الأخضر المورق بيئة مثالية للتعلم والنمو. نحن ملتزمون بإنتاج مواطنين مستنيرين سيساهمون في تنمية الأمة.",
                "principal_name": "الشيخ محمد عبد الرحمن",
                "principal_designation": "المدير",
                "quick_info": "معلومات سريعة",
                "notice_board": "لوحة الإعلانات",
                "calendar": "التقويم",
                "view_all": "عرض الكل",
                "eiin": "EIIN",
                "mpo_code": "رمز MPO",
                "estd": "تأسست",
            },
        }
        if self.current_lang == "en":
            data["en"].update(
                {
                    "welcome_title": "Welcome to Bangladesh Science and Technology Madrasa",
                    "welcome_content": "Bangladesh Science and Technology Madrasa is a premier educational institution dedicated to fostering academic excellence and moral values. Our lush green campus provides an ideal environment for learning and growth. We are committed to producing enlightened citizens who will contribute to the nation's development.",
                    "principal_name": "Maulana Md. Abdur Rahman",
                    "principal_designation": "Principal",
                    "quick_info": "Quick Info",
                    "notice_board": "Notice Board",
                    "calendar": "Calendar",
                    "view_all": "View All",
                    "eiin": "EIIN",
                    "mpo_code": "MPO Code",
                    "estd": "Estd",
                    "footer_address": "123 Education Road, Dhaka-1000, Bangladesh",
                    "footer_phone": "+880 1234 567890",
                    "footer_email": "info@bstm.edu.bd",
                    "copyright": "© 2025 Bangladesh Science and Technology Madrasa. All rights reserved.",
                    "tech_support": "Technical support by TechSolutions Ltd.",
                    "useful_links": "Useful Links",
                    "connect_with_us": "Connect With Us",
                    "marquee_label": "LATEST NEWS",
                    "marquee_text": "*** Admission Going On for Academic Session 2025 *** Result of Half Yearly Examination 2024 Published *** Holiday Notice: The Madrasa will remain closed on the occasion of Eid-ul-Fitr ***",
                }
            )
        elif self.current_lang == "bn":
            data["bn"].update(
                {
                    "welcome_title": "বাংলাদেশ বিজ্ঞান ও প্রযুক্তি মাদ্রাসায় স্বাগতম",
                    "welcome_content": "বাংলাদেশ বিজ্ঞান ও প্রযুক্তি মাদ্রাসা একাডেমিক শ্রেষ্ঠত্ব এবং নৈতিক মূল্যবোধ লালন করার জন্য নিবেদিত একটি প্রধান শিক্ষা প্রতিষ্ঠান। আমাদের সবুজ ক্যাম্পাস শেখা এবং বৃদ্ধির জন্য একটি আদর্শ পরিবেশ প্রদান করে। আমরা আলোকিত নাগরিক তৈরিতে প্রতিশ্রুতিবদ্ধ যারা জাতির উন্নয়নে অবদান রাখবে।",
                    "principal_name": "মাওলানা মোঃ আব্দুর রহমান",
                    "principal_designation": "অধ্যক্ষ",
                    "quick_info": "দ্রুত তথ্য",
                    "notice_board": "নোটিশ বোর্ড",
                    "calendar": "ক্যালেন্ডার",
                    "view_all": "সব দেখুন",
                    "eiin": "EIIN",
                    "mpo_code": "MPO কোড",
                    "estd": "স্থাপিত",
                    "footer_address": "১২৩ শিক্ষা রোড, ঢাকা-১০০০, বাংলাদেশ",
                    "footer_phone": "+৮৮০ ১২৩৪ ৫৬৭৮৯০",
                    "footer_email": "info@bstm.edu.bd",
                    "copyright": "© ২০২৫ বাংলাদেশ বিজ্ঞান ও প্রযুক্তি মাদ্রাসা। সর্বস্বত্ব সংরক্ষিত।",
                    "tech_support": "কারিগরি সহযোগিতায় টেকসলিউশন লিমিটেড।",
                    "useful_links": "প্রয়োজনীয় লিঙ্ক",
                    "connect_with_us": "আমাদের সাথে যুক্ত হোন",
                    "marquee_label": "সর্বশেষ সংবাদ",
                    "marquee_text": "*** ২০২৫ শিক্ষাবর্ষের ভর্তি চলছে *** ২০২৪ সালের অর্ধবার্ষিক পরীক্ষার ফলাফল প্রকাশিত হয়েছে *** ছুটির বিজ্ঞপ্তি: ঈদুল ফিতর উপলক্ষে মাদ্রাসা বন্ধ থাকবে ***",
                }
            )
        elif self.current_lang == "ar":
            data["ar"].update(
                {
                    "footer_address": "١٢٣ طريق التعليم، دكا-١٠٠٠، بنغلاديش",
                    "footer_phone": "+٨٨٠ ١٢٣٤ ٥٦٧٨٩٠",
                    "footer_email": "info@bstm.edu.bd",
                    "copyright": "© ٢٠٢٥ المدرسة البنغلاديشية للعلوم والتكنولوجيا. جميع الحقوق محفوظة.",
                    "tech_support": "الدعم الفني بواسطة TechSolutions Ltd.",
                    "useful_links": "روابط مفيدة",
                    "connect_with_us": "تواصل معنا",
                    "marquee_label": "آخر الأخبار",
                    "marquee_text": "*** القبول مستمر للدورة الأكاديمية ٢٠٢٥ *** تم نشر نتيجة امتحان نصف السنة لعام ٢٠٢٤ *** إشعار العطلة: ستبقى المدرسة مغلقة بمناسبة عيد الفطر ***",
                }
            )
        common_additions = {
            "en": {
                "about_content_1": "Bangladesh Science and Technology Madrasa stands as a beacon of holistic education, merging traditional Islamic values with modern scientific knowledge. Established in 2026, our institution is poised to produce scholars who are not only well-versed in religious texts but also competitive in contemporary fields.",
                "about_history": "Our journey begins with a visionary goal: to bridge the gap between Madrasa education and modern technological advancement. We are proud to act as a pioneer in this integrated educational model, preparing to serve thousands of students across the nation with excellence.",
                "about_campus": "Our sprawling campus features state-of-the-art science laboratories, a rich library with vast collections, modern ICT labs, and spacious, well-ventilated classrooms designed to foster an optimal learning environment.",
                "mission_title": "Our Mission",
                "mission_text": "To provide a balanced education that nurtures the spiritual, intellectual, and physical growth of students, preparing them to be responsible citizens and future leaders.",
                "vision_title": "Our Vision",
                "vision_text": "To become a center of excellence where Islamic wisdom meets modern innovation.",
                "principal_msg_full": "Welcome to our institution. Education is the most powerful weapon which you can use to change the world. At BSTM, we believe in empowering our students with both moral character and academic excellence. Our dedicated faculty works tirelessly to shape the minds of the future generation. We are committed to providing an environment where students can thrive academically, socially, and spiritually.",
                "routine_title": "Class Routine 2025",
                "syllabus_desc": "Our comprehensive syllabus is designed to meet National Curriculum standards while providing in-depth Islamic education. We ensure a balanced load that encourages critical thinking and spiritual development.",
                "download": "Download",
                "apply_now": "Apply Now",
                "admission_title_main": "Admission Open for Academic Year 2025",
                "admission_desc": "We are inviting applications for admission in Class 6 to Class 9 and Alim 1st Year. BSTM offers a unique blend of Islamic and Modern education with state-of-the-art facilities. Join us to build a brilliant future.",
                "full_name": "Full Name",
                "father_name": "Father's Name",
                "mother_name": "Mother's Name",
                "dob": "Date of Birth",
                "submit_application": "Submit Application",
                "check_result": "Check Result",
                "student_id": "Student ID",
                "exam_year": "Exam Year",
                "select_exam": "Select Exam",
                "send_message": "Send Message",
                "your_email": "Your Email",
                "subject": "Subject",
                "message": "Message",
                "submit": "Submit",
                "location": "Our Location",
                "follow_us": "Follow Us",
            },
            "bn": {
                "about_content_1": "বাংলাদেশ বিজ্ঞান ও প্রযুক্তি মাদ্রাসা একটি পূর্ণাঙ্গ শিক্ষার আলোকবর্তিকা হিসেবে দাঁড়িয়ে আছে, যা ঐতিহ্যবাহী ইসলামী মূল্যবোধকে আধুনিক বৈজ্ঞানিক জ্ঞানের সাথে একীভূত করে। ২০২৬ সালে প্রতিষ্ঠিত, আমাদের প্রতিষ্ঠানটি এমন আলেম তৈরি করতে প্রস্তুত যারা কেবল ধর্মীয় গ্রন্থে পারদর্শী নয় বরং সমসাময়িক ক্ষেত্রেও প্রতিযোগিতামূলক।",
                "mission_title": "আমাদের লক্ষ্য",
                "mission_text": "শিক্ষার্থীদের আধ্যাত্মিক, বুদ্ধিবৃত্তিক এবং শারীরিক বিকাশকে লালন করে এমন একটি ভারসাম্যপূর্ণ শিক্ষা প্রদান করা, যা তাদের দায়িত্বশীল নাগরিক এবং ভবিষ্যতের নেতা হিসেবে প্রস্তুত করে।",
                "vision_title": "আমাদের দৃষ্টি",
                "vision_text": "এমন একটি শ্রেষ্ঠত্বের কেন্দ্র হওয়া যেখানে ইসলামী প্রজ্ঞা আধুনিক উদ্ভাবনের সাথে মিলিত হয়।",
                "principal_msg_full": "আমাদের প্রতিষ্ঠানে স্বাগতম। শিক্ষা হলো সবচেয়ে শক্তিশালী অস্ত্র যা আপনি বিশ্বকে পরিবর্তন করতে ব্যবহার করতে পারেন। বিএসটিএম-এ, আমরা আমাদের শিক্ষার্থীদের নৈতিক চরিত্র এবং একাডেমিক শ্রেষ্ঠত্ব উভয়ের সাথে ক্ষমতায়ন করতে বিশ্বাসী। আমাদের নিবেদিত অনুষদ ভবিষ্যৎ প্রজন্মের মনন গঠনে অক্লান্ত পরিশ্রম করে...",
                "routine_title": "ক্লাস রুটিন ২০২৫",
                "download": "ডাউনলোড",
                "apply_now": "আবেদন করুন",
                "full_name": "পুরো নাম",
                "father_name": "বাবার নাম",
                "mother_name": "মায়ের নাম",
                "dob": "জন্ম তারিখ",
                "submit_application": "আবেদন জমা দিন",
                "check_result": "ফলাফল দেখুন",
                "student_id": "শিক্ষার্থী আইডি",
                "exam_year": "পরীক্ষার বছর",
                "select_exam": "পরীক্ষা নির্বাচন করুন",
                "send_message": "বার্তা পাঠান",
                "your_email": "আপনার ইমেল",
                "subject": "বিষয়",
                "message": "বার্তা",
                "submit": "জমা দিন",
                "location": "আমাদের অবস্থান",
                "follow_us": "আমাদের অনুসরণ করুন",
            },
            "ar": {
                "about_content_1": "تقف المدرسة البنغلاديشية للعلوم والتكنولوجيا كمنارة للتعليم الشامل، حيث تدمج القيم الإسلامية التقليدية مع المعرفة العلمية الحديثة. تأسست مؤسستنا في عام ٢٠٢٦، وهي تستعد لإنتاج علماء ليسوا فقط متبحرين في النصوص الدينية ولكنهم أيضًا منافسون في المجالات المعاصرة.",
                "mission_title": "رسالتنا",
                "mission_text": "توفير تعليم متوازن يغذي النمو الروحي والفكري والجسدي للطلاب، ويعدهم ليكونوا مواطنين مسؤولين وقادة المستقبل.",
                "vision_title": "رؤيتنا",
                "vision_text": "أن نصبح مركزًا للتميز حيث تلتقي الحكمة الإسلامية بالابتكار الحديث.",
                "principal_msg_full": "مرحبًا بكم في مؤسستنا. التعليم هو أقوى سلاح يمكنك استخدامه لتغيير العالم. في BSTM، نؤمن بتمكين طلابنا بكل من الشخصية الأخلاقية والتميز الأكاديمي. تعمل هيئة التدريس المخصصة لدينا بلا كلل لتشكيل عقول جيل المستقبل...",
                "routine_title": "روتين الفصل ٢٠٢٥",
                "download": "تحميل",
                "apply_now": "قدم الآن",
                "full_name": "الاسم الكامل",
                "father_name": "اسم الأب",
                "mother_name": "اسم الأم",
                "dob": "تاريخ الميلاد",
                "submit_application": "تقديم الطلب",
                "check_result": "تحقق من النتيجة",
                "student_id": "هوية الطالب",
                "exam_year": "سنة الامتحان",
                "select_exam": "اختر الامتحان",
                "send_message": "إرسال رسالة",
                "your_email": "بريدك الإلكتروني",
                "subject": "الموضوع",
                "message": "الرسالة",
                "submit": "إرسال",
                "location": "موقعنا",
                "follow_us": "تابعنا",
            },
        }
        for lang in ["en", "bn", "ar"]:
            if lang in data and lang in common_additions:
                data[lang].update(common_additions[lang])
        return data.get(self.current_lang, data["en"])