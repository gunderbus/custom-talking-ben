import dspy


class AICommunicator:
    modeltype: str

    def __init__(
        self,
        imodeltype: str,
    ):
        self.modeltype = imodeltype
        self.context = "No current context"
        try:
            self.model = dspy.OllamaLocal(model=self.modeltype)
            dspy.settings.configure(lm=self.model)
        except ValueError:
            print("Please use an actual str for modeltype")

    def readFile(self, filePath: str):
        with open(filePath, "r") as file:
            content = file.read()
            self.context = (
                "Here is the environment context to understand each question to ask: "
                + content
            )

    def callts(self, prompt: str):
        try:
            qa_module = dspy.ChainOfThought("question -> answer")
            return qa_module(question=prompt)
        except ValueError:
            print("Please use an ACTUAL prompt")
