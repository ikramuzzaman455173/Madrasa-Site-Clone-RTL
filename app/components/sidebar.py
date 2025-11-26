import reflex as rx
from app.states.base_state import BaseState


def sidebar_header(title: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="w-5 h-5 text-white mr-2"),
        rx.el.h4(
            title, class_name="text-lg font-bold text-white uppercase tracking-wide"
        ),
        class_name="bg-[#009345] p-3 rounded-t-lg flex items-center shadow-sm",
    )


def principal_card() -> rx.Component:
    return rx.el.div(
        sidebar_header(BaseState.strings["principal_message"], "user"),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("user", class_name="w-16 h-16 text-gray-400"),
                    class_name="w-32 h-32 rounded-full mx-auto border-4 border-gray-100 shadow-sm mb-4 flex items-center justify-center bg-gray-100",
                ),
                rx.el.h5(
                    BaseState.strings["principal_name"],
                    class_name="text-lg font-bold text-gray-800 text-center",
                ),
                rx.el.p(
                    BaseState.strings["principal_designation"],
                    class_name="text-sm text-[#c2188b] font-medium text-center mb-4",
                ),
                rx.el.p(
                    '"Education is the backbone of a nation. We are committed to building a strong nation..."',
                    class_name="text-gray-600 text-sm text-center italic mb-4 leading-relaxed",
                ),
                rx.el.div(
                    rx.el.a(
                        BaseState.strings["read_more"],
                        href="#",
                        class_name="text-[#009345] text-sm font-semibold hover:underline",
                    ),
                    class_name="text-center",
                ),
                class_name="p-6",
            ),
            class_name="bg-white rounded-b-lg shadow-sm border-x border-b border-gray-100",
        ),
        class_name="mb-6",
    )


def info_row(label: str, value: str) -> rx.Component:
    return rx.el.div(
        rx.el.span(label, class_name="text-gray-600 font-medium"),
        rx.el.span(value, class_name="text-gray-800 font-bold"),
        class_name="flex justify-between items-center py-2 border-b border-gray-100 last:border-0 text-sm",
    )


def quick_info_card() -> rx.Component:
    return rx.el.div(
        sidebar_header(BaseState.strings["quick_info"], "info"),
        rx.el.div(
            info_row(BaseState.strings["estd"], "2026"),
            info_row(BaseState.strings["eiin"], "123456"),
            info_row(BaseState.strings["mpo_code"], "987654321"),
            info_row("College Code", "6543"),
            class_name="p-4 bg-white rounded-b-lg shadow-sm border-x border-b border-gray-100",
        ),
        class_name="mb-6",
    )


def notice_item(date: str, month: str, title: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                date, class_name="block text-xl font-bold text-[#009345] leading-none"
            ),
            rx.el.span(month, class_name="block text-xs text-gray-500 uppercase"),
            class_name="bg-gray-50 p-2 rounded text-center min-w-[3.5rem] border border-gray-200",
        ),
        rx.el.div(
            rx.el.a(
                title,
                href="#",
                class_name="text-sm font-medium text-gray-700 hover:text-[#c2188b] transition-colors line-clamp-2",
            ),
            class_name="ml-3",
        ),
        class_name="flex items-start py-3 border-b border-gray-100 last:border-0",
    )


def notices_card() -> rx.Component:
    return rx.el.div(
        sidebar_header(BaseState.strings["notice_board"], "bell"),
        rx.el.div(
            rx.el.div(
                notice_item("26", "Nov", "Admission Circular 2025 published"),
                notice_item("24", "Nov", "Result of Half Yearly Exam 2024"),
                notice_item("20", "Nov", "Holiday Notice for Eid-e-Miladunnabi"),
                notice_item("15", "Nov", "Parent-Teacher Meeting Schedule"),
                class_name="mb-4",
            ),
            rx.el.a(
                BaseState.strings["view_all"],
                href="#",
                class_name="block w-full text-center bg-gray-50 text-[#009345] py-2 rounded text-sm font-medium hover:bg-[#009345] hover:text-white transition-colors border border-gray-200",
            ),
            class_name="p-4 bg-white rounded-b-lg shadow-sm border-x border-b border-gray-100",
        ),
        class_name="mb-6",
    )


def link_item(label: str) -> rx.Component:
    return rx.el.a(
        rx.icon(
            "chevron-right", class_name="w-4 h-4 text-[#c2188b] mr-2 rtl:rotate-180"
        ),
        label,
        href="#",
        class_name="flex items-center text-sm text-gray-600 hover:text-[#009345] py-2 border-b border-gray-100 last:border-0 transition-colors",
    )


def important_links_card() -> rx.Component:
    return rx.el.div(
        sidebar_header(BaseState.strings["important_links"], "link"),
        rx.el.div(
            link_item("Ministry of Education"),
            link_item("Madrasa Education Board"),
            link_item("Directorate of Madrasa Education"),
            link_item("BANBEIS"),
            link_item("Prime Minister's Office"),
            class_name="p-4 bg-white rounded-b-lg shadow-sm border-x border-b border-gray-100",
        ),
        class_name="mb-6",
    )


def calendar_widget() -> rx.Component:
    return rx.el.div(
        sidebar_header(BaseState.strings["calendar"], "calendar"),
        rx.el.div(
            rx.el.div(
                rx.el.span("November 2025", class_name="font-bold text-gray-700"),
                class_name="text-center py-2 border-b border-gray-100",
            ),
            rx.el.div(
                *[
                    rx.el.div(d, class_name="text-xs font-bold text-gray-400 py-1")
                    for d in ["S", "M", "T", "W", "T", "F", "S"]
                ],
                *[
                    rx.el.div(
                        i,
                        class_name=f"text-xs py-1.5 rounded-full {('bg-[#009345] text-white' if i == 26 else 'text-gray-600 hover:bg-gray-100')}",
                    )
                    for i in range(1, 31)
                ],
                class_name="grid grid-cols-7 text-center gap-1 p-2",
            ),
            class_name="p-2 bg-white rounded-b-lg shadow-sm border-x border-b border-gray-100",
        ),
        class_name="mb-6",
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        principal_card(),
        notices_card(),
        quick_info_card(),
        calendar_widget(),
        important_links_card(),
        class_name="w-full flex flex-col",
    )