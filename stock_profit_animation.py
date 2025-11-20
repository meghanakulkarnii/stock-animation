from manim import *
class StockProfitAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Best Time to Buy and Sell Stock II", font_size=42)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Example
        example_text = Text("Input: prices = [7,1,5,3,6,4]", font_size=32).next_to(title, DOWN)
        output_text = Text("Output: 7", font_size=32).next_to(example_text, DOWN)
        self.play(FadeIn(example_text), FadeIn(output_text))
        self.wait(2)

        # Draw price nodes
        prices = [7, 1, 5, 3, 6, 4]
        nodes = []

        for i, p in enumerate(prices):
            dot = Dot(point=RIGHT * i + DOWN * 2)
            label = Text(str(p), font_size=28).next_to(dot, DOWN)
            nodes.append(VGroup(dot, label))
            self.play(FadeIn(nodes[i], shift=UP), run_time=0.5)

        self.wait(1)

        # Show graph lines
        lines = []
        for i in range(len(nodes) - 1):
            line = Line(nodes[i][0].get_center(), nodes[i + 1][0].get_center())
            lines.append(line)
            self.play(Create(line), run_time=0.3)

        self.wait(1)

        # Explanation of greedy strategy
        strategy_text = Text("Strategy: Add every positive price difference.", font_size=28).next_to(output_text, DOWN * 2)
        self.play(Write(strategy_text))
        self.wait(2)

        # Highlight profitable transactions
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                highlight_line = lines[i].copy().set_color(GREEN)
                self.play(ReplacementTransform(lines[i], highlight_line), run_time=0.5)
                profit += prices[i + 1] - prices[i]
                profit_text = Text(f"Profit: {profit}", font_size=30, color=YELLOW).next_to(strategy_text, DOWN)
                self.play(FadeTransform(strategy_text.copy(), profit_text))
                self.wait(1)

        # Final Result
        final_answer = Text(f"Final Profit = {profit}", font_size=40, color=BLUE).shift(DOWN * 3)
        self.play(Write(final_answer))
        self.wait(3)


# To render:
# manim -pqh filename.py StockProfitAnimation
