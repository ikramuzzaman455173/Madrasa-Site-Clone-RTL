import reflex as rx
from app.states.base_state import BaseState


def hero() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    BaseState.strings["welcome_title"],
                    class_name="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-4 leading-tight drop-shadow-md",
                ),
                rx.el.p(
                    BaseState.strings["institute_slogan"],
                    class_name="text-lg md:text-xl text-gray-100 font-medium drop-shadow-sm max-w-2xl",
                ),
                class_name="container mx-auto px-4 h-full flex flex-col justify-center items-start",
            ),
            class_name="absolute inset-0 bg-gradient-to-r from-[#009345] via-[#009345]/80 to-[#009345]/40",
        ),
        rx.el.div(
            rx.icon(
                "book-open",
                class_name="w-96 h-96 text-white opacity-5 absolute -right-10 -bottom-10 rotate-12",
            ),
            class_name="w-full h-full bg-gradient-to-br from-[#009345] to-[#006d33]",
        ),
        class_name="relative w-full h-[400px] md:h-[500px] overflow-hidden",
    )