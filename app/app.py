import reflex as rx
from app.states.base_state import BaseState
from app.components.topbar import topbar
from app.components.header import header
from app.components.navbar import navbar
from app.components.marquee import marquee
from app.components.hero import hero
from app.components.welcome import welcome_section
from app.components.sidebar import sidebar
from app.components.footer import footer
from app.components.layout import layout
from app.pages.about import about_institute, mission_vision, principal_message
from app.pages.academic import class_routine, syllabus
from app.pages.admission import admission_circular, apply_online
from app.pages.results import internal_results, public_results
from app.pages.gallery import photo_gallery, video_gallery
from app.pages.notices import notice_board
from app.pages.contact import contact_us


def index() -> rx.Component:
    return layout(
        rx.el.div(
            rx.el.div(hero(), class_name="animate-fade-in"),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        welcome_section(),
                        class_name="col-span-1 lg:col-span-2 animate-fade-in-up delay-100",
                    ),
                    rx.el.div(
                        sidebar(), class_name="col-span-1 animate-fade-in-up delay-200"
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-3 gap-8",
                ),
                class_name="container mx-auto px-4 py-12",
            ),
        )
    )


style_content = """
@keyframes marquee {
  0% { transform: translateX(100%); }
  100% { transform: translateX(-100%); }
}
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.animate-marquee {
  animation: marquee 30s linear infinite;
}
.animate-fade-in {
  animation: fadeIn 0.8s ease-out forwards;
}
.animate-fade-in-up {
  opacity: 0;
  animation: fadeInUp 0.8s ease-out forwards;
}
.delay-100 {
  animation-delay: 0.1s;
}
.delay-200 {
  animation-delay: 0.2s;
}
/* RTL Support for Marquee - reverses direction */
[dir="rtl"] .animate-marquee {
  animation-direction: reverse;
}
"""
app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
        rx.el.style(style_content),
    ],
)
app.add_page(index, route="/")
app.add_page(about_institute, route="/about")
app.add_page(mission_vision, route="/mission")
app.add_page(principal_message, route="/principal")
app.add_page(class_routine, route="/routine")
app.add_page(syllabus, route="/syllabus")
app.add_page(admission_circular, route="/admission-circular")
app.add_page(apply_online, route="/apply")
app.add_page(internal_results, route="/results-internal")
app.add_page(public_results, route="/results-public")
app.add_page(photo_gallery, route="/gallery-photo")
app.add_page(video_gallery, route="/gallery-video")
app.add_page(notice_board, route="/notices")
app.add_page(contact_us, route="/contact")