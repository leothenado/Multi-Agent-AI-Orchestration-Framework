from python_AI_agent import generate_backend
from frontend_AI_agent import generate_frontend

print("=" * 60)
print(" Multi AI Software Developer")
print("=" * 60)

project = input("\nDescribe your project:\n\n> ")

# Initialize variables to avoid NameError later
backend = ""
frontend = ""

if "backend only" in project.lower() or "required backend" in project.lower():
    backend = generate_backend(project)
    print(backend)

elif "frontend only" in project.lower():
    frontend = generate_frontend(project)
    print(frontend)

else:
    backend = generate_backend(project)
    frontend = generate_frontend(project)
    print(backend)
    print(frontend)
