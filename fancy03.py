from fasthtml.all import *
import uvicorn

db = database('data/todos.db')
todos = db.t.todos
if todos not in db.t: todos.create(id=int, title=str, done=bool, pk='id')
Todo = todos.dataclass()

app = FastHTML(hdrs=[picolink])
rt = app.route

@rt("/")
def get():
  todolist = [Li(f'{o.title} {"✅" if o.done else ""}') for o in todos()]
  todoul = Ul(*todolist, id="todolist")
  group = Group(Input(placeholder="New Todo", name="title"), Button("Add"))
  header = Form(group, hx_post="/", target_id="details")
  footer = Div("Todo details", id="details")
  card = Card(todoul, header=header, footer=footer)
  contents = Main(H1("Hello World!"), card, cls="container")
  return Title("FastHTML"), contents

@rt("/")
def post(todo:Todo):
  todo = todos.insert(todo)
  return todo.title

