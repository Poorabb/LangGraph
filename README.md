# Agentic AI using LangGraph — Tutorial Notebooks

Hands-on notebooks following the **[Agentic AI using LangGraph](https://www.youtube.com/playlist?list=)** playlist by **CampusX**. Each notebook maps to a video in the series and builds up LangGraph concepts from basic LLM calls to full conditional/iterative workflows.

## 🧠 What's Covered

- **Sequential Workflows** — chaining nodes in a fixed order (BMI calculator, prompt chaining)
- **Parallel Workflows** — fanning out to multiple nodes and merging state (batsman stats, essay grading)
- **Conditional Workflows** — branching graph execution based on state, e.g. the quadratic equation solver which computes the discriminant and routes to *two roots / one repeating root / no real roots*
- **Iterative Workflows** — looping nodes until a condition is met *(in progress)*

### Example: Conditional Workflow (Quadratic Equation)

```python
initial_state = {'a': 2, 'b': 4, 'c': 2}
workflow.invoke(initial_state)

# Output
{
  'a': 2, 'b': 4, 'c': 2,
  'equation': '2x²+4x+2',
  'discriminant': 0,
  'result': 'Only repeating root is -1.0'
}
```

## ⚙️ Setup

```bash
git clone https://github.com/<your-username>/langgraph-tutorials.git
cd langgraph-tutorials

python -m venv myenv
source myenv/bin/activate   # Windows: myenv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file for any API keys used in the LLM-based notebooks:

```
OPENAI_API_KEY=your_key_here
# or GROQ_API_KEY / GOOGLE_API_KEY, depending on the model provider used
```

## ▶️ Running

Open any notebook in Jupyter or VS Code and run all cells:

```bash
jupyter notebook
```

## 🙏 Credits

Tutorial series by **[CampusX](https://www.youtube.com/@campusx-official)** — *Agentic AI using LangGraph* playlist.

## 📄 License

MIT — for personal learning purposes.
