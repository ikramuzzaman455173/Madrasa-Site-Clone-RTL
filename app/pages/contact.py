import reflex as rx
from app.states.base_state import BaseState
from app.components.layout import layout, page_wrapper


def contact_us() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["contact"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            BaseState.strings["send_message"],
                            class_name="text-xl font-bold text-gray-800 mb-6",
                        ),
                        rx.el.form(
                            rx.el.div(
                                rx.el.label(
                                    BaseState.strings["full_name"],
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    type="text",
                                    class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-2 border mb-4",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    BaseState.strings["your_email"],
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    type="email",
                                    class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-2 border mb-4",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    BaseState.strings["subject"],
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.input(
                                    type="text",
                                    class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-2 border mb-4",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    BaseState.strings["message"],
                                    class_name="block text-sm font-medium text-gray-700 mb-1",
                                ),
                                rx.el.textarea(
                                    rows=4,
                                    class_name="w-full rounded-md border-gray-300 shadow-sm focus:border-[#009345] focus:ring focus:ring-[#009345] focus:ring-opacity-50 p-2 border mb-4",
                                ),
                            ),
                            rx.el.button(
                                BaseState.strings["submit"],
                                type="button",
                                class_name="bg-[#009345] text-white px-8 py-3 rounded-lg font-bold hover:bg-[#007a3a] transition-colors",
                            ),
                        ),
                        class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                BaseState.strings["location"],
                                class_name="text-xl font-bold text-gray-800 mb-6",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "map-pin",
                                    class_name="w-8 h-8 text-[#009345] mr-4 mt-1 shrink-0",
                                ),
                                rx.el.p(
                                    BaseState.strings["footer_address"],
                                    class_name="text-gray-600",
                                ),
                                class_name="flex items-start mb-6",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "phone",
                                    class_name="w-8 h-8 text-[#009345] mr-4 mt-1 shrink-0",
                                ),
                                rx.el.p(
                                    BaseState.strings["footer_phone"],
                                    class_name="text-gray-600",
                                ),
                                class_name="flex items-start mb-6",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "mail",
                                    class_name="w-8 h-8 text-[#009345] mr-4 mt-1 shrink-0",
                                ),
                                rx.el.p(
                                    BaseState.strings["footer_email"],
                                    class_name="text-gray-600",
                                ),
                                class_name="flex items-start mb-6",
                            ),
                            class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100 mb-6",
                        ),
                        rx.el.div(
                            rx.image(
                                src="/modern_islamic_professional.png",
                                class_name="w-full h-64 object-cover rounded-xl shadow-sm",
                                alt="Admin Building",
                            ),
                            class_name="w-full h-64 rounded-xl shadow-sm overflow-hidden mb-4",
                        ),
                        rx.el.div(
                            rx.image(
                                src="placeholder.svg",
                                class_name="w-full h-full object-cover opacity-50",
                                alt="Map Placeholder",
                            ),
                            class_name="w-full h-64 bg-gray-200 rounded-xl shadow-sm flex items-center justify-center border border-gray-300 mb-6",
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "Office Hours",
                                class_name="text-lg font-bold text-gray-800 mb-4",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.span(
                                        "Saturday - Thursday",
                                        class_name="font-medium text-gray-600",
                                    ),
                                    rx.el.span(
                                        "08:00 AM - 04:00 PM",
                                        class_name="text-gray-800 font-bold",
                                    ),
                                    class_name="flex justify-between items-center py-2 border-b border-gray-100",
                                ),
                                rx.el.div(
                                    rx.el.span(
                                        "Friday", class_name="font-medium text-gray-600"
                                    ),
                                    rx.el.span(
                                        "Closed", class_name="text-[#c2188b] font-bold"
                                    ),
                                    class_name="flex justify-between items-center py-2",
                                ),
                                class_name="bg-gray-50 p-4 rounded-lg border border-gray-200",
                            ),
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-8",
                ),
            )
        )
    )