import reflex as rx
from app.states.base_state import BaseState
from app.components.logo import logo


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    logo(class_name="h-20 w-20 md:h-24 md:w-24 mr-4 md:mr-6 shrink-0"),
                    rx.el.div(
                        rx.el.h1(
                            BaseState.strings["institute_name"],
                            class_name="text-2xl md:text-3xl lg:text-4xl font-bold text-[#009345] leading-tight",
                        ),
                        rx.el.p(
                            BaseState.strings["institute_slogan"],
                            class_name="text-sm md:text-base text-[#c2188b] font-medium mt-1",
                        ),
                        rx.el.p(
                            "EIIN: 123456 | MPO Code: 987654321",
                            class_name="text-xs text-gray-500 mt-1",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="flex items-center text-center md:text-left flex-col md:flex-row",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "graduation-cap",
                            class_name="w-12 h-12 text-[#009345] opacity-20",
                        ),
                        class_name="h-24 w-24 bg-gray-50 rounded-full flex items-center justify-center border-4 border-gray-100 hidden lg:flex",
                    ),
                    class_name="hidden lg:block",
                ),
                class_name="container mx-auto px-4 py-6 flex flex-col md:flex-row items-center justify-between gap-4",
            ),
            class_name="bg-white w-full shadow-sm border-b-4 border-[#c2188b]",
        )
    )