import reflex as rx
from app.states.base_state import BaseState
from app.components.layout import layout, page_wrapper


def about_institute() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["about_institute"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src="/beautiful_modern_islamic.png",
                            class_name="w-full h-full object-cover rounded-lg shadow-lg mb-6",
                            alt="Campus View",
                        ),
                        rx.el.div(
                            rx.image(
                                src="/educational_islamic_madrasa.png",
                                class_name="w-full h-48 object-cover rounded-lg shadow-md mt-4",
                                alt="Educational Environment",
                            ),
                            class_name="hidden lg:block",
                        ),
                        class_name="col-span-1 lg:col-span-1",
                    ),
                    rx.el.div(
                        rx.el.p(
                            BaseState.strings["about_content_1"],
                            class_name="text-lg text-gray-700 leading-relaxed mb-6",
                        ),
                        rx.el.h3(
                            "Our History",
                            class_name="text-xl font-bold text-[#009345] mb-3",
                        ),
                        rx.el.p(
                            BaseState.strings["about_history"],
                            class_name="text-gray-600 leading-relaxed mb-6",
                        ),
                        rx.el.h3(
                            "Campus Life",
                            class_name="text-xl font-bold text-[#009345] mb-3",
                        ),
                        rx.el.p(
                            BaseState.strings["about_campus"],
                            class_name="text-gray-600 leading-relaxed mb-6",
                        ),
                        rx.el.div(
                            rx.image(
                                src="/modern_science_laboratory.png",
                                class_name="w-full h-64 object-cover rounded-lg shadow-md",
                                alt="Modern Labs",
                            ),
                            class_name="mt-4",
                        ),
                        class_name="col-span-1 lg:col-span-2",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-3 gap-8",
                ),
                rx.el.div(
                    rx.el.h3(
                        "Our Core Values",
                        class_name="text-2xl font-bold text-[#009345] mb-6 text-center",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "heart",
                                class_name="w-10 h-10 text-[#c2188b] mb-4 mx-auto",
                            ),
                            rx.el.h4(
                                "Integrity",
                                class_name="text-lg font-bold text-gray-800 mb-2 text-center",
                            ),
                            rx.el.p(
                                "Upholding the highest standards of honesty and strong moral principles.",
                                class_name="text-gray-600 text-center text-sm",
                            ),
                            class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow",
                        ),
                        rx.el.div(
                            rx.icon(
                                "book-open",
                                class_name="w-10 h-10 text-[#009345] mb-4 mx-auto",
                            ),
                            rx.el.h4(
                                "Excellence",
                                class_name="text-lg font-bold text-gray-800 mb-2 text-center",
                            ),
                            rx.el.p(
                                "Striving for the highest quality in academic and spiritual education.",
                                class_name="text-gray-600 text-center text-sm",
                            ),
                            class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow",
                        ),
                        rx.el.div(
                            rx.icon(
                                "users",
                                class_name="w-10 h-10 text-[#c2188b] mb-4 mx-auto",
                            ),
                            rx.el.h4(
                                "Community",
                                class_name="text-lg font-bold text-gray-800 mb-2 text-center",
                            ),
                            rx.el.p(
                                "Fostering a supportive environment of mutual respect and cooperation.",
                                class_name="text-gray-600 text-center text-sm",
                            ),
                            class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow",
                        ),
                        rx.el.div(
                            rx.icon(
                                "lightbulb",
                                class_name="w-10 h-10 text-[#009345] mb-4 mx-auto",
                            ),
                            rx.el.h4(
                                "Innovation",
                                class_name="text-lg font-bold text-gray-800 mb-2 text-center",
                            ),
                            rx.el.p(
                                "Embracing modern technology and creative teaching methodologies.",
                                class_name="text-gray-600 text-center text-sm",
                            ),
                            class_name="bg-white p-6 rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-12",
                    ),
                    class_name="mt-16",
                ),
            )
        )
    )


def mission_vision() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["mission_vision"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.image(
                        src="/islamic_beautiful_calligraphy.png",
                        class_name="w-full h-64 object-cover rounded-xl shadow-md mb-8",
                        alt="Vision Banner",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.icon("target", class_name="w-8 h-8 text-white"),
                                class_name="w-16 h-16 bg-[#009345] rounded-full flex items-center justify-center mb-6 shadow-md",
                            ),
                            rx.el.h2(
                                BaseState.strings["mission_title"],
                                class_name="text-2xl font-bold text-gray-800 mb-4",
                            ),
                            rx.el.p(
                                BaseState.strings["mission_text"],
                                class_name="text-gray-600 leading-relaxed",
                            ),
                            class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:border-[#009345] transition-all hover:-translate-y-1 duration-300",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.icon("eye", class_name="w-8 h-8 text-white"),
                                class_name="w-16 h-16 bg-[#c2188b] rounded-full flex items-center justify-center mb-6 shadow-md",
                            ),
                            rx.el.h2(
                                BaseState.strings["vision_title"],
                                class_name="text-2xl font-bold text-gray-800 mb-4",
                            ),
                            rx.el.p(
                                BaseState.strings["vision_text"],
                                class_name="text-gray-600 leading-relaxed",
                            ),
                            class_name="bg-white p-8 rounded-xl shadow-sm border border-gray-100 hover:border-[#c2188b] transition-all hover:-translate-y-1 duration-300",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
                    ),
                ),
            )
        )
    )


def principal_message() -> rx.Component:
    return layout(
        page_wrapper(
            rx.el.div(
                rx.el.h1(
                    BaseState.strings["principal_message"],
                    class_name="text-3xl font-bold text-[#009345] mb-8 border-b-2 border-[#c2188b] inline-block",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.image(
                                src="/portrait_professional_dignified.png",
                                class_name="w-full h-full object-cover",
                                alt="Principal",
                            ),
                            class_name="w-full aspect-[3/4] rounded-lg shadow-lg overflow-hidden mb-4",
                        ),
                        rx.el.div(
                            rx.el.h3(
                                BaseState.strings["principal_name"],
                                class_name="text-xl font-bold text-center",
                            ),
                            rx.el.p(
                                BaseState.strings["principal_designation"],
                                class_name="text-[#009345] text-center font-medium",
                            ),
                            class_name="bg-white p-4 rounded-lg shadow-sm border border-gray-100",
                        ),
                        class_name="col-span-1 md:col-span-1",
                    ),
                    rx.el.div(
                        rx.icon(
                            "quote",
                            class_name="w-16 h-16 text-[#009345] opacity-10 mb-2",
                        ),
                        rx.el.div(
                            rx.el.h2(
                                "Message from the Desk",
                                class_name="text-2xl font-bold text-gray-800 mb-4",
                            ),
                            rx.el.p(
                                BaseState.strings["principal_msg_full"],
                                class_name="text-lg text-gray-700 leading-loose mb-6",
                            ),
                            rx.el.p(
                                "Our institution is not just about academic grades; it is about character building, spiritual growth, and social responsibility. We invite you to join us in this noble journey of knowledge and enlightenment.",
                                class_name="text-lg text-gray-700 leading-loose",
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Sincerely,",
                                    class_name="font-medium text-gray-500 mt-8",
                                ),
                                rx.el.img(
                                    src="placeholder.svg",
                                    class_name="h-12 opacity-50 my-2",
                                ),
                                rx.el.p(
                                    BaseState.strings["principal_name"],
                                    class_name="font-bold text-gray-800",
                                ),
                                class_name="mt-4",
                            ),
                            class_name="prose max-w-none relative z-10",
                        ),
                        class_name="col-span-1 md:col-span-3 bg-white p-8 md:p-12 rounded-xl shadow-sm border border-gray-100 relative overflow-hidden",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-4 gap-8",
                ),
            )
        )
    )