import reflex as rx


def logo(class_name: str = "h-16 w-16") -> rx.Component:
    return rx.el.div(
        rx.image(
            src="placeholder.svg",
            class_name="w-full h-full object-contain p-0.5",
            alt="BSTM Logo",
        ),
        class_name=f"bg-white rounded-full flex items-center justify-center shadow-sm overflow-hidden {class_name}",
    )