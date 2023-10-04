from processors.csv_processor import (
    calcular_somatorio_genero,
    plot_porcentagem_sobreviventes,
    processar_csv,
    plota_dispersao_idade_tarifa,
)
import os


import pytermgui as ptg


from argparse import ArgumentParser, Namespace


PALETTE_LIGHT = "#FCBA03"
PALETTE_MID = "#8C6701"
PALETTE_DARK = "#4D4940"
PALETTE_DARKER = "#242321"


def _process_arguments(argv: list[str] | None = None) -> Namespace:
    """Processes command line arguments.

    Note that you don't _have to_ use the bultin argparse module for this; it
    is just what the module uses.

    Args:
        argv: A list of command line arguments, not including the binary path
            (sys.argv[0]).
    """

    parser = ArgumentParser(description="My first PTG application.")

    return parser.parse_args(argv)


def _create_aliases() -> None:
    """Creates all the TIM aliases used by the application.

    Aliases should generally follow the following format:

        namespace.item

    For example, the title color of an app named "myapp" could be something like:

        myapp.title
    """

    ptg.tim.alias("app.text", "#cfc7b0")

    ptg.tim.alias("app.header", f"bold @{PALETTE_MID} #d9d2bd")
    ptg.tim.alias("app.header.fill", f"@{PALETTE_LIGHT}")

    ptg.tim.alias("app.title", f"bold {PALETTE_LIGHT}")
    ptg.tim.alias("app.button.label", f"bold @{PALETTE_DARK} app.text")
    ptg.tim.alias("app.button.highlight", "inverse app.button.label")

    ptg.tim.alias("app.footer", f"@{PALETTE_DARKER}")


def _configure_widgets() -> None:
    """Defines all the global widget configurations.

    Some example lines you could use here:

        ptg.boxes.DOUBLE.set_chars_of(ptg.Window)
        ptg.Splitter.set_char("separator", " ")
        ptg.Button.styles.label = "myapp.button.label"
        ptg.Container.styles.border__corner = "myapp.border"
    """

    ptg.boxes.DOUBLE.set_chars_of(ptg.Window)
    ptg.boxes.ROUNDED.set_chars_of(ptg.Container)

    ptg.Button.styles.label = "app.button.label"
    ptg.Button.styles.highlight = "app.button.highlight"

    ptg.Slider.styles.filled__cursor = PALETTE_MID
    ptg.Slider.styles.filled_selected = PALETTE_LIGHT

    ptg.Label.styles.value = "app.text"

    ptg.Window.styles.border__corner = "#C2B280"
    ptg.Container.styles.border__corner = PALETTE_DARK

    ptg.Splitter.set_char("separator", "")


def _define_layout() -> ptg.Layout:
    """Defines the application layout.

    Layouts work based on "slots" within them. Each slot can be given dimensions for
    both width and height. Integer values are interpreted to mean a static width, float
    values will be used to "scale" the relevant terminal dimension, and giving nothing
    will allow PTG to calculate the corrent dimension.
    """

    layout = ptg.Layout()

    # A header slot with a height of 1
    layout.add_slot("Header", height=1)
    layout.add_break()

    # A body slot that will fill the entire width, and the height is remaining
    layout.add_slot("Body")

    layout.add_break()

    # A footer with a static height of 1
    layout.add_slot("Footer", height=1)

    return layout


def _confirm_quit(manager: ptg.WindowManager) -> None:
    """Cria uma janela com "Tem certeza que deseja sair?"""

    modal = ptg.Window(
        "[app.title]Tem certeza que deseja sair?",
        "",
        ptg.Container(
            ptg.Splitter(
                ptg.Button("Sim", lambda *_: manager.stop()),
                ptg.Button("Não", lambda *_: modal.close()),
            ),
        ),
    ).center()

    modal.select(1)
    manager.add(modal)


def _display_message_modal(manager: ptg.WindowManager, message: str):
    modal = ptg.Window(
        "[app.title]Resultado:",
        "",
        ptg.Container(
            ptg.Label(message),
            ptg.Splitter(
                ptg.Button("OK", lambda *_: modal.close()),
            ),
        ),
    ).center()
    modal.select(1)
    manager.add(modal)


def main(argv: list[str] | None = None) -> None:
    """Runs the application."""

    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    _create_aliases()
    _configure_widgets()

    args = _process_arguments(argv)

    with ptg.WindowManager() as manager:
        manager.layout = _define_layout()

        header = ptg.Window(
            "[app.header] Trabalho Machine Learning",
            box="EMPTY",
            is_persistant=True,
        )

        header.styles.fill = "app.header.fill"

        manager.add(header)

        footer = ptg.Window(
            ptg.Button("Sair", lambda *_: _confirm_quit(manager)),
            box="EMPTY",
        )
        footer.styles.fill = "app.footer"

        manager.add(footer, assign="footer")

        manager.add(
            ptg.Window(
                "[app.title]Pedro Martins Pereira - 2124290019",
                "",
                ptg.Collapsible(
                    "Exercícios",
                    "",
                    ptg.Container(
                        ptg.Button(
                            "Limpeza de Dados",
                            lambda *_: _display_message_modal(
                                manager,
                                processar_csv(
                                    "../data/dados.csv", "../respostas/Resposta01.txt"
                                ),
                            ),
                        ),
                        ptg.Button(
                            "Contagem de Gêneros",
                            lambda *_: _display_message_modal(
                                manager,
                                calcular_somatorio_genero("../data/dados.csv"),
                            ),
                        ),
                        ptg.Button(
                            "Análise de Sobreviventes",
                            lambda *_: _display_message_modal(
                                manager,
                                plot_porcentagem_sobreviventes(
                                    "../data/dados.csv",
                                    "../respostas/sobrevivtentes.png",
                                ),
                            ),
                        ),
                        ptg.Button(
                            "Gráfico de Dispersão",
                            lambda *_: _display_message_modal(
                                manager,
                                plota_dispersao_idade_tarifa(
                                    "../data/dados.csv", "../respostas/scatter.png"
                                ),
                            ),
                        ),
                        static_width=40,
                    ),
                ),
                "",
                "",
                vertical_align=ptg.VerticalAlignment.TOP,
                overflow=ptg.Overflow.SCROLL,
            ),
            assign="body",
        )

    ptg.tim.print(f"[{PALETTE_LIGHT}]Até a próxima!")


if __name__ == "__main__":
    main()
