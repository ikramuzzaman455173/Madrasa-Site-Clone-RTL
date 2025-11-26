import reflex as rx
from app.states.base_state import BaseState


def marquee() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    BaseState.strings["marquee_label"],
                    class_name="font-bold text-xs md:text-sm uppercase tracking-wider",
                ),
                class_name="bg-[#c2188b] text-white px-3 md:px-6 py-2 md:py-3 z-10 flex items-center whitespace-nowrap shadow-md",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        BaseState.strings["marquee_text"],
                        class_name="text-sm md:text-base font-medium text-gray-700 inline-block px-4",
                    ),
                    class_name="animate-marquee whitespace-nowrap inline-block",
                ),
                class_name="flex-1 overflow-hidden flex items-center bg-gray-50 py-2",
            ),
            class_name="container mx-auto flex items-stretch border-x border-gray-100",
        ),
        class_name="w-full bg-gray-50 border-b border-gray-200 shadow-sm overflow-hidden",
        dir=rx.cond(BaseState.is_rtl, "rtl", "ltr"),
    )