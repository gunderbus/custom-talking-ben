import dspy


class AICommunicator:
    modeltype: str

    def __init__(
        self,
        imodeltype: str,
    ):
        self.modeltype = imodeltype

        try:
            self.model = dspy.OllamaLocal(model=self.modeltype)
            dspy.settings.configure(lm=self.model)
        except ValueError:
            print("Please use an actual str for modeltype")

    def callts(self, prompt: str):
        try:
            # 2. Define the module (Strategy)
            qa_module = dspy.ChainOfThought("question -> answer")

            return qa_module(question=prompt)
        except ValueError:
            print("Please use an ACTUAL prompt")
