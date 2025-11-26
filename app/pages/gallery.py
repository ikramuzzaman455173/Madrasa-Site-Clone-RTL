import reflex as rx
from app.states.base_state import BaseState
from app.components.layout import layout, page_wrapper


def photo_gallery() -> rx.Component:
    images = [
        "/beautiful_modern_islamic.png",
        "/ceremony_madrasa_graduation.png",
        "/educational_islamic_madrasa.png",
        "/educational_learning_modern.png",
        "/educational_modern_computer.png",
        "/educational_modern_science.png",
        "/graduation_ceremony_islamic.png",
        "/graduation_ceremony_madrasa.png",
        "/green_science_flask.png",
        "/islamic_beautiful_calligraphy.png",
        "/islamic_calligraphy_quran.png",
        "/islamic_graduation_ceremony.png",
        "/islamic_madrasa_classroom.png",
        "/modern_islamic_beautiful.png",
        "/modern_islamic_professional.png",
        "/modern_science_laboratory.png",
        "/portrait_professional_dignified.png",
        "/professional_beautiful_modern.png",
        "/professional_portrait_dignified.png",
        "/students_modern_computer.png",
    ]
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["photo_gallery"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    *[
                        rx.image(
                            src=img,
                            class_name="w-full h-64 object-cover rounded-xl shadow-md hover:scale-105 transition-transform duration-300 cursor-pointer hover:shadow-xl",
                        )
                        for img in images
                    ],
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
                ),
            )
        )
    )


def video_gallery() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["video_gallery"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.image(
                        src="/modern_islamic_professional.png",
                        class_name="w-full h-48 md:h-64 object-cover rounded-xl shadow-md mb-8",
                        alt="Video Gallery Banner",
                    ),
                    class_name="w-full",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "play", class_name="w-16 h-16 text-white opacity-80"
                            ),
                            class_name="w-full h-64 bg-gray-800 rounded-xl shadow-md flex items-center justify-center cursor-pointer hover:bg-gray-700 transition-colors relative overflow-hidden group",
                        ),
                        rx.el.h3(
                            "Annual Sports Day 2024 Highlights",
                            class_name="mt-3 font-bold text-gray-800 text-lg",
                        ),
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "play", class_name="w-16 h-16 text-white opacity-80"
                            ),
                            class_name="w-full h-64 bg-gray-800 rounded-xl shadow-md flex items-center justify-center cursor-pointer hover:bg-gray-700 transition-colors relative overflow-hidden group",
                        ),
                        rx.el.h3(
                            "Science Fair Project Exhibition",
                            class_name="mt-3 font-bold text-gray-800 text-lg",
                        ),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
                ),
            )
        )
    )