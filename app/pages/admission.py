import reflex as rx
from app.states.base_state import BaseState
from app.components.layout import layout, page_wrapper


def admission_circular() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["admission_circular"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.image(
                        src="/graduation_ceremony_madrasa.png",
                        class_name="w-full h-64 object-cover rounded-t-xl mb-0",
                        alt="Graduation Ceremony",
                    ),
                    rx.el.div(
                        rx.el.h2(
                            BaseState.strings["admission_title_main"],
                            class_name="text-2xl font-bold text-gray-800 mb-4",
                        ),
                        rx.el.p(
                            BaseState.strings["admission_desc"],
                            class_name="text-gray-600 mb-6 leading-relaxed",
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "Key Dates",
                                class_name="font-bold text-lg mb-2 text-[#009345]",
                            ),
                            rx.el.ul(
                                rx.el.li(
                                    "Application Start: 01 November 2024",
                                    class_name="mb-1",
                                ),
                                rx.el.li(
                                    "Application Deadline: 25 December 2024",
                                    class_name="mb-1",
                                ),
                                rx.el.li(
                                    "Admission Test: 02 January 2025", class_name="mb-1"
                                ),
                                class_name="list-disc list-inside text-gray-700 mb-6",
                            ),
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "Requirements",
                                class_name="font-bold text-lg mb-2 text-[#009345]",
                            ),
                            rx.el.ul(
                                rx.el.li(
                                    "Birth Certificate / NID Copy", class_name="mb-1"
                                ),
                                rx.el.li("Previous Exam Marksheet", class_name="mb-1"),
                                rx.el.li("2 Passport Size Photos", class_name="mb-1"),
                                class_name="list-disc list-inside text-gray-700 mb-6",
                            ),
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "Fee Structure (Monthly)",
                                class_name="font-bold text-lg mb-4 text-[#009345] mt-8",
                            ),
                            rx.el.table(
                                rx.el.thead(
                                    rx.el.tr(
                                        rx.el.th(
                                            "Class",
                                            class_name="text-left py-2 px-4 bg-gray-50 text-sm font-semibold text-gray-600 rounded-tl-lg",
                                        ),
                                        rx.el.th(
                                            "Tuition Fee",
                                            class_name="text-left py-2 px-4 bg-gray-50 text-sm font-semibold text-gray-600",
                                        ),
                                        rx.el.th(
                                            "Exam Fee",
                                            class_name="text-left py-2 px-4 bg-gray-50 text-sm font-semibold text-gray-600 rounded-tr-lg",
                                        ),
                                    )
                                ),
                                rx.el.tbody(
                                    rx.el.tr(
                                        rx.el.td(
                                            "Class 6",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                        rx.el.td(
                                            "৳ 800",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                        rx.el.td(
                                            "৳ 500",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                    ),
                                    rx.el.tr(
                                        rx.el.td(
                                            "Class 7",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                        rx.el.td(
                                            "৳ 900",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                        rx.el.td(
                                            "৳ 500",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                    ),
                                    rx.el.tr(
                                        rx.el.td(
                                            "Class 8",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                        rx.el.td(
                                            "৳ 1000",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                        rx.el.td(
                                            "৳ 600",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                    ),
                                    rx.el.tr(
                                        rx.el.td(
                                            "Class 9-10 (Science)",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                        rx.el.td(
                                            "৳ 1200",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                        rx.el.td(
                                            "৳ 800",
                                            class_name="py-2 px-4 border-b border-gray-100 text-sm text-gray-700",
                                        ),
                                    ),
                                ),
                                class_name="w-full mb-8 border border-gray-100 rounded-lg overflow-hidden",
                            ),
                        ),
                        rx.el.button(
                            BaseState.strings["apply_now"],
                            class_name="bg-[#c2188b] text-white px-8 py-3 rounded-lg font-bold hover:bg-[#a01473] transition-colors w-full md:w-auto",
                        ),
                        class_name="p-8 bg-white rounded-b-xl shadow-sm border border-gray-100",
                    ),
                    class_name="max-w-3xl mx-auto shadow-lg rounded-xl",
                ),
            )
        )
    )


def apply_online() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["apply_online"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Online Application Form",
                            class_name="text-xl font-bold text-gray-800 mb-6",
                        ),
                        rx.el.form(
                            rx.el.div(
                                rx.el.div(
                                    rx.el.label(
                                        BaseState.strings["full_name"],
                                        class_name="block text-sm font-medium text-gray-700 mb-1",
                                    ),
                                    rx.el.input(
                                        type="text",
                                        class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-2 border",
                                    ),
                                    class_name="col-span-1",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        BaseState.strings["dob"],
                                        class_name="block text-sm font-medium text-gray-700 mb-1",
                                    ),
                                    rx.el.input(
                                        type="date",
                                        class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-2 border",
                                    ),
                                    class_name="col-span-1",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        BaseState.strings["father_name"],
                                        class_name="block text-sm font-medium text-gray-700 mb-1",
                                    ),
                                    rx.el.input(
                                        type="text",
                                        class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-2 border",
                                    ),
                                    class_name="col-span-1",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        BaseState.strings["mother_name"],
                                        class_name="block text-sm font-medium text-gray-700 mb-1",
                                    ),
                                    rx.el.input(
                                        type="text",
                                        class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-2 border",
                                    ),
                                    class_name="col-span-1",
                                ),
                                class_name="grid grid-cols-1 gap-6 mb-6",
                            ),
                            rx.el.button(
                                BaseState.strings["submit_application"],
                                type="button",
                                class_name="bg-[#009345] text-white px-8 py-3 rounded-lg font-bold hover:bg-[#007a3a] transition-colors w-full",
                            ),
                        ),
                        class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100",
                    ),
                    rx.el.div(
                        rx.image(
                            src="/modern_science_laboratory.png",
                            class_name="w-full h-full object-cover rounded-xl shadow-md min-h-[300px]",
                            alt="Science Lab",
                        ),
                        class_name="hidden lg:block",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-5xl mx-auto",
                ),
            )
        )
    )