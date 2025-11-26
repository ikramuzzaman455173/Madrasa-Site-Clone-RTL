import reflex as rx
from app.states.base_state import BaseState
from app.components.layout import layout, page_wrapper


def internal_results() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["internal_result"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "graduation-cap",
                                class_name="w-24 h-24 text-[#009345] mb-4",
                            ),
                            class_name="flex justify-center",
                        ),
                        rx.el.h2(
                            "Student Result Portal",
                            class_name="text-2xl font-bold text-gray-800 text-center mb-6",
                        ),
                        rx.el.div(
                            rx.el.label(
                                BaseState.strings["student_id"],
                                class_name="block text-sm font-bold text-gray-700 mb-1",
                            ),
                            rx.el.input(
                                type="text",
                                placeholder="e.g. 2025101",
                                class_name="w-full rounded-lg border-gray-300 bg-gray-50 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-3 border mb-4",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                BaseState.strings["select_exam"],
                                class_name="block text-sm font-bold text-gray-700 mb-1",
                            ),
                            rx.el.select(
                                rx.el.option("Half Yearly Exam 2024"),
                                rx.el.option("Annual Exam 2023"),
                                class_name="w-full rounded-lg border-gray-300 bg-gray-50 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-3 border mb-6",
                            ),
                        ),
                        rx.el.button(
                            BaseState.strings["check_result"],
                            class_name="w-full bg-[#009345] text-white px-6 py-3 rounded-lg font-bold hover:bg-[#007a3a] transition-colors shadow-lg transform hover:-translate-y-0.5",
                        ),
                        class_name="bg-white p-8 rounded-2xl shadow-lg border border-gray-100 max-w-md mx-auto relative z-10",
                    ),
                    rx.el.div(
                        class_name="absolute top-0 left-0 w-full h-64 bg-[#009345]/10 rounded-t-3xl -z-0 translate-y-12 max-w-md mx-auto inset-x-0"
                    ),
                    rx.el.div(
                        rx.image(
                            src="/students_modern_computer.png",
                            class_name="w-full max-w-4xl mx-auto mt-12 rounded-xl shadow-lg opacity-90",
                            alt="Digital Result Processing",
                        ),
                        class_name="hidden md:block",
                    ),
                    class_name="relative pt-12",
                ),
            )
        )
    )


def public_results() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["public_result"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.image(
                        src="/educational_modern_computer.png",
                        class_name="w-full h-64 object-cover rounded-xl shadow-md mb-8",
                        alt="Public Results Banner",
                    ),
                    class_name="w-full mb-8",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.el.div(
                            rx.icon(
                                "external-link",
                                class_name="w-8 h-8 text-[#009345] mb-4",
                            ),
                            rx.el.h3(
                                "Education Board Results",
                                class_name="text-xl font-bold text-[#009345] mb-2",
                            ),
                            rx.el.p(
                                "Click here to visit the official website for SSC/Dakhil results.",
                                class_name="text-gray-600",
                            ),
                            class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-lg transition-shadow hover:border-[#009345] h-full",
                        ),
                        href="#",
                        target="_blank",
                    ),
                    rx.el.a(
                        rx.el.div(
                            rx.icon("globe", class_name="w-8 h-8 text-[#c2188b] mb-4"),
                            rx.el.h3(
                                "Madrasa Education Board",
                                class_name="text-xl font-bold text-[#c2188b] mb-2",
                            ),
                            rx.el.p(
                                "Official website of Bangladesh Madrasa Education Board.",
                                class_name="text-gray-600",
                            ),
                            class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:shadow-lg transition-shadow hover:border-[#c2188b] h-full",
                        ),
                        href="#",
                        target="_blank",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                ),
            )
        )
    )