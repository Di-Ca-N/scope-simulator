
from antlr4 import *
import pathlib
import shutil
import click

from visualization import StepVisualizer, ImageSlideshow
from scoping import DynamicScoping, StaticScoping
from interpreter import PoodleInterpreter, PoodleParser, PoodleLexer


scoping_strategies = {
    "static": StaticScoping,
    "dynamic": DynamicScoping,
}

@click.command()
@click.argument("file", type=click.Path(exists=True, path_type=pathlib.Path))
@click.option(
    "--scoping",
    default="static",
    type=click.Choice(list(scoping_strategies.keys())),
    help="Scoping type to be used",
)
@click.option("--visualize", is_flag=True, help="Visualize the scopes")
def main(file, scoping, visualize):
    lexer = PoodleLexer(InputStream(file.read_text()))
    stream = CommonTokenStream(lexer)
    parser = PoodleParser(stream)
    visualizer = StepVisualizer()
    tree = parser.parse()
    interpreter = PoodleInterpreter(
        scopingType=scoping_strategies[scoping](),
        stepCallback=visualizer.log_and_visualize if visualize else None
    )
    interpreter.visit(tree)
    if visualize:
        slideshow = ImageSlideshow("visuals")
        slideshow.show()
        shutil.rmtree(pathlib.Path(slideshow.image_folder))

main()
