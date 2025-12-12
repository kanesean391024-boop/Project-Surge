class Raindrop:
    """
    Lightweight adaptive learning layer.
    Updates internal parameters based on outcomes.
    """

    def __init__(self, alpha=0.1):
        self.alpha = alpha
        self.bias = 0.0

    def update(self, feedback):
        self.bias += self.alpha * feedback

    def apply(self, value):
        return value + self.bias
