import reflex as rx
from app.states.base_state import BaseState
from app.components.layout import layout, page_wrapper


def routine_row(day: str, subjects: list[str]) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            day,
            class_name="px-6 py-4 whitespace-nowrap font-medium text-gray-900 border-b",
        ),
        *[
            rx.el.td(
                sub, class_name="px-6 py-4 whitespace-nowrap text-gray-600 border-b"
            )
            for sub in subjects
        ],
    )


def class_routine() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["routine_title"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.image(
                        src="/islamic_madrasa_classroom.png",
                        class_name="w-full h-48 md:h-64 object-cover rounded-xl shadow-md mb-8",
                        alt="Classroom",
                    ),
                    rx.el.div(
                        rx.el.table(
                            rx.el.thead(
                                rx.el.tr(
                                    rx.el.th(
                                        "Day / Time",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b",
                                    ),
                                    rx.el.th(
                                        "09:00 - 09:45",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b",
                                    ),
                                    rx.el.th(
                                        "09:45 - 10:30",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b",
                                    ),
                                    rx.el.th(
                                        "10:30 - 11:15",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b",
                                    ),
                                    rx.el.th(
                                        "11:45 - 12:30",
                                        class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b",
                                    ),
                                ),
                                class_name="bg-gray-50",
                            ),
                            rx.el.tbody(
                                routine_row(
                                    "Saturday", ["Arabic", "Math", "English", "Science"]
                                ),
                                routine_row(
                                    "Sunday", ["Quran", "Bangla", "History", "Math"]
                                ),
                                routine_row(
                                    "Monday", ["Fiqh", "English", "Science", "Arabic"]
                                ),
                                routine_row(
                                    "Tuesday", ["Hadith", "Math", "Bangla", "ICT"]
                                ),
                                routine_row(
                                    "Wednesday",
                                    ["Science", "Arabic", "English", "History"],
                                ),
                                class_name="bg-white divide-y divide-gray-200",
                            ),
                            class_name="min-w-full table-auto",
                        ),
                        class_name="overflow-x-auto shadow border-b border-gray-200 rounded-lg",
                    ),
                ),
            )
        )
    )


def syllabus_item(title: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("file-text", class_name="w-8 h-8 text-[#c2188b] mr-4"),
            rx.el.div(
                rx.el.h4(title, class_name="font-bold text-gray-800"),
                rx.el.p("Updated: Jan 2025", class_name="text-xs text-gray-500"),
            ),
            class_name="flex items-center flex-1",
        ),
        rx.el.button(
            rx.icon("download", class_name="w-4 h-4 mr-2"),
            BaseState.strings["download"],
            class_name="flex items-center text-sm bg-[#009345] text-white px-4 py-2 rounded hover:bg-[#007a3a] transition-colors",
        ),
        class_name="flex items-center justify-between bg-white p-4 rounded-lg shadow-sm border border-gray-100 hover:shadow-md transition-shadow",
    )


def syllabus() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["syllabus"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src="/educational_learning_modern.png",
                            class_name="w-full h-48 object-cover rounded-lg shadow-md mb-6",
                            alt="Academic Excellence",
                        ),
                        rx.el.p(
                            BaseState.strings["syllabus_desc"],
                            class_name="text-gray-600 mb-6",
                        ),
                        class_name="mb-8",
                    ),
                    rx.el.div(
                        syllabus_item("Class 6 - Full Syllabus 2025"),
                        syllabus_item("Class 7 - Full Syllabus 2025"),
                        syllabus_item("Class 8 - Full Syllabus 2025"),
                        syllabus_item("Class 9 - Science Group Syllabus"),
                        syllabus_item("Class 9 - Arts Group Syllabus"),
                        syllabus_item("Alim 1st Year Syllabus"),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                    ),
                ),
            )
        )
    )