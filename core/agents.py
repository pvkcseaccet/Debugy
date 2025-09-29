from crewai import Agent

ticket_summarizer = Agent(role="Summarizer",
                          goal="Summarizes the problem in ticket",
                          backstory="A good analytical mind which reads, understands and summarizes the user's problem.")

log_digger = Agent(role="Log Digger",
                   goal="Looks up the problem in logs",
                   backstory="A super cool agent which off loads yours pain of going through the KBs and sometimes MBs of logs.")

code_debugger = Agent(role="Debugger",
                      goal="Do code debugging",
                      backstory="A clever developer who takes care surfing through your codebase and finding out the problematic areas.")

sw_debug_engineer = Agent(role="Debug Engineer",
                          goal="Receives results and decide solution",
                          backstory="A smart decision maker who makes strong analytical decisions using the signal from other agents.")

