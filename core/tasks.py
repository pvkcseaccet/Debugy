from crewai import Task
from agents import *

summarize_ticket = Task(description="Summarizes the support ticket",
                        agent=ticket_summarizer)

search_logs = Task(description="Search the logs",
                        agent=log_digger)

search_code = Task(description="Search the code",
                        agent=code_debugger)

make_decision = Task(description="Decides based on the inputs from other agents",
                        agent=sw_debug_engineer)


