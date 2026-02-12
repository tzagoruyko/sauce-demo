import os
from dotenv import load_dotenv
load_dotenv()

STANDARD_USER = os.getenv("STANDARD_USER")
PROBLEM_USER = os.getenv("PROBLEM_USER")
PERFORMANCE_GLITCH_USER = os.getenv("PERFORMANCE_GLITCH_USER")
ERROR_USER = os.getenv("ERROR_USER")
VISUAL_USER = os.getenv("VISUAL_USER")

PASSWORD = os.getenv("PASSWORD")
