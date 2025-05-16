from langchain_experimental.tools.python.tool import PythonREPLTool

tool = PythonREPLTool()
output = tool.run("print(7.1**3.1)")
print(output)  # Should print: 12