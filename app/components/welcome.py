import reflex as rx
from app.states.base_state import BaseState


def welcome_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                BaseState.strings["welcome_title"],
                class_name="text-2xl md:text-3xl font-bold text-[#009345] mb-6 pb-2 border-b-2 border-[#c2188b] inline-block",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("image", class_name="w-16 h-16 text-gray-300"),
                    class_name="w-full h-64 md:h-80 bg-gray-100 rounded-lg shadow-sm mb-6 border border-gray-100 flex items-center justify-center",
                ),
                rx.el.div(
                    rx.el.p(
                        BaseState.strings["welcome_content"],
                        class_name="text-gray-600 leading-relaxed mb-4 text-justify",
                    ),
                    rx.el.p(
                        BaseState.strings["welcome_content"],
                        class_name="text-gray-600 leading-relaxed mb-6 text-justify hidden md:block",
                    ),
                    rx.el.button(
                        BaseState.strings["read_more"],
                        class_name="bg-[#009345] text-white px-6 py-2 rounded hover:bg-[#007a3a] transition-colors font-medium shadow-sm",
                    ),
                ),
                class_name="prose max-w-none",
            ),
            class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100",
        ),
        class_name="w-full",
    )