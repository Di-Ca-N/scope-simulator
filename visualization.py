from graphviz import Digraph
from matplotlib.widgets import Button

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
from PIL import Image
from scoping import StackFrame

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
        image_files.sort()
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

    def visualize(self, scopes: list[StackFrame], ctx, line_text, filename="scope"):
        dot = Digraph(comment="Scopes", graph_attr={"dpi": "300", "label": f"{self.step}. {line_text}", "labelloc": "t", "labeljust": "l"})

        for i, scope in enumerate(scopes):
            scope_id = f"scope_{i}"
            dot.node(scope_id, label=f'{scope.name}')

            vars_label = "\n".join(f"{var}={val}" for var, val in scope.vars.items())
            label = f'{scope.name}\n{vars_label}'

            dot.node(scope_id, label=label, shape="box", color="black" if i == len(scopes) - 1 else "gray")

            if scope.staticLink is not None:
                parent_scope_id = f'scope_{scopes.index(scope.staticLink)}'
                dot.edge(parent_scope_id, scope_id)

            if i > 0:
                parent_scope_id = f"scope_{i-1}"
                dot.edge(parent_scope_id, scope_id, style="dotted")

        dot.render(os.path.join(self.folder, filename), format="png", cleanup=True)

    def log_and_visualize(self, scopes, ctx, line_text):
        self.step += 1
        self.visualize(scopes, ctx, line_text, filename=f"scope_step_{self.step:03}")
