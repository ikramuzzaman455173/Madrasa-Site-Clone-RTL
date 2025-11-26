import reflex as rx
from app.states.base_state import BaseState
from app.components.topbar import topbar
from app.components.header import header
from app.components.navbar import navbar
from app.components.marquee import marquee
from app.components.footer import footer


def layout(content: rx.Component) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            topbar(),
            header(),
            navbar(),
            marquee(),
            rx.el.main(content, class_name="flex-1 bg-[#f8f8f8] min-h-[600px]"),
            footer(),
            class_name=rx.cond(
                BaseState.is_rtl,
                "font-['Inter'] bg-white min-h-screen flex flex-col",
                "font-['Inter'] bg-white min-h-screen flex flex-col",
            ),
            dir=rx.cond(BaseState.is_rtl, "rtl", "ltr"),
        )
    )


def page_wrapper(content: rx.Component) -> rx.Component:
    """Wraps page content in a container"""
    return rx.el.div(content, class_name="container mx-auto px-4 py-12 animate-fade-in")