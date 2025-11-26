import reflex as rx
from app.states.base_state import BaseState


def lang_button(code: str, label: str) -> rx.Component:
    return rx.el.button(
        label,
        on_click=lambda: BaseState.set_language(code),
        class_name=rx.cond(
            BaseState.current_lang == code,
            "bg-white text-[#009345] px-2 py-0.5 rounded text-xs font-bold",
            "text-white hover:text-gray-200 px-2 py-0.5 text-xs transition-colors",
        ),
    )


def topbar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("calendar", class_name="w-4 h-4 mr-2 opacity-80"),
                rx.el.span(BaseState.current_date_display, class_name="text-sm"),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.el.div(
                            rx.icon("mail", class_name="w-3 h-3 mr-1"),
                            rx.el.span(BaseState.strings["webmail"]),
                            class_name="flex items-center",
                        ),
                        href="#",
                        class_name="hover:underline mr-4 text-sm flex items-center",
                    ),
                    rx.el.a(
                        rx.el.div(
                            rx.icon("log-in", class_name="w-3 h-3 mr-1"),
                            rx.el.span(BaseState.strings["login"]),
                            class_name="flex items-center",
                        ),
                        href="#",
                        class_name="hover:underline mr-4 text-sm flex items-center",
                    ),
                    class_name="flex items-center border-r border-green-600 pr-4 mr-4",
                ),
                rx.el.div(
                    lang_button("bn", "BN"),
                    rx.el.span("|", class_name="mx-1 opacity-50"),
                    lang_button("en", "EN"),
                    rx.el.span("|", class_name="mx-1 opacity-50"),
                    lang_button("ar", "AR"),
                    class_name="flex items-center",
                ),
                class_name="flex items-center",
            ),
            class_name="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center py-2",
        ),
        class_name="bg-[#009345] text-white w-full border-b border-[#007a3a]",
    )