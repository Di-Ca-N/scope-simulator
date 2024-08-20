from antlr4 import *
from parser.PoodleParser import PoodleParser
from parser.PoodleLexer import PoodleLexer
from parser.PoodleVisitor import PoodleVisitor
from graphviz import Digraph
from matplotlib.widgets import Button

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pathlib
import click
import os
from PIL import Image


class ImageSlideshow:
    def __init__(self, image_folder, delay=2000):
        self.image_folder = image_folder
        self.delay = delay
        self.images = self.load_images()
        self.index = 0
        self.fig, self.ax = plt.subplots()
        self.ax.axis("off")
        self.load_image()

        self.ax_button_next = plt.axes([0.8, 0.02, 0.1, 0.05])
        self.button_next = Button(self.ax_button_next, "Next")
        self.button_next.on_clicked(self.next_image)

        self.ax_button_prev = plt.axes([0.6, 0.02, 0.1, 0.05])
        self.button_prev = Button(self.ax_button_prev, "Previous")
        self.button_prev.on_clicked(self.prev_image)

        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_frame,
            frames=len(self.images),
            interval=self.delay,
            repeat=True,
        )

    def load_images(self):
        image_files = [
            f
            for f in os.listdir(self.image_folder)
            if f.endswith(("png", "jpg", "jpeg", "gif"))
        ]
        images = []
        for file in image_files:
            img_path = os.path.join(self.image_folder, file)
            img = Image.open(img_path)
            images.append(img)
        return images

    def load_image(self):
        self.ax.clear()
        self.ax.imshow(self.images[self.index])
        self.ax.axis("off")

    def update_frame(self, i):
        self.ax.clear()
        self.load_image()

    def next_image(self, event):
        self.index = (self.index + 1) % len(self.images)
        self.load_image()
        plt.draw()

    def prev_image(self, event):
        self.index = (self.index - 1) % len(self.images)
        self.load_image()
        plt.draw()

    def show(self):
        plt.show()


class StepVisualizer:
    def __init__(self, folder="visuals"):
        self.step = 0
        self.folder = folder
        self.last_scope = None

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def visualize(self, scopes, filename="scope"):
        dot = Digraph(comment="Scopes")

        for i, scope in enumerate(scopes):
            scope_id = f"scope_{i}"
            dot.node(scope_id, label=f'{scope["name"]}')

            vars_label = "\n".join(f"{var}={val}" for var, val in scope["vars"].items())
            label = f'{scope["name"]}\n{vars_label}'

            dot.node(scope_id, label=label, shape="box")

            if scope["staticParent"] is not None:
                parent_scope_id = f'scope_{scope["staticParent"]}'
                dot.edge(parent_scope_id, scope_id)

            if i > 0:
                parent_scope_id = f"scope_{i-1}"
                dot.edge(parent_scope_id, scope_id, style="dotted")

        dot.render(os.path.join(self.folder, filename), format="png", cleanup=True)

    def log_and_visualize(self, scopes):
        self.step += 1
        self.visualize(scopes, filename=f"scope_step_{self.step}")


class Scoper:
    def __init__(self):
        self.call_stack = [
            {"staticParent": None, "vars": {}, "name": "global"}
        ]  # Starts with the global scope

    def pushScope(self, staticParent, args, scopeName):
        self.call_stack.append(
            {"staticParent": staticParent, "vars": args, "name": scopeName}
        )

    def popScope(self):
        self.call_stack.pop()

    def getTopScope(self):
        return self.call_stack[-1]

    def getTopIdx(self):
        return len(self.call_stack) - 1


class DynamicScoping(Scoper):
    def get(self, var):
        for scope in reversed(self.call_stack):
            if var in scope["vars"]:
                return scope["vars"][var]
        return None

    def assign(self, var, val):
        for scope in reversed(self.call_stack):
            if var in scope["vars"]:
                scope["vars"][var] = val
                return
        return None

    def declare(self, var, val):
        self.call_stack[-1]["vars"][var] = val


class StaticScoping(Scoper):
    def get(self, var):
        current_scope = self.call_stack[-1]
        while current_scope is not None:
            if var in current_scope["vars"]:
                return current_scope["vars"][var]
            current_scope = self.call_stack[current_scope["staticParent"]]
        return None

    def assign(self, var, val):
        current_scope = self.call_stack[-1]
        while current_scope is not None:
            if var in current_scope["vars"]:
                current_scope["vars"][var] = val
                return
            current_scope = self.call_stack[current_scope["staticParent"]]

    def declare(self, var, val):
        self.call_stack[-1]["vars"][var] = val


class PoodleInterpreter(PoodleVisitor):
    def __init__(self, scopingType, visualizer=None):
        self.scoping = scopingType
        self.functions = {}
        self.visualizer = visualizer

    def visitProgStmt(self, ctx: PoodleParser.ProgStmtContext):
        if self.visualizer:
            self.visualizer.log_and_visualize(self.scoping.call_stack)

        if ctx.varDeclaration():
            _, var, _, val, _ = ctx.varDeclaration().children
            evaluated_value = self.evalMathExpr(val)

            self.scoping.declare(var.getText(), evaluated_value)

        elif ctx.varAssignment():
            var, _, val, _ = ctx.varAssignment().children
            evaluated_value = self.evalMathExpr(val)

            self.scoping.assign(var.getText(), evaluated_value)

        elif ctx.funcDef():
            _, funcName, _, args, _, _, body, _ = ctx.funcDef().children
            self.functions[funcName.getText()] = {
                "args": args,
                "body": body,
                "staticParent": self.scoping.getTopIdx(),
            }

        elif ctx.funcCall():
            funcName, _, args, _, _ = ctx.funcCall().children

            if funcName.getText() == "print":
                for arg in args.children:
                    print(self.scoping.get(arg.getText()))
                return
            else:
                function = self.functions[funcName.getText()]
                funcArgs = {}
                if function["args"].children is not None:
                    for arg, parameter in zip(args.children, function["args"].children):
                        funcArgs[parameter.getText()] = self.eval(arg.getText())
                self.scoping.pushScope(
                    function["staticParent"], funcArgs, funcName.getText()
                )
                self.visit(self.functions[funcName.getText()]["body"])
                if self.visualizer:
                    self.visualizer.log_and_visualize(self.scoping.call_stack)

            self.scoping.popScope()

    def evalMathExpr(self, ctx: PoodleParser.MathExprContext):
        match ctx.children:
            case [TerminalNode() as t]:
                return self.eval(t.getText())

            case [
                PoodleParser.MathExprContext() as left,
                TerminalNode() as op,
                PoodleParser.MathExprContext() as right,
            ]:
                left_value = self.evalMathExpr(left)
                right_value = self.evalMathExpr(right)

                op = op.getText()
                if op == "+":
                    return left_value + right_value
                elif op == "-":
                    return left_value - right_value
                elif op == "*":
                    return left_value * right_value
                elif op == "/":
                    return left_value / right_value

            case [
                TerminalNode(),
                PoodleParser.MathExprContext() as expr,
                TerminalNode(),
            ]:
                return self.evalMathExpr(expr)

    def eval(self, value):
        if value.isnumeric():
            return int(value)
        return self.scoping.get(value)


@click.command()
@click.argument("file", type=click.Path(exists=True, path_type=pathlib.Path))
@click.option(
    "--scoping",
    default="static",
    type=click.Choice(["dynamic", "static"]),
    help="Scoping type to be used",
)
@click.option("--visualize", is_flag=True, help="Visualize the scopes")
def main(file, scoping, visualize):
    lexer = PoodleLexer(InputStream(file.read_text()))
    stream = CommonTokenStream(lexer)
    parser = PoodleParser(stream)
    visualizer = StepVisualizer() if visualize else None

    tree = parser.parse()
    visualizer = StepVisualizer() if visualize else None
    interpreter = PoodleInterpreter(
        scopingType=DynamicScoping() if scoping == "dynamic" else StaticScoping(),
        visualizer=visualizer,
    )
    interpreter.visit(tree)
    if visualize:
        slideshow = ImageSlideshow("visuals")
        slideshow.show()


main()
