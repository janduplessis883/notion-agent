install:
	@pip install -e .
	@echo "🌵 pip install -e . completed!"

clean:
	@rm -f */version.txt
	@rm -f .DS_Store
	@rm -f .coverage
	@rm -rf */.ipynb_checkpoints
	@rm -Rf build
	@rm -Rf */__pycache__
	@rm -Rf */*.pyc
	@echo "🧽 Cleaned up successfully!"

all: install clean


timeblock:
	@python timeblocker.py
	@echo "✅ Successfully ran Re-schedule Tasks with CrewAI"

newtask:
	@python new_task.py
	@echo "✅ Successfully ran New Task Creation with CrewAI"

experimental:
	@python new_task exp.py
	@echo "✅ Successfully ran New Task Creation EXPERIMENTAL with CrewAI"
