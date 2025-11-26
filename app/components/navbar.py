import reflex as rx
from app.states.base_state import BaseState


def nav_link(text: str, href: str = "#") -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name=rx.cond(
            rx.State.router.page.path == href,
            "text-white bg-[#007a3a] px-4 py-3 block md:inline-block font-bold transition-colors whitespace-nowrap text-sm uppercase tracking-wide shadow-inner",
            "text-white hover:bg-[#007a3a] px-4 py-3 block md:inline-block font-medium transition-colors whitespace-nowrap text-sm uppercase tracking-wide",
        ),
    )


def dropdown_item(text: str, href: str = "#") -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name=rx.cond(
            rx.State.router.page.path == href,
            "block px-4 py-2 text-sm text-[#009345] bg-gray-50 font-bold hover:bg-gray-100 border-l-4 border-[#009345]",
            "block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-[#009345] border-l-4 border-transparent",
        ),
    )


def dropdown_group(title: str, items: list[tuple[str, str]]) -> rx.Component:
    is_active = rx.cond(
        rx.State.router.page.path.is_in([link for _, link in items]), True, False
    )
    return rx.el.div(
        rx.el.button(
            title,
            rx.icon("chevron-down", class_name="w-4 h-4 ml-1 inline-block"),
            class_name=rx.cond(
                is_active,
                "text-white bg-[#007a3a] px-4 py-3 font-bold transition-colors flex items-center w-full md:w-auto justify-between md:justify-start text-sm uppercase tracking-wide shadow-inner",
                "text-white hover:bg-[#007a3a] px-4 py-3 font-medium transition-colors flex items-center w-full md:w-auto justify-between md:justify-start text-sm uppercase tracking-wide group-hover:bg-[#007a3a]",
            ),
        ),
        rx.el.div(
            *[dropdown_item(label, link) for label, link in items],
            class_name="hidden group-hover:block md:absolute md:top-full md:left-0 md:bg-white md:shadow-lg md:min-w-[200px] md:z-50 border-t-2 border-[#c2188b]",
        ),
        class_name="relative group w-full md:w-auto",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    BaseState.strings["home"],
                    class_name="font-bold text-white md:hidden ml-2",
                ),
                rx.el.button(
                    rx.icon("menu", class_name="w-6 h-6 text-white"),
                    on_click=BaseState.toggle_mobile_menu,
                    class_name="md:hidden p-2 focus:outline-none",
                ),
                class_name="flex md:hidden justify-between items-center p-2",
            ),
            rx.el.div(
                nav_link(BaseState.strings["home"], "/"),
                dropdown_group(
                    BaseState.strings["about"],
                    [
                        (BaseState.strings["about_institute"], "/about"),
                        (BaseState.strings["mission_vision"], "/mission"),
                        (BaseState.strings["principal_message"], "/principal"),
                    ],
                ),
                dropdown_group(
                    BaseState.strings["academic"],
                    [
                        (BaseState.strings["class_routine"], "/routine"),
                        (BaseState.strings["syllabus"], "/syllabus"),
                    ],
                ),
                dropdown_group(
                    BaseState.strings["admission"],
                    [
                        (
                            BaseState.strings["admission_circular"],
                            "/admission-circular",
                        ),
                        (BaseState.strings["apply_online"], "/apply"),
                    ],
                ),
                dropdown_group(
                    BaseState.strings["results"],
                    [
                        (BaseState.strings["internal_result"], "/results-internal"),
                        (BaseState.strings["public_result"], "/results-public"),
                    ],
                ),
                dropdown_group(
                    BaseState.strings["gallery"],
                    [
                        (BaseState.strings["photo_gallery"], "/gallery-photo"),
                        (BaseState.strings["video_gallery"], "/gallery-video"),
                    ],
                ),
                nav_link(BaseState.strings["notice"], "/notices"),
                nav_link(BaseState.strings["contact"], "/contact"),
                class_name=rx.cond(
                    BaseState.is_mobile_menu_open,
                    "flex flex-col w-full md:flex md:flex-row md:w-auto md:items-center",
                    "hidden md:flex md:flex-row md:w-auto md:items-center",
                ),
            ),
            class_name="container mx-auto px-0 md:px-4",
        ),
        class_name="bg-[#222222] md:bg-[#009345] md:border-t border-white/20 shadow-md w-full sticky top-0 z-40",
    )