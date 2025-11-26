import reflex as rx
from app.states.base_state import BaseState
from app.components.layout import layout, page_wrapper
from app.components.sidebar import notice_item


def notice_board() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["notice_board"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.image(
                        src="/professional_beautiful_modern.png",
                        class_name="w-full h-48 md:h-64 object-cover rounded-xl shadow-md mb-8",
                        alt="Notice Board Banner",
                    ),
                    class_name="w-full",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "Latest Announcements",
                            class_name="text-lg font-bold text-gray-700 mb-4 block",
                        ),
                        class_name="border-b border-gray-200 mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            notice_item(
                                "26",
                                "Nov",
                                "Admission Circular 2025 published for all classes - Apply Now!",
                            ),
                            class_name="bg-white px-6 rounded-lg shadow-sm border border-gray-100 hover:bg-gray-50 transition-colors border-l-4 border-l-[#009345]",
                        ),
                        rx.el.div(
                            notice_item(
                                "24",
                                "Nov",
                                "Result of Half Yearly Examination 2024 has been published",
                            ),
                            class_name="bg-white px-6 rounded-lg shadow-sm border border-gray-100 hover:bg-gray-50 transition-colors border-l-4 border-l-[#c2188b]",
                        ),
                        rx.el.div(
                            notice_item(
                                "20",
                                "Nov",
                                "Holiday Notice: Institute closed for Eid-e-Miladunnabi",
                            ),
                            class_name="bg-white px-6 rounded-lg shadow-sm border border-gray-100 hover:bg-gray-50 transition-colors border-l-4 border-l-gray-400",
                        ),
                        rx.el.div(
                            notice_item(
                                "15",
                                "Nov",
                                "Parent-Teacher Meeting Schedule for Class 10",
                            ),
                            class_name="bg-white px-6 rounded-lg shadow-sm border border-gray-100 hover:bg-gray-50 transition-colors border-l-4 border-l-[#009345]",
                        ),
                        rx.el.div(
                            notice_item(
                                "10", "Nov", "Winter Vacation Start Date Announcement"
                            ),
                            class_name="bg-white px-6 rounded-lg shadow-sm border border-gray-100 hover:bg-gray-50 transition-colors border-l-4 border-l-gray-400",
                        ),
                        class_name="space-y-4",
                    ),
                ),
            )
        )
    )