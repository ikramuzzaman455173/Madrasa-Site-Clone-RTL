import reflex as rx
from app.states.base_state import BaseState


def footer_link(text: str, href: str = "#") -> rx.Component:
    return rx.el.li(
        rx.el.a(
            rx.icon(
                "chevron-right",
                class_name="w-3 h-3 mr-2 text-[#009345] rtl:rotate-180 rtl:mr-0 rtl:ml-2",
            ),
            text,
            href=href,
            class_name="text-gray-400 hover:text-white transition-colors text-sm flex items-center",
        ),
        class_name="mb-2",
    )


def social_icon(icon: str, href: str = "#") -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-5 h-5 text-white"),
        href=href,
        class_name="bg-[#333] hover:bg-[#009345] p-2 rounded-full transition-colors duration-300",
    )


from app.components.logo import logo


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        logo(class_name="h-16 w-16 mb-4"),
                        rx.el.h3(
                            BaseState.strings["institute_name"],
                            class_name="text-lg font-bold text-white mb-4",
                        ),
                        rx.el.p(
                            BaseState.strings["institute_slogan"],
                            class_name="text-gray-400 text-sm leading-relaxed mb-6",
                        ),
                        class_name="flex flex-col items-start",
                    ),
                    class_name="col-span-1 md:col-span-2 lg:col-span-1",
                ),
                rx.el.div(
                    rx.el.h4(
                        BaseState.strings["contact"],
                        class_name="text-white font-bold text-lg mb-6 border-b-2 border-[#009345] inline-block pb-1",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "map-pin",
                                class_name="w-5 h-5 text-[#009345] mr-3 mt-1 rtl:mr-0 rtl:ml-3 shrink-0",
                            ),
                            rx.el.span(
                                BaseState.strings["footer_address"],
                                class_name="text-gray-400 text-sm",
                            ),
                            class_name="flex items-start mb-4",
                        ),
                        rx.el.div(
                            rx.icon(
                                "phone",
                                class_name="w-5 h-5 text-[#009345] mr-3 mt-1 rtl:mr-0 rtl:ml-3 shrink-0",
                            ),
                            rx.el.span(
                                BaseState.strings["footer_phone"],
                                class_name="text-gray-400 text-sm",
                            ),
                            class_name="flex items-center mb-4",
                        ),
                        rx.el.div(
                            rx.icon(
                                "mail",
                                class_name="w-5 h-5 text-[#009345] mr-3 mt-1 rtl:mr-0 rtl:ml-3 shrink-0",
                            ),
                            rx.el.span(
                                BaseState.strings["footer_email"],
                                class_name="text-gray-400 text-sm",
                            ),
                            class_name="flex items-center",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.h4(
                        BaseState.strings["useful_links"],
                        class_name="text-white font-bold text-lg mb-6 border-b-2 border-[#009345] inline-block pb-1",
                    ),
                    rx.el.ul(
                        footer_link(BaseState.strings["home"], "/"),
                        footer_link(BaseState.strings["about"], "/about"),
                        footer_link(
                            BaseState.strings["admission"], "/admission-circular"
                        ),
                        footer_link(BaseState.strings["results"], "/results-internal"),
                        footer_link(BaseState.strings["contact"], "/contact"),
                        class_name="list-none space-y-2",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.h4(
                        BaseState.strings["connect_with_us"],
                        class_name="text-white font-bold text-lg mb-6 border-b-2 border-[#009345] inline-block pb-1",
                    ),
                    rx.el.div(
                        social_icon("facebook"),
                        social_icon("twitter"),
                        social_icon("youtube"),
                        social_icon("instagram"),
                        class_name="flex space-x-3 rtl:space-x-reverse mb-6",
                    ),
                    rx.el.div(
                        rx.el.h5("Map", class_name="text-white font-bold text-sm mb-3"),
                        rx.el.div(
                            rx.icon("map-pin", class_name="w-8 h-8 text-gray-400 mb-2"),
                            rx.el.span(
                                "View on Map",
                                class_name="text-gray-400 text-xs font-medium",
                            ),
                            class_name="w-full h-32 bg-[#333] rounded border border-gray-700 flex flex-col items-center justify-center hover:bg-[#444] transition-colors cursor-pointer",
                        ),
                    ),
                    class_name="col-span-1",
                ),
                class_name="container mx-auto px-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12",
            ),
            class_name="bg-[#222222] py-16 border-t-4 border-[#009345]",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    BaseState.strings["copyright"],
                    class_name="text-gray-400 text-xs md:text-sm text-center md:text-left",
                ),
                rx.el.p(
                    BaseState.strings["tech_support"],
                    class_name="text-gray-500 text-xs md:text-sm text-center md:text-right mt-2 md:mt-0",
                ),
                class_name="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center",
            ),
            class_name="bg-[#1a1a1a] py-4 border-t border-gray-800",
        ),
        class_name="w-full mt-auto",
        dir=rx.cond(BaseState.is_rtl, "rtl", "ltr"),
    )